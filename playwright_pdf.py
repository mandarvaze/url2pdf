import asyncio
from playwright.async_api import async_playwright
import argparse
import time


async def create_pdf(url, path):
    async with async_playwright() as p:
        start = time.process_time()
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto(url)
        await page.pdf(path=path)
        await browser.close()
        print(f"playwright: Took {time.process_time()-start} seconds")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--url", help="URL to convert", type=str)
    parser.add_argument("-o", "--out", help="Path to PDF output", type=str)
    args = parser.parse_args()
    asyncio.run(create_pdf(args.url, args.out))
