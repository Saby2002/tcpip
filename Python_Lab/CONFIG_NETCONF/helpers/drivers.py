#/usr/bin/env python

# Module
from ncclient import manager
import os
import re


# Class
class NetConfDriver(object):

    def __init__(self, ip, host, nos, user, passwd):
        self.__ip_address = ip
        self.__hostname = host
        self.__nos = nos
        self.__username = user
        self.__password = passwd

    def prepareMessage(self, json_text, temp_path):
        if not os.path.exists(temp_path):
            os.mkdir(temp_path)

        if not os.path.exists(f'{temp_path}/driver.jtox'):
            os.system(f'pyang -f jtox -o {temp_path}/driver.jtox -p files/public/release/models/ files/public/release/models/interfaces/openconfig-i*')

        with open(f'{temp_path}/{self.__hostname}.json', 'w') as f:
            f.write(json_text)

        os.system(f"json2xml -t config -o {temp_path}/{self.__hostname}.xml {temp_path}/driver.jtox {temp_path}/{self.__hostname}.json")

        with open(f'{temp_path}/{self.__hostname}.xml', 'r') as f:
            self.__xml = f.read()

        self.__modifyXML()
            

    def pushConfig(self):
        print(f'Configuring {self.__hostname}..')
        device_type = 'default' if self.__nos != 'iosxr' else self.__nos

        with manager.connect(host=self.__ip_address, username=self.__username,
                             password=self.__password, device_params={'name': device_type},
                             hostkey_verify=False) as netconf_session:

            netconf_session.lock()

            target_datastore = 'candidate' if self.__nos != 'eos' else 'running'

            response = netconf_session.edit_config(target=target_datastore, config=self.__xml)

            if self.__nos != 'eos':
                netconf_session.commit()

            else:
                netconf_session.copy_config(target='startup', source=target_datastore)

            netconf_session.unlock()

    def __modifyXML(self):
        self.__xml = re.sub('^<\?.+?\?>\n','', self.__xml)

        if self.__nos == 'sros':
            self.__xml = re.sub('>ianaift:','>', self.__xml)
            self.__xml = re.sub('<nc:.+">','<nc:config xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0" xmlns:oc-if="http://openconfig.net/yang/interfaces" xmlns:oc-ip="http://openconfig.net/yang/interfaces/ip" xmlns:oc-vlan="http://openconfig.net/yang/vlan" xmlns:oc-eth="http://openconfig.net/yang/interfaces/ethernet" xmlns:oc-inet="http://openconfig.net/yang/types/inet" xmlns:oc-ip-ext="http://openconfig.net/yang/interfaces/ip-ext" xmlns:oc-lag="http://openconfig.net/yang/interfaces/aggregate" xmlns:oc-types="http://openconfig.net/yang/openconfig-types" xmlns:oc-vlan-types="http://openconfig.net/yang/vlan-types" xmlns:oc-yang="http://openconfig.net/yang/types/yang">', self.__xml)

        elif self.__nos == 'iosxr':
            self.__xml = re.sub('type>ianaift','type xmlns:idx="urn:ietf:params:xml:ns:yang:iana-if-type">idx', self.__xml)
            self.__xml = re.sub('xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type"','', self.__xml)

        elif self.__nos == 'eos':
            self.__xml = re.sub('<oc-if:interface><oc-if:name>','<oc-if:interface><oc-if:name nc:operation="replace">', self.__xml)
            self.__xml = re.sub('<oc-ip:config><oc-ip:ip>','<oc-ip:config><addr-type xmlns="http://arista.com/yang/openconfig/interfaces/augments">PRIMARY</addr-type><oc-ip:ip>', self.__xml)        
