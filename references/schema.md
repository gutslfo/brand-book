# brand.json

One file drives both pages. The explorer and the book read it, `check.py` validates it, `build.py`
embeds the logo and images into it. Never edit the built HTML: change `brand.json` and rebuild.
A complete working example lives in `docs/example/brand.json` in this skill's repository.

## Fields

Required fields are marked. Everything else has a default, shown in the last column.

| Field | Type | Notes | Default |
|---|---|---|---|
| `name` | string, required | The brand name. Also the wordmark when there is no logo file. | |
| `tagline` | string | One line. Used on the web hero, grid mock, hierarchy. | the name |
| `version`, `date` | string | Shown on the cover and in the footer. | `1.0`, none |
| `essence.purpose` | string | One sentence, under 15 words. | |
| `essence.personality` | list of `{word, line}` or strings | Three words, each with a one-line meaning. | |
| `essence.voice` | list of `{is, not}` | Three or four "We are / We are not" pairs. | |
| `essence.voiceNote` | string | Intro under the Voice title. | a generic line |
| `essence.write`, `essence.avoid` | string | One sentence in the voice, one that breaks it. | page omits them |
| `essence.letter` | string | Body of the letterhead mockup. | the purpose |
| `logo.file` | path | SVG, PNG or JPEG, relative to `brand.json`. Omit for a wordmark. | wordmark |
| `logo.color` | colour name | Logo colour on light backgrounds. | the primary |
| `logo.fullColour` | bool | True for a multi-colour logo: the primary view shows the file as is. Other views use a one-colour silhouette. | false |
| `logo.clearSpace` | number | x as a fraction of the logo height. | 0.5 |
| `logo.unitLabel` | string | How x is described in the text. | "half the height of the logo" |
| `logo.minWidthPx`, `logo.minWidthMm` | number | Minimum width on screen and in print. | 96 (80 for a wordmark), 25 |
| `logo.smallUse` | string | What to do below the minimum. | none |
| `logo.backgrounds` | list of colour names | The closed list of approved backgrounds. | colours at 3:1 or more |
| `logo.misuse` | list | Any of `stretch rotate recolor effects busy contrast crowd small`. | all eight |
| `logo.note`, `logo.crowdText` | string | Text on the logo page, text in the crowding tile. | generic lines |
| `colors` | list, required for the book | 6 or 8 of `{name, hex, role, share, use, given}`. The picker fills it from the first proposal when it is missing. | |
| `colors[].given` | bool | The user brought this colour: it stays in every proposal and is marked "yours". | false |
| `colors[].role` | required | Exactly one each of `dark`, `light`, `primary`, `accent`. At most one `secondary`. The rest `support`. | |
| `colors[].share` | integer | Percent of a typical page. All shares add up to 100. | |
| `fonts.display`, `fonts.text` | object, required | `{family, weights, weight, fallback, role, local}` | |
| `fonts.mono` | object | Same shape. Omit for a two-family system. | none |
| `fonts.*.weights` | list | The weights to load, two per family. | `[400]` |
| `fonts.display.weight` | number | The weight headlines use. | first weight |
| `fonts.*.file` | path | The user's own font file (WOFF2, WOFF, OTF, TTF), embedded at build. | none |
| `fonts.*.local` | bool | True for a font that is not on Google Fonts: a file, or a font installed on the user's machine. | false |
| `type.headlineCase` | `none` or `upper` | Sentence case or capitals for headlines. | `none` |
| `type.headlineTracking` | number, em | Letter spacing for headlines. | -0.015, or 0.04 in capitals |
| `type.scale` | list of `{level, font, size, leading, tracking}` | Five levels. Sizes in px, 12 or more. | 72 / 44 / 28 / 16 / 13 |
| `type.samples` | object | Specimen line per level name. | built from the essence |
| `type.rules`, `type.familiesNote` | list, string | Shown on the Hierarchy and Families pages. | none, a generic line |
| `layout.columns`, `layout.gutter`, `layout.unit` | number | Grid page values. | 12, 2, 8 |
| `layout.radius` | number, px | Corner radius for buttons and cards. | 2 |
| `layout.margin`, `layout.rules` | string, list | Grid page text. | the eBay 5% rule, none |
| `imagery.direction`, `imagery.do`, `imagery.dont` | string, lists | Imagery page. | |
| `imagery.images` | list of `{file, caption}` | Up to three images, embedded at build. | none |
| `contact` | object | `person, role, email, phone, web, address, brandContact` for the mockups and back cover. | |
| `cta`, `navLinks`, `social`, `slideTitle` | strings, list | Lines inside the mockups. | generic lines |
| `never` | list | The Never page. Six to eight lines. | |
| `chapters` | object | Override a chapter's divider line, keyed by chapter name. | generic lines |
| `paletteNote`, `neverNote` | string | Intro lines on those pages. | generic lines |
| `explore.palettes` | list of `{name, why, colors}` | The three palette directions in the picker. Given colours appear in each. | none |
| `explore.pairings` | list of `{display, text, mono, why}` | The font pairings in the picker. | none |
| `explore.shortlist` | `{display, text, mono}` lists | About six families per role, shown as "Picked for this brand". | none |
| `explore.start` | `colours` or `fonts` | Which tab the picker opens on. Use `fonts` when only fonts are missing. | `colours` |
| `intake` | object | The user's answers (`feeling`, `lightness`, `colour`, `typeVoice`, `admire`, `avoid`), kept for drafting the book's words. Not rendered. | none |

