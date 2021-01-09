#usr/bin/ven python

# Module
import json
import sys
import csv


# User-defined functions
def jsontodict(filename):
    '''
    This function use to convert JSON to Dictionary
    '''
    try:
        f = open(filename, 'r')
        result = json.loads(f.read())
        f.close()
        return result
    except:
        sys.exit('The inventory  cant be imported')

def csvtodict(filename):
    '''
    This function use to convert csv to dictionary
    '''
    try:
        result = []
        f = open(filename, newline='')
        csv_reader = csv.DictReader(f)
        
        for line in csv_reader:
            temp_count = {
                            "name": line['interfaces'],
                            "type": line['type'],
                            "enabled": line['enabled'],
                            "mtu": line['mtu'],
                            "vlan": line['vlan'],
                            "description": line['description'],
                            "ip_address": line['ip_address'],
                        }
            result.append(temp_count)

        f.close()

        return result

    except:
        sys.exit('Per device data cannot be imported')



