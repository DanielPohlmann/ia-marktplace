// build-pdf.mjs — Markdown -> styled HTML -> PDF
//
// Usage:
//   node build-pdf.mjs <path-to-report.md> [output.pdf]
//
// Renders a Markdown audit report into a professional PDF using markdown-it for
// HTML conversion and a locally installed Chrome/Edge (via puppeteer-core) for
// print-to-PDF. No Chromium download required.
//
// Conventions used in the Markdown for nice PDFs:
//   - A leading `<div class="cover">…</div>` block renders as the cover page
//     (see framework/TEMPLATE.md for the skeleton and build/style.css `.cover*`).
//   - A line "<!-- pagebreak -->" forces a page break.
//   - Fenced code blocks render as monospace boxes (no syntax highlighter is wired).
//
// Trust premise: `html: true` passes raw HTML from the Markdown through unescaped
// (needed for the cover block and status spans), so the input Markdown is TRUSTED.
// Do NOT run this pipeline on audit reports authored by third parties.

import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import MarkdownIt from 'markdown-it';
import anchor from 'markdown-it-anchor';
import attrs from 'markdown-it-attrs';
import puppeteer from 'puppeteer-core';

const __dirname = path.dirname(fileURLToPath(import.meta.url));

const inputArg = process.argv[2];
if (!inputArg) {
  console.error('Usage: node build-pdf.mjs <report.md> [output.pdf]');
  process.exit(1);
}
const mdPath = path.resolve(inputArg);
const outPath = path.resolve(process.argv[3] || mdPath.replace(/\.md$/i, '.pdf'));
const htmlPath = outPath.replace(/\.pdf$/i, '.html');

function findBrowser() {
  // Env override wins on any OS, then the common install paths per platform.
  if (process.env.BROWSER_PATH && fs.existsSync(process.env.BROWSER_PATH)) return process.env.BROWSER_PATH;
  const candidates = [
    // Windows
    'C:/Program Files/Google/Chrome/Application/chrome.exe',
    'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe',
    'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe',
    'C:/Program Files/Microsoft/Edge/Application/msedge.exe',
    // macOS
    '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
    '/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge',
    // Linux
    '/usr/bin/google-chrome',
    '/usr/bin/chromium',
    '/usr/bin/chromium-browser',
    '/usr/bin/microsoft-edge',
  ];
  for (const c of candidates) if (fs.existsSync(c)) return c;
  throw new Error('No Chrome/Edge found. Install one, set BROWSER_PATH, or edit findBrowser().');
}

// linkify is OFF on purpose: bare tokens like `SKILL.md` or `ASP.NET` are real TLDs
// and would otherwise be turned into fake hyperlinks in the deliverable. Write any
// intended link as an explicit Markdown link instead.
const md = new MarkdownIt({ html: true, linkify: false, typographer: true })
  .use(anchor, { permalink: false })
  .use(attrs);

const raw = fs.readFileSync(mdPath, 'utf8');
// Support an explicit page break marker.
const withBreaks = raw.replace(/<!--\s*pagebreak\s*-->/g, '<div class="pagebreak"></div>');

// Semantic styling injected post-render (keeps the Markdown source clean):
const sevClass = (s) => 'sev-' + s.toLowerCase().replace('–', '-');
const impClass = (s) => {
  const k = s.toLowerCase();
  if (k.startsWith('high')) return 'imp-high';
  if (k.startsWith('low') && !k.includes('med')) return 'imp-low';
  return 'imp-med'; // med, low–med
};
const body = md.render(withBreaks)
  // Finding lead-ins:  **F1 · High** -> bold id + coloured severity pill
  .replace(/<strong>F(\d+)\s*·\s*(Critical|High|Med|Low)<\/strong>/g,
    (_m, n, sev) => `<strong class="fid">F${n}</strong>&nbsp;<span class="sev ${sevClass(sev)}">${sev}</span>`)
  // Maturity-rationale paragraph:  *Why L2:* … -> styled callout
  .replace(/<p><em>(Why L\d:)<\/em>/g, '<p class="rationale"><em>$1</em>')
  // Impact column cells -> coloured impact pill (cells whose entire content is the impact word)
  .replace(/<td>(High|Med|Low|Low–Med|Low-Med)<\/td>/g,
    (_m, v) => `<td><span class="imp ${impClass(v)}">${v}</span></td>`)
  // Effort column cells -> coloured effort pill (5.x corrective-action tables write plain words)
  .replace(/<td>(cheap|deeper|gated)<\/td>/g,
    (_m, v) => `<td><span class="tag tag-${v}">${v}</span></td>`);

const css = fs.readFileSync(path.join(__dirname, 'style.css'), 'utf8');
const html = `<!doctype html>
<html lang="en"><head><meta charset="utf-8"><style>${css}</style></head>
<body><main class="report">${body}</main></body></html>`;

fs.writeFileSync(htmlPath, html, 'utf8');
console.log('HTML written:', htmlPath);

// --no-sandbox is only needed when running Chrome as root (CI/containers). On a normal
// dev machine it needlessly drops the sandbox, so it is opt-in via NO_SANDBOX=1.
const launchArgs = ['--disable-gpu'];
if (process.env.NO_SANDBOX) launchArgs.push('--no-sandbox');
const browser = await puppeteer.launch({
  executablePath: findBrowser(),
  headless: 'new',
  args: launchArgs,
});
const page = await browser.newPage();
// Footer label is engagement-neutral by default so the reusable pipeline doesn't stamp
// every future audit with the first engagement's name. Override per report via AUDIT_FOOTER.
const footerLabel = process.env.AUDIT_FOOTER || 'AI Harness Audit · Confidential';
await page.goto('file:///' + htmlPath.replace(/\\/g, '/'), { waitUntil: 'networkidle0' });
await page.pdf({
  path: outPath,
  format: 'A4',
  printBackground: true,
  margin: { top: '18mm', bottom: '20mm', left: '16mm', right: '16mm' },
  displayHeaderFooter: true,
  headerTemplate: '<span></span>',
  footerTemplate:
    '<div style="width:100%;font-size:8px;color:#8a94a6;padding:0 16mm;display:flex;justify-content:space-between;">' +
    `<span>${footerLabel}</span>` +
    '<span>Page <span class="pageNumber"></span> / <span class="totalPages"></span></span></div>',
});
await browser.close();
console.log('PDF written:', outPath);
