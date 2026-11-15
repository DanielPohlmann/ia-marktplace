# Design — elicitation question bank

Questions to ask **before** drawing journeys or screens. They come from
established UX research methods; each block names its source. The approved
idea brief already answers *why* and *for whom* — these questions find *how
people actually work* and *what the screens must handle*.

## How to run the interview

- **Ask everything that applies.** Too many questions beat screens built on
  guesses. Skip a question only when the idea brief, the design system or an
  earlier answer already answers it — say which.
- **One question per message**, multiple choice when the options are known,
  always with an "other / don't know" way out.
- **Show me, don't tell me** (Contextual Inquiry): ask for the last real
  occurrence, a screenshot, a spreadsheet, a printed form. "Usually" and "it
  depends" are weak signals → "Tell me about the last time".
- **Ask about behavior, not preferences.** "Which layout do you like?" is not a
  research question; "What do you look at first when…?" is.
- **"Don't know" is valid.** Record it under `## Open questions` with how we
  would find out (observe a user, check analytics, usability test).
- **Record answers** in the design's `## Interview notes` table in the user's
  words, and use them to fill the sections listed per block.
- Close every block with: "Anything about <block topic> I didn't ask?"

## A. Context of use — Contextual Inquiry (Beyer & Holtzblatt), ISO 9241-11

Fills: `Journeys`, `Screen inventory` (surface), `States`.

