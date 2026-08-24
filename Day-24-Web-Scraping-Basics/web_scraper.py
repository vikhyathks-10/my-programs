# ============================================================
# MONTH 8 - DAY 24
# WEB SCRAPING BASICS
#
# Programs 121-125
#
# Concepts:
# HTML + requests + BeautifulSoup
#
# 121. Extract page title
# 122. Extract all headings
# 123. Extract links
# 124. Extract structured information
# 125. Basic webpage information extractor
#
# How to run:
# python web_scraper.py
# ============================================================

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin


# ============================================================
# CONFIGURATION
# ============================================================

DEFAULT_URL = "https://www.python.org"


# ============================================================
# HELPER FUNCTION
# FETCH WEBPAGE
# ============================================================

def fetch_webpage(url):

    try:

        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        response = requests.get(
            url,
            headers=headers,
            timeout=10
        )

        if response.status_code == 200:

            return response

        print(
            f"\nHTTP Error: {response.status_code}"
        )

        return None

    except requests.exceptions.ConnectionError:

        print(
            "\nError: No internet connection "
            "or website could not be reached."
        )

        return None

    except requests.exceptions.Timeout:

        print(
            "\nError: Request timed out."
        )

        return None

    except requests.exceptions.RequestException as e:

        print(
            f"\nRequest error: {e}"
        )

        return None


# ============================================================
# HELPER FUNCTION
# CREATE BEAUTIFULSOUP OBJECT
# ============================================================

def create_soup(response):

    if response is None:

        return None

    try:

        soup = BeautifulSoup(
            response.text,
            "html.parser"
        )

        return soup

    except Exception as e:

        print(
            f"\nError parsing HTML: {e}"
        )

        return None


# ============================================================
# GET URL
# ============================================================

def get_url():

    url = input(
        f"\nEnter webpage URL "
        f"[Press Enter for {DEFAULT_URL}]: "
    ).strip()

    if not url:

        url = DEFAULT_URL

    # Add https:// if the user enters
    # only the domain name.

    if not (
        url.startswith("http://")
        or url.startswith("https://")
    ):

        url = "https://" + url

    return url


# ============================================================
# PROGRAM 121
# EXTRACT PAGE TITLE
# ============================================================

def extract_page_title():

    print("\n" + "=" * 60)
    print("                 PROGRAM 121")
    print("               EXTRACT PAGE TITLE")
    print("=" * 60)

    url = get_url()

    print(
        f"\nFetching: {url}"
    )

    response = fetch_webpage(url)

    if response is None:

        return

    soup = create_soup(response)

    if soup is None:

        return

    title = soup.find("title")

    if title:

        title_text = title.get_text(
            " ",
            strip=True
        )

        print(
            f"\nPage Title: {title_text}"
        )

    else:

        print(
            "\nNo page title found."
        )


# ============================================================
# PROGRAM 122
# EXTRACT ALL HEADINGS
# ============================================================

def extract_headings():

    print("\n" + "=" * 60)
    print("                 PROGRAM 122")
    print("              EXTRACT ALL HEADINGS")
    print("=" * 60)

    url = get_url()

    print(
        f"\nFetching: {url}"
    )

    response = fetch_webpage(url)

    if response is None:

        return

    soup = create_soup(response)

    if soup is None:

        return

    headings = soup.find_all(
        [
            "h1",
            "h2",
            "h3",
            "h4",
            "h5",
            "h6"
        ]
    )

    if not headings:

        print(
            "\nNo headings found."
        )

        return

    print(
        f"\nTotal headings found: "
        f"{len(headings)}"
    )

    print()

    count = 0

    for heading in headings:

        text = heading.get_text(
            " ",
            strip=True
        )

        if text:

            count += 1

            print(
                f"{count}. "
                f"{heading.name.upper()} : "
                f"{text}"
            )


# ============================================================
# PROGRAM 123
# EXTRACT LINKS
# ============================================================

