import csv
import requests

# API endpoint
url = "https://restcountries.eu/rest/v2/all"

# Send GET request to the API
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    countries = response.json()

    # Specify the file name
    file_name = "countries.csv"

    # Open the CSV file for writing
    with open(file_name, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)

        # Write the header
        writer.writerow(['Country Name', 'Capital City', 'Region', 'Population Size', 'Number of Currencies', 'Number of Languages'])

        # Write data to the CSV file
        for country in countries:
            name = country.get('name', '')
            capital = country.get('capital', '')
            region = country.get('region', '')
            population = country.get('population', '')
            currencies = len(country.get('currencies', []))
            languages = len(country.get('languages', []))
            writer.writerow([name, capital, region, population, currencies, languages])

    print(f"CSV file {file_name} has been created.")
else:
    print("Failed to retrieve data from the API.")