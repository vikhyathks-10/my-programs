# ============================================================
# MONTH 8 - DAY 21
# WEB DATA & APIs
#
# Programs 106-110
#
# Concepts:
# APIs, JSON, requests, dictionaries, lists
#
# How to run:
# python api_information.py
# ============================================================

import requests


# ============================================================
# API CONFIGURATION
# ============================================================

BASE_URL = "https://api.restcountries.com/countries/v5/name"

# Demo key provided by REST Countries documentation
API_KEY = "rc_live_demo"


# ============================================================
# PROGRAM 106
# FETCH DATA FROM A PUBLIC API
# ============================================================

def fetch_country_data(country):

    url = BASE_URL

    params = {
        "q": country
    }

    headers = {
        "Authorization": f"Bearer {API_KEY}"
    }

    try:

        response = requests.get(
            url,
            params=params,
            headers=headers,
            timeout=10
        )

        return response

    except requests.exceptions.ConnectionError:

        print(
            "\nError: Unable to connect to the internet."
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
# PROGRAM 107
# PARSE JSON RESPONSE
# ============================================================

def parse_json_response(response):

    if response is None:
        return None

    try:

        data = response.json()

        return data

    except ValueError:

        print(
            "\nError: Response is not valid JSON."
        )

        return None


# ============================================================
# PROGRAM 108
# EXTRACT SELECTED FIELDS
# ============================================================

def extract_country_information(data):

    if not data:

        print(
            "\nNo country data received."
        )

        return None

    try:

        # ----------------------------------------------------
        # Current REST Countries API v5 structure:
        #
        # {
        #     "data": {
        #         "objects": [
        #             {...}
        #         ]
        #     }
        # }
        # ----------------------------------------------------

        data_section = data.get(
            "data",
            {}
        )

        if not isinstance(
            data_section,
            dict
        ):

            print(
                "\nInvalid data format."
            )

            return None

        countries = data_section.get(
            "objects",
            []
        )

        if not countries:

            print(
                "\nNo country found."
            )

            return None

        country_data = countries[0]

        # ----------------------------------------------------
        # NAME
        # ----------------------------------------------------

        names = country_data.get(
            "names",
            {}
        )

        country_name = names.get(
            "common",
            "Not available"
        )

        official_name = names.get(
            "official",
            "Not available"
        )

        # ----------------------------------------------------
        # CAPITAL
        # ----------------------------------------------------

        capitals = country_data.get(
            "capitals",
            []
        )

        capital = "Not available"

        if capitals:

            first_capital = capitals[0]

            if isinstance(
                first_capital,
                dict
            ):

                capital = first_capital.get(
                    "name",
                    "Not available"
                )

            else:

                capital = str(
                    first_capital
                )

        # ----------------------------------------------------
        # REGION
        # ----------------------------------------------------

        region = country_data.get(
            "region",
            "Not available"
        )

        # ----------------------------------------------------
        # SUBREGION
        # ----------------------------------------------------

        subregion = country_data.get(
            "subregion",
            "Not available"
        )

        # ----------------------------------------------------
        # POPULATION
        # ----------------------------------------------------

        population = country_data.get(
            "population",
            0
        )

        # ----------------------------------------------------
        # AREA
        # ----------------------------------------------------

        area_data = country_data.get(
            "area",
            {}
        )

        if isinstance(
            area_data,
            dict
        ):

            area = area_data.get(
                "kilometers",
                0
            )

        else:

            area = area_data

        # ----------------------------------------------------
        # LANGUAGES
        # ----------------------------------------------------

        languages = country_data.get(
            "languages",
            []
        )

        language_names = []

        if isinstance(
            languages,
            list
        ):

            for language in languages:

                if isinstance(
                    language,
                    dict
                ):

                    language_name = language.get(
                        "name",
                        language.get(
                            "english",
                            "Unknown"
                        )
                    )

                    language_names.append(
                        language_name
                    )

                else:

                    language_names.append(
                        str(language)
                    )

        elif isinstance(
            languages,
            dict
        ):

            language_names = list(
                languages.values()
            )

        # ----------------------------------------------------
        # CURRENCIES
        # ----------------------------------------------------

        currencies = country_data.get(
            "currencies",
            {}
        )

        currency_names = []

        if isinstance(
            currencies,
            dict
        ):

            for currency in currencies.values():

                if isinstance(
                    currency,
                    dict
                ):

                    currency_name = currency.get(
                        "name",
                        "Unknown"
                    )

                    currency_names.append(
                        currency_name
                    )

                else:

                    currency_names.append(
                        str(currency)
                    )

        # ----------------------------------------------------
        # RETURN INFORMATION
        # ----------------------------------------------------

        return {

            "name": country_name,

            "official_name": official_name,

            "capital": capital,

            "region": region,

            "subregion": subregion,

            "population": population,

            "area": area,

            "languages": language_names,

            "currencies": currency_names
        }

    except Exception as e:

        print(
            f"\nError extracting country information: {e}"
        )

        return None


# ============================================================
# PROGRAM 109
# HANDLE API ERRORS
# ============================================================

def handle_api_response(response):

    if response is None:

        return False

    if response.status_code == 200:

        return True

    elif response.status_code == 400:

        print(
            "\nBad request."
        )

    elif response.status_code == 401:

        print(
            "\nUnauthorized."
            "\nPlease check your API key."
        )

    elif response.status_code == 404:

        print(
            "\nCountry not found."
        )

    elif response.status_code == 429:

        print(
            "\nToo many requests."
            "\nPlease try again later."
        )

    elif response.status_code >= 500:

        print(
            "\nServer error."
            "\nThe API may be temporarily unavailable."
        )

    else:

        print(
            f"\nAPI Error."
            f"\nStatus Code: {response.status_code}"
        )

    return False


# ============================================================
# DISPLAY COUNTRY INFORMATION
# ============================================================

def display_country_information(info):

    if not info:
        return

    print("\n" + "=" * 60)

    print(
        "              COUNTRY INFORMATION"
    )

    print("=" * 60)

    print(
        f"Country       : "
        f"{info['name']}"
    )

    print(
        f"Official Name : "
        f"{info['official_name']}"
    )

    print(
        f"Capital       : "
        f"{info['capital']}"
    )

    print(
        f"Region        : "
        f"{info['region']}"
    )

    print(
        f"Subregion     : "
        f"{info['subregion']}"
    )

    print(
        f"Population    : "
        f"{info['population']:,}"
    )

    print(
        f"Area          : "
        f"{info['area']:,} km²"
    )

    if info["languages"]:

        languages = ", ".join(
            info["languages"]
        )

    else:

        languages = "Not available"

    if info["currencies"]:

        currencies = ", ".join(
            info["currencies"]
        )

    else:

        currencies = "Not available"

    print(
        f"Languages     : "
        f"{languages}"
    )

    print(
        f"Currencies    : "
        f"{currencies}"
    )

    print("=" * 60)


# ============================================================
# PROGRAM 110
# COMPLETE API-BASED INFORMATION PROGRAM
# ============================================================

def country_information_program():

    country = input(
        "\nEnter country name: "
    ).strip()

    if not country:

        print(
            "\nPlease enter a country name."
        )

        return

    print(
        f"\nFetching information for "
        f"'{country}'..."
    )

    # --------------------------------------------------------
    # Program 106
    # --------------------------------------------------------

    response = fetch_country_data(
        country
    )

    # --------------------------------------------------------
    # Program 109
    # --------------------------------------------------------

    if not handle_api_response(
        response
    ):

        return

    # --------------------------------------------------------
    # Program 107
    # --------------------------------------------------------

    data = parse_json_response(
        response
    )

    if data is None:

        return

    # --------------------------------------------------------
    # Program 108
    # --------------------------------------------------------

    information = extract_country_information(
        data
    )

    if information is None:

        return

    # --------------------------------------------------------
    # Display result
    # --------------------------------------------------------

    display_country_information(
        information
    )


# ============================================================
# PROGRAM 106
# SIMPLE API FETCH
# ============================================================

def simple_api_fetch():

    country = input(
        "\nEnter country name: "
    ).strip()

    if not country:

        print(
            "\nPlease enter a country name."
        )

        return

    response = fetch_country_data(
        country
    )

    if response is None:

        return

    print(
        f"\nHTTP Status Code: "
        f"{response.status_code}"
    )

    if response.status_code == 200:

        print(
            "\nData successfully "
            "fetched from API."
        )

    else:

        handle_api_response(
            response
        )


# ============================================================
# PROGRAM 107
# DISPLAY RAW JSON
# ============================================================

def show_raw_json():

    country = input(
        "\nEnter country name: "
    ).strip()

    if not country:

        print(
            "\nPlease enter a country name."
        )

        return

    response = fetch_country_data(
        country
    )

    if not handle_api_response(
        response
    ):

        return

    data = parse_json_response(
        response
    )

    if data is None:

        return

    print("\n" + "=" * 60)

    print(
        "                  JSON RESPONSE"
    )

    print("=" * 60)

    print(data)

    print("=" * 60)


# ============================================================
# PROGRAM 109
# ERROR TESTING
# ============================================================

def test_api_error_handling():

    print(
        "\nEnter an invalid country name "
        "to test API error handling."
    )

    country = input(
        "Country: "
    ).strip()

    if not country:

        print(
            "\nCountry name cannot be empty."
        )

        return

    response = fetch_country_data(
        country
    )

    if response is not None:

        print(
            f"\nHTTP Status Code: "
            f"{response.status_code}"
        )

    handle_api_response(
        response
    )


# ============================================================
# MENU
# ============================================================

def display_menu():

    print("\n" + "=" * 60)

    print(
        "                WEB DATA & APIs"
    )

    print("=" * 60)

    print(
        "1. Fetch Country Data"
    )

    print(
        "2. Parse and Display JSON"
    )

    print(
        "3. Extract Selected Fields"
    )

    print(
        "4. Test API Error Handling"
    )

    print(
        "5. Country Information Program"
    )

    print(
        "6. Exit"
    )

    print("=" * 60)


# ============================================================
# MAIN PROGRAM
# ============================================================

def main():

    print(
        "\nWelcome to Web Data & APIs!"
    )

    while True:

        display_menu()

        choice = input(
            "Enter your choice: "
        ).strip()

        # ----------------------------------------------------
        # Program 106
        # ----------------------------------------------------

        if choice == "1":

            simple_api_fetch()

        # ----------------------------------------------------
        # Program 107
        # ----------------------------------------------------

        elif choice == "2":

            show_raw_json()

        # ----------------------------------------------------
        # Program 108
        # ----------------------------------------------------

        elif choice == "3":

            country_information_program()

        # ----------------------------------------------------
        # Program 109
        # ----------------------------------------------------

        elif choice == "4":

            test_api_error_handling()

        # ----------------------------------------------------
        # Program 110
        # ----------------------------------------------------

        elif choice == "5":

            country_information_program()

        # ----------------------------------------------------
        # Exit
        # ----------------------------------------------------

        elif choice == "6":

            print(
                "\nThank you for using "
                "Web Data & APIs!"
            )

            break

        else:

            print(
                "\nInvalid choice."
                " Please enter a number from 1 to 6."
            )


# ============================================================
# PROGRAM ENTRY POINT
# ============================================================

if __name__ == "__main__":

    main()