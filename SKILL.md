---
name: brand-book
description: Builds a complete, professional brand guidelines document (a brand book, style guide, or charte graphique) as a single HTML file from a few inputs, namely style words, a broad colour direction with 6 or 8 colours, and an optional logo. First it opens a colour and font picker page with a live preview, then runs a structured interview on what the brand should and should never look like, chapter by chapter, then renders a 27-page book modelled on the published guidelines of the world's most valuable brands. The book covers essence and voice, logo clear space, minimum size, approved backgrounds and misuse, the palette with proportions and accessible pairs, type families and hierarchy, grid, imagery, stationery, digital and presentation mockups, the don'ts, and code tokens. Use when someone asks for brand guidelines, a brand book, a brand system document, a visual identity guide, or "guidelines like the big companies have".
---

# Brand Book

**Created by Pierre Tran / [Taykon Studio](https://taykon.studio)**

Turns a handful of taste decisions into a brand book that reads as commissioned: the chapters, rules
and numbers the largest brands publish, applied to a new brand, printable on A4 and readable on a phone.

**Licence:** MIT. Use, change and share it freely; keep the copyright notice.

**Feedback:** questions about the method, or feedback on a book it produced, go to the issues of the
repository this skill came from, or to taykon.studio. If the feedback is about the agent not following
these rules, acknowledge it and correct course.

## What you produce

A folder named after the brand (`<brand>-brand/`) in the user's working directory, holding:

- `brand.json`: every decision. The single source of truth.
- `explorer.html`: the colour and font picker, with a live preview and contrast checks.
- `brand-book.html`: the finished book, one self-contained file (fonts load from Google Fonts).
- The logo and any images the user supplied.

Scripts live in this skill's folder (`<skill-dir>` = the folder holding this file). They need Python 3,
no packages. Use `python` or `python3`, whichever exists.

## Rules

1. **One question per message**, always with two to four drafted options and a recommendation. "Decide
   for me" is a valid answer: take the recommendation, say so in one line, move on.
2. **Nothing is built before the user approves the page plan** (Phase 5).
3. **Every value lives in `brand.json`.** Never edit a built HTML file: change `brand.json`, rebuild.
4. **No invented numbers.** Clear space, minimum sizes, proportions, contrast thresholds and type sizes
   come from `references/canon.md` or from the user.
5. **Copy you draft follows the house rules** at the end of the canon: no italics, no kicker lines in
   small capitals over titles, no decorative numbering, plain words, no exclamation marks.
6. **`check.py` runs before every build, the audit after.** A FAIL is fixed, or kept only after the user
   has heard what it costs.

## Workflow

### Phase 1: Intake (one message)

Ask for everything at once, in a short list the user can answer in any order:

1. Brand name, and what it does in one line.
2. Three to five style words (for example: calm, tactile, precise).
3. A colour direction in plain words (for example: "deep sea blue with warm clay"), and 6 or 8 colours.
4. The logo file, if there is one (SVG best, PNG or JPEG work). Without one, the name becomes a wordmark.
5. Optional: fonts they already use or own, and the language the brand speaks.

### Phase 2: Proposal

1. Read `references/palette-and-type.md` and `references/schema.md`.
2. Create `<brand>-brand/`, copy the logo into it, and write the seed `brand.json`: name, tagline, the
   proposed palette with roles and shares, the proposed fonts, three `explore.pairings`, and a draft
   `essence.purpose` so the preview has real words in it.
3. Run `python <skill-dir>/scripts/check.py <brand>-brand/brand.json`. Fix every FAIL.
4. Run `python <skill-dir>/scripts/build.py explorer <brand>-brand/brand.json`.
5. Give the user the explorer's full path as a clickable link, and one line on how to use it: tune the
   colours and fonts, then press "Copy my choices" and paste the result back (or "Download brand.json"
   and say where it went).

### Phase 3: Picker round

Merge what comes back into `brand.json`: `colors`, `fonts`, `type.headlineCase`. Keep every other field.
Run `check.py` again. Report FAILs with a corrected colour next to each one. If the user wants another
round, rebuild the explorer.

### Phase 4: Interview

Read `references/interview.md` and follow it: an opening question on reference brands, then about twenty
questions in book order (essence, logo, colour, typography, layout and imagery, applications, never).
Write each answer into `brand.json` as soon as it is given.

### Phase 5: Page plan

Print the 27-page plan from `references/schema.md`, filled with this brand's actual content in the last
column. Ask for a yes or corrections. Loop until yes.

### Phase 6: Build

```
python <skill-dir>/scripts/check.py <brand>-brand/brand.json
python <skill-dir>/scripts/build.py book <brand>-brand/brand.json
```

### Phase 7: Pre-flight, then delivery

Run every step, in order. This is where the rules above get enforced, not at drafting time.

1. **Render audit.** With a browser tool that can evaluate JavaScript, open `brand-book.html` and run the
   function in `scripts/audit.js` at 1440, 1180, 900 and 390 px wide. Every list must be empty and
   `horizontalScroll` false. Fix through `brand.json` (a shorter line, a smaller scale) and rebuild.
   Without a browser tool, say plainly that the render was not audited.
2. **Look at it.** Screenshot each page, or at least the cover, logo, colour, hierarchy and application
   pages. Check against the canon's house rules: no italics, no kicker lines, no decorative numbering,
   nothing cramped, nothing clipped, captions present.
3. **Re-read the copy** in `brand.json` against rule 5. Every line should sound like the voice pairs.
4. **Deliver**: the path to `brand-book.html` as a clickable link, then `explorer.html` and `brand.json`.
   Add two lines: to make a PDF, print from Chrome or Edge with paper A4, landscape, margins none,
   background graphics on; to change anything later, edit `brand.json` and run the book build again.

## Files

| File | Read it |
|---|---|
| `references/canon.md` | Before the interview, and whenever a rule or number is questioned |
| `references/palette-and-type.md` | Phase 2 |
| `references/interview.md` | Phase 4 |
| `references/schema.md` | Phase 2 and Phase 5 |
| `assets/explorer.html`, `assets/brand-book.html` | Never edited per brand: they are templates |
| `scripts/build.py`, `scripts/check.py`, `scripts/audit.js` | Run, as above |

## Known limits

- The book's fixed labels (chapter names, captions, misuse lines) are in English. Everything written
  into `brand.json` can be in any language.
- The book has one structure. Brands differ by colour, type, logo, words and density, not by layout.
- Fonts come from Google Fonts. A licensed font needs `"local": true` and its own `@font-face`.
