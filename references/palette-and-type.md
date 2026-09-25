# Proposing palettes and type pairings

Read this in Phase 3, before writing the seed `brand.json`. The goal is proposals good enough that the
picker round is choosing and fine-tuning, not starting over.

## Three directions, not three shades

When colours are missing, write three palettes in `explore.palettes`, each `{name, why, colors}`. They
must differ in character: for a warm brief, one earth-led, one led by a green or a blue, one quieter and
darker. Three variations of the same brown are one proposal. Give each a short name and a one-line
reason tied to the user's words ("Green leads, like a market stall awning").

Colours the user already has go into every proposal, unchanged, with `"given": true`. Build the missing
roles around them: if their colour is a strong mid-tone, it is the `primary`; if it is very dark or very
light, it is a base. A refused colour appears in no proposal. The first proposal is the one you
recommend.

## The palette, role by role

Work from the user's style words and colour direction. Build each role in this order, because each one
constrains the next. Lightness values are OKLCH L (0 is black, 1 is white). Chroma values are OKLCH C.

| Role | What it is | Target |
|---|---|---|
| `light` | The page. Carries most of the surface. | L 0.95 to 0.98, C 0.005 to 0.02. Warm off-white for tactile, crafted, organic words; cool off-white for tech, clinical, precise; pure `#FFFFFF` only for corporate or medical. |
| `dark` | Text and dark surfaces. | L 0.15 to 0.22, C 0.01 to 0.03, tinted toward the primary hue. Never pure `#000000` unless the brand is monochrome by intent. |
| `primary` | The ownable colour. The logo and brand surfaces. | Taken from the colour direction. L 0.35 to 0.55 so it carries light text and reads on `light` (3:1 or more both ways). |
| `accent` | Action and emphasis, rationed. | A contrasting hue (warm against cool, or 120 to 180 degrees from primary), C higher than primary. L 0.45 to 0.55 so a label on it reaches 4.5:1. |
| `secondary` | Quiet panels and image grounds. | A light or mid tint, L 0.80 to 0.90, from the direction's second colour or from primary. |
| `support` | Everything else: one for a 6-colour palette, three for 8. | A mid neutral that can carry secondary text on `light` (L 0.50 or darker), a tint of primary, and for 8 colours one seasonal or expressive hue. |

Default shares (they must add up to 100): light 40 to 55, dark 15 to 25, primary 10 to 20, secondary 5 to 10,
accent 3 to 8, supports share the rest. This is the canon's 60 / 30 / 10 made concrete.

Name each colour with a short, concrete noun that fits the brand (Paper, Ink, Sea, Clay), not a hex
description ("Dark blue 2"). Names appear on every colour page.

After writing the palette, run `check.py`. Fix every FAIL before showing the explorer: a proposal that
fails contrast wastes the user's first look.

## The type pairing

Pick two families (three with a mono) with a clear job each. Offer three or four pairings in
`explore.pairings`, each with a one-line reason, so the user chooses between directions, not fonts.
Then write a shortlist of about six families per role in `explore.shortlist` (`display`, `text`,
optionally `mono`): the picker shows them as "Picked for this brand", above the search.

Research with the catalogue, not from memory alone. `scripts/fonts.py search` filters the 1,600 Latin
families of Google Fonts by category and number of weights, sorted by popularity:

```
python <skill-dir>/scripts/fonts.py search --category serif --weights 2 --skip-top 30
python <skill-dir>/scripts/fonts.py search --category sans --weights 3 --skip-top 30 --limit 60
python <skill-dir>/scripts/fonts.py check "Young Serif" "Figtree"
```

`--skip-top 30` leaves out the thirty most used families (Roboto, Open Sans, Montserrat, Poppins and
the like), which is how a proposal avoids looking like every generated site. Combine the list with what
you know of each face's character, and run `check` on every family you write down: a wrong name or a
weight the family does not ship stops the font from loading.

Fonts the user already has stay in place. If they gave one role (a headline face), pair it: the three
pairings keep their font and vary the other role. Their own files go in `fonts.<role>.file`, their
installed fonts get `"local": true`.

| Style words | Display | Text | Mono |
|---|---|---|---|
| editorial, calm, literary, considered | Newsreader, Source Serif 4, Spectral | Hanken Grotesk, Inter, Public Sans | DM Mono |
| luxury, couture, refined, precise | Bodoni Moda, Cormorant Garamond, Playfair Display | Instrument Sans, Manrope | none |
| warm, crafted, organic, human | Fraunces, Young Serif, Lora | Figtree, DM Sans, Instrument Sans | none |
| modern, technical, clear | Schibsted Grotesk, Space Grotesk, Inter | Inter, IBM Plex Sans | JetBrains Mono, IBM Plex Mono |
| bold, loud, sporty, urgent | Anton, Bebas Neue, Archivo Black, Oswald | Archivo, Inter | Space Mono |
| friendly, approachable, playful | Bricolage Grotesque, Sora, Outfit | Plus Jakarta Sans, Figtree | none |
| institutional, trusted, public | Source Serif 4, Libre Caslon Text, EB Garamond | Public Sans, IBM Plex Sans | IBM Plex Mono |
| cultural, experimental, art | Syne, Unbounded, Gloock, Darker Grotesque | Space Grotesk, Onest | Fragment Mono |

Pairing rules:

- Contrast of structure (a serif over a sans), or one family doing both jobs. Never two sans serifs that
  look alike.
- The text family needs at least two weights. Display-only faces (Anton, Bebas Neue, Instrument Serif,
  DM Serif Display, Gloock, Young Serif) never set body text.
- Weights come from the catalogue: two per family, regular plus the nearest strong weight it ships. The
  picker does this on its own when the user clicks a family.
- A licensed font the user owns as a file (WOFF2, WOFF, OTF, TTF): put the file in the brand folder and
  set `fonts.<role>.file`. The build embeds it, so the book shows it on any machine. A font only
  installed on their computer: `"local": true`, and it shows on that computer only.
- Avoid defaulting to the most common generated pairings (Inter with Playfair Display, Poppins with
  anything). Offer them only when the brief really points there.

Headline case: sentence case unless the style words are loud (bold, sporty, urgent, industrial), where
capitals with +4% tracking fit. The explorer lets the user flip it.
