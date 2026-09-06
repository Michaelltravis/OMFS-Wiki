# Jacobs proposal voice guide

Content-bank standard for proposal prose. Derived from three measured analyses (rhythm and sentence; proof and persuasion; client address and voice) of two winning Jacobs O&M proposals — Hull WWTF (`verbatim/hull-wwtf-om-2026/pages/p0003–p0030`) and Santa Monica SWIP (`verbatim/santamonica-swip-om-2025/pages/p0004–p0034`) — against our Richmond pilot (`Desktop/Richmond/Draft Sections/02 Claude Working Drafts/_work/draft_03_qualifications_edited.md`), with the measured metrics in `voice/samples/comparison.md` and the brand voice rules in `end-game-sales-suite/skills/jacobs-documents/SKILL.md`.

**Authority.** `voice/exemplar/` contains only its README (checked 2026-09-05); no exemplar document has been supplied. Until one is, the Hull and Santa Monica sections are the primary authority for voice, and the Jacobs brand rules are the authority for typography and naming. When an exemplar lands, re-run the three lenses against it, record every difference in a "Where the exemplar differs" section at the end of this file, and let the exemplar win on conflicts.

**Where the brand rules and the winners differ, this guide resolves it as follows.**

| Topic | Winners (as laid out) | Brand rule | Content-bank rule |
|---|---|---|---|
| Heading case | ALL-CAPS primary headings, italic Title Case sub-labels | Sentence case for headings and subheads; ALL CAPS only for small standing heads and chart labels | Write heading text in sentence case. Keep the winners' heading *content* (benefit noun phrase, 3–9 words) and *density*. A sidebar label such as "Benefits to Richmond" may be set as a small standing head in caps by the template. |
| Second person | "you/your" only for collaboration and respect; client named as subject and beneficiary | Address the reader as "you" | Use "you/your" for what the client owns, values, or will receive. Name the client ("the City", "Richmond") in proof and commitment sentences. Never "you" in a deficit sentence; never mix "the City" and "you" in one sentence. |
| Em dash | Hull 1.3, Santa Monica 9.0 per 1,000 words | Em dash with spaces either side — like this; en dash for ranges | Spaced em dash when used; budget ≤9 per 1,000 words, aim ≤3. |
| Hype words | Winners each carry 4 (robust, holistic, seamless, proven track record) | No hype, no stacked adjectives | Zero. The house standard is stricter than the winners because the fix costs nothing. |
| Falsifiable claims | Every sentence names Jacobs, the client, a facility, a person, a number, or an action | A named owner, a frequency, a date, or a number; delete any sentence a competitor could use unchanged | Same rule (Rule 25). |
| Company name | "Jacobs", "we/our" | "Jacobs" in text; "Jacobs Solutions Inc." only in legal contexts; possessive Jacobs'; never JS/JE | Same. The contracting entity's legal name appears in the proposer-identification table and legal paragraphs only. |

---

## 1. The voice in one paragraph

The Jacobs proposal voice is a senior operator talking to a client it already respects: the client's situation opens every section, Jacobs answers in the second sentence, and every claim after that carries a name, a number, a date, or a named tool. Sentences run about 20 words, paragraphs one or two sentences, and each paragraph closes on what the client gains, often in a triad with the serial comma and the outcome clause in bold. Headings are benefit labels, not RFP echoes; bold text marks outcomes, not topics; tables and callouts repeat proof the prose has already stated and point the reader to it. Commitments are promises with an owner and a cadence ("Nathan Callison will maintain day-to-day coordination"), never present-tense descriptions; the competition is "the previous contract operator"; the client's needs are aspirations, never deficits; and required negatives are disclosed in four moves and then left alone. Nothing in the body narrates the document, argues with the reader, or hedges a fact. The writing is confident because every sentence is checkable, not because it is loud.

---

## 2. Rules

Each rule ends with a **Test** a judge can apply without interpretation. Numeric thresholds are calibrated in Section 4; where a rule states a number, Section 4 says whether it is a hard gate or directional.

### Sentences & rhythm

**1. Sentence length band.** Median 18–25 words; p90 ≤40; no sentence over 50 words except legal or financial boilerplate copied from corporate. Winners: median 21.5 and 18.0, p90 38 and 37, nothing above 50 outside boilerplate. The pilot's opener ran 56 words and its 3.3 opener 63.
**Test:** sort every body sentence by word count; any sentence >50 words outside approved boilerplate fails; p90 >40 fails.

**2. Punch sentences are verb-bearing assertions at paragraph edges, paired with a long sentence.** A punch sentence is ≤8 words, has Jacobs or the client as subject and a finite verb, and sits first or last in its paragraph ("Jacobs delivers on all fronts." "The onsite team will never operate alone."). They make up 5–10% of sentences (0.5–1.3 per 120 words). A bold run-in fragment ("California depth." "Lines of authority.") is not a punch sentence. Every section-opening and section-closing paragraph contains an adjacent pair in which one sentence is ≤9 words and the other ≥18.
**Test:** list every ≤8-word sentence; strike any without a finite verb or with a generic subject; the survivors must sit first or last in their paragraph; check the first and last paragraph of each H2 for a ≤9 / ≥18 adjacent pair.

**3. Paragraph size.** Median 30–50 words, average ≤55; at least 55% of body paragraphs are one or two sentences; no body paragraph over 110 words. Winners: 41.5 and 31.6 average words, 59% and 73% one-or-two-sentence paragraphs. Pilot: 63.7 average, 21 of 30 paragraphs with three or more sentences, 7 over 100 words.
**Test:** count words and sentences per paragraph; any paragraph >110 words fails; average >55 fails.

**4. Triads with the serial comma.** The house closing rhythm is "X, Y, and Z" of client outcomes ("compliance, reliability, and transparency"): at least 8 per 1,000 words (winners 17 and 12; pilot 0.5) and at least one in every section-closing paragraph. The serial comma is never dropped.
**Test:** regex-count "A, B, and C" per 1,000 words; any list of three or more without the serial comma fails.

