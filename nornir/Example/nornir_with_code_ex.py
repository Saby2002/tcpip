#/usr/bin/venv python

from nornir import InitNornir

nr = InitNornir(
    num_workers=100,
    inventory={
        "options": {
            "host_file": "inventory/hosts.yaml",
            "group_file": "inventory/groups.yaml",
            "defaults_file": "inventory/defaults.yaml",
            }
        }
    )

print("Number of threads:", nr.config.num_workers)
print("Hosts file:", nr.config.inventory.options["host_file"])
print("Groups file:", nr.config.inventory.options["group_file"])
print("Defaults file:", nr.config.inventory.options["defaults_file"])


