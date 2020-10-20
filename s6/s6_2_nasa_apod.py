# Use NASA's APOD API

import requests
import json

# Set file name to be used locally
filename = "s6_2_nasa_apod.png"

# Either hard-code the parameters into the URL and run a get call
#url = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY&date=2010-05-05"
#r = requests.get(url)

# Or create a payload dictionary and pass the payload as parameters to the get call
url = "https://api.nasa.gov/planetary/apod"
payload = {'api_key' : 'DEMO_KEY', 'date' : '2010-07-05'}
r = requests.get(url, params=payload)

# Convert the content of the response to json and return available keys
data = json.loads(r.content)
print(data.keys())

# Choose appropriate key using standard dictionary notation
img_url = data['url']

# Use the image URL within a second get call and store the content of the response
r_img = requests.get(img_url)
img = r_img.content

# Save the image, i.e. content of the response, into the file
with open(filename, "wb") as f:
    f.write(img)