def extract_links():

    print("\n" + "=" * 60)
    print("                 PROGRAM 123")
    print("                  EXTRACT LINKS")
    print("=" * 60)

    url = get_url()

    print(
        f"\nFetching: {url}"
    )

    response = fetch_webpage(url)

    if response is None:

        return

    soup = create_soup(response)

    if soup is None:

        return

    links = soup.find_all("a")

    valid_links = []

    for link in links:

        href = link.get("href")

        # IMPORTANT:
        # BeautifulSoup can return different
        # attribute types, so only use href
        # when it is a string.

        if href and isinstance(href, str):

            absolute_url = urljoin(
                url,
                href
            )

            link_text = link.get_text(
                " ",
                strip=True
            )

            valid_links.append(
                (
                    link_text,
                    absolute_url
                )
            )

    if not valid_links:

        print(
            "\nNo links found."
        )

        return

    print(
        f"\nTotal links found: "
        f"{len(valid_links)}"
    )

    print(
        "\nShowing first 30 links:"
    )

    print("-" * 60)

    for index, (
        link_text,
        link_url
    ) in enumerate(
        valid_links[:30],
        start=1
    ):

        if not link_text:

            link_text = "No text"

        print(
            f"{index}. {link_text}"
        )

        print(
            f"   {link_url}"
        )


# ============================================================
# PROGRAM 124
# EXTRACT STRUCTURED INFORMATION
# ============================================================

def extract_structured_information():

    print("\n" + "=" * 60)
    print("                 PROGRAM 124")
    print("         EXTRACT STRUCTURED INFORMATION")
    print("=" * 60)

    url = get_url()

    print(
        f"\nFetching: {url}"
    )

    response = fetch_webpage(url)

    if response is None:

        return

    soup = create_soup(response)

    if soup is None:

        return

    # --------------------------------------------------------
    # PAGE TITLE
    # --------------------------------------------------------

    title = soup.find("title")

    if title:

        title_text = title.get_text(
            " ",
            strip=True
        )

    else:

        title_text = "Not available"

    # --------------------------------------------------------
    # META DESCRIPTION
    # --------------------------------------------------------

    meta_description = soup.find(
        "meta",
        attrs={
            "name": "description"
        }
    )

    if meta_description:

        description = meta_description.get(
            "content"
        )

        if not isinstance(
            description,
            str
        ):

            description = "Not available"

    else:

        description = "Not available"

    # --------------------------------------------------------
    # HEADINGS
    # --------------------------------------------------------

    headings = soup.find_all(
        [
            "h1",
            "h2",
            "h3"
        ]
    )

    heading_texts = []

    for heading in headings:

        text = heading.get_text(
            " ",
            strip=True
        )

        if text:

            heading_texts.append(
                text
            )

    # --------------------------------------------------------
    # LINKS
    # --------------------------------------------------------

    links = soup.find_all("a")

    valid_link_count = 0

    for link in links:

        href = link.get("href")

        if href and isinstance(
            href,
            str
        ):

            valid_link_count += 1

    # --------------------------------------------------------
    # IMAGES
    # --------------------------------------------------------

    images = soup.find_all("img")

    # --------------------------------------------------------
    # PARAGRAPHS
    # --------------------------------------------------------

    paragraphs = soup.find_all("p")

    # --------------------------------------------------------
    # DISPLAY
    # --------------------------------------------------------

    print("\n" + "-" * 60)

    print(
        f"Page Title       : {title_text}"
    )

    print(
        f"Meta Description  : {description}"
    )

    print(
        f"Headings (H1-H3) : "
        f"{len(heading_texts)}"
    )

    print(
        f"Links             : "
        f"{valid_link_count}"
    )

    print(
        f"Images            : "
        f"{len(images)}"
    )

    print(
        f"Paragraphs        : "
        f"{len(paragraphs)}"
    )

    print("-" * 60)

    if heading_texts:

        print(
            "\nMain Headings:"
        )

        for heading in heading_texts:

            print(
                f"  • {heading}"
            )


# ============================================================
# PROGRAM 125
# BASIC WEBPAGE INFORMATION EXTRACTOR
# ============================================================

