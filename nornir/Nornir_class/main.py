#/usr/bin/env python


# Module 
from nornir import InitNornir
from nornir.core.task import Task, Result
from helper.functions import csv_to_dict
from nornir_utils.plugins.functions import print_result
import jinja2
import datetime
import requests
# from pprint import pprint

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

def rest_request(task: Task) -> Result:
    t1 = datetime.datetime.now()
    response = requests.get("https://tcpipworld.com")
   # print(response.status_code)
    t2 = datetime.datetime.now()

    result = f"Request duration: {t2 - t1}"
    return Result(host=task.host, result=result)

# Body
if __name__ == "__main__":
    t1 = datetime.datetime.now()
    print(f" Started at {t1}")

    ifdict = csv_to_dict(path["input"])
    
    nr = InitNornir(config_file="config.yaml")

    r1 = nr.run(task=prepare_config, template_path=path["templates"], arg1=ifdict)
    r2 = nr.run(task=rest_request)
    t2 = datetime.datetime.now()
    print(f" Finished at {t2}, completed in {t2 - t1}")
    
   # print(r1["leaf11"].result)

   # print_result(r1)
    print_result(r2)
#    pprint(dict(r1))
