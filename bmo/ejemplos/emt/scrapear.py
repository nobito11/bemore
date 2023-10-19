import requests
import json

# URL for the EMT Málaga API with the bus stop code
bus_stop_url = "https://www.emtmalaga.es/emt-mobile/informacionParada.html?codParada=3325"

# Send an HTTP GET request to the URL
response = requests.get(bus_stop_url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content to extract the arrival time (You may need to use a library like BeautifulSoup for HTML parsing)
    # For this example, I'll assume the arrival time is in a JSON format in the HTML response.
    
    # Extract the JSON data from the HTML content
    start_index = response.text.find("var frecuencias =") + len("var frecuencias =")
    end_index = response.text.find("];", start_index) + 1
    json_data = response.text[start_index:end_index]

    # Parse the JSON data
    data = json.loads(json_data)

    # Extract the arrival time (you may need to adjust the index based on the actual JSON structure)
    arrival_time = data[0]['tiempo1']

    # Print the arrival time
    print("Estimated arrival time:", arrival_time)

    # You can store the arrival time in a variable for further use
    # arrival_time_variable = arrival_time

else:
    print("Failed to fetch data. Status code:", response.status_code)