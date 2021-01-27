# using function 

import re

def eos_maintenance_images(host):
    """ EOS images end either in M (maintenance images) or F(feature images) """
    return bool(re.match(".*M$", host["system"]["image"]))


maintenance_images = nr.filter(filter_func=eos_maintenance_images)
for host, host_data in maintenance_images.inventory.hosts.items():
    print(f"{host}: {host_data.platform}, {host_data['system']['image']}")





