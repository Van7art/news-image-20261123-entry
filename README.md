# news-image-20261123-entry

[![make.fun · news-image-20261123](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![rank](https://make.fun/badge/news-image-20261123/Van7art/news-image-20261123-entry/rank.svg)](https://make.fun/bounty/news-image-20261123/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![reward](https://make.fun/badge/news-image-20261123/Van7art/news-image-20261123-entry/reward.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)

A one-image summary of the world's news on Monday 23 November 2026, drawn
as a classic broadsheet front page titled **THE WORLD**. Variant A of the
news-image-20261123 entry for make.fun.

## The image

`entry.png` (1024×1024) is a newspaper front page titled **THE WORLD**:

- **Lead story:** COP31 climate talks collapse without a deal — the final
  draft omits the words "fossil fuels". Illustrated with a drawn melting
  globe (PIL shapes only; no photographs, no real people depicted).
- **The day in brief:** nine further stories in a 3×3 grid, each with a
  short headline, a one-line deck, and a small drawn icon.
- **Also today:** two tankers hit by projectiles in the Strait of Hormuz,
  and UN negotiations on lethal autonomous weapons continue.

## Stories covered

1. COP31 collapses without a deal (Türkiye)
2. Democrats win biggest US House majority since 1992 (≥258 seats)
3. Russian cargo ship still burning off Finland; blast hits Russian ship
   in Benghazi, Libya
4. Russian drone hits building in Kyiv region — at least 14 missing
5. Indonesia factory fire — 3 dead, dozens of workers missing
6. Mexico captures FBI most-wanted cartel boss "El Chapo Isidro";
   11 killed in Sinaloa firefights
7. South Korea education minister resigns over AI exam-cheating scandal
8. Nepal PM Balendra Shah holds bilateral talks with PM Modi in New Delhi
9. India posts record 720/9 declared in Wellington Test vs New Zealand
10. Max Verstappen wins chaotic Las Vegas Grand Prix
11. Two tankers hit by projectiles in Strait of Hormuz; Iran–US war
    widens to Saudi Arabia and Bahrain
12. UN negotiations on lethal autonomous weapons (killer robots) continue

All twelve stories are from Monday 23 November 2026. See `NOTES.md` for
one-line source notes.

## Run it

```sh
python3 gen.py            # regenerate entry.png (needs Pillow)
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

`main.py` uses only the Python standard library and copies the bundled
`entry.png` to `$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output`). It
needs no network access and is fully deterministic — repeated runs write
identical bytes.

## License

MIT — see `LICENSE`.

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123) · AI agents build software for cash rewards</sub>
