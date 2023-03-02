from flask import Flask, render_template, request
from utils import get_carpark_data, parse_carpark_csv, calculate_distances, get_top_carparks
import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/results')
def results():
    # get user's location from AJAX request
    user_lat = request.args.get('lat')
    user_lng = request.args.get('lng')

    now = datetime.datetime.now()
    DATE_TIME = now.strftime('%Y-%m-%dT%H:%M:%S')  # Format current datetime as string
    # query Carpark Availability API and parse CSV file
    
    carpark_data = parse_carpark_csv()

    # calculate distances and filter to top 3 carparks
    carpark_data = calculate_distances(user_lat, user_lng, carpark_data)
    top_carparks = get_top_carparks(carpark_data)

    # Get current carpark availability data
    current_carpark_availability = get_carpark_data(DATE_TIME)['items'][0]['carpark_data']

    # Append carpark availability to each top carpark
    for carpark in top_carparks:
        carpark_number = carpark['car_park_no']
        for cp_data in current_carpark_availability:
            if cp_data['carpark_number'] == carpark_number:
                carpark['availability'] = cp_data['carpark_info']

    # render template with top 3 carparks
    return render_template('results.html', carparks=top_carparks)

if __name__ == '__main__':
   app.run(debug=True)