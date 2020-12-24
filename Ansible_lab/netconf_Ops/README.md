# Ansible with NETCONF
- NETCONF allows the user to send a configuration XML file to a netconf device


# Requirment for NETCONF
- ncclient
- Python >= 2.7


# Requriment for NETCONF/YANG Operation
- Pyang used to create JTOX driver
- NETCONF Module
- JSON2XML (Ability to convert data models with date into XML
- Valid XML Document
- Automated Operation


# Logic of NETCONF Automation with Ansible
- Create JTOX driver
- Generate XML out of JSON
- Format XML per Vendor Requirement
- Push Config over NETCONF
- Get Config over NETCONF
- Verify intend with result


# Ansible utilizes Python's module ncclient for its NETCONF operation. Therefore we need to install ncclient 

# Other module of NETCONF is netconf_get, netconf_rpc
- netconf_get : Fetch configuration/state data from NETCONF enabled network devices
	- Source (Running/Candidate)
	- filter Explicit information that we need to collect. 
	- display (Output that we need to collect) JSON 
- netconf_rpc : To lock and unlock the configuration, also commit operation. 


# How to provide the XML
- Directly the XML content to send the device. Note we need to remove the header of XML file. 
- SRC (Specify the source path to the XML file that contains the configuration or configuration template


# NETCONF MODULES 
- netconf_config (Module dedicated for NETCONF edit-config operation)
- replace (Module dedicated for to replace text in XML file)
	- regexp: Pattern to find
        - replace : Text to relace the pattern


# Version `0.1.0`
