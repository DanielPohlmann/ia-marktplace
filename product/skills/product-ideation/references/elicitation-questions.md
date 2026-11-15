# Ideation — elicitation question bank

Questions to ask **before** writing the idea brief. They come from established
discovery methods; each block names its source so the reasoning behind a
question can be looked up.

## How to run the interview

- **Ask everything that applies.** Too many questions beat a brief built on
  guesses. Skip a question only when the context, an earlier answer or the
  research subagent already answered it — say which.
- **One question per message**, multiple choice when the options are known,
  always with an "other / don't know" way out.
- **Past behavior over opinions** (The Mom Test): ask "When did this last
  happen? Walk me through it", never "Would you use…?" or "Do you think it's a
  good idea?". Compliments, hypotheticals ("I would…", "I might…") and
  feature wishes are *weak signals*: dig with "Why?", "Can you give a recent
  example?", "What did you do about it?".
- **Do not pitch.** Describe the problem, not the solution, until block H.
- **"Don't know" is a valid answer.** Record it under `## Open questions` with
  how we would find out (interview N people, check data, run a probe).
- **Record answers** in the brief's `## Interview notes` table in the user's
  words, then use them to fill the sections listed per block.
- Close every block with: "Anything about <block topic> I didn't ask?"

## A. Problem and context — The Mom Test, problem framing

Fills: `Problem`, `One-liner`.

| # | Question | Weak-answer signal → follow-up |
|---|---|---|
| A1 | In one sentence, what problem are we solving and for whom? | Describes a feature → "What problem does that feature remove?" |
| A2 | When did this problem last happen? Walk me through that moment step by step. | No concrete recent example → the problem may not be frequent or real |
| A3 | Who exactly was involved (role, company size, context)? | "Everyone" → "Who feels it most and first?" |
| A4 | At what moment of their day / week / process does it show up? | Vague → "What were they doing right before?" |
| A5 | How often does it happen? | "Sometimes" → ask for a number per week or month |
| A6 | What does it cost them each time — time, money, risk, stress, lost customers? | No cost → low willingness to change |
| A7 | What is the worst consequence when it goes wrong? | — |
| A8 | Is this a top-3 problem for them, or a nice-to-have? | Not top-3 → adoption risk; flag it |
| A9 | Who else is affected downstream (team, clients, manager)? | — |
| A10 | What have they already tried to solve it? | Tried nothing → the pain may be tolerable |
| A11 | Why hasn't it been solved yet? | — |
| A12 | Why now — what changed (regulation, technology, behavior, market)? | No trigger → timing risk |
| A13 | What evidence do we have: interviews, tickets, data, our own experience? | Only our opinion → plan validation in block I |

## B. Switch timeline and forces — Jobs to Be Done (Bob Moesta, Clayton Christensen)

Fills: `Jobs to be done`, `Proto-personas`.

| # | Question | Weak-answer signal → follow-up |
|---|---|---|
| B1 | Finish the sentence: "When ___, I want to ___, so I can ___." | Solution inside the job → strip it out |
| B2 | First thought: when did they first realize the current way wasn't good enough? | — |
| B3 | What event made them start actively looking for something better? | No event → passive interest only |
| B4 | Where did they look, and what did they compare? | — |
| B5 | What made them decide (or almost decide)? | — |
| B6 | **Push**: what about the current situation pushes them away? | — |
| B7 | **Pull**: what attracts them to a new way? | — |
| B8 | **Anxiety**: what worries them about switching (cost, learning, data loss, risk)? | Ignored anxieties kill adoption |
| B9 | **Habit**: what keeps them in the current way even though it hurts? | — |
| B10 | What would "done well" look like to them — how do they measure success? | — |
| B11 | Functional job, emotional job (how they want to feel), social job (how they want to be seen)? | Only functional → ask the other two |
| B12 | Which jobs are most important and least satisfied today? (rate 1–5 each) | Fills Importance / Current satisfaction |

## C. Customer segments and personas — Business Model Canvas, proto-personas

Fills: `Proto-personas`, `One-liner`.

| # | Question | Weak-answer signal → follow-up |
|---|---|---|
| C1 | Who is the user and who is the buyer? Are they the same person? | Different → two personas, two value propositions |
| C2 | Who influences or can veto the decision? | — |
| C3 | Who are the early adopters — who has the problem worst and is already hacking a fix? | "Everyone" → pick one segment |
| C4 | How do these people differ (size, sector, region, maturity, tech literacy)? | — |
| C5 | Which segment do we serve first, and which do we explicitly not serve? | No exclusion → scope risk |
| C6 | What does a typical day look like for the main persona? | — |
| C7 | What tools, devices and channels do they already use? | — |
| C8 | A quote they would actually say about this problem? | — |

## D. Value proposition — Value Proposition Canvas (Osterwalder)

Fills: `Value proposition`, `Options considered`.

| # | Question | Weak-answer signal → follow-up |
|---|---|---|
| D1 | Top pains: what annoys, blocks or scares them before, during and after the job? | — |
| D2 | Top gains: what outcomes or benefits would delight them? | — |
| D3 | Which pains does our idea relieve, and how much? | "All of them" → rank them |
| D4 | Which gains does it create? | — |
| D5 | What is the one thing we must do better than anything else? | Several → no focus |
| D6 | What will we deliberately not do? | — |
| D7 | Headline of the launch press release (one sentence a customer would forward)? | Jargon → rewrite in customer words |
| D8 | Positioning: For <target> who <need>, <product> is a <category> that <benefit>, unlike <alternative>, we <differentiator>. | — |

