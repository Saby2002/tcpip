#!/usr/bin/env python

# Module
import paramiko
import time

# Variables
device_list = [{ 'ip_address': '169.254.255.64', 'username': 'saby', 'password': 'saby' }]

# Body
for device in device_list:
    get_connection_ready = paramiko.SSHClient()
    get_connection_ready.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    get_connection_ready.connect(hostname=device['ip_address'], port=22,
                                 username=device['username'], password=device['password'],
                                 look_for_keys=False, allow_agent=False)
    active_connection = get_connection_ready.invoke_shell()
    time.sleep(1.0)
    output = active_connection.recv(65535).decode("utf-8")
    print(output)
    active_connection.send("show ip int brief" + "\n")
    time.sleep(1.0)
    output = active_connection.recv(65535).decode("utf-8")
    print(output)
    active_connection.close()
