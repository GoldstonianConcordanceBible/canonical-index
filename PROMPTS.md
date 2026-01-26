# PROMPTS.md — Standard Continuation Prompts (Goldstonian Doctrine)
**Purpose:** Copy/paste prompts that force GPT to keep continuity, stay aligned to **Mirror → Water → Fire**, and write in the correct “Goldstonian Doctrine” voice without drifting.

---

## 0) One-time setup prompt (use at the start of any session)
**Copy/paste:**
> You are my co-author and continuity engine for this book folder.  
> **Non-negotiables:**  
> 1) Stay aligned to **The Goldstonian Doctrine (Mirror → Water → Fire)**.  
> 2) Maintain continuity with `toc.md`, `outline.md`, and `doctrine-fit.md`.  
> 3) Never contradict the definitions in `canon/definitions.md`.  
> 4) No filler. No generic sermon tone. Keep it precise, builder-minded, and covenant-serious.  
> 5) Every chapter must include: **Chapter Aim**, **Key Idea**, **Draft**, **Mirror/Water/Fire checkpoint**, **Transition**.  
> 6) If you are uncertain, write a short “Assumptions” list **inside the chapter notes**, not as questions to me.  
> Start by confirming the chapter number/title and restating the doctrine thesis in one line: **“Forgiven ≠ Undone.”**

---

## 1) Generate a brand-new chapter (from scratch)
**Copy/paste:**
> Draft `manuscript/XX-chapter-XX.md` for this book using the chapter template.  
> Inputs you must honor:  
> - TOC placement: Chapter __ is titled “__________”  
> - Doctrine thesis: **Repentance restores standing; repair restores footprint. Forgiven doesn’t mean undone.**  
> - Keep the chapter *tight* (about 1,000–1,800 words) and structured with headings.  
> Required sections (in this order):  
> 1) Chapter Aim  
> 2) Key Idea  
> 3) Draft (with 3–6 subheadings)  
> 4) Mirror → Water → Fire checkpoint (bullets)  
> 5) Transition (leads into next chapter title explicitly)  
> Ensure at least **one** memorable “Goldstonian line” (short, quotable) appears in the Draft.

---

## 2) Continue a chapter where you left off (no rewriting earlier text)
**Copy/paste:**
> Continue drafting Chapter __ from the exact last sentence below.  
> **Do not rewrite** earlier paragraphs.  
> Add the next 600–1,000 words, keep doctrine alignment, and maintain the same voice, pacing, and argument logic.  
> End with a **clean transition paragraph** toward Chapter __ (“__________”).  
> Last sentence to continue from: “__________”

---

## 3) Tighten a chapter (reduce fluff, increase impact)
**Copy/paste:**
> Revise Chapter __ for density and clarity.  
> Goals:  
> - Remove repetition and vague phrasing  
> - Strengthen logic chains (cause → residue → repair → consequence)  
> - Keep “builder” tone, not generic inspiration  
> Constraints:  
> - Preserve headings and required sections  
> - Keep length within ±10% of current word count  
> - Add no new doctrine terms unless defined in `canon/definitions.md`  
> Output the full revised chapter.

---

## 4) Doctrine audit (make sure it’s Goldstonian, not generic)
**Copy/paste:**
> Run a **Doctrine Audit** on Chapter __.  
> Output:  
> 1) A checklist showing where Mirror/Water/Fire appears (quote short excerpts, max 1–2 sentences each)  
> 2) Any drift detected (generic tone, missing repair phase, cheap grace, unclear trespasser definition)  
> 3) Exact line edits to fix drift (provide replacement sentences)  
> 4) A final one-line summary that matches the Doctrine thesis.

---

## 5) Create “Goldstonian Lines” (quotables) for a chapter
**Copy/paste:**
> Create 15 original **Goldstonian lines** (one sentence each) that fit Chapter __.  
> Rules:  
> - Short, memorable, no clichés  
> - Must reinforce “Forgiven ≠ Undone” and Mirror/Water/Fire  
> - Avoid insults, avoid naming real people  
> Provide them as a numbered list.

---

## 6) Add Scripture integration without turning it into a commentary
**Copy/paste:**
> Add scripture integration to Chapter __ using **brief references** only (no long quotes).  
> Requirements:  
> - Reference 2 Chronicles 33 and 2 Kings 21 at least once each where relevant  
> - Keep focus on doctrine + systems residue, not verse-by-verse exposition  
> - Add a short “Scripture Anchors” subsection near the end with bullet references and 1-sentence tie-ins.

---

## 7) Build the glossary entries (canon-safe)
**Copy/paste:**
> Draft glossary entries for the following terms in `canon/definitions.md`.  
> Each entry: 2–5 sentences, doctrine-aligned, plain language, no fluff.  
> Terms: (paste list)

---

## 8) Create a “One-Page Doctrine Summary” for the back matter
**Copy/paste:**
> Write `manuscript/99-back-matter.md` section: **One-Page Doctrine Summary**.  
> Format:  
> - Title line  
> - 5 bullet “Doctrine laws” (short)  
> - Mirror/Water/Fire explained in 2–3 lines each  
> - Anti-Manasseh Protocol (5 steps)  
> - Final closing paragraph (strong, sober, builder tone)

---

## 9) Chapter-to-chapter continuity bridge (no duplication)
**Copy/paste:**
> Write a continuity bridge from Chapter __ to Chapter __.  
> Output two parts:  
> 1) A final paragraph for Chapter __ that tees up the next chapter’s central question  
> 2) An opening paragraph for Chapter __ that answers the tee-up and moves forward  
> Rules: no repeating full sentences from either chapter; keep it seamless.

---

## 10) “Where did I leave off?” tracker (for status.md)
**Copy/paste:**
> Update `status.md` fields based on this work session.  
> Output only the updated section:  
> - Last edited date (today)  
> - Working on (chapter)  
> - Next step (single sentence)  
> - Open questions (bullets if any)  
> Keep it short.

---

## 11) Fast drafting mode (if you want speed + structure)
**Copy/paste:**
> Fast Draft Mode for Chapter __:  
> 1) Provide a 6-bullet micro-outline (argument steps).  
> 2) Draft the chapter at ~1,200–1,500 words following the required section structure.  
> 3) Include exactly 3 “Goldstonian lines” labeled **[LINE]** inside the Draft.  
> 4) End with a Transition that names the next chapter title.

---

## 12) Quality gate (final pass before publishing)
**Copy/paste:**
> Apply the **Goldstonian Quality Gate** to Chapter __.  
> Check for:  
> - Mirror truth clarity (no evasive language)  
> - Water repair specificity (actionable, time-based)  
> - Fire consequence realism (no cheap grace, no despair)  
> - Definitions consistent with canon  
> - No contradictions with TOC logic  
> Output:  
> 1) Pass/Fail for each gate  
> 2) 5–10 surgical edits (exact replacements)  
> 3) Final “ready” version of the chapter.

---

## 13) Universal prompt to create any missing file
**Copy/paste:**
> Create the missing file: `books/<book-slug>/<path>/<filename>.md`  
> It must match the Goldstonian Doctrine voice and the repo’s canon rules.  
> Use clear headings, concise language, and link to adjacent files where helpful.  
> If the file is a template, make it reusable across books.

---