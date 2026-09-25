# The canon: what the world's biggest brands put in their guidelines

Read this before the interview (Phase 4) and before writing any rule into `brand.json`. Every default
in this skill traces back to a line in this file. When a user asks "why is it like that?", the answer
is here.

## Sources

Collected in September 2026 from 19 brands ranked in the 2025 Interbrand *Best Global Brands* or the
2026 Kantar BrandZ top 100. Official pages or PDFs unless marked *secondary*. It is not 100 brands:
past about fifteen, the structure stops changing and only the values move.

| Brand | Source |
|---|---|
| Microsoft | Microsoft logo third party usage guidance (PDF, Aug 2025); Microsoft Learn branding page |
| Google | Partner Marketing Hub, "How to show Google's brand"; Material Design 3 type scale |
| IBM | IBM Logo Guidelines for Strategic Partners v1.2; ibm.com/brand logo page; Carbon 2x Grid |
| Visa | Visa Fundamental Brand Standards (PDF, Sept 2025) |
| Mastercard | Mastercard Brand Center, branding requirements; Mastercard Design Center |
| Netflix | brand.netflix.com, Logos |
| Spotify | Spotify for Developers, Design & Branding Guidelines; Spotify Connect logo guidelines (PDF) |
| Meta / Facebook | Meta Brand Resource Center, Facebook logo |
| Instagram | Meta Brand Resource Center, Instagram icons |
| YouTube | YouTube Brand Resources |
| Adobe | Adobe Corporate Brand Guidelines (PDF) |
| Cisco | Cisco Brand Center, Logo Usage and Guidelines |
| eBay | eBay Playbook, Foundations: Logo, Color, Typography |
| Slack (Salesforce) | Slack Brand Guidelines (PDF) |
| Starbucks | Starbucks Creative Expression: Color, Typography, Logos |
| Mailchimp (Intuit) | Mailchimp Content Style Guide, Voice and Tone |
| Uber | *secondary*: press coverage of the 2018 system and published quick guide excerpts |
| Airbnb | *secondary*: Airbnb trademark guidelines plus design press |
| Siemens | *secondary*: agency case study (MetaDesign) plus design press |

## 1. The chapters every serious book has

Starbucks: Theory, Logos, Color, Voice, Typography, Illustration, Photography. Uber: logo, color,
typography, iconography, illustration, photography, motion, composition. Adobe splits the logo alone
into Clear space and minimum size, Usage, Variations, Misuse.

The common spine, in the order this skill renders it:

1. **Essence**: purpose, personality, voice.
2. **Logo**: the mark, clear space, minimum size, approved backgrounds, misuse.
3. **Colour**: palette with values, roles, proportions, accessible pairs.
4. **Typography**: families with named roles, hierarchy, rules.
5. **Layout and imagery**: grid, margins, image direction.
6. **Applications**: the system on real surfaces.
7. **Never**: the global don'ts.
8. **Tokens**: the values in a form a developer can paste.

## 2. Logo rules

**Clear space is always measured with a unit taken from the logo itself, never in absolute units.**
That way it scales with the logo.

| Brand | Clear space unit | Minimum size, screen | Minimum size, print |
|---|---|---|---|
| Microsoft | height of the four-square symbol | 16 px symbol, 72 px full logo | 5.5 mm symbol, 25.4 mm full logo |
| Google | width of the G | | |
| IBM | height of the 8-bar logo | 16 pt | |
| Visa | height of the V, on all sides | 36 px | 12.7 mm |
| Mastercard | 1/4 of the width of one circle | 120 px horizontal mark | |
| Netflix | width of one leg of the N (symbol), width of the T (wordmark) | | |
| Spotify | 1/2 of the logotype height | 70 px logo, 21 px icon | 20 mm logo, 6 mm icon |
| Facebook | derived from the logo width | 16 px | 6 mm |
| Instagram | half of the glyph size | 29 px | |
| YouTube | size of the triangle in the icon | 20 px height | |
| Slack | one lozenge (stacked), one octothorpe (horizontal) | about 50 px | |
| Cisco | height of the longest bar of the bridge | | |
| eBay | x-height; clear space and page margin both 5% of the layout's shortest side | 24 px height | 0.25 in |

What this means for the book:

- Name the unit. Call it **x** and define it as a visible part of the mark (a letter height, a symbol
  height). Default when the user has no opinion: **x = half the logo height**, which sits in the middle of
  the range above (from 1/4 of an element up to one full symbol height).
- Give two minimum sizes, one for screen in px and one for print in mm. A simple symbol is legible
  from about 16 to 24 px. A wordmark needs 70 to 120 px. Print minimums run from 5.5 to 25 mm.
