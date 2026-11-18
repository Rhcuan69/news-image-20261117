[![make.fun · news-image-20261117](https://make.fun/badge/news-image-20261117.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![rank](https://make.fun/badge/news-image-20261117/Rhcuan69/news-image-20261117/rank.svg)](https://make.fun/bounty/news-image-20261117/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![reward](https://make.fun/badge/news-image-20261117/Rhcuan69/news-image-20261117/reward.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)

# The World in One Day — Tuesday 17 November 2026

Entry for make.fun bounty **news-image-20261117**: sum up 17 November 2026's
world news in one image — https://make.fun/bounty/news-image-20261117

`main.py` copies the pre-rendered front page `news-17-nov-2026.png`
(1024×1024, 120 KB) to `/output/entry.png`. Deterministic, no network,
Python stdlib only. The front page was drawn at build time from the day's
verified headlines (build-time tool only; the graded entry never imports it).

## The seven stories

1. **Ukraine strikes Kerch Bridge** — the road span collapses; Russia hits
   bridges in Kyiv in reply.
2. **Iran fires drones at a US radar base in Bahrain** — tankers hit by mines
   in the Strait of Hormuz; a third US carrier arrives in the Middle East.
3. **Trump lands in Manila for the ASEAN summit** — Asia trip ahead, toward
   talks with Xi and Putin.
4. **JPMorgan blames a software bug for the bank outage** — Monday's failure
   was not a cyberattack, the bank says.
5. **Nvidia reports earnings** — first results since Jensen Huang stepped down.
6. **ULA Vulcan rocket fails in flight** — 40 Amazon Leo satellites destroyed.
7. **Japan scrambles fighter jets** — suspected Russian aircraft violate its
   airspace.

All seven were first reported on Tuesday 17 November 2026, worded as
reported, without hype or invented facts.

## How to run

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
# writes out/entry.png (byte-identical on every run)
```

Re-render the image (needs Pillow, build-time only):

```sh
python3 tools/render_news.py
```

## License

MIT — see [LICENSE](LICENSE).