**5. Punctuation budget.** Per 1,000 words of body prose: colons ≤6, semicolons ≤4, em dashes ≤9 (aim ≤3, spaced per brand), square brackets 0. No sentence carries both a colon and a semicolon list of three or more items; convert it to bullets. One colon per paragraph at most, used as payoff ("We treat communication as an operational control: the right information will reach the right decision-maker at the right time"), not as a list launcher. Winners: 3 / 1.6 / 1.3 (Hull) and 4.7 / 3.8 / 9.0 (Santa Monica). Pilot: 15.8 / 10.7 / 10.2 with 14.9 brackets.
**Test:** count each character per 1,000 words; flag any sentence containing both ":" and two or more ";".

**6. Actor-first openers and lexical transitions; no meta-narration.** At least 30% of body paragraphs open with Jacobs / We / Our [noun] / a named person and reach a present- or future-tense verb within six words ("Jacobs will develop…", "Nathan is supported by…"). Client-first openers are reserved for the first paragraph under a heading. Paragraphs are carried forward by repeating the prior sentence's key noun (objectives → objectives; data → dashboards → visibility) or by an exhibit pointer ("as shown in Exhibit 3-2"), and occasionally by "From Day 1,", "Beyond…", "Building on…". No sentence has the section, the argument, or "what follows" as its subject.
**Test:** tally first words of each paragraph (≥30% actor-first); flag "this section", "what follows", "set(s) … apart", "the question … is", "organized around", "is here because" (count must be 0).

### Headings & structure

**7. Heading density.** One heading or italic sub-label per 100–220 words of running prose, aiming at 130–170; no page without at least one. Winners: 148.6 and 157.9 words per heading. Pilot: 281 (11 headings over 2,150 words, five of them bare project names). Write sub-labels as markdown headings (`####`) so the tool counts them and the template can style them.
**Test:** count words between consecutive headings; any gap >220 fails; a whole section averaging <100 is fragment-writing and fails.

**8. Heading content.** A heading is a 3–9-word benefit or capability noun phrase in sentence case ("Leadership-driven operations and accountability", "Proven operations in coastal and complex systems", "Legal standing in California"), never an RFP question stem. Digits appear only where the RFP mandates numbering, and then a benefit phrase follows the number ("3.1 One California corporation, backed by Jacobs"). At least one heading per major section names the client or its state. Second-tier sub-labels are italic, sentence case, 2–6 words.
**Test:** scan the heading list; each must contain a benefit or capability noun (leadership, compliance, transition, reliability, readiness, expertise, standing, value, partnership, continuity) and no RFP question wording; ≥1 heading per section carries the client or state name.

**9. Assertion headings are rationed.** At most one claim-bearing heading per major section, ≤10 words, either an italic tagline directly under the label ("The Town of Hull is ready for a change.") or an em-dash compound ("Our role — an extension of City staff"). Fewer than one heading in five carries a verb; the rest are labels.
**Test:** count headings containing a finite verb; >20% fails; more than one assertion heading in a section fails.

**10. Run-in bold belongs to bullets, not the spine.** A bold lead-in is ≤6 words, followed by an en dash or colon and a 15–40-word sentence, and it introduces one bullet only. Any run-in longer than 6 words, or any run-in that governs more than one paragraph, is promoted to a sub-heading on its own line. The pilot built three subsections on 13 run-ins up to 14 words long.
**Test:** count bold run-ins and their word length; any >6 words or governing >1 paragraph fails.

**11. Section opener and closer shape.** A section opens with two or three paragraphs of 40–70 words: (1) the client's situation or asset with three or more numbers and a triad of pressures, (2) "Jacobs will / Jacobs brings…" ending on a bolded outcome triad, (3) a pointer to the exhibit that follows. The first sentence is ≤30 words, the first paragraph ≤70 words, and no bracket or placeholder appears in the first two paragraphs. A section closes with a 40–70-word next-chapter paragraph ("By selecting Jacobs, the Town of Hull positions itself to strengthen leadership, improve transparency, and align capital investment…") that names the client, the lead person or team, and three outcomes. Litigation, termination, and legal boilerplate sit before the closer, never last.
**Test:** read the first paragraph (≤70 words, first sentence ≤30, no bracket) and the last body paragraph (names client + person or team + three outcomes; is not a table, disclaimer, or bracket).

### Proof & consequence

**12. Comparator in the same sentence.** Every headline or bolded figure carries its anchor inside the sentence: the RFP threshold ("EMR is 0.45, well below the RFP requirement of 1.0"), the industry range ("multiplier of 2.6, compared to a typical industry range of 3.0–3.2"), the client's own scale, or the prior state ("compared to the previous operating approach"). The pilot anchors once ("$1.6 billion — 32 times the $50 million threshold") and leaves TRIR, EMR, D&B 5A3, and the portfolio counts floating.
**Test:** for each bold or headline figure, the judge points to the comparator inside the same sentence; any figure without one fails.

**13. Bold the consequence, not the feature.** At least 35% of paragraphs end on a bolded 2–3-outcome clause built on ensure / deliver / reduce / improve / protect / strengthen ("…ensuring consistent, responsive, and reliable service"). Bold density is 10–30 runs per 1,000 words (Hull 32, Santa Monica 11; pilot 5.6, all labels), and at least 70% of bold runs contain a number, a client noun, or an outcome verb. No sub-head beginning "Why this matters".
**Test:** read only the bold text on a page; it must read as a chain of client outcomes, not a list of topics; classify each bold run as outcome/proof or label and compute the share.

**14. Requirement → our figure → exceeds, in prose.** Each RFP desired qualification is answered in a sentence containing the requirement, the Jacobs figure, and an exceedance verb ("106 wastewater facilities… including 50 above 3 MGD, demonstrating experience well beyond the requirement to operate more than 10"). A compliance table repeats the answer; it does not replace it.
**Test:** for each RFP qualification, find the prose sentence with all three parts; a qualification answered only in a table fails.

