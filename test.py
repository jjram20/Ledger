import os
import re

file = open('Bitcoin.ledger', 'r')
for line in file.readlines():
    if re.match(r"\t", line):
        print(line.split('\t'), end='\n')