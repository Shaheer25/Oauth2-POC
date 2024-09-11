from geopy.geocoders import Nominatim

def get_location(lat, lon):
    geolocator = Nominatim(user_agent="geoapiExercises")

    try:
        location = geolocator.reverse((lat, lon), language='en')
        address = location.raw['address']
        print(address)
        city = address.get('city', '')
        state = address.get('state', '')
        code = address.get('postcode', '')
        country = address.get('country', '')
        country_code = address.get('country_code', '')
        if not city:
            city = address.get('town', '') or address.get('province', '')

        return ({
            'city' : city,
            'state' : state,
            'zip-code' : code if code else '',
            'country' : country,
            'country_code' : country_code

        })
    except Exception as e:
        return f"Error: {e}"

# Example usage
latitude = 27.973126
longitude = 61.796085
print(get_location(latitude, longitude))