## The pages

What each page shows and which fields feed it. Use it to draft the fields in Phase 5, and to walk the
user through the book in Phase 6.

| Page | Title | Shows | From |
|---|---|---|---|
| 1 | Cover | Logo on primary, "Brand guidelines", version and date | `logo`, `version`, `date` |
| 2 | Contents | Chapters and their page numbers | computed |
| 3 | Essence | Divider | `chapters` |
| 4 | Essence | Purpose, three traits with their meaning | `essence.purpose`, `essence.personality` |
| 5 | Voice | We are / We are not, write this / not this | `essence.voice`, `essence.write`, `essence.avoid` |
| 6 | Logo | Divider | |
| 7 | The logo | Primary on light, reversed on dark | `logo.file`, `logo.color` |
| 8 | Clear space and minimum size | x diagram, actual-size minimum | `logo.clearSpace`, `logo.minWidth*` |
| 9 | Backgrounds | Logo on every colour, approved or avoid | `logo.backgrounds` |
| 10 | Misuse | Eight mistakes, drawn from the real logo | `logo.misuse` |
| 11 | Colour | Divider | |
| 12 | Palette | Swatches with name, role, HEX, RGB | `colors` |
| 13 | Proportions | Share bar and one use line per colour | `colors[].share`, `colors[].use` |
| 14 | Accessible pairs | Every text and background pair with its contrast ratio | computed |
| 15 | Typography | Divider | |
| 16 | Families | Each family, its weights, its character set, its job | `fonts` |
| 17 | Hierarchy | Five levels with size, leading, tracking, and rules | `type.scale`, `type.samples`, `type.rules` |
| 18 | Layout and imagery | Divider | |
| 19 | Grid and margins | A page on the twelve-column grid, the grid values and rules | `layout` |
| 20 | Imagery | Direction, images, do and do not | `imagery` |
| 21 | Applications | Divider | |
| 22 | Stationery | Business card front and back, letterhead, envelope | `contact` |
| 23 | Digital | Website first screen, social post | `cta`, `navLinks`, `social` |
| 24 | Presentations and email | Title slide, email signature | `slideTitle`, `contact` |
| 25 | Never | The global don'ts | `never` |
| 26 | Tokens | CSS variables, download buttons | computed |
| 27 | Back cover | Logo and brand contact | `contact.brandContact` |
