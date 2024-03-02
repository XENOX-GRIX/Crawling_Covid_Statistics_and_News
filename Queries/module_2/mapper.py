#!/usr/bin/env python3
import sys
from datetime import datetime

file_name = None 
index = 0
try : 
    file_name = sys.argv[1]
    country_name = sys.srgv[2]
    country_name = country_name.strip().lower()
    f = open(sys.argv[1])
    for line in f:
        date , cases = line.strip().split("\t")
        cases = str(line[index]).replace(',','')
        print(f"{date} {country_name} {cases}")
except : 
    print("Error in Mapper ..")