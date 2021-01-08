#!/usr/bin/env python

# Modules

import json
import jinja2
import datetime
import paramiko 
import time

# Variables
path_inventory = 'Inventory/inventory.json'


# User defined functon for jsontodict
def JSONtoDICT(filepath):
    f = open(filepath, 'r')
    new_dict = json.loads(f.read())
    f.close()

    return new_dict

# User defined function for Jinja2 to create template
def create_config(nos, dev_vars):
    f = open(f'Inventory/jinja_template/{nos}_if_oc.j2', 'r')
    config_template = jinja2.Template(f.read())
    f.close()
    result_config = config_template.render(interfaces=dev_vars['interfaces'])
    
    return result_config

# User defined function for Paramiko
def push_config(ip_addr, hostname, config, username, password):
    get_connection_ready = paramiko.SSHClient()
    get_connection_ready.set_missing_host_key_policy(paramiko.AutoAddPolicy())        
    get_connection_ready.connect(ip_addr, port=22, username=username, password=password,
                                 look_for_keys=False, allow_agent=False)
    cli = get_connection_ready.invoke_shell()
    cli.recv(65535)

    for config_line in config:
        cli.send(f'{config_line}\n')
        cli.recv(65535)
            
        time.sleep(.5)

# Body
print(f'##### {datetime.datetime.now()} ##### Importing inventory')
inventory = JSONtoDICT(path_inventory)
print(f'##### {datetime.datetime.now()} ##### Importing complete')
for inventory_entry in inventory['devices']:
    print(f'##### {datetime.datetime.now()} ##### Importing Variables #### {inventory_entry["hostname"]}')
    device_vars = JSONtoDICT(f'Inventory/json_templates/{inventory_entry["hostname"]}_oc_if.json')
    print(f'##### {datetime.datetime.now()} ##### Importing Variables #### {inventory_entry["hostname"]} completed')
    print(f'##### {datetime.datetime.now()} ##### DEVICE CONFIG  #### {inventory_entry["hostname"]}')
    device_config = create_config(inventory_entry['nos'], device_vars)
    config_line = device_config.split('\n')
    config_line = list(filter(None, config_line))
    print(config_line)
    print(f'##### {datetime.datetime.now()} ##### DEVICE CONFIG  #### {inventory_entry["hostname"]} completed')

    print(f'##### {datetime.datetime.now()} ##### PUSHING CONFIG  #### {inventory_entry["hostname"]}')


    push_config(ip_addr=inventory_entry['ip_address'], hostname=inventory_entry['hostname'],
                username=inventory_entry['username'], password=inventory_entry['password'],
                config=config_line)


    print(f'##### {datetime.datetime.now()} ##### COMPLETED  #### {inventory_entry["hostname"]} completed')



