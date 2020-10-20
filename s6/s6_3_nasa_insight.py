# Use NASA InSight API to write temperature information for most recent sols into a file

import requests
import json

# Set file name to be used and NASA URL
filename = "s6_3_nasa_insight_temp.txt"
url = "https://api.nasa.gov/insight_weather/?api_key=DEMO_KEY&feedtype=json&ver=1.0"

# Run a get call and pull out response content
r = requests.get(url)
r_content = r.content

# Convert content to json
data = json.loads(r_content)

# Loop through all top-level keys
for key in data:
    # If key can be converted to an integer, write into file, otherwise pass
    try:
        int_key = int(key)
    except ValueError:
        pass
    else:
        temp = str(data[key]['AT'])
        with open(filename, 'a') as f:
            f.write(key)
            f.write(temp)
            f.write("\n")
