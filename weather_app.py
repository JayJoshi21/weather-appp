import requests

API_KEY = "b6907d289e10d714a6e88b30761fae22"
BASE_URL = "https://samples.openweathermap.org/data/2.5/forecast/hourly"


def get_weather_data(city):
    url = f"{BASE_URL}?q={city}&appid={API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None


def print_temperature_by_date(weather_data, date):
    for forecast in weather_data["list"]:
        if date in forecast["dt_txt"]:
            print(
                f"Temperature at {forecast['dt_txt']}: {forecast['main']['temp']}°C")
            break
    else:
        print("No data available for the given date.")


def print_wind_speed_by_date(weather_data, date):
    for forecast in weather_data["list"]:
        if date in forecast["dt_txt"]:
            print(
                f"Wind Speed at {forecast['dt_txt']}: {forecast['wind']['speed']} m/s")
            break
    else:
        print("No data available for the given date.")


def print_pressure_by_date(weather_data, date):
    for forecast in weather_data["list"]:
        if date in forecast["dt_txt"]:
            print(
                f"Pressure at {forecast['dt_txt']}: {forecast['main']['pressure']} hPa")
            break
    else:
        print("No data available for the given date.")


def main():
    city = "London"
    weather_data = get_weather_data(city)

    if not weather_data:
        print("Failed to fetch weather data. Please try again later.")
        return

    while True:
        print("\nChoose an option:")
        print("1. Get weather")
        print("2. Get Wind Speed")
        print("3. Get Pressure")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            date = input("Enter the date (YYYY-MM-DD HH:MM:SS): ")
            print_temperature_by_date(weather_data, date)
        elif choice == "2":
            date = input("Enter the date (YYYY-MM-DD HH:MM:SS): ")
            print_wind_speed_by_date(weather_data, date)
        elif choice == "3":
            date = input("Enter the date (YYYY-MM-DD HH:MM:SS): ")
            print_pressure_by_date(weather_data, date)
        elif choice == "0":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
