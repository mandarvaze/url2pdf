import argparse
import asyncio
import time
from pyppeteer import connect
browserless_endpoint = 'https://chrome.browserless.io/pdf'


async def create_pdf(url, path):
    start = time.process_time()
    pdfHeightMargin = 150
    browser = await connect(
        {'browserWSEndpoint': 'wss://chrome.browserless.io/'})
    page = await browser.newPage()
    await page.setViewport({'width': 412,
                            'height': 800,
                            'deviceScaleFactor': 1})
    await page.goto(url)
    await page.emulateMedia('screen')
    await page.addStyleTag({
        'content': """
        html {
            -webkit - print-color - adjust: exact !important
            color - adjust: exact !important
            print-color - adjust: exact !important
        }
        * {
            box - shadow: none !important
        }
       """
    })
    height = await page.evaluate('() => document.documentElement.offsetHeight')
    await page.pdf(
        {'path': path,
         'scale': 1,
         'margin': {
             'top': '20px',
             'bottom': '20px'
         },
         'preferCSSPageSize': True,
         'fullPage': True,
         'omitBackground': True,
         'height': f"{height + pdfHeightMargin}px",
         'printBackground': True
         })
    await browser.close()
    print(f"browserless: Took {time.process_time()-start} seconds")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--url", help="URL to convert", type=str)
    parser.add_argument("-o", "--out", help="Path to PDF output", type=str)
    args = parser.parse_args()
    asyncio.get_event_loop().run_until_complete(create_pdf(args.url, args.out))
