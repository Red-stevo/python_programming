import phonenumbers
from phonenumbers import geocoder, carrier, NumberParseException
from opencage.geocoder import OpenCageGeocode
import folium
import os


# Function to validate the phone number
def validate_phone_number(phone_number_input):
    try:
        phone_number = phonenumbers.parse(phone_number_input)
        if not phonenumbers.is_valid_number(phone_number):
            raise ValueError("Invalid phone number.")
        return phone_number
    except NumberParseException:
        raise ValueError("Invalid phone number format.")


# Function to get detailed location information
def get_location_details(phone_number):
    try:
        # Get the country name
        country = geocoder.country_name_for_number(phone_number, "en")
        # Get the city or region if available
        region = geocoder.description_for_number(phone_number, "en")
        # Get the service provider
        service_provider = carrier.name_for_number(phone_number, "en")
        return country, region, service_provider
    except Exception as e:
        raise RuntimeError(f"Error in fetching details: {e}")


# Function to get geographical coordinates
def get_coordinates(geocoder, location_query):
    try:
        results = geocoder.geocode(location_query)
        if results:
            # Get the most accurate result available
            precise_result = max(results, key=lambda r: r['confidence'])
            lat = precise_result['geometry']['lat']
            lng = precise_result['geometry']['lng']
            return lat, lng
        else:
            raise ValueError("Location not found.")
    except Exception as e:
        raise RuntimeError(f"Error in fetching coordinates: {e}")


def main():
    # Load OpenCage API key from environment variable
    key = os.getenv("OPENCAGE_API_KEY", "83c1a12cac344aa9a95de6efa7c2d5f9")  # replace with your key
    geocoder = OpenCageGeocode(key)

    # Input the phone number with country code
    phone_number_input = "+254705695815"

    try:
        phone_number = validate_phone_number(phone_number_input)
        country, region, service_provider = get_location_details(phone_number)

        print(f"Country: {country}")
        print(f"Region/City: {region}")
        print(f"Service Provider: {service_provider}")

        # Initialize location_query with a fallback value
        location_query = f"{region}, {country}" if region else country

        # Bias towards Nyeri if region is not specific enough
        if "Nyeri" not in region and "Kenya" in country:
            region = "Nyeri, Dedan Kimathi University"
            lat, lng = 0.5143, 36.9571
            location_query = region  # Set location_query explicitly
        else:
            # Try to get coordinates for the region or city if available, otherwise fallback to country
            lat, lng = get_coordinates(geocoder, location_query)

        print(f"Latitude: {lat}, Longitude: {lng}")

        # Create a map to visualize the location
        my_map = folium.Map(location=[lat, lng], zoom_start=15 if "Nyeri" in location_query else 6)
        folium.Marker([lat, lng], popup=f"{region if region else country} - {service_provider}").add_to(my_map)
        my_map.save("location.html")
        print("Location map saved as 'location.html'.")

    except ValueError as ve:
        print(f"Input Error: {ve}")
    except RuntimeError as re:
        print(f"Runtime Error: {re}")


if __name__ == "__main__":
    main()
