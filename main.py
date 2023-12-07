import requests
import json

def get_iss_location():
    # API endpoint for ISS current location
    api_url = "https://api.wheretheiss.at/v1/satellites/25544"

    try:
        # Send GET request to the API
        response = requests.get(api_url)
        response.raise_for_status()

        # Parse the JSON data
        iss_data = response.json()

        # Extract relevant information
        latitude = iss_data["latitude"]
        longitude = iss_data["longitude"]

        print(f"ISS Current Location: Latitude {latitude}, Longitude {longitude}")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching ISS location: {e}")

if __name__ == "__main__":
    get_iss_location()
