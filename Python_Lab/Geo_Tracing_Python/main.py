#/usr/bin/env python 

# Modules 
import json 
import asyncio
import os
import sys
from bin.poller import GetIP
import folium

# Variables
path_data = 'input/sites.json'

# Body 
try:
    with open(path_data, 'r') as f:
        sites = json.loads(f.read())

except FileNotFoundError:
    sys.exit(f'The file {path_data} does not exits. Check it.')

except json.decoder.JSONDecodeError:
    sys.exit(f'The file {path_data} is malformed and can\'t be read.')


ip_info = asyncio.run(GetIP(sites['sites']))

with open('.cache.json', 'w') as f:
    f.write(json.dumps(ip_info, sort_keys=True, indent=4))

m = folium.Map()
for ip_ad in ip_info:
    if isinstance(ip_ad['latitude'], float):
        folium.Marker(
            location=[ip_ad['latitude'], ip_ad['longitude']],
            popup=f'{ip_ad["ip"]}, {ip_ad["org"]}, {ip_ad["asn"]}, {ip_ad["country_code_iso3"]}',
            icon=folium.Icon(color='red', icon='cloud')
        ).add_to(m)

m.save('index.html')

