from napalm import get_network_driver
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument("-ip", "--router_ip", help="Enter device ip address")
args = parser.parse_args()
device_ip = args.router_ip

driver = get_network_driver('iosxr')
device = driver(username='saby',
                password='saby',
                hostname=device_ip)

device.open()
print("NAPALM IS RUNNING .....")
device.load_replace_candidate(filename='XRVM_Config.cfg')
diffs = device.compare_config()

if len(diffs) > 0:
    print(diffs)

    commit = input("Type COMMIT to commit the configuration or hit ENTER to abort: ")
    if commit == 'COMMIT':

        try:
            device.commit_config()
        except Exception as inst:
            print('\nAn error occured with the commit: ')
            print(type(inst))
            sys.exit(inst)
            print()

        else:
            print('Config committed')
    else:
        sys.exit('Script aborted by user')
else:
    print('No changes needed')
    device.discard_config()

device.close()

