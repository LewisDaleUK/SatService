# SatService

Simple REST API that accepts a lat/lon location and an optional date, and returns a list of satellites visible in an open sky at that location.

## Example Request

### Input

```python
import json
from urllib import request

data = {
  'lat': 51.501476,
  'lon': -0.140634,
  'date': "2017/12/25 15:00:00"
}

json_data = json.dumps(data).encode('utf-8')

req = request.Request('http://my-endpoint:5000/satellites', data=json_data, headers={'content-type': 'application/json'})

res = request.urlopen(req)
```

### Output

```
>>> res.readlines()
[{'lat': 52.563920078745866, 'alt': 61.594789369147556, 'name': 'GPS BIIR-2  (PRN 13)', 'lon': -35.95546816840278},
{'lat': 34.275067462755814, 'alt': 58.959053519385485, 'name': 'GPS BIIR-4  (PRN 20)', 'lon': -23.239479594347436},
{'lat': 24.650483978750763, 'alt': 41.4327129770519, 'name': 'GPS BIIR-5  (PRN 28)', 'lon': 35.82845055550264},
{'lat': 50.345689787284584, 'alt': 14.728590897911523, 'name': 'GPS BIIR-9  (PRN 21)', 'lon': -110.23844724168374},
{'lat': 41.52387209680948, 'alt': 31.083176629636284, 'name': 'GPS BIIRM-4 (PRN 15)', 'lon': -69.6022094539362},
{'lat': 48.79378884558765, 'alt': 28.462701130027313, 'name': 'GPS BIIRM-6 (PRN 07)', 'lon': 81.18547262584747},
{'lat': 25.95847545009196, 'alt': 56.12177586268927, 'name': 'GPS BIIRM-8 (PRN 05)', 'lon': -8.172562959862146},
{'lat': 55.992063740161555, 'alt': 4.7660103801865175, 'name': 'GPS BIIF-4  (PRN 27)', 'lon': 162.4636992206237},
{'lat': 54.040067392358196, 'alt': 51.0589015555119, 'name': 'GPS BIIF-5  (PRN 30)', 'lon': 50.834348841263974},
{'lat': 38.3512833782844, 'alt': 7.053095381783879, 'name': 'GPS BIIF-10  (PRN 08)', 'lon': 105.5435527911354},
{'lat': 51.92441971204133, 'alt': 9.828597819418743, 'name': 'COSMOS 2425 (716)', 'lon': 122.99386649781758},
{'lat': 35.55258263002041, 'alt': 63.330080890059335, 'name': 'COSMOS 2457 (733)', 'lon': 17.360416464373763},
{'lat': -7.197752385102402, 'alt': 7.270380347868087, 'name': 'COSMOS 2458 (734)', 'lon': 41.11850719975839},
{'lat': 64.48456727489908, 'alt': 12.115888153578029, 'name': 'COSMOS 2461 (735)', 'lon': 170.99782934325788},
{'lat': 49.28839016414495, 'alt': 11.669121211099263, 'name': 'COSMOS 2460 (732)', 'lon': -113.16098956488382},
{'lat': 56.95320796016575, 'alt': 69.38416249487271, 'name': 'COSMOS 2464 (736)', 'lon': 24.966299973141105},
{'lat': 63.8370380208252, 'alt': 59.63972968150145, 'name': 'COSMOS 2477 (745)', 'lon': -37.77242484612582},
{'lat': 45.998793474948386, 'alt': 9.576567254139858, 'name': 'COSMOS 2475 (743)', 'lon': -111.9624006485733},
{'lat': 20.306253147738165, 'alt': 48.2479474478769, 'name': 'COSMOS 2501 (702)', 'lon': -10.564574608149712}]
```