**15. Four registers of proof.** Under every major heading, proof appears as (1) an inline number in prose, (2) a stat callout or exhibit pointed to in bold, (3) a table row, and (4) a named, titled third-party voice; at least three of the four appear within any two consecutive pages. The pilot used registers 1 and 3 only: ten tables, no exhibit pointers, no callout statistics, no named quotes.
**Test:** tick the four registers on each page pair; fewer than three fails.

**16. Numbers per sentence and lists per sentence.** At most 3 numeric facts per sentence; a sentence that scopes a facility ("a 3.07-MGD facility, seven pump stations…") may carry up to 5. Four or more facts otherwise, or any inline list longer than four items, becomes bullets, a table row, or a map callout ("398 staff in Massachusetts · 712 in New England"). Overall density 4.5–6.5 numbers per 100 words (winners 5.66 and 5.47).
**Test:** count numeric tokens per sentence (>5 fails; >3 outside a scoping sentence fails); count items in any inline list (>4 fails).

**17. Reference narratives.** A reference is a narrative block, not a key-value table: size / years / fee / contact, three or more relevance tags ("EPA Region 1 · Odor control study · Large collection system"), then Services provided / Facilities managed / Accomplishments, with every Accomplishments block carrying a dollar or percent. The prose is first-person past-tense actions → quantified result → one relevance clause ("comparable in size and complexity to the Town of Hull's system"). At most one sentence names the target client; there is no analogy to the client's procurement, settlement, or politics.
**Test:** each reference has ≥3 relevance tags, ≥1 quantified accomplishment, ≤1 sentence naming the target client.

**18. Let the client say the number.** Prefer client-attributed outcomes ("The City estimated cost savings of up to $12.7 million compared to the previous operating approach") and named, titled quotes ("— Firooz Fath-Azam, Former South Huron Valley System Manager") over self-claims. Any "clients have said" or "city leaders have said publicly" without a name and title is cut.
**Test:** every testimonial or attributed figure carries name + title + organization; unnamed paraphrase count is 0.

**19. Dollarize the give.** Every value-add carries a dollar value or a measurable quantity (2,000 hours, 1,000 hours, a 2.6 multiplier, a 20-minute response), the items sum to one headline ("$5 million in value at no additional cost"), and each is tied to a client priority (SmartCover → I/I). A callout that commits only to a reporting cadence carries no value.
**Test:** every commitment in a callout or value-add list has a number attached and a client priority named.

### Client address

**20. The client opens every section as grammatical subject; Jacobs is absent from sentence one.** "The Town of Hull's residents, businesses, and coastal environment depend on…"; "The City of Santa Monica is setting the national standard…". Jacobs first appears in sentence two or later. "The City gets" makes Jacobs the topic and fails.
**Test:** the subject of the first sentence under each H2 is the client or the client's assets, and its verb is not gets / is buying / contracts with.

**21. The client is beneficiary, never buyer.** The client sits in the benefit slot of Jacobs sentences: "providing the City with", "Richmond will gain", "so the City will have real-time visibility", "representing a significant cost savings to the Town". Never gets, is buying, contracts with, counterparty, contract party, or balance sheet outside the financial-qualifications table. Relationship nouns are partner, extension of City staff, one team, shoulder-to-shoulder.
**Test:** grep the buyer list in narrative prose; count must be 0; the client appears as object of gain / receive / have / provide in ≥1 sentence per subsection.

**22. Jacobs names itself as Jacobs / we / our / our team / the on-site team; second person is spent on respect.** Never "the operator", "the contractor", "the proposer", or "they" for Jacobs in own-voice prose ("the Offeror" is allowed once in legal boilerplate). Every "you/your" sentence names something the client owns, values, or will receive ("your visionary investment", "your single point of contact", "names your staff already know"); no "you" in a sentence naming a shortcoming; no "you" dropped into an otherwise third-person paragraph.
**Test:** grep "the operator", "the contractor", "they" referring to Jacobs (0); read each "you/your" sentence and confirm the client-owned object.

**23. Needs are aspirations or operating conditions, never lacks.** "The Town is seeking more than regulatory compliance. It is looking for stronger leadership, clearer communication…"; "operates under conditions that require disciplined execution". Site deficiencies observed on a visit belong in the technical approach as Observed issue → Improvement → Expected outcome, paired with credit for what the plant has sustained ("Despite the data challenges, the facility has maintained NPDES compliance"). In Qualifications they do not appear.
**Test:** in Qualifications, count lacks / lacked / what it has lacked / over-stretched / failing / deferred / inconsistent applied to the client (0); in the approach, every deficiency has an improvement and an outcome beside it.

**24. Commitment grammar.** [Named person or role] + will + operational verb + object + cadence or deadline (+ artifact): "Project Manager Nathan Callison will maintain open day-to-day coordination with Town staff"; "increase Ocean Avenue vac-truck cleaning to every eight weeks"; "answered by a person who will respond within 20 minutes". Cadence words: Day 1, daily, weekly, monthly, quarterly, annually, within 72 hours, by January 2026. Present tense is for standing facts only ("Jacobs operates 106 wastewater facilities"). Commitment verbs are ones a supervisor could be observed doing: deploy, deliver, hold, issue, route, invite, validate, cross-train; benefit verbs: strengthens, reduces, improves, protects, positions. Rhetorical verbs (proves, answers, sets apart, discloses) are not commitments.
**Test:** tag each commitment sentence with owner, verb, cadence; a present-tense commitment or one with no owner fails.

**25. Unshippable content.** Every subsection carries at least two of: (a) a named person with credential and current role ("Mack Mckenzie (WW Grade V, AWT3)"); (b) a named Jacobs tool or program (SmartCover®, Six-Point Compliance Program, Sample Tracking Tool, Annual Innovation Workshop); (c) a client-specific identifier in the client's own vocabulary (Baykeeper Settlement Agreement, the 2025 Cease and Desist Order, NexGen, Keller Beach Pump Station); (d) a quantified included offer ("2,000 hours of dedicated support annually"). Any intensifier (significant, industry leader, extensive) sits in the same sentence as the number that earns it.
**Test:** for each paragraph ask "could a competitor paste this unchanged?"; if yes it fails; each subsection has ≥2 of (a)–(d); every comparative or superlative has a number or named comparison in its sentence.

