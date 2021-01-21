#!/usr/bin/bash

# Variables

DEVICES = ('EOS1', 'XRVM', 'SROS', 'VX1', 'XR1')

# User-Defined functions

function test_function() {
	echo "Print some variables for ${1}"
}

function read_device_ifaces() {
	NAME=$(echo "${1}" | sed -e 's/\,//g')
	cat ${NAME}_interfaces.json
}

# Body

for device in ${DEVICES[@]}; do
	DEVIICE_VARS=$(read_device_ifaces ${device})
	IFACES=$(echo "${DEVICE_VARS}" | jq '."openconfig-interfaces:interfaces"."interface"')
	IFACES=$(echo "${IFACES}" | jq '.[] | ."name" as $name | ."config"."enabled" as $enabled | {name: $name, enabled:$enabled}' sed -e 's/"//gi')


