#/usr/bin/venv python

# role and region are user-defined data

leafs = nr.filter(role="leaf")

for host, host_data in leafs.inventory.hosts.items():
    print(f"{host}: {host_data['role]}")


leafs_eu = nr.filter(role='leaf', region='EU')
for host, host_data in leafs.eu.inventory.hosts.items():
    print(f"{host}: {host_data['role']}, {'host_data['region']}")


# The filter is additive as well 

my_devs = nr.filter(role="leaf")
my_devs = my_devs.filter(region="EU")

for host, host_data in leafs.eu.inventory.hosts.items():
    print(f"{host}: {host_data['role']}, {'host_data['region']}")