def webpage_information_extractor():

    print("\n" + "=" * 60)
    print("                 PROGRAM 125")
    print("        WEBPAGE INFORMATION EXTRACTOR")
    print("=" * 60)

    url = get_url()

    print(
        f"\nFetching webpage..."
    )

    response = fetch_webpage(url)

    if response is None:

        return

    soup = create_soup(response)

    if soup is None:

        return

    # --------------------------------------------------------
    # TITLE
    # --------------------------------------------------------

    title = soup.find("title")

    if title:

        title_text = title.get_text(
            " ",
            strip=True
        )

    else:

        title_text = "Not available"

    # --------------------------------------------------------
    # META DESCRIPTION
    # --------------------------------------------------------

    meta_description = soup.find(
        "meta",
        attrs={
            "name": "description"
        }
    )

    if meta_description:

        description = meta_description.get(
            "content"
        )

        if not isinstance(
            description,
            str
        ):

            description = "Not available"

    else:

        description = "Not available"

    # --------------------------------------------------------
    # HEADINGS
    # --------------------------------------------------------

    headings = soup.find_all(
        [
            "h1",
            "h2",
            "h3",
            "h4",
            "h5",
            "h6"
        ]
    )

    # --------------------------------------------------------
    # LINKS
    # --------------------------------------------------------

    links = soup.find_all("a")

    valid_links = []

    for link in links:

        href = link.get("href")

        if href and isinstance(
            href,
            str
        ):

            absolute_url = urljoin(
                url,
                href
            )

            link_text = link.get_text(
                " ",
                strip=True
            )

            valid_links.append(
                (
                    link_text,
                    absolute_url
                )
            )

    # --------------------------------------------------------
    # IMAGES
    # --------------------------------------------------------

    images = soup.find_all("img")

    # --------------------------------------------------------
    # PARAGRAPHS
    # --------------------------------------------------------

    paragraphs = soup.find_all("p")

    # --------------------------------------------------------
    # DISPLAY BASIC INFORMATION
    # --------------------------------------------------------

    print("\n" + "=" * 60)
    print("               WEBPAGE INFORMATION")
    print("=" * 60)

    print(
        f"URL             : {url}"
    )

    print(
        f"Page Title      : {title_text}"
    )

    print(
        f"Headings        : {len(headings)}"
    )

    print(
        f"Links           : {len(valid_links)}"
    )

    print(
        f"Images          : {len(images)}"
    )

    print(
        f"Paragraphs      : {len(paragraphs)}"
    )

    print(
        f"Meta Description : {description}"
    )

    # --------------------------------------------------------
    # DISPLAY HEADINGS
    # --------------------------------------------------------

    print("\n" + "-" * 60)
    print("HEADINGS")
    print("-" * 60)

    if headings:

        heading_count = 0

        for heading in headings:

            text = heading.get_text(
                " ",
                strip=True
            )

            if text:

                heading_count += 1

                print(
                    f"{heading_count}. "
                    f"{heading.name.upper()} - "
                    f"{text}"
                )

    else:

        print(
            "No headings found."
        )

    # --------------------------------------------------------
    # DISPLAY LINKS
    # --------------------------------------------------------

    print("\n" + "-" * 60)
    print("LINKS")
    print("-" * 60)

    if valid_links:

        for index, (
            link_text,
            link_url
        ) in enumerate(
            valid_links[:20],
            start=1
        ):

            if not link_text:

                link_text = "No text"

            print(
                f"{index}. {link_text}"
            )

            print(
                f"   {link_url}"
            )

        if len(valid_links) > 20:

            print(
                f"\n... and "
                f"{len(valid_links) - 20} "
                f"more links."
            )

    else:

        print(
            "No links found."
        )

    # --------------------------------------------------------
    # DISPLAY PARAGRAPHS
    # --------------------------------------------------------

    print("\n" + "-" * 60)
    print("FIRST 10 PARAGRAPHS")
    print("-" * 60)

    paragraph_count = 0

    for paragraph in paragraphs:

        text = paragraph.get_text(
            " ",
            strip=True
        )

        if text:

            paragraph_count += 1

            print(
                f"{paragraph_count}. {text}"
            )

            if paragraph_count >= 10:

                break

    if paragraph_count == 0:

        print(
            "No paragraphs found."
        )

    # --------------------------------------------------------
    # IMAGE COUNT
    # --------------------------------------------------------

    print("\n" + "-" * 60)

    print(
        f"Total images found: "
        f"{len(images)}"
    )

    print("-" * 60)


# ============================================================
# PROGRAMS 121-125
# RUN ALL
# ============================================================

