#/usr/bin/env python


# Module 
from nornir import InitNornir
from nornir.core.task import Task, Result
from helper.functions import csv_to_dict
from nornir_utils.plugins.functions import print_result
import jinja2
import datetime
import pynetbox




# Variable
path = {
            "input": "./input/interfaces.csv",
            "templates": "./Template"
        }

# Nornir Task

def prepare_config(task: Task, template_path: str, arg1: dict) -> Result:

    with open(f"{template_path}/{task.host.groups[0]}/interfaces.j2", "r") as f:
        active_template = jinja2.Template(f.read())

    result = active_template.render(interfaces=arg1[task.host.name])
    
    print(f"{task.host.name}: Completed {datetime.datetime.now()}")
   
    return Result(host=task.host, result=result, changed=True)


def netbox_poll(task) -> Result:
    nb = pynetbox.api(url=f"{task.host['connectivity']['protocol']}://{task.host['connectivity']['ip']}:{task.host['connectivity']['port']}", token=task.host.password)

    interfaces = nb.dcim.interfaces.all()
    
    for entry in interfaces:
        print(dict(entry))

    result = "AA"

    return Result(host=task.host, result=result)


# Body
if __name__ == "__main__":
    t1 = datetime.datetime.now()
    print(f"Start time {t1}")

    ifdict = csv_to_dict(path["input"])
    
    nr = InitNornir(config_file="config.yaml")
    
    fabric = nr.filter(role="network_device")
    netbox = nr.filter(role="netbox")
    
    netbox_results = netbox.run(task=netbox_poll)

   # r1 = fabric.run(task=prepare_config, template_path=path["templates"], arg1=ifdict)
    
   # t2 = datetime.datetime.now()
   # print(f"Finished at {t2}, completed in {t2 - t1}")
   
   # print_result(r1)
   
    
  



