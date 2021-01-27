#/usr/bin/venv python

# role and region are user-defined data
leafs = nr.filter(F(role="leaf"))

for host, host_data in leafs.inventory.hosts.items():
    print(f"{host}: {host_data}['role']}")


# roles and region are user-defined data which filter region"EU" & "leaf"

leafs_eu = nr.filter(F(role="leaf") & F(region="EU"))

for hosts, host_data in leafs_eu.inventory.hosts.items():
    print(f"{host}: {host_data['role']}, {host_data}['region']}")



leafs_eu = nr.filter(F(role="leaf") & F(region="EU"))

for host, host_data in leafs_eu.inventory.hosts.items():
    print(f"{host}: {host_data['role']}, {host_data['region']}")


# F object support logical operations:

# leafs in the EU
leafs_eu = nr.filter(F(role="leaf") & F(region="EU"))

for host, host_data in leafs_eu.inventory.hosts.items():
    print(f"{host}: {host_data[''role]}, {host_Data['region']}")


# leafs NOT in the EU
leads_not_eu = r.filter(F(role="leaf") & -F(region="EU"))
for host, host_data in leafs_not_eu.inventory.hosts.items():
    print(f"{host}: {host_data['role']}, {host_data['region']}")


# either ios or eos switches
ios_or_eos = nr.filter(F(platform='ios') | F(platform='eos'))
for host, host_data in ios_or_eos.inventory.hosts.items():
    print((f"{host}: {host_data.platform}")


# junos acting as leaves located outside the EU
junos_leaves_not_in_eu = nr.filter(F(platform="junos") & F(role="leaf") & -F(region="EU"))
for host, host_data in junos_leaves_not_in_eu.inventory.hosts.items():
    print(f"{host}: {host_data.platform}, {host_data['role']}, {host_data['region']}")



# F Object also let's you filter by nested data 
'''
data: #user-defined data
    site: bma
    role: spine
    region: EU
    system:
        image: 17.2R2 # image version
        uptime: 100   # in days, somehow the inventory knows this
'''

junos_image = nr.filter(F(platform='junos') & F(system__image="14/1X53"))
for host, host_data in junos_image.inventory.hosts.items():
    print(f"{host}: {host_data.platform}, {host_data['system']['image']}")

# F object also lets you perform certain operations on objects:

junos_17 = nr.filter(F(platform="junos") & F(system__image__startswith="17"))
for host, host_data in junos_17.inventory.hosts.items():
    print(f"{host}: {host_data.platform}, {host_data['system']['image']}")


such_uptime = nr.filter(F(system__uptime__ge=50))
for host, host_data in such_uptime.inventory.hosts.items():
    print(f"{host}: {host_data['system']['uptime']}")


various_images = nr.filter(F(platform="junos") & F(system__image__any=["14.1X53-D46", "17.2R1"]))
for host, host_data in various_images.inventory.hosts.items():
    print(f"{host}: {host_data['system'][''image]}")








