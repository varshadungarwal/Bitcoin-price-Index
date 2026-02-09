# Bitcoin-price-Index
Bitcoin Price Index

This project allows users to calculate the current cost of a specified number of Bitcoins in USD using the CoinCap v3 API.

Inspired by

This project was inspired by CS50’s Bitcoin Price Index problem set, where students learn to interact with APIs, handle JSON data, and manage command-line input and error handling in Python.

Features

Accepts the number of Bitcoins to buy as a command-line argument.

Validates input and exits gracefully if the input is missing or invalid.

Fetches real-time Bitcoin price from the CoinCap API.

Displays the total cost in USD to four decimal places with thousands separators.

Handles network or API exceptions safely.

Setup

Sign up for a CoinCap account and generate an API key.

Install the requests library if not already installed:

pip install requests


Run the program with:

python bitcoin.py <number_of_bitcoins>

Example
python bitcoin.py 2.5
# Output: 2.5 Bitcoins = $97,123.4567
