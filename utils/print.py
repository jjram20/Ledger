import os
import re

locationStorage = 'storage'

def get_files():
    listFiles = os.listdir(locationStorage)
    listFiles = list(filter(lambda x: (x[-7:] == ".ledger" and x != "index.ledger"), listFiles))
    return listFiles

def print_files(files):
    for element in files:
        print_file(element)

def print_file(filename):
    file = open(filename, 'r')
    counter = 0
    for line in file.readlines():
        # Indentify comments in file
        if (line[0] in [";", "#", "%", "|", "*"]):
            continue
        else:
            print(line, end='')
    file.close()

#printFiles2(getFiles())
#printFiles(getFiles())
