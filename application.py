from datetime import datetime
import json

from flask import Flask, request
from src import data, tle

application = Flask(__name__)

@application.route("/satellites", methods=["POST"])
def get_satellites():
    req_data = request.get_json()

    lat = float(req_data.get('lat', None))
    lon = float(req_data.get('lon', None))
    date = req_data.get('date', None)

    if date is None:
        date = datetime.now().strftime("%Y/%m/%d %H:%M:%S")

    tles = data.get_data()
    visible_satellites = []

    for tle_data in tles:
        sat = tle.read_tle((lat,lon), date, tle_data)
        if(sat['alt'] > 0.0):
            visible_satellites.append(sat)

    return json.dumps(visible_satellites)

if __name__ == "__main__":
    application.run(debug=True)