| # | Question | Weak-answer signal → follow-up |
|---|---|---|
| A1 | Where are they when they do this (office, street, client's house, car, counter)? | — |
| A2 | Which device: phone, tablet, desktop, shared kiosk? Screen size? One hand or two? | "All" → which one is primary for the first release |
| A3 | Connectivity: always online, poor signal, offline at times? | Offline → state and sync requirements |
| A4 | How often do they do it: many times a day, weekly, once a year? | Rare task → must be self-explanatory; frequent → must be fast |
| A5 | How long do they have? Are they in a hurry or interrupted? | Interruptions → save progress, resumable flows |
| A6 | What else are they doing at the same time (talking to a client, driving, working with gloves)? | — |
| A7 | Lighting, noise, privacy — can someone see their screen? | Shared screen → hide sensitive data |
| A8 | Are they experts in the domain? In technology? | — |

## B. Task analysis — Hierarchical Task Analysis, Contextual Inquiry

Fills: `Journeys`, `Story map`, `Screen inventory`.

| # | Question | Weak-answer signal → follow-up |
|---|---|---|
| B1 | Walk me through the last time they did this task, step by step. | Skipped steps → "What happened between X and Y?" |
| B2 | What triggers the task — what makes them start? | — |
| B3 | What tools are involved today (apps, spreadsheets, paper, phone, WhatsApp)? | — |
| B4 | What information do they need at each step, and where do they get it? | — |
| B5 | What decisions do they make along the way, and based on what? | — |
| B6 | Who else takes part — handoffs, approvals, waiting on someone? | Handoffs → notification and status needs |
| B7 | Where do they make mistakes or get stuck? | — |
| B8 | What workarounds have they invented (copy-paste, sticky notes, double entry)? | Workarounds are requirements in disguise |
| B9 | What does "done" look like — how do they know the task succeeded? | — |
| B10 | What do they do right after? | Defines the next screen / exit point |

## C. Users, roles and permissions

Fills: `Screen inventory`, `States` (no-permission), `Handoff to architecture`.

| # | Question | Weak-answer signal → follow-up |
|---|---|---|
| C1 | Which roles use these screens (owner, staff, admin, end customer, guest)? | — |
| C2 | What can each role see, create, edit, delete, approve? | "Everyone sees everything" → confirm explicitly |
| C3 | Is anything visible without login (public pages, shared links)? | — |
| C4 | Can one person have several roles or several accounts/tenants? Switch between them? | — |
| C5 | What happens when someone without permission reaches a screen? | Fills the no-permission state |
| C6 | Does anyone act on behalf of someone else (assistant, support, admin impersonation)? | Audit needs |

## D. Journey and emotions — Customer Journey Mapping

Fills: `Journeys` (Feeling column, low point).

| # | Question | Weak-answer signal → follow-up |
|---|---|---|
| D1 | Where does the journey start (ad, link, notification, search, recommendation)? | — |
| D2 | What is the first value they get, and how long until they get it? | Long time-to-value → onboarding risk |
| D3 | What is the moment of truth — the step where they decide it's worth it? | — |
| D4 | Where is the low point: the most frustrating or anxious step today? | — |
| D5 | What would make them abandon halfway? | — |
| D6 | What brings them back the next time? | — |
| D7 | What happens after the main task (receipt, follow-up, review, sharing)? | — |

## E. Scope — User Story Mapping (Jeff Patton), Kano model

Fills: `Story map (first release)`.

| # | Question | Weak-answer signal → follow-up |
|---|---|---|
| E1 | What are the big activities, in the order the user does them? | — |
| E2 | What is the thinnest end-to-end flow that already delivers value (walking skeleton)? | Everything is "must" → ask E4–E5 per feature |
| E3 | What can wait for a later release without breaking the flow? | — |
| E4 | **Kano, functional:** "If the product has <feature>, how do you feel?" (like / expect / neutral / tolerate / dislike) | — |
| E5 | **Kano, dysfunctional:** "If the product does not have <feature>, how do you feel?" | Expect + dislike → must-be; like + neutral → attractive |
| E6 | Which features are must-be (absence = complaint), performance (more = better), attractive (delight), indifferent? | Indifferent → cut |
| E7 | What do competitors have that we deliberately won't do? | — |

## F. Content and data

Fills: `Screen inventory` (data shown), `States` (edge cases), `Handoff to architecture`.

| # | Question | Weak-answer signal → follow-up |
|---|---|---|
| F1 | What information must each screen show? Which is primary, which secondary? | — |
| F2 | How much data: 0, 1, 10, 1 000, 100 000 items? | Large lists → search, filters, pagination |
| F3 | Longest realistic values (names, addresses, descriptions)? Other languages? | Edge case: long text |
| F4 | How do they search, filter, sort, group? | — |
| F5 | Do they need to export, print, share or import? Which format? | — |
| F6 | Must data be up to date in real time, or is a refresh fine? How stale is acceptable? | Real-time → handoff flag |
| F7 | Images, files or media? Size and type limits? | — |
| F8 | Dates, times, time zones, currencies, units, number formats involved? | Localization keys and formats |
| F9 | What does the screen look like the first time, with no data (empty state)? What should it teach? | — |

## G. Errors, edge cases and recovery — Nielsen heuristics 5 and 9

Fills: `States`.

| # | Question | Weak-answer signal → follow-up |
|---|---|---|
| G1 | What are the most common user mistakes? How do we prevent them? | — |
| G2 | What validations apply to each input? When should they show? | — |
| G3 | Which actions are destructive or irreversible? Confirm, undo, or soft-delete? | — |
| G4 | What if the network or a dependency fails mid-action? | — |
| G5 | What if two people edit the same thing? | Conflict state |
| G6 | What if they leave halfway and come back (draft, resume)? | — |
| G7 | Limits: plan quotas, maximums, rate limits — what does the user see when hit? | — |
| G8 | What should an error message say so they can fix it themselves? | — |

## H. Notifications and communication

Fills: `Journeys`, `Copy`, `Handoff to architecture`.

| # | Question | Weak-answer signal → follow-up |
|---|---|---|
| H1 | Which events must the user be told about? Who else must be told? | — |
| H2 | Through which channel (in-app, email, SMS, WhatsApp, push)? | — |
| H3 | How urgent is each one? Can it be batched? | — |
| H4 | Can users configure or opt out? Legal requirements for consent? | — |
| H5 | What action should the notification lead to (deep link)? | — |

## I. Accessibility and inclusion — WCAG 2.2, inclusive design

Fills: `Accessibility checklist`, `Copy`.

| # | Question | Weak-answer signal → follow-up |
|---|---|---|
| I1 | Any users with low vision, blindness, motor, hearing or cognitive impairments? Assistive tech used? | "No" → still meet WCAG 2.2 AA |
| I2 | Literacy and digital-literacy level of the audience? | Low → plain language, icons with labels |
| I3 | Languages and locales needed now and later? | — |
| I4 | Older devices, small screens or low-end phones in the audience? | Performance budget |
| I5 | Any legal accessibility obligation (public sector, LBI, EAA, ADA)? | Point at `legal:legal-accessibility` |

## J. Brand, tone and copy

Fills: `Copy (localization keys)`.

| # | Question | Weak-answer signal → follow-up |
|---|---|---|
| J1 | Tone of voice: formal, friendly, playful, technical? Tu / você / senhor? | — |
| J2 | Words the users use for things (their vocabulary, not ours)? | Mismatch → follow the user's words |
| J3 | Words or phrases to avoid? | — |
| J4 | Legal texts required on screen (terms, consent, disclaimers)? | — |

## K. Design system and surfaces

Fills: `Design system used`.

| # | Question | Weak-answer signal → follow-up |
|---|---|---|
| K1 | Which surface(s) does this touch (public site, admin/back-office, mobile app, email)? | — |
| K2 | Existing screens or components we must reuse or match? | — |
| K3 | Any open design-system decision this feature forces (new component, new pattern)? | Raise it, do not invent |
| K4 | Light and dark mode? Brand themes per customer? | — |
| K5 | Is there a Figma or reference that must be followed? | — |

## L. UX success metrics — Google HEART

Fills: `Journeys`, handoff to the idea brief's metrics.

| # | Question | Weak-answer signal → follow-up |
|---|---|---|
| L1 | **Happiness**: how will we know users are satisfied (survey, rating, NPS)? | — |
| L2 | **Engagement**: which action, how often, shows they use it? | — |
| L3 | **Adoption**: what counts as a new user actually adopting it? | — |
| L4 | **Retention**: what shows they keep coming back? | — |
| L5 | **Task success**: completion rate, time on task, error rate — targets? | — |

## M. Self-check of the proposal — Nielsen's 10 usability heuristics

Not asked to the user: answer these about your own screens before showing
them, and fix any "no".

1. Does every screen show the system status (loading, saved, sent)?
2. Does it use the user's words and real-world order?
3. Can the user undo, cancel or go back from every step?
4. Are patterns consistent with the design system and the rest of the product?
5. Are errors prevented (constraints, defaults, confirmation) before they happen?
6. Can the user recognize options instead of remembering them?
7. Are there shortcuts for frequent users without confusing new ones?
8. Is every element on screen needed for this step?
9. Do error messages say what happened and how to fix it, in plain language?
10. Is help available in context where users get stuck?