## E. Alternatives and competition

Fills: `Competitors and alternatives`, feeds the market researcher.

| # | Question | Weak-answer signal → follow-up |
|---|---|---|
| E1 | What do they use today: a competitor, a spreadsheet, WhatsApp, paper, a person, nothing? | "No competition" → the alternative is "do nothing"; still a competitor |
| E2 | Which direct competitors do we know? Which indirect ones? | — |
| E3 | What do users like about the current alternative? | — |
| E4 | What do they hate about it? | — |
| E5 | How much do they pay for it (money and time)? | Sets the price anchor |
| E6 | What would make them switch — and what would make them stay? | — |
| E7 | What could a big player copy quickly? | — |

## F. Business model — Lean Canvas (Ash Maurya) / Business Model Canvas

Fills: `Value proposition`, `Market`, `Risks and flags`; record extra answers in `## Interview notes`.

| # | Question | Weak-answer signal → follow-up |
|---|---|---|
| F1 | Who pays? (user, company, third party, advertiser, marketplace take-rate) | — |
| F2 | Revenue model: subscription, per use, commission, license, freemium, one-off? | — |
| F3 | Price range and what it is anchored to (alternative cost, value created)? | "Cheap" → a number |
| F4 | Willingness to pay: has anyone already paid, pre-ordered or committed? | No commitment → validation needed |
| F5 | Channels: how do customers find us, buy, onboard, get support? | "Viral" / "SEO" without a plan → flag |
| F6 | Customer acquisition cost estimate and lifetime value estimate? | — |
| F7 | Main cost drivers (people, infrastructure, third-party APIs, payments, support)? | — |
| F8 | Key partners or suppliers we depend on? | Single critical supplier → risk |
| F9 | Key resources and activities we need (team, licences, data, content)? | — |
| F10 | Unfair advantage: what can't be easily copied or bought? | "First mover" / "better UX" → not unfair |
| F11 | Key metrics that tell the business is working (activation, retention, revenue, NPS)? | Vanity metrics → ask for a behavior metric |
| F12 | Break-even: how many paying customers to cover costs? | — |

## G. Market and timing

Fills: `Market`.

| # | Question | Weak-answer signal → follow-up |
|---|---|---|
| G1 | Which country / region / language first? | — |
| G2 | How many potential customers exist (TAM), how many can we reach (SAM), how many can we win in 1–3 years (SOM)? State the assumptions. | Top-down only → also bottom-up (customers × price) |
| G3 | Is the market growing, flat or shrinking? Source? | — |
| G4 | Seasonality or cycles? | — |
| G5 | Regulation or platform changes that open or close the window? | — |

## H. Product risks and opportunity — Marty Cagan (4 risks, Opportunity Assessment)

Fills: `Options considered`, `Risks and flags`, `Hypotheses and validation`.

| # | Question | Weak-answer signal → follow-up |
|---|---|---|
| H1 | Exactly what problem will this solve? (value proposition) | — |
| H2 | For whom? (target market) | — |
| H3 | How big is the opportunity? | — |
| H4 | What alternatives are out there? | — |
| H5 | Why are we best suited to pursue this? | — |
| H6 | Why now? | — |
| H7 | How will we get it to market? | — |
| H8 | How will we measure success? | — |
| H9 | What factors are critical to success? | — |
| H10 | Given the above, go or no-go? | — |
| H11 | **Value risk**: will customers choose to use / buy it? | — |
| H12 | **Usability risk**: can users figure out how to use it? | — |
| H13 | **Feasibility risk**: can we build it with our time, skills and technology? | — |
| H14 | **Viability risk**: does it work for the business — legal, finance, sales, brand, support? | — |
| H15 | Which of these four risks is the biggest for each option? | Fills "Riskiest assumption" |

## I. Success and validation — Lean UX hypotheses, Opportunity Solution Tree (Teresa Torres)

Fills: `Hypotheses and validation`, `Success metrics (90 days)`.

| # | Question | Weak-answer signal → follow-up |
|---|---|---|
| I1 | What desired outcome (business or customer) are we driving? | Output ("launch X") → ask for an outcome |
| I2 | What would make this a success in 90 days? Which number, which target? | No number → propose one and confirm |
| I3 | What result would make us stop or pivot? | No kill criterion → add one |
| I4 | What is the riskiest assumption, and the cheapest test (interview, fake door, concierge, landing page, prototype)? | — |
| I5 | Who can we talk to this week to validate it? | Nobody → flag |
| I6 | What data do we already have that supports or contradicts the idea? | — |

## J. Constraints and risk flags

Fills: `Risks and flags`. Flag, do not solve — legal topics go to `legal:legal`.

| # | Question | Weak-answer signal → follow-up |
|---|---|---|
| J1 | Does it handle personal data, payments, health, minors, location or user-generated content? | Any yes → legal flag |
| J2 | Any sector regulation (financial, health, education, consumer protection)? | — |
| J3 | Deadline, budget and team available? | — |
| J4 | Dependencies on other teams, partners or contracts? | — |
| J5 | Brand or reputational risk if it fails publicly? | — |
| J6 | Operational load it creates (support, moderation, manual work)? | — |
