# Print the values of name, post_code and street_number from the dictionary
# Extension: Print the values of longitude and latitude from the inner dictionary (edited)

# Provided dictionary
place = {
    'name': 'The Anchor',
    'post_code': 'E14 6HY',
    'street_number': '54',
    'location': {
        'longitude': 127,
        'latitude': 63,
    }
}

# Print requested values
print(place['name'])
print(place['post_code'])
print(place['street_number'])

# Print longitude and latitude
print('longitude:', place['location']['longitude'])
print('latitude:', place['location']['latitude'])
