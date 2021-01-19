#/usr/bin/env python

# Module
from helpers.functions import jsontodict,csvtodict
from helpers.yangbuilder import YANGBuilder
from helpers.drivers import NetConfDriver,GnmiDriver,NetboxDriver
import datetime

# Variable
path_inventory = 'Inventory/inventory.json'
path_temporary = 'Inventory/NETCONF'
netbox_url = 'http://0.0.0.0:8000/api'
netbox_token = '0123456789abcdef0123456789abcdef01234567'
site_name = 'lab-nat'


# Body
#inventory = jsontodict(path_inventory)
print(f'Start Time {datetime.datetime.now()}')

nb = NetboxDriver(url=netbox_url, token=netbox_token)
inventory = nb.buildInventory(site_name=site_name)
print(inventory)

print(f'End Time {datetime.datetime.now()}')


if False:
    for inventory_entry in inventory['devices']:
        device_vars = csvtodict(f'Inventory/{inventory_entry["hostname"]}.csv')

        ddm = YANGBuilder(inventory_entry['nos'])
        ddm.fillin(device_vars)
        device_json = ddm.getJSON()

    # Netconf Operation
   # dc = NetConfDriver(ip=inventory_entry['ip_address'], host=inventory_entry['hostname'],
                       #nos=inventory_entry['nos'], user=inventory_entry['username'],
                       #passwd=inventory_entry['password'])

   # dc.prepareMessage(device_json, path_temporary)
   # dc.pushConfig()


    # Gnmi Operation
        dc = GnmiDriver(ip=inventory_entry['ip_address'], host=inventory_entry['hostname'],
                    nos=inventory_entry['nos'], user=inventory_entry['username'],
                    passwd=inventory_entry['password'])

        dc.prepareMessage(device_json)
    
        if inventory_entry['nos'] != 'iosxr' and 'eos':

            dc.pushConfig()
    

