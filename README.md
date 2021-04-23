# Setup

- Install `poetry` from [here](https://python-poetry.org/docs/#installation)
- `poetry install` (Will install dependencies from the poetry.lock file)

# Basic usage

```shell

$ poetry run python playwright_pdf.py --url "https://en.wikipedia.org/wiki/Deep_Impact_(spacecraft)" --out play-wikipedia.pdf`
playwright: Took 0.1422239999999999 seconds

$ poetry run python browserless_pdf.py --url "https://en.wikipedia.org/wiki/Deep_Impact_(spacecraft)" --out browserless-wikipedia.pdf
browerless: Took 0.04257199999999983 seconds

$ poetry run python pyppeteer_pdf.py --url "https://en.wikipedia.org/wiki/Deep_Impact_(spacecraft)" --out pyp-wikipedia.pdf
pyppeteer: Took 0.31097300000000017 seconds
```