### Win-theme threading

**26. Name the themes once, then repeat them as headings.** Three to five win themes are named once (cover letter or an executive-summary exhibit), then each is used verbatim as a section heading, a callout title, and a closer, and re-mapped as rows in the approach goals table. Each theme phrase appears at least three times across cover letter, executive summary, and section headings. The pilot named three themes in its italic deck and never turned one into a heading.
**Test:** count each theme phrase across the document (≥3 each, ≥1 as a heading).

**27. Signature phrases repeat; sentence frames do not.** Three to five signature phrases ("extension of City staff", "more than an operator", "no surprises", "defensible compliance", "Day 1") each appear at least twice. Any other 3+-word frame appears at most once per section ("The City gets…" four times, "one thing" twice, "line by line" twice are tics, not themes). No more than two consecutive paragraphs share the same opening syntax (Name + is + comparative).
**Test:** 3-gram frequency scan; ≥3 signature phrases at ≥2 occurrences; any non-signature 3-gram at ≥2 occurrences in one section fails.

### Handling the incumbent and concessions

**28. Never name a competitor or incumbent.** Use "the previous contract operator", "the previous provider", "the previous operating approach", "traditional O&M providers", "something no typical O&M firm offers", "qualified incumbent employees". Competition is handled by a Traditional-vs-Jacobs comparison table, never by name. No swipes at ownership models ("private-equity models typically prioritize"). The pilot named the incumbent six times.
**Test:** competitor-name count 0; ownership-model swipes 0.

**29. Frame the incumbent's failures as the client's aspirations.** "But the Town is seeking more than regulatory compliance. It is looking for stronger leadership, clearer communication, and a proactive asset-management approach" tells the evaluator what went wrong without an accusation. No sentence attributes a deficiency to the City, its staff, or its program; the incumbent transition is written people-first ("We will invite qualified incumbent employees to join our team").
**Test:** read every sentence with the client, its staff, or its program as subject; none names a shortcoming.

**30. Four-move concession; disclose only what the RFP asks.** Every required negative follows, in one paragraph: (a) scale context ("Given Jacobs' size… from time to time and in the ordinary course of business"), (b) bounding ("minor", "administrative in nature"), (c) resolution ("the applicators renewed their expired licenses… in coordination with regulators"), (d) no-impact close ("with no impact to our ability to deliver services"). Disclosures use the RFP's format with a Resolution column beside every item. Nothing negative is volunteered beyond the RFP ask — no self-disclosed incident tables, no "We make no claim yet about long-run results", no "It is here because", no disclosure used as a rhetorical device for candor.
**Test:** each disclosed negative has all four moves in its paragraph; every negative table or list traces to an RFP requirement; self-disclaimer count 0.

**31. Acknowledge a weakness in a subordinate clause, answer it in the main clause.** "While not all of the reference projects are located within EPA Region 1, they demonstrate our extensive experience operating similar facilities under comparable regulatory frameworks." One sentence, the evaluator's own criterion in the main clause, no dwelling.
**Test:** any concession longer than one sentence, or lacking an answering main clause, fails.

### Devices — what each carries and when to use it

**32. Choose the device by what it carries.** Devices repeat proof the prose has stated; they never introduce a claim the prose lacks.

| Device | Use when | Shape | Limit |
|---|---|---|---|
| Stat callout | One figure carries a theme and has a comparator | Number + comparator + consequence in 8–20 words ("2.6 engineering multiplier vs. an industry range of 3.0–3.2 — savings to the Town over the contract life"); the figure also appears in prose | ≤1 per page |
| Fact box / benefit sidebar ("Benefits to Richmond") | Closing a subsection | Verbless triad of outcomes, 15–30 words, zero feature or tool names, client named ("Longer asset life, fewer reactive repairs, clearer budget forecasts, and faster parts availability to shorten outages") | 1 per subsection |
| Pull quote | A client has said it better than we can and we hold name + title | ≤35 words, name, title, organization; placed beside the theme it proves | ≤1 per major section; never unnamed |
| Commitment callout | A promise with owner, cadence, and artifact | "[Person or role] will [verb] [object] [cadence]" plus a number or value | ≤2 per section |
| Table | An RFP-mandated form, or ≥4 items with ≥3 attributes each | Numbered caption ("Table 3-1."); rightmost column is the client's outcome ("Value to the City"); prose states the claim and points to the table | Table share ≤0.35 of words |
| Map / footprint exhibit | Staff counts, tenures, sites | Callouts on the map ("398 staff in Massachusetts"); replaces any inline list of >4 items | 1 per section |
| Org chart | Chain of authority | Client at top, names and titles, reach-back groups as dotted lines; pointed to in prose | 1 |
| Bulleted list | 3–8 parallel items | ≤6-word bold lead-in + en dash or colon + 15–40 words; all "We will…" or all noun phrases; numbered only for sequenced steps | — |
| Traditional-vs-Jacobs table | Competition without names | "Traditional O&M provider" column vs "Jacobs" column; rows are the client's priorities | 1 per proposal |

**Test:** each device on a page matches its row (use, shape, limit); a device introducing a claim absent from the prose fails.

**33. Exhibits support the prose; they never carry the argument.** The claim lives in a sentence, the exhibit is pointed to in bold ("as shown in Table 3-8"), every figure and table has a numbered caption in the brand format, and the rightmost column of every proof exhibit names the client's outcome (Hull "Value to the Town", Santa Monica "Strategies to Deliver Results"). About every third paragraph points to an exhibit or numbered section. Reference key-value tables do not replace reference narratives (Rule 17).
**Test:** each exhibit has a pointer sentence in prose; the rightmost column header names an outcome for the client; caption present.

