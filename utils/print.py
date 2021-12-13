import os
import re

locationStorage = 'storage'

def getFiles():
    listFiles = os.listdir(locationStorage)
    listFiles = list(filter(lambda x: (x[-7:] == ".ledger" and x != "index.ledger"), listFiles))
    return listFiles

def printFiles(files):
    for element in files:
        file = open(locationStorage + '/' + element, 'r')
        counter = 0
        for line in file.readlines():
        # Indentify comments in file
            if (line[0] in [";", "#", "%", "|", "*"]):
                continue
            else:
                print(line, end = '')
        file.close()

#Testing function
def printFiles2(files):
    for element in files:
        file = open(locationStorage + '/' + element, 'r')
        for line in file.readlines():
            line = re.sub(r"\t", "", line)
            line = re.sub(r"\n", "", line)
            print(line, end = '')
            print(line.split(' '))
        file.close()

#printFiles2(getFiles())
#printFiles(getFiles())
