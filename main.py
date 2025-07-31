from config import URL_LIST
from fetch import fetch_page_content
from util import collect_relevant_content


def scrape_optics_database():

    all_rows = []
    for url in URL_LIST:
        print(f"Processing rows for {url}")
        content = fetch_page_content(url)
        content_rows = collect_relevant_content(content)
        all_rows.extend(content_rows)

    print(f"{len(all_rows)} rows scraped")


if __name__ == "__main__":
    scrape_optics_database()