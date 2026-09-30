---
name: brand-book
description: Builds a professional brand guidelines document (brand book, style guide, charte graphique) as one HTML file. It asks what the person already has (logo, colours, fonts), asks a few questions only about what is missing, then opens a picker page with three palette proposals, font pairings, search across all of Google Fonts, room for the person's own fonts and a live preview. From the choices it writes a 27-page book modelled on the published guidelines of the world's most valuable brands: essence and voice, logo clear space, minimum size and misuse, palette, proportions and accessible pairs, type and hierarchy, grid, imagery, stationery, digital and slide mockups, the don'ts, and code tokens. Use when someone asks for brand guidelines, a brand book, a visual identity guide, help choosing brand colours or fonts, or "guidelines like the big companies have".
---

# Brand Book

**Created by Pierre Tran / Taykon Studio**

Turns what a person already knows about their brand, and a few answers about what they do not know
yet, into a brand book that reads as commissioned: the chapters, rules and numbers the largest brands
publish, applied to a new brand, printable on A4 and readable on a phone.

**Licence:** MIT. Use, change and share it freely; keep the copyright notice.

**Feedback:** questions about the method, or feedback on a book it produced, go to
[github.com/gutslfo/brand-book/issues](https://github.com/gutslfo/brand-book/issues), or to pierre@taykonstudio.com.
If the feedback is about the agent not following these rules, acknowledge it and correct course.

## What you produce

A folder named after the brand (`<brand>-brand/`) in the user's working directory, holding:

- `brand.json`: every decision. The single source of truth.
- `explorer.html`: the picker, with the proposals, the font search, the user's own fonts, a live
  preview and contrast checks.
- `brand-book.html`: the finished book, one self-contained file.
- The logo, the user's own font files, and any images they supplied.

Scripts live in this skill's folder (`<skill-dir>` = the folder holding this file). They need Python 3,
no packages. Use `python` or `python3`, whichever exists.

## Rules

1. **Ask only about what is missing.** Whatever the user already has (logo, colours, fonts) is taken as
   given, never questioned, and pinned in every proposal.
2. **Proposals live in the picker, not in the chat.** Palettes and fonts are shown as a page the user can
   click through. The chat carries the link and one line on what to do. Do not describe colours or fonts
   at length in a message.
3. **Every value lives in `brand.json`.** Never edit a built HTML file: change `brand.json`, rebuild.
4. **No invented numbers.** Clear space, minimum sizes, proportions, contrast thresholds and type sizes
   come from `references/canon.md` or from the user.
5. **Copy you draft follows the house rules** at the end of the canon: no italics, no kicker lines in
   small capitals over titles, no decorative numbering, plain words, no exclamation marks.
6. **`check.py` runs before every build, the audit after.** A FAIL is fixed, or kept only after the user
   has heard what it costs.
7. **The skill does not design logos.** Without a logo file, the brand name is set in the chosen display
   font and used as a wordmark throughout the book.

## Where it runs, and who it is for

The skill runs in Claude Code and in the Claude apps (claude.ai, desktop, mobile) with code execution on.
Many people who use it have never opened a terminal. So:

- **You run everything.** Never ask the person to run a command, open a folder, or edit `brand.json`.
  Scripts, paths and file names are your business; talk about "the picker" and "your brand book".
- **Files reach them the way the environment allows.** Where they share a file system with you (Claude
  Code), give each file's full path as a clickable link. Where they do not (the Claude apps), write the
  brand folder in your working directory, then share `explorer.html` and `brand-book.html` as files they
  can download or open, using whatever the environment provides for files meant for the user.
- **Say what to do with the picker in one plain line**, for example: "Open the picker, choose a direction
  and fonts, then press Copy my choices and paste the result here." In the apps, add that it opens in any
  browser once downloaded.
- **Logos and font files arrive as attachments** in the apps. Save them into the brand folder.

## Workflow

### Phase 1: What do you already have?

Read `references/intake.md`. Ask the first round: the brand name and what it does, then whether the logo,
the colours and the fonts already exist. Use a multiple-choice question tool if the environment has one;
otherwise one short message with the options written out. Collect whatever exists: logo file, hex values,
font names or font files.

### Phase 2: The atmosphere, only for what is missing

If colours or fonts (or both) are missing, ask the atmosphere questions from `references/intake.md`: the
feeling, light or dark, colour temperature, the voice of the type, and the brands to admire or avoid. Only
the questions that serve a missing element. Say once that more detail gives sharper proposals. If
everything already exists, skip this phase.

### Phase 3: Research and proposals

1. Read `references/palette-and-type.md` and `references/schema.md`.
2. **Colours missing or partial:** build three palette directions that differ in character, not in shade,
   each with the user's own colours pinned (`"given": true`) and the rest proposed.
3. **Fonts missing or partial:** search the catalogue with `python <skill-dir>/scripts/fonts.py search`
   (by category, number of weights, and `--skip-top` to leave out the fonts every generated site uses),
   combine it with what you know of each family's character, then write three or four pairings and a
   shortlist of six per role. The user's own fonts go in as given.
4. Create `<brand>-brand/`, copy in the logo and any font files, and write the seed `brand.json`: name,
   tagline, a draft purpose line so the preview has real words, `explore.palettes`, `explore.pairings`,
   `explore.shortlist`, and `fonts` set to the first pairing (or the user's fonts).
5. Run `python <skill-dir>/scripts/check.py <brand>-brand/brand.json` and fix every FAIL. A proposal that
   fails contrast never reaches the user.
6. Run `python <skill-dir>/scripts/build.py explorer <brand>-brand/brand.json`, then hand over the
   picker as described in "Where it runs", with one line: pick a direction, adjust it, then press "Copy
   my choices" and paste the result here. Own font files added in the picker must be attached to the
   conversation: they cannot travel in the copied text.

### Phase 4: Choices back

Merge what comes back into `brand.json` (`colors`, `fonts`, `type.headlineCase`), keeping every other
field. Copy any new font files into the brand folder. Run `check.py`. Report a FAIL with a corrected
colour next to it; rebuild the explorer only if the user wants another look.

### Phase 5: Write and build the book

1. Draft every text field from what the user said: purpose, three personality words with their meaning,
   voice pairs, a line to write and a line to avoid, logo rules from the canon's defaults, type samples
   and rules, layout rules, image direction, mockup lines, and the never list (include what they said to
   avoid). `references/schema.md` lists each field and its page.
2. Run `check.py`, then `python <skill-dir>/scripts/build.py book <brand>-brand/brand.json`.
3. **Pre-flight.** With a browser tool that can evaluate JavaScript, open the book and run the function
   in `scripts/audit.js` at 1440, 1180, 900 and 390 px wide. Every list must be empty and
   `horizontalScroll` false. Fix through `brand.json` and rebuild. Look at the pages (or at least the
   cover, logo, colour, hierarchy and applications pages) against the canon's house rules. Without a
   browser tool, say plainly that the render was not audited.
4. **Deliver** `brand-book.html`, then `brand.json`, as described in "Where it runs". Two lines: for a
   PDF, open the book in Chrome or Edge and print it on A4, landscape, no margins, background graphics
   on; to change anything later, ask in this conversation (or a new one, with `brand.json` attached).

### Phase 6: Refine, if wanted

Offer once: "Want to go through the pages and adjust the words or the rules?" If yes, follow
`references/interview.md`, one question at a time, then rebuild.

## Files

| File | Read it |
|---|---|
| `references/intake.md` | Phases 1 and 2 |
| `references/palette-and-type.md` | Phase 3 |
| `references/schema.md` | Phases 3 and 5 |
| `references/canon.md` | Phase 5, and whenever a rule or number is questioned |
| `references/interview.md` | Phase 6 |
| `assets/explorer.html`, `assets/brand-book.html` | Never edited per brand: they are templates |
| `assets/fonts.json` | The Google Fonts catalogue snapshot; `fonts.py refresh` updates it |
| `scripts/fonts.py`, `scripts/build.py`, `scripts/check.py`, `scripts/audit.js` | Run, as above |

## Known limits

- The book's fixed labels (chapter names, captions, misuse lines) are in English. Everything written
  into `brand.json` can be in any language.
- The book has one structure. Brands differ by colour, type, logo, words and density, not by layout.
- Fonts come from Google Fonts or from the user's files. A font installed only on the user's machine
  shows on that machine and falls back elsewhere.
