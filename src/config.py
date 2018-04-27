import os
dir_path = os.getcwd()

DATA_LOCATION = "{}/ephemeral.data".format(dir_path)

EPHEM_URLS = [
    "https://www.celestrak.com/NORAD/elements/gps-ops.txt",
    "https://www.celestrak.com/NORAD/elements/supplemental/glonass.txt"
]

