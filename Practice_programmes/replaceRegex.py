#!/bin/python3

import sys
import os
import io
import re


# Complete the function below.
import re
def subst(pattern, replace_str, string):
    return re.sub(pattern, replace_str, string)


def main():
    addr = ['100 NORTH MAIN ROAD',
            '100 BROAD ROAD APT.',
            'SAROJINI DEVI ROAD',
            'BROAD AVENUE ROAD']
            
    #Create pattern Implementation here 
    #Use subst function to replace 'ROAD' to 'RD.',Store as new_address
    new_address=[]
    for line in addr:
        new_address.append(subst(r' ROAD',' RD.', line))
    return new_address

'''For testing the code, no input is required'''

print(main())
