#!/usr/bin/env bash

# Variables
PATH_INVENTORY='./inventory.json'
PATH_TEMP='temp'

# User-Defined Functions
function collector() {


	case ${3} in
		'cisco-iosxr')
			USERNAME=saby
			COMMAND="show interface brief"
		;;
		'arista-eos')
			USERNAME=admin
			COMMAND="show interface status"
		;;
		'cumulus-linux')
			USERNAME=cumulus
			COMMAND="net show interface"
		;;
		'sros')
			USERNAME=admin
			COMMAND="show port"
	esac

	if [[ -d ${4} ]]; then
		:
	else
		mkdir ${4}
	fi

	echo "Collecting info from ${1}"

	ssh ${USERNAME}@${2} "${COMMAND}" > ${4}/${1}.txt
}


# Body 
DEVICE_NUMBER=$(cat "${PATH_INVENTORY}" | jq '."devices" | length')

for ((ID = 0; ID < ${DEVICE_NUMBER}; ID ++)); do
	HOST=$(cat "${PATH_INVENTORY}" | jq ".\"devices\"[${ID}].\"hostname\"" | sed -e 's/"//g')
	IP=$(cat "${PATH_INVENTORY}" | jq ".\"devices\"[${ID}].\"ip_address\"" | sed -e 's/"//g')
	NOS=$(cat "${PATH_INVENTORY}" | jq ".\"devices\"[${ID}].\"nos\"" | sed -e 's/"//g')
	
	collector "${HOST}" "${IP}" "${NOS}" "${PATH_TEMP}"
done
