#/usr/bin/env python

# Module
from bindings.openconfig_interfaces import openconfig_interfaces
import pyangbind.lib.pybindJSON as pybindJSON # Alias Method
import re


# Class
class YANGBuilder(object):
    def __init__(self, vendor_type):
        self.__nos = vendor_type
        self.__dm = openconfig_interfaces()

    def fillin(self, extvars):
        for if_entry in extvars:
            iface = self.__dm.interfaces.interface.add(if_entry['name'])
            iface.config.name = if_entry['name']

            if if_entry['type'] == 'loopback':
                iface.config.type = 'softwareLoopback'
            elif if_entry['type'] == 'ethernet':
                iface.config.type = 'ethernetCsmacd'

            iface.config.enabled = if_entry['enabled']
           
            
            if self.__nos != 'eos' and if_entry['mtu']:
                iface.config.mtu = if_entry['mtu']
            
            if if_entry['vlan']:
                index = if_entry['vlan']
            else:
                index = 0
           #index = if_entry['vlan'] if if_entry['vlan'] else 0

            subif = iface.subinterfaces.subinterface.add(index)
            subif.config.index = index
            subif.config.description = if_entry['description']

            ip_add = subif.ipv4.addresses.address.add(if_entry['ip_address'].split('/')[0])
            ip_add.config.ip = if_entry['ip_address'].split('/')[0]
            ip_add.config.prefix_length = if_entry['ip_address'].split('/')[1]

            

    def getJSON(self):
        result = pybindJSON.dumps(self.__dm, mode='ietf')
        result = re.sub('"(\d+)"', '\g<1>', result)

        return result


