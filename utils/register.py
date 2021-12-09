import os
import re

def readFiles():
    listFiles = os.listdir("../storage")
    print(listFiles)
    listFiles = list(filter(lambda x: (x[-7:] == ".ledger" and x != "index.ledger"), listFiles))
    print(listFiles)
    return listFiles

"""def storeInformation(filename):
    file = open(filename, 'r')
    counter = 0
    for line in file.readline():
        # Indentify comments in file
        if (line[0] in [";", "#", "%", "|", "*"]):
            continue
        if re.match("\t", line):"""

readFiles()