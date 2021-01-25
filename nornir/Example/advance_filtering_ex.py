#/usr/bin/venv python

# role and region are user-defined data
leafs = nr.filter(F(role="leaf"))

for host, host_data in leafs.inventory.hosts.items():
    print(f"{host}: {host_data}['role']}")


# roles and region are user-defined data which filter region"EU" & "leaf"

leafs_eu = nr.filter(F(role="leaf") & F(region="EU"))

for hosts, host_data in leafs_eu.inventory.hosts.items():
    print(f"{host}: {host_data['role']}, {host_data}['region']}")


