import os
import sys
import datetime
import logging
import requests
from time import sleep
from urllib.parse import quote


class BraveSearchException(Exception):
    pass


NOW = datetime.datetime.now().strftime("_%Y_%m_%d-%H_%M")
LOG_FILE = os.path.join(os.getcwd(), "search_brave" + NOW + ".log")
FORMAT = logging.Formatter("%(asctime)s jlopez.mx [%(module)s - %(funcName)s:%(lineno)s] %(levelname)s: %(message)s")
HANDLER = logging.FileHandler(filename=LOG_FILE)
HANDLER.setFormatter(FORMAT)

LOG = logging.getLogger(__name__)
LOG.addHandler(HANDLER)
LOG.setLevel(logging.INFO)


if not os.getenv('BRAVE_TOKEN'):
    raise Exception('BRAVE_TOKEN not set')

BRAVE_API_SEARCH = "api.search.brave.com/res/v1/web"

HEADERS = {
    "Accept": "application/json",
    "Accept-Encoding": "gzip",
    "User-Agent": "Python {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}".format(sys=sys),
    "X-Subscription-Token": os.getenv('BRAVE_TOKEN'),
}

while True:

    # clear screen
    os.system('cls' if os.name == 'nt' else 'clear')

    id = 0
    offset = 0

    # prompt user for input
    print("Enter your query:")
    raw_query = input()

    # encode query
    query = quote(raw_query)
    raw_query = raw_query.replace(" ", "_")
    NOW = datetime.datetime.now().strftime("_%Y_%m_%d-%H_%M")
    RESULTS_FILE_NAME = f"brave-api-client-{NOW}-{raw_query}.csv"
    RESULTS_FILE_PATH = os.path.join(os.getcwd(), RESULTS_FILE_NAME)

    # open file
    with open(RESULTS_FILE_PATH, "w") as f:
        print("[INFO] Submitting query...")
        print()
        print("[INFO] Using api.search.brave.com v1.0")
        print("[INFO] You can find documentation at: https://api.search.brave.com/app/documentation")
        print("-" * 80)

        # write file headers
        f.write("ID,Title,URL,Description\n")

        try:
            while True:
                # make request
                SEARCH_URL = f"https://{BRAVE_API_SEARCH}/search?q={query}&offset={offset}&count=20&safesearch=off&spellcheck=false"

                LOG.info(f"Brave Search API Query Request: {SEARCH_URL}")

                response = requests.get(url=SEARCH_URL, headers=HEADERS)

                data = response.json()

                if not data['query']["more_results_available"]:
                    raise BraveSearchException("No more results returned by Brave API Search.")

                results = data['web']['results']

                if len(results) == 0:
                    raise BraveSearchException("No more web results available.")

                # iterate over results
                for i in results:
                    id += 1
                    print("-" * 80)
                    print(f"ID: {id}")
                    print(f"Title: {i['title']}")
                    print(f"URL: {i['url']}")
                    print(f"Description: {i['description']}")
                    print()
                    f.write(f"{id},{i['title']},{i['url']},{i['description']}\n")

                sleep(3)
                offset += 1

        except BraveSearchException as e:
            LOG.warning(f"BraveSearchException: {e}")

    print()
    print("-" * 80)
    print(f"[INFO] Results saved to: {RESULTS_FILE_PATH}")
    f.close()

    # press enter to continue
    input("[INFO] Press Enter to continue or CTRL+C to exit...")
