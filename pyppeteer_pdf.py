import asyncio
from pyppeteer import launch
import argparse
import time


async def create_pdf(url, path):
    start = time.process_time()
    browser = await launch()
    page = await browser.newPage()
    await page.goto(url)
    await page.pdf({'path': path})
    await browser.close()
    print(f"pyppeteer: Took {time.process_time()-start} seconds")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--url", help="URL to convert", type=str)
    parser.add_argument("-o", "--out", help="Path to PDF output", type=str)
    args = parser.parse_args()
    asyncio.get_event_loop().run_until_complete(create_pdf(args.url, args.out))
