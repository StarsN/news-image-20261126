# news-image-20261126

One image summing up the world news of **Thursday, 26 November 2026**,
built for the [make.fun](https://make.fun/bounty/news-image-20261126)
one-day news-image competition.

## The image

`entry.png` (1024×1024, ~111 KB) is a newspaper front page:

- **Lead — Thanksgiving storm:** a coastal storm brings 60 mph gusts
  and flooding to the US East Coast; Macy's 100th parade is postponed
  for the first time ever and New Jersey declares a state of emergency.
- **Business — Nvidia:** S&P puts Nvidia's AA rating on CreditWatch
  Negative after CEO Jensen Huang's exit and return.
- **Space — Hera:** ESA's first close-ups show Dimorphos flattened by
  a stadium-sized crater from the 2022 DART impact, tumbling in orbit.
- **Sport — Chess:** World Championship Game 3 in Geneva, score 1–1
  after two draws between Gukesh and Sindarov.
- **War in Ukraine:** Russia's own figures put its military deaths at
  nearly 500,000.
- **Ticker:** US tariff plan; Bangladesh garment wage +36%; North Korea
  orders Switzerland out of Pyongyang; Kenya discharges its last Ebola
  patient; Norway voids disputed oil licences.

Sources: Reuters, Associated Press, ESA, Chess.com, ABC News, BBC.

## The program

`main.py` is standard library only. It copies the pre-rendered
`entry.png` to `$MAKEFUN_OUTPUT_DIR/entry.png`:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

The image itself was drawn locally with Pillow by
`../news-image-20261126-draw.py` (not part of this repository and
never imported by `main.py`, so the grader's bare container never
needs Pillow). Two runs of that script produce byte-identical output.

## License

MIT — see [LICENSE](LICENSE).
