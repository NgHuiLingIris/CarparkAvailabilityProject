import requests
import csv
import geopy.distance

# Define API endpoint and parameters
API_ENDPOINT = 'https://api.data.gov.sg/v1/transport/carpark-availability'
carpark_data = None  # Initialize the in-memory data to None
# Define function to get carpark availability data
def get_carpark_data(date_time):
    params = {'date_time': date_time}
    response = requests.get(API_ENDPOINT, params=params)
    data = response.json()
    return data

def parse_carpark_csv():
    global carpark_data  # Use the global carpark_data variable

    # If the carpark data is already in memory, return it
    if carpark_data is not None:
        return carpark_data

    # Otherwise, read the CSV file and store the data in memory
    with open('data/hdb_carpark_information_wgs84.csv') as f:
        reader = csv.DictReader(f)
        carpark_data = [row for row in reader]
    return carpark_data

def calculate_distances(user_lat, user_lng, carpark_data):
    # calculate distances to each carpark and add to list of dictionaries
    for carpark in carpark_data:
        lat = float(carpark['lat'])
        lng = float(carpark['lon'])
        coords = (lat, lng)
        distance = geopy.distance.distance((user_lat, user_lng), coords).km
        carpark['distance'] = distance
    return carpark_data

def get_top_carparks(carpark_data, num_carparks=10):
    # sort carpark list by distance
    sorted_carparks = sorted(carpark_data, key=lambda x: x['distance'])

    # filter list to top N carparks
    top_carparks = sorted_carparks[:num_carparks]
    return top_carparks
