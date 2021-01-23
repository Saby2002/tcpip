#!/usr/bin/env bash

# Variables
BRIDGE=(br0 br11 br12 br13 br14 br15 br16)
CONTAINERS=(nnat_ftp netbox-docker_nginx_1 netbox-docker_netbox_1 netbox-docker_netbox-worker_1 netbox-docker_postgres_1 netbox-docker_redis-cache_1 netbox-docker_redis_1)
VMS=(VX1 XRVM)


# Body
echo "$(date): Dealing with network bridges"

ACTUAL_BRIDGES=$(nmcli connection show | awk '{print $1}')

for BRI in ${BRIDGE[@]}; do 
    if [[ ${ACTUAL_BRIDGES} =~ ${BRI} ]]; then
	    echo "${BRI} exits"
    else
	    echo "${BRI} need to created"

	    nmcli connection add type bridge con-name ${BRI} ifname ${BRI}
	    nmcli connection modify ${BRI} stp no
	    nmcli connection modify ${BRI} ipv4.method disable
	    nmcli connection modify ${BRI} ipv6.method disable
	    nmcli connection up ${BRI} 
    fi
done

echo "$(date): Dealing with Docker Service"

ACTUAL_DOCKER_STATUS=$(sudo systemctl status docker.service | awk '/Active/ {print $2}')

if [[ ${ACTUAL_DOCKER_STATUS} == inactive ]]; then
	echo "Docker service is not operational"
	sudo systemctl start docker.service
else
	echo "Docker service is operational"
fi

echo "$(date): Dealing with Docker Container"

ALL_CONTAINERS=$(sudo docker container ls --all)

for CRE in ${ALL_CONTAINERS[@]}; do 
	CL=$(echo "${ALL_CONTAINERS}" | grep "${CRE}")        	
	if [[ ${CL} =~ Up ]]; then 
		echo "######## The Container ${CRE} is up and running #############"
	elif [[ ${CRE} == netbox-* && ${CL} == Exited ]]; then
		echo "########### The Netbox need to start ###############"
	        cd ~/tcpip/Container/netbox-docker/
		docker-compose up -d
		cd
	else [[ ${CRE} != netbox-* ]]; 
		echo "########### The Container ${CRE} shall be started###########"
		sudo docker container start ${CRE}
	fi
done


echo "$(date): Dealing with Virtual Machines"

ALL_VMS=$(sudo virsh list --all)

for VME in ${VMS[@]}; do
	if [[ ${ALL_VMS} =~ ${VME} ]]; then
		VML=$(echo "${ALL_VMS}" | grep "${VME}")
		if [[ ${VML} =~ running ]]; then
			echo "VM ${VME} is up and running"
		else
			echo "VM ${VME} shall be Launched"
			sudo virsh start ${VME}
		fi
	else 
		echo "VM ${VME} shall be created"
		./VMS/${VME}.sh ${VME}
	fi
done


