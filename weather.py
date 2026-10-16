import requests

API_KEY = "dda176e0dc88c57faa87fa28e43da414"

town_name = input("Enter the name of a town: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={town_name}&appid={API_KEY}&units=metric"

try:
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        temp = data["main"]["temp"]
        # Extract the official country code for better presentation
        country = data["sys"]["country"]
        print(f"\nThe current temperature in {town_name.title()}, {country} is {temp}°C")

    elif response.status_code == 404:
        print(f"\nError: The town '{town_name}' was not found. Please check the spelling.")

    else:
        print(f"\nError: Unable to fetch data (Status Code: {response.status_code})")
        print(response.json().get("message"))

except Exception as e:
    print(f"\nAn error occurred: {e}")