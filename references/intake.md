# Intake: what exists, and what the brand should feel like

Read this in Phases 1 and 2. The intake is short on purpose: a couple of rounds of questions, then the
answers take visual form in the picker. Nobody should have to describe a colour in words when they can
click on it.

## How to ask

- Use a multiple-choice question tool when the environment has one: it takes several questions at once,
  each with up to four options plus a free answer. Otherwise, one message with the options written as a
  short list the user can answer in any order.
- Every question offers options. The free answer is always open, and detail is always welcome: say once
  that more detail gives sharper proposals.
- Never ask about something the user already gave.

## Round 1: what already exists

1. **Name and activity.** "What is the brand called, and what does it do, in one line?"
2. **Logo.** Options: "Yes, I have a file" (then ask for the path or the attachment: SVG best, PNG or
   JPEG work), "Not yet". Without a logo, the book uses the name as a wordmark in the chosen font. The
   skill does not design logos: say so in one line if they ask.
3. **Colours.** Options: "All defined" (ask for the hex values, or a file or page where they are),
   "Some" (ask for those), "None yet".
4. **Fonts.** Options: "Defined" (ask for the names, or the font files), "One of them" (which role:
   headlines or text), "None yet".

If the user's palette has fewer than 6 colours, the missing roles are proposed around theirs. If it has
more than 8, ask which 6 or 8 are the brand's core; the rest are left out of the book.

## Round 2: the atmosphere (only for what is missing)

Ask the questions that serve a missing element. Colours missing: 1, 2, 3, 5. Fonts missing: 1, 4, 5.
Both missing: all five.

1. **The feeling.** "Which of these is closest? Pick one, or give your own words." Options: "Quiet and
   refined", "Warm and human", "Bold and energetic", "Sharp and technical". Free words are better than a
   pick: take up to five of them.
2. **Light or dark.** Options: "Mostly light pages", "Mostly dark", "Colour-led: big surfaces of the brand
   colour".
3. **Colour.** "A colour you love, or one you refuse?" Options: "Warm (earth, terracotta, sand)", "Cool
   (sea, slate, green)", "Neutral with one strong colour", "Surprise me". A named colour ("deep sea blue",
   "no pink") beats any option.
4. **The voice of the type.** Options: "Classic, with serifs", "Modern, without serifs", "Serif headlines
   with simple text", "Expressive, with character".
5. **References.** "Two or three brands whose look you admire, from any sector, and one you would hate to
   be confused with." Optional, and the single most useful answer.

## What the answers become

| Answer | Drives |
|---|---|
| Feeling words | Palette temperature and contrast, type category, the three palette directions, the personality words in the book |
| Light or dark | Which role carries the most share, and the `light` and `dark` values |
| Colour love or refusal | The primary hue and the accent; a refused colour appears in no proposal |
| Voice of the type | Which categories `fonts.py search` looks in, and the pairings |
| References | The spread between the three directions; the "avoid" brand goes into the never list |

Record the answers in `brand.json` under `intake` (free-form: `feeling`, `lightness`, `colour`,
`typeVoice`, `admire`, `avoid`). The explorer ignores that field; it is there so Phase 5 can draft the
book's words from the user's own.
