import os
import time
import stat
from urllib import request

from .config import DATA_LOCATION, EPHEM_URLS

def file_age():
    return time.time() - os.stat(DATA_LOCATION)[stat.ST_MTIME]

def download_data():
    data = []
    for url in EPHEM_URLS:
        d = request.urlopen(url)
        data += d.readlines()

    with open(DATA_LOCATION, 'w') as f:
        for line in data:
            f.write(line.decode("utf-8"))

def data_exists():
    return os.path.isfile(DATA_LOCATION) and file_age() < 604800

def get_data():
    if not data_exists():
        download_data()

    with open(DATA_LOCATION, 'r') as f:
        lines = f.readlines()
        lines = [l.replace('\n','').rstrip() for l in lines]
        chunked = [lines[i:i+3] for i in range(0, len(lines), 3)]
        return chunked




