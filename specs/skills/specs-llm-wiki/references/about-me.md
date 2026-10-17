# Building an about-me.md for the LLM Wiki

When the user asks to build or update their `about-me.md` (a persona page that feeds into how agents understand them), this is a cross-source research task. The `about-me.md` lives outside the wiki directory (usually `~/about-me.md` or similar) but the wiki's sources are the primary research material.

## Sections to Cover

Adapt based on the user's role and available data, but aim for:

- **Who I Am** — role, company, industry, team, manager, what a good week looks like
- **How I Work** — daily tools, zero→done workflow, review/QA process, what "done" looks like
- **What Good Looks Like** — best recent output, what separates great from average, what to look for in their work
- **What I Hate** — bad patterns in their field, shortcuts that make them cringe, what LLMs get wrong
- **My Rules** — never-dos, 2-3 non-negotiables
- **My Opinions** — beliefs peers push back on, what's overrated, what's underrated

## Research Methodology

### 1. Orient in the wiki first
Read SCHEMA.md, index.md, and recent log.md. The wiki's domain shapes what matters.

### 2. Gather from all available data sources
Pull from every source you have access to — don't stop at one:

- **Calendar** — meeting cadence, recurring patterns, who they meet with, what meeting titles and descriptions reveal about priorities. Look at the last 2 weeks minimum.
- **Email** — search for their name/sent mail. Look for GitLab pipeline notifications (what projects they commit to), code review threads (are they reviewer or author?), meeting note forwards (Gemini "Anotações"). Batch-fetch message content — don't judge by subject lines alone.
- **Wiki transcripts** — read the raw meeting notes. They reveal what the user actually says, owns, and tracks.
- **Session history** — what they've asked agents to do, how they phrase requests, what they automate vs. delegate.
- **GitLab/CI** — projects they commit to, MRs they're assigned, review patterns, pipeline failures they deal with.

### 3. Follow interesting threads
If a pipeline email shows a project name, pull the thread to see if they're author or reviewer. If a calendar event has a quirky title ("POST /v1/heber.abreu"), read the description — it reveals culture. If a meeting transcript assigns them an action item, note the domain and verb ("Ajustar agregação" → they own data mapping). Go one level deeper on anything unexpected.

### 4. Extract patterns, not raw data
Don't paste transcripts. Look for:
- Repeated meeting types (standup, refinement, planning → Scrum/agile)
- Tools consistently in play (SonarQube, Datadog, GitLab CI, Sentry)
- Ownership domains (which projects/areas do their action items cluster around?)
- What they automate vs. what they do manually
- Tone of meeting descriptions (casual? formal? deadline-driven?)

### 5. Identify gaps and formulate questions
Every `about-me.md` will have blind spots the data can't cover. List them as specific, answerable questions (max 20). Good questions are concrete: "What's your code review style?" not "How do you collaborate?"

### 6. Write condensed, evidence-backed prose
- Under 2,000 tokens
- Every claim should trace to a source (MR, meeting note, calendar pattern, commit)
- Cut sentences that don't carry signal
- Section headings: Who I am / How I work / What good looks like / What I hate / My rules

## Pitfalls

- **Don't fabricate opinions.** If the data shows they use feature toggles but doesn't show their opinion on them, say "feature toggles are default" (observable fact), not "they believe feature toggles are essential" (inferred opinion).
- **Don't skip sources.** Calendar alone won't tell you how they code. Email alone won't tell you their meeting cadence. Cross-reference.
- **Don't accept generic answers.** If the meeting notes say "discussed security," find the specific vulnerability (IDOR? SEC ticket number?). Specificity is the difference between a useful about-me and a generic one.
- **Don't confuse the wiki's voice with the user's voice.** The wiki was written by an agent summarizing meeting notes — it reflects what was discussed, not necessarily the user's personal style.
- **Respect privacy boundaries.** The about-me feeds into agents. Don't include sensitive details (salary, private conversations, personal calendar events beyond what's clearly public).
