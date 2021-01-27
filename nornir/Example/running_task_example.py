

from nornir.plugins.tasks.networking import napalm_get 

# we filter the hosts (optional, this would be the equivalent of "role")
spine_bma = nr.filter(role="spine", site="bma")

# we run the task, saving the result in the variables 'r'

r = spine_bma.run(name="Get facts",
                        task=napalm_get,
                        getters=["facts"])



