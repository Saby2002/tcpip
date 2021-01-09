#/usr/bin/env python

# Module
from helpers.functions import jsontodict,csvtodict
from helpers.yangbuilder import YANGBuilder

# Variable
path_inventory = 'Inventory/inventory.json'

# Body
inventory = jsontodict(path_inventory)

for inventory_entry in inventory['devices']:
    device_vars = csvtodict(f'Inventory/{inventory_entry["hostname"]}.csv')

    ddm = YANGBuilder(inventory_entry['nos'])
    ddm.fillin(device_vars)
    device_json = ddm.getJSON()

    print(device_json)

