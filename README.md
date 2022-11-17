# nocapaipy
[BETA]: A python wrapper for NoCaptchaAI

## Installation

```bash
$ pip install git+https://github.com/noCaptchaAi/nocapaipy
```

## Usage

```py
import asyncio
import json

from pyppeteer import launch

from nocapaipy import solve_captcha

URL = 'https://accounts.hcaptcha.com/demo'
API_KEY = ''
UID = ''


async def main():
    browser = await launch(headless=True)
    page = await browser.newPage()

    await page.goto(URL)
    await page.waitForNetworkIdle()

    await solve_captcha(page, API_KEY, UID, 'free')

    await page.screenshot({'path': 'test.jpeg', 'type': 'jpeg'})

    await browser.close()


asyncio.get_event_loop().run_until_complete(main())
```
