#!/usr/bin/venv python

# Module
from csv import DictReader

# User-defined functions

def csv_to_dict(filename: str):
    '''
    Converting the CSV table into a dictionary with list organised per the hostnames.
    '''

    result = {}
    with open(filename, "r") as f:
        reader = DictReader(f)
        for row in reader:
            tc = {}
            th = None

            for a, b in row.items():
                if a == "hostname":
                    th = b

                    if th not in result:
                        result.update({th: []})

                else:
                    b = None if not b else b
                    tc.update({a: b})

            result[th].append(tc)


    return result
