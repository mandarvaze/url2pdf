import argparse
import time
import requests
browserless_endpoint = 'https://chrome.browserless.io/pdf'


def create_pdf(url, path):
    headers = {
        'Cache-Control': 'no-cache',
        'Content-Type': 'application/json',
    }
    data = {'url': url}
    start = time.process_time()
    response = requests.post(browserless_endpoint, headers=headers, json=data)
    open(path, 'wb').write(response.content)
    print(f"browerless: Took {time.process_time()-start} seconds")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--url", help="URL to convert", type=str)
    parser.add_argument("-o", "--out", help="Path to PDF output", type=str)
    args = parser.parse_args()
    create_pdf(args.url, args.out)
