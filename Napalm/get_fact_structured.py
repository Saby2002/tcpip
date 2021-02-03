from napalm import get_network_driver
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("-ip", "--router_ip", help="Enter device ip address")
args = parser.parse_args()
device_ip = args.router_ip

driver = get_network_driver('iosxr')
device = driver(username='saby',
                password='saby',
                #optional_agrs={'port': 22},
                hostname=device_ip)

device.open()

print('NAPALM IS RUNNING .........')

router_dict = device.get_facts()

for i in router_dict:
    if type(router_dict[i]) == list:
        for k in router_dict[i]:
            print("\t -{}".format(k))
        else:
            print("{}: {}".format(i, router_dict[i]))

device.close()