### Banned words and patterns

**34. Banned vocabulary and patterns.** Count must be 0 in body prose.

- **Hype (metrics.py list):** world-class, best-in-class, leverage (as a verb), synergy, cutting-edge, state-of-the-art, robust, seamless, holistic, utilize, passionate, unparalleled, proven track record, we are pleased, as a leading, comprehensive suite.
- **Buyer framing of the client:** gets, is buying, contracts with, counterparty, contract party, balance sheet, threshold (as what the client wants).
- **Deficit language about the client:** lacks, lacked, what it has lacked, over-stretched, failing, deferred, inconsistent, what the City has been missing.
- **Forensic frame:** proof, prove(s), evidence that, that test, answers the question, the case, scrutiny, the jury.
- **Meta-narration:** this section, what follows, set(s) … apart, the question … is really, organized around, is here because, two facts.
- **Self-disclaimers:** we make no claim, we cannot yet, it is too early, is here because, contacts and fees are as last confirmed.
- **Aphorisms:** any sentence whose grammatical subject is an indefinite generic noun (a firm, a contract, nothing, one) and which contains no proper noun, digit, or named action ("A strained contract is usually a starved one.").
- **Bolted-on so-what:** any sub-head or run-in beginning "Why this matters".
- **Competitor and incumbent names**, and ownership-model swipes.
- **Intensifiers without a number in the same sentence:** significant(ly), industry leader, extensive, unmatched, deep.
- **Repeated frames:** "The City gets…", "one thing", "line by line" or any 3-gram used twice in a section.
- **Mechanics (brand):** serial comma omitted; "#" for number (use №); "Jacobs Solutions Inc." outside legal text; JS or JE; emoji.

**Test:** grep each list against body prose; any hit fails; for aphorisms and intensifiers, read the flagged sentence and confirm a proper noun, digit, or named comparison is present.

### What never appears in body text

**35. Zero editorial residue.** Body prose carries no square brackets of any kind — [PLACEHOLDER], [VERIFY], [CONFIRM], [TBD], [FIGURE …], [CALLOUT …] — no draft notes, source lists, decision lists, or hedges attached to figures ("99.8% [VERIFY — 99.98% in other sources]"). Conflicting figures are reconciled in the fact pack, not in the sentence; until reconciled, the draft carries the figure the fact pack currently approves, stated flat at the precision both sources support ("more than 300 miles", "approximately $12 billion"), and logs the conflict in a draft-notes footer below a horizontal rule that is stripped before layout. An unconfirmed person or role is written as confirmed past fact or cut, never tagged. Hull carried $12B and $16B on different pages and never showed the seam; winners have 0 tags, the pilot 52 plus 14.9 brackets per 1,000 words.
**Test:** grep "[" in body prose (0); grep "Draft notes", "Sources used", "Decisions needed" above the footer rule (0); any figure followed by a bracket or a hedging parenthesis fails.

---

## 3. Before / after pairs

BEFORE text is verbatim from the pilot (`draft_03_qualifications_edited.md`). AFTER rewrites use only facts present in the pilot; where the pilot hedged a fact, the AFTER writes around it and the note says how. Ellipses ("…") mark omitted pilot text; nothing is altered inside the quoted passages.

### Pair 1 — Italic deck: client as buyer, incumbent named, three claims in one tagline (Rules 9, 21, 28)

**BEFORE**
> _The City gets a California operator with 45 years of contract O&M, a compliance record it can audit line by line, and a firm that has replaced Veolia twice and is doing so now in California._

**AFTER**
> _A California operator Richmond can audit line by line._
>
> Jacobs brings the City 45 years of contract O&M through OMI, a California corporation since 1980, two completed transitions from a previous contract operator, and a third under way in California today.

*Note.* The tagline carries one claim in nine words; the three facts move to a 33-word body sentence with the client in the benefit slot. The incumbent becomes "a previous contract operator."

### Pair 2 — Section opener: 56-word colon sentence, buyer framing, Jacobs in third person, meta-narration (Rules 1, 6, 11, 22, 24)

**BEFORE**
> The City is buying one thing: confidence that the Water Pollution Control Plant, 190 miles of sewer, 20 lift stations and the stormwater system will meet the Baykeeper Settlement Agreement and the 2025 stormwater Cease and Desist Order every month of the term — and that the operator will tell you first when they do not. This section is organized around that test.

**AFTER**
> Richmond's Water Pollution Control Plant, 190 miles of sewer, 20 lift stations, and stormwater system operate under the Baykeeper Settlement Agreement and the 2025 stormwater Cease and Desist Order. Jacobs will meet those obligations every month of the term and will tell the City first when a result falls short.

*Note.* First sentence 29 words with the client's assets as subject; second sentence is a "Jacobs will" commitment with an owner and a cadence. The meta sentence is deleted; if navigation is needed, point to an exhibit instead.

### Pair 3 — Named person wrapped in placeholders, preceded by meta-narration (Rules 6, 25, 35)

**BEFORE**
> Two facts set this pursuit apart. Mack Mckenzie, a Jacobs operations leader, ran this plant: as Chief Plant Operator and Assistant General Manager at the Richmond WPCP he supervised 27 people across Operations, Maintenance, Collections, Laboratory and Administration, presented at monthly board meetings and carried regulatory and laboratory compliance. [PLACEHOLDER: proposed role for Mack Mckenzie — decision pending] [VERIFY availability before naming]

**AFTER**
> Mack Mckenzie, a Jacobs operations leader, served as Chief Plant Operator and Assistant General Manager at the Richmond WPCP. He supervised 27 people across operations, maintenance, collections, laboratory, and administration, presented at monthly board meetings, and carried regulatory and laboratory compliance for the City.

*Note.* Only the confirmed past fact is stated. His proposed role is a fact-pack decision: once confirmed it becomes "Mack Mckenzie will serve as…"; if it cannot be confirmed the paragraph stays as history or is cut. No tag reaches the prose.

