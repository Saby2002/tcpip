# running a task will return a dict-like object
# where the keys are the hosts names and the values
# a list of results (more on why a list later)

for host, task_results in r.items():
    print(f"{host}: {task_results}")


for host, task_results in r.items():
    my_task = task_results[0]  # The only task we ran
    my_task_result = my_task.result # this should contain the exact output from napalm's 'get_facts'
    print((f"{host}: {my_task_result['facts']['os_version']}")