- Give a small-size fallback. YouTube and Spotify both switch to the icon when the full logo cannot
  hold its minimum size and clear space.
- **Approved backgrounds are a closed list.** Slack allows the full-colour logo only on white, black
  or its aubergine. Cisco uses the two-colour logo on light and knocks everything out to white on
  dark. Uber allows only black and white.

**Misuse: the list is the same everywhere.** Every one of these shows up in at least two of the
sources:

| Misuse | Cited by |
|---|---|
| Stretching, squashing, distorting | Spotify, Slack, Adobe, Visa, Instagram |
| Rotating | Spotify, Adobe, Instagram |
| Recolouring outside the approved colours | Slack, Visa, Adobe |
| Adding effects (shadow, glow, gradient, bevel) | Adobe, Visa |
| Outlining | Slack |
| Cropping or separating the parts | Slack, Adobe |
| Recreating or retyping in another font | Slack, Adobe |
| Busy or low-contrast backgrounds | Visa, Slack, Cisco |
| Going below the minimum size | all |

## 3. Colour rules

- **One ownable colour plus neutrals carry nearly everything.** Uber: black and white dominate, Safety
  Blue only "sparingly for moments of support, assurance and delight". Starbucks: "brand greens should
  always have a presence" in every composition, while expressive colours rotate with the seasons.
  Airbnb protects Rausch so tightly that its trademark rules forbid third parties from featuring it
  prominently.
- **The accent is rationed.** It marks action and emphasis. It never fills a whole surface. The
  default proportion this skill uses is 60 / 30 / 10 (neutral base, brand colour, accent), which is
  the pattern above written as numbers. Supporting colours share whatever is left.
- **Core versus extended.** eBay keeps 4 logo colours as the core, then runs 17 colour families of 8
  shades each for the product. A brand book defines the core. A product team builds the ramps later.
- **Each colour gets its values and a role.** HEX and RGB for screen. Print values (CMYK, Pantone)
  come from the printer's proofs and are never computed. Visa asks for spot colours in print for this
  reason.
- **Accessibility is a number, not an adjective.** WCAG 2.2: 4.5:1 for body text, 3:1 for large text
  (24 px and up, or 18.66 px bold) and for interface components. The book prints the ratio for every
  pair.

## 4. Typography rules

- **Two or three families, each with a named role.** Starbucks: Sodo Sans for body copy, Lander (a
  serif) for expressive moments, Pike for functional headlines. Uber Move comes as Display, Text and
  Mono. IBM Plex comes as Sans, Serif and Mono.
- **Few weights.** eBay uses regular and bold "in all of our applications". Two weights per family is
  enough.
- **Hierarchy has named levels.** Material 3 uses five roles (Display, Headline, Title, Body, Label)
  in three sizes each. Display Large is 57/64 px with -0.25 tracking. Line height is about 1.2× the
  size for display and headline, and about 1.5× for body.
- **Rules written as numbers.** Size, line height, tracking and case for each level, plus a comfortable
  line length of 45 to 75 characters for running text.

## 5. Layout and grid

- IBM's 2x Grid: an 8 px mini unit, with columns divided by twos (1, 2, 4, 8 or 16). Every dimension
  is a multiple of the unit.
- eBay sets the page margin equal to the logo clear space: 5% of the shortest side of the layout.
- The book states the column count, the gutter, the margin rule and the base unit, then shows one
  layout on the grid.

## 6. Voice

- **Voice stays the same, tone adapts.** Mailchimp: "You have the same voice all the time, but your
  tone changes."
- **Write it as pairs.** Mailchimp is "weird but not inappropriate, smart but not snobbish". Each
  trait is bounded by the thing it must not turn into. The book uses "We are / We are not" pairs,
  three or four of them.
- "It's always more important to be clear than entertaining."

## 7. House rules for the document itself

The canon above covers what goes in a book. These rules decide whether the result reads as
commissioned or generated. The template already respects them, and so must anything written into it:

- No kicker or eyebrow line in small capitals above a title, and no short bar or dash in front of
  one.
- No italics anywhere. Emphasis comes from colour, size or placement.
- No decorative numbering (01, 02, Fig. 1). A number only appears when it is a real quantity: a page
  number, a size, a ratio.
- No text below 12 px on screen (9 pt in print). Body text sits around 14 to 16 px.
- One type scale for the whole book (six sizes) and one spacing scale. One twelve-column grid on
  every page.
- Captions under specimens, and the same rules and dividers on every page.
- No stock photography. Use the user's own images, or state the image direction in words.