### Pair 4 — Cataloguing the client's deficits in Qualifications, then a forensic frame (Rules 23, 29, 34)

**BEFORE**
> And we already know what the City knows. Our August 18, 2026 due-diligence visit recorded the housekeeping, deferred corrosion, inconsistent lockout-tagout, end-of-life PLCs and odor at the uncovered primary clarifiers and Keller Beach Pump Station. What follows is evidence that we have fixed those conditions elsewhere under scrutiny as sharp as Baykeeper's.

**AFTER**
> Our operations leaders walked the WPCP and Keller Beach Pump Station on August 18, 2026. What we saw shapes our technical approach, where each site observation is paired with the improvement Jacobs will make and the result the City can expect.

*Note.* The deficiency list moves to the approach section as Observed issue → Improvement → Expected outcome, with credit for what the plant has sustained. The only self-reference left is navigational.

### Pair 5 — Run-in bold as skeleton, a bracketed figure spec, and "what it has lacked" (Rules 10, 13, 23, 33, 35)

**BEFORE**
> **Lines of authority.** [FIGURE 3-1: Project organization chart — City of Richmond Public Works at the top; Jacobs project manager reporting to the California O&M Director (Howard Brewen), then VP Operations, West (Paul Rheault), then President, OMFS & Design-Build (Greg Fischer); on-site operations, maintenance, collections, stormwater and laboratory leads beneath the project manager; the four regional support groups as dotted-line reach-back. Names to match Section 4.] The chart gives the City what it has lacked: one accountable project manager with a short, named chain to an executive who can release money and people.

**AFTER**
> #### One accountable project manager, one short chain to authority
>
> Richmond will have one accountable project manager and a short, named chain to executives who can release people and money. Figure 3-1 shows that chain: California O&M Director Howard Brewen, VP Operations, West Paul Rheault, and President, OMFS and Design-Build Greg Fischer.

*Note.* The run-in becomes a sentence-case sub-heading; the figure specification goes to the draft-notes footer and the prose points to the numbered figure; the names come from the pilot's own figure note. "What it has lacked" becomes "Richmond will have."

### Pair 6 — "Why this matters" block, an aphorism, an ownership-model swipe, and hedged figures (Rules 13, 21, 28, 34, 35)

**BEFORE**
> **Why this matters to Richmond.** A strained contract is usually a starved one. Jacobs is publicly owned; our ownership structure rewards long-term client relationships rather than the short-term return that private-equity models typically prioritize. Our contract renewal rate since 2013 is 98% [VERIFY — one source states 99%], and no Jacobs O&M contract has been canceled for compliance failure [VERIFY].

**AFTER**
> Jacobs is publicly owned, and our audited financial statements are filed with the SEC and published at invest.jacobs.com, so the City can read our finances at any time. Our contract renewal rate since 2013 is 98%, and no Jacobs O&M contract has been canceled for a compliance failure, **giving Richmond a partner whose ownership rewards long-term relationships.**

*Note.* The aphorism and the swipe are gone; the benefit is a bolded tail clause, not a labeled block. 98% is the figure the fact pack carries and the figure Hull shipped; the 99% variant and the cancellation statement are settled in the fact pack, and a clause that cannot be confirmed is cut, never tagged.

### Pair 7 — A hedge glued to the proof it undermines (Rules 12, 35)

**BEFORE**
> Our 20-year NPDES compliance record across the plants we operate is 99.8% [VERIFY — 99.98% in other sources]. That record lets us guarantee compliance rather than promise effort.

**AFTER**
> Across the plants Jacobs operates, our 20-year NPDES compliance record is 99.8%, and that record is why we **guarantee permit compliance at Richmond rather than promise effort.**

*Note.* The conservative figure both sources support, and the one Hull shipped, is stated flat; the 99.98% variant is logged in the draft-notes footer for the fact pack. Two sentences become one, ending on the client and the guarantee.

### Pair 8 — Eleven numeric facts in one table cell (Rules 14, 16, 33)

**BEFORE**
> Eleven systems: Waterbury 320, Pembroke Pines 445, Farmington 350, Prescott Valley 360, Fort Campbell 162.5, The Villages 127, West Melbourne 125, Pampa 120, Ontario OR 78, Wilsonville 70, Key West 57 miles [VERIFY]

**AFTER**
> Jacobs operates 11 collection systems of 50 miles or more, **more than twice the five the RFP asks for.** Table 3-8 lists each system, from 57 to 445 miles.

*Note.* Requirement, Jacobs figure, and exceedance in one prose sentence with three numeric facts; the eleven systems become one table row each, verified in the fact pack. The range sentence carries two numbers and the exhibit pointer.

### Pair 9 — Incumbent named, self-disclaimer, and "answers the question" (Rules 17, 28, 30, 34)

**BEFORE**
> West Basin answers the question the City is really asking: what happens in the first year after Veolia leaves. We are leading that transition in California now at a 40 MGD, nine-train facility. We make no claim yet about long-run results; the contract began in 2025. Susanna Li can describe how the handover was run and how the incumbent's staff were treated.

**AFTER**
> Since 2025, Jacobs has led the transition of West Basin Municipal Water District's 40 MGD, nine-train Edward C. Little Water Recycling Facility from the District's previous contract operator, the same first-year transition Richmond will make. Susanna Li, the District's Manager of Engineering, can describe how the handover was run and how incumbent staff were treated.

*Note.* "We make no claim yet" becomes "Since 2025, Jacobs has led…"; the incumbent is unnamed; the one relevance clause replaces the lecture; the reference contact gains her title.

### Pair 10 — Lecturing the client about its own settlement, an em-dash argument, and a 41-word sentence (Rules 5, 16, 17, 35)

**BEFORE**
> Waterbury is the closest match to Richmond in our portfolio: a primary-plus-activated-sludge plant, 20 pump stations and a sewer network of Richmond's order, procured after sewer overflows reached the Naugatuck River. The City kept ownership and every decision; we took the operating risk, wet-weather management and the CMOM program. That split — owner keeps control, operator carries compliance — is the one the Baykeeper Settlement asks Richmond to make work.

