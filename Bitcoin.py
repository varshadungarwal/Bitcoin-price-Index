import sys
import requests


def main():
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")

    try:
        n = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")
    api_key = "4a99fd0fcf0b71c3420e495351194064e0e525796c93ac547e9e9b507c3bece4"
    try:
        url = f"https://rest.coincap.io/v3/assets/bitcoin?apiKey={api_key}"
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException:
        sys.exit("Error fetching data from API")
    try:
        data = response.json()
        price = float(data["data"]["priceUsd"])
    except (KeyError, ValueError):
        sys.exit("Error parsing API response")


    cost = n * price


    print(f"${cost:,.4f}")


if __name__ == "__main__":
    main()
