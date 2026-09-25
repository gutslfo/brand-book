# Proposing a palette and a type pairing

Read this in Phase 2, before writing the seed `brand.json`. The goal is a first proposal good enough that
the explorer round is fine-tuning, not starting over.

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

Pick two families (three with a mono) with a clear job each. Offer three pairings in
`explore.pairings`, each with a one-line reason, so the user chooses between directions, not fonts.

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
- A face from the explorer's catalogue loads with verified weights. Anything else: the user types its
  exact Google Fonts name, and it loads at 400 only.
- A licensed font the user owns: set `"local": true` on that role and tell them to add its `@font-face`
  to the built page, or to install it on the machine that opens the book. The book cannot fetch it.
- Avoid defaulting to the most common generated pairings (Inter with Playfair Display, Poppins with
  anything). Offer them only when the brief really points there.

Headline case: sentence case unless the style words are loud (bold, sporty, urgent, industrial), where
capitals with +4% tracking fit. The explorer lets the user flip it.