**AFTER**
> Since November 2018, Jacobs has operated Waterbury's 27 MGD primary and activated-sludge plant, its 20 pump stations, and more than 300 miles of sanitary sewer. The City kept ownership and every decision while we carried the operating risk, wet-weather management, and the CMOM program, the same division of responsibility Richmond's Baykeeper Settlement Agreement calls for.

*Note.* The scoping sentence carries four facts (allowed for a facility-scoping sentence); "more than 300 miles" is true under both conflicting sources (310 and 320) and needs no tag. One relevance clause, no em dashes, no procurement history.

### Pair 11 — Commitment in present tense with no owner (Rules 19, 24, 32)

**BEFORE**
> CALLOUT: Compliance transparency commitment — the Jacobs project manager delivers a monthly compliance report to the Public Works Director within ten days of month end, covering compliance status, near-exceedances, corrective actions and Baykeeper and CDO deliverables, and the City has read access to the process control and laboratory data systems from day one.

**AFTER**
> **Compliance transparency.** Our project manager will deliver a monthly compliance report to the Public Works Director within ten days of month end, covering compliance status, near-exceedances, corrective actions, and Baykeeper and CDO deliverables. From Day 1, the City will have read access to our process control and laboratory data systems.

*Note.* "Will" plus a role plus a cadence plus an artifact. When the project manager is confirmed, the role becomes the name: "[Name], our Project Manager, will deliver…". The callout should also carry its value once the value-added stack is dollarized (Rule 19).

### Pair 12 — Violations disclosure ending on an aphorism instead of the four-move close (Rules 30, 34, 35)

**BEFORE**
> Health, safety or environmental violations in the last five years: two, both administrative. On May 26, 2022 the Oregon Department of Agriculture fined our Ontario, OR project $660 and our Roseburg, OR project $1,628 for applying herbicides on expired applicator licenses; the applicators renewed their licenses and the matters were closed with the regulator. [PLACEHOLDER: Any OSHA citations in the last five years — none identified in current records; legal to confirm.] [PLACEHOLDER: Regenerated five-year environmental violations table current to September 2026.] A firm that discloses a $660 fine will disclose a permit exceedance.

**AFTER**
> Given the scale of Jacobs' operations, regulatory matters arise from time to time in the ordinary course of business. In the past five years there were two, both administrative. On May 26, 2022, the Oregon Department of Agriculture fined our Ontario, Oregon project $660 and our Roseburg, Oregon project $1,628 for herbicide application on expired applicator licenses. The applicators renewed their licenses, both matters were closed with the regulator, and neither affected our ability to deliver services.

*Note.* Scale context → bounding → resolution → no-impact close, in one paragraph. The no-impact clause is the approved corporate close (Hull p0017) and is confirmed with legal through the fact pack. The two placeholders move to the draft-notes footer; the aphorism, which primes the reader to expect exceedances, is deleted.

---

## 4. Calibrated numeric targets

Targets are set from the winners' measured values (`voice/samples/comparison.md`, `metrics_hull.json`, `metrics_santamonica.json`), not idealized. Four of the original `comparison.md` targets fail both winners and are recalibrated here: punch sentences ≥1 (Hull 0.54), words per heading 150–220 (Hull 148.6), client paragraph density ≥0.8 (winners 0.40–0.44), so-what rate ≥0.6 (winners 0.10–0.32). **Hard** = a fail blocks release regardless of rubric score. **Directional** = informs the rubric score; a miss is a finding, not a block. Tool metrics apply to units of ≥1,000 words of body prose; shorter units (letters, callouts) are judged by the rules only.

### 4a. Metrics computed by `voice/metrics.py`

