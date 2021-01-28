#/usr/bin/venv python

# Modules
from getpass import getpass
from pprint import pprint
from napalm import get_network_driver


# Variables
XRVM = dict(
        hostname="tcpipworld",
        device_type="iosxr",
        username="saby",
        password=getpass(),
        optional_args={},
)

# Body
device_type = XRVM.pop("device_type")
driver = get_network_driver(device_type)
device = driver(**XRVM)

print()
print("\n\n>>> Test device open")
device.open() # Make a Netmiko SSH connection

print()
output = device.get_facts()
pprint(output)
pprint()


