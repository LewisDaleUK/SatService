import ephem
import numpy as np

def read_tle(location, date, tle):
    sat, line1, line2 = tle
    lat, lon = location

    observer = ephem.Observer()
    observer.lat = np.deg2rad(lat)
    observer.lon = np.deg2rad(lon)
    observer.date = date

    body = ephem.readtle(sat, line1, line2)

    body.compute(observer)
    lat = np.rad2deg(body.sublat)
    lon = np.rad2deg(body.sublong)
    alt = np.rad2deg(body.alt)

    return { 'name': sat, 'lat': lat, 'lon': lon, 'alt': alt }

