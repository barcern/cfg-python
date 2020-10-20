# Use an API call to save an image locally

import requests

# Specify URL of image and file name to be used locally
url = "https://images.unsplash.com/photo-1580645316873-870c9ac044d4?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=500&q=60"
filename = "s6_1_get_request_image.png"

# Use requests package to run a get call
response = requests.get(url)

# Check the status code of the response
if response.status_code == 200:
    # Set image to be the content of the response and save it into the file
    img = response.content
    with open(filename, "wb") as image:
        image.write(img)
else:
    # Otherwise print the problem status code
    print(f"There is a problem with your API call (status code {response.status_code}).")
