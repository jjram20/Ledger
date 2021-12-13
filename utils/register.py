import os
import re
from datetime import datetime

data = []

def getFiles():
    listFiles = os.listdir("../storage")
    listFiles = list(filter(lambda x: (x[-7:] == ".ledger" and x != "index.ledger"), listFiles))
    print(listFiles)
    return listFiles

def storeInformation(filename):
    file = open(filename, 'r')
    record = []
    for line in file.readline():
        line = re.sub(r"\n", "", line)
        # Indentify comments in file
        if (line[0] in [";", "#", "%", "|", "*"]):
            continue
        elif not re.match("\t", line):
            line = re.sub(r"\t", "", line)
            data.append(record)
            print(line)
            newLine = line.split(' ')
            print(newLine)
            record = [newLine[0], ' '.join(newLine[1:])]
        else:
            record += line.split("\t")
    print(data)

def datetimeFormat(date, attribute):
    dateFormat = datetime.strptime(date, '%Y/%m/%d')
    print(dateFormat)
    return dateFormat

def sortObjects(objects):
    objects.sort(key = lambda x: x.attribute)


storeInformation('../storage/Bitcoin.ledger')
