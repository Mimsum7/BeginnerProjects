import requests  # To make the API call
import json  # To work with JSON data

def get_exchange_rate(base_currency, target_currency):
    try:
        # Use an open API that gives real-time exchange rates
        url = f"https://api.exchangerate-api.com/v4/latest/{base_currency.upper()}" # f string is used to dynsmically create a url
        response = requests.get(url) # Makes GET request to the API for it to get the exchange rate data
        data = response.json()

        # Check if the currency exists
        if target_currency.upper() in data["rates"]:
            return data["rates"][target_currency.upper()] # .upper() is a funtion to turn the input into upper case if it is lower case
        else:
            print("Invalid target currency code.")
            return None

    except Exception as e:
        print("Error fetching data:", e)
        return None

def convert_currency():
    base = input("Enter base currency (e.g. USD): ")
    target = input("Enter target currency (e.g. EUR): ")

    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    rate = get_exchange_rate(base, target)
    if rate:
        converted = amount * rate
        print(f"{amount} {base.upper()} = {converted:.2f} {target.upper()}")

if __name__ == "__main__":
    convert_currency()