def run_all_programs():

    print(
        "\nRunning Programs 121-125..."
    )

    url = DEFAULT_URL

    response = fetch_webpage(
        url
    )

    if response is None:

        return

    soup = create_soup(
        response
    )

    if soup is None:

        return

    # ========================================================
    # PROGRAM 121
    # ========================================================

    print("\n" + "=" * 60)
    print("PROGRAM 121 - PAGE TITLE")
    print("=" * 60)

    title = soup.find("title")

    if title:

        print(
            title.get_text(
                " ",
                strip=True
            )
        )

    else:

        print(
            "No title found."
        )

    # ========================================================
    # PROGRAM 122
    # ========================================================

    print("\n" + "=" * 60)
    print("PROGRAM 122 - ALL HEADINGS")
    print("=" * 60)

    headings = soup.find_all(
        [
            "h1",
            "h2",
            "h3",
            "h4",
            "h5",
            "h6"
        ]
    )

    heading_count = 0

    for heading in headings:

        text = heading.get_text(
            " ",
            strip=True
        )

        if text:

            heading_count += 1

            print(
                f"{heading_count}. "
                f"{heading.name.upper()} : "
                f"{text}"
            )

    print(
        f"\nTotal headings: "
        f"{heading_count}"
    )

    # ========================================================
    # PROGRAM 123
    # ========================================================

    print("\n" + "=" * 60)
    print("PROGRAM 123 - LINKS")
    print("=" * 60)

    links = soup.find_all("a")

    valid_links = []

    for link in links:

        href = link.get("href")

        # Fixes Pylance type warning
        if href and isinstance(
            href,
            str
        ):

            absolute_url = urljoin(
                url,
                href
            )

            valid_links.append(
                absolute_url
            )

    print(
        f"Total links: "
        f"{len(valid_links)}"
    )

    print(
        "\nFirst 20 links:"
    )

    for index, link_url in enumerate(
        valid_links[:20],
        start=1
    ):

        print(
            f"{index}. {link_url}"
        )

    # ========================================================
    # PROGRAM 124
    # ========================================================

    print("\n" + "=" * 60)
    print("PROGRAM 124 - STRUCTURED INFORMATION")
    print("=" * 60)

    images = soup.find_all("img")

    paragraphs = soup.find_all("p")

    print(
        f"Page Title : "
        f"{title.get_text(strip=True) if title else 'N/A'}"
    )

    print(
        f"Headings   : "
        f"{len(headings)}"
    )

    print(
        f"Links      : "
        f"{len(valid_links)}"
    )

    print(
        f"Images     : "
        f"{len(images)}"
    )

    print(
        f"Paragraphs : "
        f"{len(paragraphs)}"
    )

    # ========================================================
    # PROGRAM 125
    # ========================================================

    print("\n" + "=" * 60)
    print("PROGRAM 125 - WEBPAGE INFORMATION EXTRACTOR")
    print("=" * 60)

    print(
        f"Website: {url}"
    )

    print(
        "Webpage analysis completed successfully."
    )


# ============================================================
# MENU
# ============================================================

def display_menu():

    print("\n" + "=" * 65)
    print("              WEB SCRAPING BASICS")
    print("=" * 65)

    print("1. Extract Page Title")
    print("2. Extract All Headings")
    print("3. Extract Links")
    print("4. Extract Structured Information")
    print("5. Webpage Information Extractor")
    print("6. Run All Programs")
    print("7. Exit")

    print("=" * 65)


# ============================================================
# MAIN PROGRAM
# ============================================================

def main():

    print(
        "\nWelcome to Web Scraping Basics!"
    )

    print(
        f"\nDefault website: "
        f"{DEFAULT_URL}"
    )

    while True:

        display_menu()

        choice = input(
            "Enter your choice: "
        ).strip()

        # ----------------------------------------------------
        # Program 121
        # ----------------------------------------------------

        if choice == "1":

            extract_page_title()

        # ----------------------------------------------------
        # Program 122
        # ----------------------------------------------------

        elif choice == "2":

            extract_headings()

        # ----------------------------------------------------
        # Program 123
        # ----------------------------------------------------

        elif choice == "3":

            extract_links()

        # ----------------------------------------------------
        # Program 124
        # ----------------------------------------------------

        elif choice == "4":

            extract_structured_information()

        # ----------------------------------------------------
        # Program 125
        # ----------------------------------------------------

        elif choice == "5":

            webpage_information_extractor()

        # ----------------------------------------------------
        # Run all programs
        # ----------------------------------------------------

        elif choice == "6":

            run_all_programs()

        # ----------------------------------------------------
        # Exit
        # ----------------------------------------------------

        elif choice == "7":

            print(
                "\nThank you for using "
                "Web Scraping Basics!"
            )

            break

        # ----------------------------------------------------
        # Invalid choice
        # ----------------------------------------------------

        else:

            print(
                "\nInvalid choice."
                " Please enter a number from 1 to 7."
            )


# ============================================================
# PROGRAM ENTRY POINT
# ============================================================

if __name__ == "__main__":

    main()