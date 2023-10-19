import urllib.request
import pandas as pd
import json

#url = 'https://lwbin-dev.ad.umanitoba.ca/data/api/3/action/datastore_search?resource_id=ea474f80-dcbe-4647-a28d-7fdce1293e09'  
url = 'https://ouvert.canada.ca/fr/search/hospitalityq'
# make a request and receive a response with urlopen()
http_response = urllib.request.urlopen(url)

# Returns and reads the response body
raw_data=http_response.read()

# raw_data is a bytes object and will need to be decoded.
# Get the encoding from the response.
encoding = http_response.info().get_content_charset()

# Decode the byte object using json.loads
data_dict = json.loads(raw_data.decode(encoding))

# get the resource data
data=data_dict['result']['records']

#Output data as a dataframe for easy manipulation
df1= pd.DataFrame(data)

# Save to csv file
df1.to_csv('output.csv', index=False)