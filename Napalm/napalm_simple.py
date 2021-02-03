#/usr/bin/venv python

# Modules
from getpass import getpass
from pprint import pprint
from napalm import get_network_driver


# Variables
XR1 = dict(
        hostname="tcpipworld",
        device_type="iosxr",
        username="saby",
        password=getpass(),
        #optional_args={},
)

# Body
device_type = XR1.pop("device_type")
driver = get_network_driver(device_type)
device = driver(**XR1)

print()
print("\n\n>>> Test device open")
device.open() # Make a Netmiko SSH connection

print()
output = device.get_facts()
pprint(output)
pprint()


