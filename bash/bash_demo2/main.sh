#!/usr/bin/env bash

# Variables
PATH_INVENTORY='./inventory.json'
PATH_TEMP='temp'
PATH_OUTPUT='result'

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

	echo "Collectiong information from ${1}"

	ssh ${USERNAME}@${2} "${COMMAND}" > ${4}/${1}.txt
}

function parser() {
        if [[ -d ${4} ]]; then 
                :
        else
                mkdir ${4}
        fi

	echo "---" > ${4}/${1}.yaml
	echo "interfaces:" >> ${4}/${1}.yaml
	echo "  interfaces:" >> ${4}/${1}.yaml
	
	while read LINE; do
		case ${2} in
			'cisco-iosxr')
				IF_NAME=$(echo "${LINE}" | awk '/(Loopback|ARPA)/ {print $1}')
				IF_TYPE=$(echo "${LINE}" | awk '/(Loopback|ARPA)/ {print $4}' | sed -e 's/ARPA/Ethernet/')
				IF_ADMN=$(echo "${LINE}" | awk '/(Loopback|ARPA)/ {print $2}' | sed -e 's/admin-down/down/')
				IF_OPER=$(echo "${LINE}" | awk '/(Loopback|ARPA)/ {print $3}' | sed -e 's/admin-down/down/')
			;;
			'arista-eos;')
                                IF_NAME=$(echo "${LINE}" | awk '/(^Et|^Ma)/ {print $1}')
                                IF_TYPE=Ethernet
                                IF_ADMN=$(echo "${LINE}" | awk '/(Loopback|ARPA)/ {print $2}' | sed -e 's/admin-down/down/')
                                IF_OPER=$(echo "${LINE}" | awk '/(Loopback|ARPA)/ {print $3}' | sed -e 's/admin-down/down/')
			;;
			'cumulus-linux')

		esac
		if [[ ${IF_NAME} ]]; then		
			echo "   - name: ${IF_NAME}" >> ${4}/${1}.yaml
        		echo "     state:" >> ${4}/${1}.yaml
        		echo "       name: ${IF_NAME}" >> ${4}/${1}.yaml
        		echo "       type: ${IF_TYPE}" >> ${4}/${1}.yaml
        		echo "       admin: ${IF_ADMN}" >> ${4}/${1}.yaml
        		echo "       state: ${IF_OPER}" >> ${4}/${1}.yaml
		else
			:
		fi

	done < ./${3}/${1}.txt
 	  
	echo "..." >> ${4}/${1}.yaml

}

# Body

DEVICE_NUMBER=$(cat "${PATH_INVENTORY}" | jq '."devices" | length')

for ((ID = 0; ID < ${DEVICE_NUMBER}; ID ++)); do
	HOST=$(cat "${PATH_INVENTORY}" | jq ".\"devices\"[${ID}].\"hostname\"" | sed -e 's/"//g')
	IP=$(cat "${PATH_INVENTORY}" | jq ".\"devices\"[${ID}].\"ip_address\"" | sed -e 's/"//g')
	NOS=$(cat "${PATH_INVENTORY}" | jq ".\"devices\"[${ID}].\"nos\"" | sed -e 's/"//g')
	
#	collector "${HOST}" "${IP}" "${NOS}" "${PATH_TEMP}"
	parser "${HOST}" "${NOS}" "${PATH_TEMP}" "${PATH_OUTPUT}"


done
