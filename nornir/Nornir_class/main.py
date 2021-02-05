#/usr/bin/env python


# Module 
from nornir import InitNornir
from nornir.core.task import Task, Result
from helper.functions import csv_to_dict
import jinja2

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

    return Result(host=task.host, result=result)

# Body
if __name__ == "__main__":
    ifdict = csv_to_dict(path["input"])
    
    nr = InitNornir(config_file="config.yaml")

    r1 = nr.run(task=prepare_config, template_path=path["templates"], arg1=ifdict)

    print(r1["leaf11"].result)