| Metric (metrics.py key) | Hull | Santa Monica | Pilot | Target | Gate | Note |
|---|---|---|---|---|---|---|
| sentence_median_words | 21.5 | 18.0 | 18 | 18–25 | **Hard** | ChatGPT draft at 12.5 is fragment-writing |
| sentence_p90_words | 38.0 | 37.0 | 60.0 | ≤40 hard; ≤38 directional | **Hard** | |
| punch_sentences_per_120_words | 0.54 | 1.14 | 1.28 | 0.5–1.3 | Directional | Tool counts run-in fragments; judge strikes verbless ones first (Rule 2) |
| avg_paragraph_words | 41.5 | 31.6 | 63.7 | ≤55 hard; 30–45 directional | **Hard** | Pilot fails on fat paragraphs; comparison.md's ≤110 let it pass |
| words_per_heading | 148.6 | 157.9 | 281.2 | 100–220 hard; 130–170 directional | **Hard** | Mark italic sub-labels as `####` so they count |
| numbers_per_100_words | 5.66 | 5.47 | 6.4 | ≥3.0 hard; 4.5–6.5 directional | **Hard** | Density alone is not enough; see numeric facts per sentence below |
| so_what_rate | 0.098 | 0.318 | 0.405 | ≥0.10 | Directional | Regex counts "—" as a cue, so dash-heavy drafts inflate it; the judge's consequence test (Rule 12–13) is the real check |
| table_share | 0.235 | 0.032 | 0.242 | ≤0.35 hard; 0.05–0.25 directional | **Hard** | RFP-mandated forms raise it legitimately |
| client_paragraph_density | 0.437 | 0.403 | 0.519 | ≥0.40 | Directional | Counts literal client names only; the pilot scored higher than the winners while framing the client as buyer |
| we_you_ratio | 1.14 | 1.00 | 0.89 | 0.8–1.3 | Directional | "you" side includes the client's name |
| passive_voice_rate | 0.101 | 0.031 | 0.113 | ≤0.15 hard; ≤0.10 directional | **Hard** | |
| tags_in_body | 0 | 0 | 52 | 0 | **Hard** | Counts [PLACEHOLDER, [VERIFY, [CONFIRM, [TBD only; see bracket gate below |
| banned_words_total | 4 | 4 | 0 | 0 | **Hard** | Stricter than the winners by design (brand rule) |
| pct_headings_assertion | 0.46 | 0.79 | 0.58 | informational | — | Tool's definition (≥5 words or a colon) is looser than Rule 9; use the judge's verb count |

### 4b. Metrics applied by the judge (from the three lens analyses)

| Metric | Hull | Santa Monica | Pilot | Target | Gate |
|---|---|---|---|---|---|
| Max sentence words, non-boilerplate | ≤50 | ≤50 | 63 | ≤50 | **Hard** |
| Square brackets of any kind in body, per 1,000 words | 0.9 | 0 | 14.9 | 0 | **Hard** |
| Competitor or incumbent names | 0 | 0 | 6 | 0 | **Hard** |
| Sentences attributing a deficiency to the client (Qualifications) | 0 | 0 | 4+ | 0 | **Hard** |
| Aphorisms (generic indefinite subject, no proper noun or digit) | 0 | 0 | 3+ | 0 | **Hard** |
| Meta-narration sentences (Rule 6 list) | 0 | 0 | 5+ | 0 | **Hard** |
| First sentence of each H2 ≤30 words; first paragraph ≤70; no bracket in first two paragraphs | yes | yes | no | yes | **Hard** |
| Last body paragraph of each major section is a client-benefit paragraph (client + person or team + 3 outcomes) | yes | yes | no | yes | **Hard** |
| Headline or bolded figures with a comparator in the same sentence | all | all | 1 of ~8 | 100% | **Hard** |
| Volunteered negative exhibits not traceable to an RFP requirement | 0 | 0 | 1 | 0 | **Hard** |
| Disclosures with all four concession moves | all | n/a | 1 of 2 | all | **Hard** |
| Present-tense or owner-less commitments | 0 | 0 | 2 | 0 | **Hard** |
| Unnamed testimonials or "clients have said" paraphrases | 0 | 0 | 1 | 0 | **Hard** |
| Numeric facts per sentence, maximum | 5 (scoping) | ≤3 | 11 | ≤5; ≤3 outside a scoping sentence | **Hard** at 5; directional at 3 |
| Punch sentences (≤8 words) that have a finite verb and sit first or last in the paragraph | 100% | 100% | ~43% | 100% | Directional |
| Long–short pair (≤9 / ≥18) in every section opener and closer | yes | yes | none | yes | Directional |
| Paragraphs of 1–2 sentences | 59% | 73% | 30% | ≥55% | Directional |
| Body paragraphs over 110 words (boilerplate excluded) | 0 | 0 | 7 over 100 | 0 | Directional |
| Actor-first paragraph openers (Jacobs / We / Our / named person) | 33% | — | 0% | ≥30% | Directional |
| Paragraphs ending on a client-benefit clause | 35% bold + 34% verb tail | every subsection | 7% | ≥35% | Directional |
| Closing triads "X, Y, and Z" per 1,000 words | 17 | 12 | 0.5 | ≥8 | Directional |
| Colons / semicolons / em dashes per 1,000 words | 3 / 1.6 / 1.3 | 4.7 / 3.8 / 9.0 | 15.8 / 10.7 / 10.2 | ≤6 / ≤4 / ≤9 (aim ≤3) | Directional |
| Bold runs per 1,000 words; share that are outcome or proof | 32; high | 11; high | 5.6; 0% | 10–30; ≥70% | Directional |
| Headings carrying a finite verb | <20% | <20% | 0% (but 0 benefit headings) | ≤20%, ≤1 assertion heading per section | Directional |
| Headings with a benefit or capability noun | ~all | ~all | 0% | ≥80%; ≥1 per section names client or state | Directional |
| Words per heading measured on prose with sub-labels counted | 112 (57 headings / 6,400 words) | 85 (43 / 3,650) | 281 | 100–180 | Directional |
| Proof registers present per two consecutive pages (of 4) | 4 | 3–4 | 2 | ≥3 | Directional |
| Named, titled third-party voices per major section | ≥1 (ES) | ≥1 (ES) | 0 | ≥1 | Directional |
| Unshippable items per subsection (named person, named tool, client identifier, quantified offer) | ≥2 | ≥2 | mostly in placeholders | ≥2 | Directional |
| Win-theme phrases used ≥3 times including as a heading | 5 themes | 4–5 | 0 | 3–5 themes | Directional |
| Signature phrases appearing ≥2 times | ≥3 | ≥3 | 0 (one syntactic tic) | ≥3 | Directional |
| Non-signature 3-grams repeated within a section | 0 | 0 | 3 | 0 | Directional |
| Reference narratives with ≥3 relevance tags and ≥1 quantified accomplishment | all | n/a | 0 of 5 | all | Directional |
| Value-add commitments carrying a $ or measurable quantity | all | all | 0 of 2 | all | Directional |
| Rightmost column of proof exhibits names the client outcome | all | all | 0 of 10 | all | Directional |

### 4c. Recommended recalibration of `metrics.py` TARGETS

So that the tool's PASS/FAIL agrees with this guide: `punch_sentences_per_120_words` 0.5–1.3 (was ≥1); `words_per_heading` 100–220 (was 150–220); `client_paragraph_density` ≥0.40 (was ≥0.8); `so_what_rate` ≥0.10 informational (was ≥0.6); `avg_paragraph_words` ≤55 (was ≤110); `numbers_per_100_words` ≥3.0 (was ≥1.5). Add a bracket counter that catches any `[` in body prose, not only the four tag prefixes.

---

## 5. How to use this guide

1. Write from the fact pack with the section shape in Rule 11 and the device table in Rule 32.
2. Run `python voice/metrics.py <file> --client "Richmond" --client "the City" --json`; fix every hard-gate failure in 4a before anyone reads the prose.
3. Apply the judge tests in 4b, then score the eight dimensions in `voice/rubric.json`.
4. Release only on the rubric pass rule: every dimension ≥8, mean ≥8.5, all hard gates passed.
5. Strip the draft-notes footer before layout; body text must be bracket-free.
