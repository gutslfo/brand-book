# The interview

Read this at the start of Phase 4. The interview turns taste into decisions: for every chapter, what the
brand should look like and what it must never look like. Each answer is written into `brand.json` the
moment it is given, so nothing lives only in the conversation.

## How to ask

- **One question per message.** The next question often depends on the last answer.
- **Always offer options.** Two to four concrete answers, drafted from what you already know, with the
  one you recommend first and marked. The user can pick, edit, or write their own. A blank question
  ("What is your purpose?") gets vague answers; a drafted one gets corrections, which are faster and
  better.
- **Draft the copy yourself.** Purpose lines, voice pairs, rules and never-lines are proposed by you and
  corrected by the user. Follow the canon's house rules when drafting: no italics, no exclamation marks
  in brand lines, plain words.
- **"Decide for me" is a valid answer.** Take the recommended option, say so in one line, move on. If the
  user says it for the whole interview, fill every field with the recommendations and go straight to the
  page plan.
- **Name the field.** End each question with the page it shapes ("This goes on the Essence page."), so
  the user sees the book being built.
- **Keep a running tally.** Every five questions, one line: what is settled, what is left.

## Opening question: references

"Name two or three brands, from any sector, whose look you admire, and one or two you would hate to be
confused with." Use the answer to calibrate every later proposal. It is not written into the book.

## Essence (pages: Essence, Voice)

1. **Purpose.** Draft three one-sentence purposes from the intake: what the brand does for people and
   why it matters. Under 15 words each. → `essence.purpose`
2. **Personality.** Offer six to eight candidate words from the style words, ask for three. Then draft a
   one-line meaning for each ("Calm: nothing shouts, space does the work."). → `essence.personality`
3. **Voice pairs.** For each trait, what it must never turn into: "Calm, not sleepy". Draft three or
   four pairs. → `essence.voice`
4. **Write this, not this.** Draft one sentence in the brand's voice and one that breaks it (the
   generic, over-excited version). → `essence.write`, `essence.avoid`

## Logo (pages: The logo, Clear space, Backgrounds, Misuse)

5. **Default colour.** Which palette colour the logo takes on light backgrounds. Recommend `primary`.
   → `logo.color`
6. **Clear space.** Define x. Recommend half the logo height; offer a visible part of the mark instead
   (the height of the symbol, the height of a capital). → `logo.clearSpace`, `logo.unitLabel`
7. **Minimum size.** Recommend from the canon: a compact symbol 24 to 32 px, a wordmark or a lockup 80 to
   120 px wide; print 20 to 30 mm. Ask what happens below it (use the symbol alone, or never go
   smaller). → `logo.minWidthPx`, `logo.minWidthMm`, `logo.smallUse`
8. **Approved backgrounds.** Show which palette colours the logo reads on (the explorer's logo row).
   Recommend the ones at 3:1 or more that feel on-brand; the accent is usually excluded. → `logo.backgrounds`
9. **Misuse.** All eight tiles by default (stretch, rotate, recolour, effects, busy, contrast, crowd,
   small). Ask if one does not apply. Brand-specific misuses the tiles cannot draw go to the Never page.
   → `logo.misuse`

## Colour (pages: Palette, Proportions, Accessible pairs)

10. **Should look like.** "Mostly light pages with colour used sparingly, or bold full-colour surfaces?"
    Adjust the shares accordingly and restate them. → `colors[].share`
11. **One job per colour.** Draft a short use line for each colour ("One call to action per page").
    → `colors[].use`
12. **Any FAIL left from check.py** is raised here, with a fixed colour proposed next to the original.
    The user decides; if they keep a failing colour, say what it costs in one line.

## Typography (pages: Families, Hierarchy)

13. **Density.** "Editorial (large display, lots of air) or functional (compact, more on the page)?"
    Editorial scale: 80 / 48 / 30 / 17 / 13 px. Functional: 56 / 36 / 24 / 16 / 13 px. Default: the
    scale in the example, 72 / 44 / 28 / 16 / 13. → `type.scale`
14. **Specimen lines.** Draft the five sample lines from the brand's own words: Display 18 characters or
    fewer, Headline 32 or fewer, Title 40 or fewer. → `type.samples`
15. **Rules.** Draft three to five typography rules (case, weights, minimum body size, line length).
    → `type.rules`, `fonts.*.role`

## Layout and imagery (pages: Grid and margins, Imagery)

16. **Corners.** Square (0 px), crisp (2 px), soft (8 px) or round (16 px). → `layout.radius`
17. **Should and should never.** Draft two layout rules ("One idea per page", "Images bleed or sit on the
    grid, they never float"). → `layout.rules`
18. **Image direction.** Photography, illustration, both, or none. Then draft one direction sentence and
    three do and three do-not lines. Ask whether they have up to three images to show (paths, embedded
    at build). → `imagery.direction`, `imagery.do`, `imagery.dont`, `imagery.images`

## Applications (pages: Stationery, Digital, Presentations and email)

19. **Details for the mockups.** Name, role, email, phone, website and address to print on the business
    card, letterhead and signature. Offer to use obvious placeholders (`example` domain, a fictional
    number) if they would rather not. → `contact`
20. **Lines for the mockups.** Button label, three navigation links, one social post line, one slide
    title. Draft them. → `cta`, `navLinks`, `social`, `slideTitle`

## Never (page: Never)

21. **Must never look like.** Draft six to eight never-lines from everything decided so far, including
    the reference brands the user did not want to be confused with, then ask what to add or cut.
    → `never`

## The page plan

After the last answer, print the plan before building: every page, what it shows, and where its content
comes from. Use the page list in `schema.md`. Ask for a yes or corrections. Nothing is built before the
yes.
