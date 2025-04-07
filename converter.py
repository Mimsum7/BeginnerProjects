import requests  # To make API calls to fetch exchange rates
from datetime import datetime  # To add timestamps for the saved file
import os  # For handling file operations

# Function to fetch the conversion rate using the API
def get_conversion_rate(from_currency, to_currency):
    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency.upper()}"
    response = requests.get(url)  # Make the API request
    data = response.json()  # Convert response to JSON format
    if response.status_code != 200:  # Handle network errors or invalid response
        print(f"Error: Unable to retrieve exchange rates for {from_currency}")
        return None
    if to_currency.upper() not in data["rates"]:  # Handle invalid target currency
        print(f"Error: Currency code '{to_currency}' not supported.")
        return None
    return data["rates"][to_currency.upper()]  # Return the conversion rate

# Main function to handle user input and convert currency
def convert_currency():
    print("Currency Converter Application\n")

    # Ask user for input currencies and the amount
    from_currency = input("Enter the base currency (e.g., USD): ")
    to_currency_input = input("Enter the target currency/currencies (comma-separated, e.g., EUR,GBP,JPY): ")
    to_currencies = [c.strip() for c in to_currency_input.split(",")]
    
    # Ensure the amount is a valid number
    try:
        amount = float(input(f"Enter amount in {from_currency.upper()}: "))
    except ValueError:
        print("Invalid input for amount. Please enter a number.")
        return

    results = []  # Store results to write into the text file later

    # Loop through all target currencies and perform the conversion
    for to_currency in to_currencies:
        rate = get_conversion_rate(from_currency, to_currency)
        if rate is not None:  # If rate is valid, perform conversion
            converted = amount * rate
            result = f"{amount} {from_currency.upper()} = {converted:.2f} {to_currency.upper()}"
            results.append(result)
            print(result)
        else:
            print(f"Conversion failed for {to_currency.upper()}")
    
    # Saving results to a text file with a timestamp
    filename = f"conversion_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(filename, "w") as file:
        file.write(f"Currency Conversion on {datetime.now()}\n\n")
        for line in results:
            file.write(line + "\n")
    print(f"Conversion results saved to {filename}")

# Run the main function
if __name__ == "__main__":
    convert_currency()
