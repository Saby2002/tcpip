#/usr/bin/env python


# Module 
from nornir import InitNornir
from nornir.core.task import Task, Result
from helper.functions import csv_to_dict
from nornir_utils.plugins.functions import print_result
import jinja2
import datetime
import pynetbox
from pprint import pprint




# Variable
path = {
            "input": "./input/interfaces.csv",
            "templates": "./Template"
        }

netbox_var = {
             "url": "http://0.0.0.0:8000",
             "token": "0123456789abcdef0123456789abcdef01234567"
}


# Nornir Task

def prepare_config(task: Task, template_path: str, arg1: dict) -> Result:

    with open(f"{template_path}/{task.host.groups[0]}/interfaces.j2", "r") as f:
        active_template = jinja2.Template(f.read())

    result = active_template.render(interfaces=arg1[task.host.name])
    
    print(f"{task.host.name}: Completed {datetime.datetime.now()}")
   
    return Result(host=task.host, result=result, changed=True)

def prepare_config2(task: Task, template_path: str, nb: pynetbox.api) -> Result:

    interface = nb.dcim.interfaces.filter(device=task.host.name)
    ip_address = nb.ipam.ip_addresses.filter(device=task.host.name)
    
    with open(f"{template_path}/{task.host.groups[0]}/interfaces2.j2", "r") as f:
        active_template = jinja2.Template(f.read())

    result = active_template.render(interfaces=interfaces, ips=ip_address)

    print(f"{task.host.name}: Completed {datetime.datetime.now()}")

    return Result(host=task.host, result=result, changed=True)


    return Result(host=task.host, result=result, changed=True)



# Body
if __name__ == "__main__":
    t1 = datetime.datetime.now()
    print(f"Start time {t1}")

    ifdict = csv_to_dict(path["input"])
    
    nr = InitNornir(config_file="config.yaml")
    
    fabric = nr.filter(role="network_device")
   
    nb = pynetbox.api(url=netbox_var["url"], token=netbox_var["token"])

    r1 = fabric.run(task=prepare_config2, template_path=path["templates"], nb=nb)
    
   # t2 = datetime.datetime.now()
   # print(f"Finished at {t2}, completed in {t2 - t1}")
   
   # print_result(r1)
   
    
  



