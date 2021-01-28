#/usr/bin/venv python

# Module

from getpass import getpass
from pprint import pprint
from napalm import get_network_driver

# Supress SSL Certifcation Warnings
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


# Device Definitions
password = getpass()

R1 = dict(
        hostname="R1",
        device_type="ios",
        username="lab",
        password=password,
        optional_args={},
)
eos1 = dict(
        hostname="EOS1",
        device_type="eos",
        username="admin",
        password=password,
        optional_args={"port": 8443},
)
XRVM = dict(
        hostname="tcpipworld",
        device_type="iosxr",
        username="saby",
        password=password,
)

# Device we are testing
my_device = XRVM

# NAPALM Class Selection/Object Creation
device_type = my_device.pop("device_type")
driver = get_network_driver(device_type)
device = driver(**my_device)

# NAPALM Action
print()
print("\n\n>>>Test Device open")
device.open()

print()
output = device.get_facts()
#output = device.get_interfaces()
#output = device.get_lld_neighbors()
pprint(output)
print()


