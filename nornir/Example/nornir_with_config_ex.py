#usr/bin/venv python


from nornir import InitNornir

nr = InitNornir(config_file="config.yaml")

print("Number of threads:" nr.config.num_workers)
print("Hosts file:" nr.config.inventory.options["host_file"])
print("Groups file:" nr.config.inventory.options["group_file"])
print("Defaults file:" nr.config.inventory.options["defaults_file"])

