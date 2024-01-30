import re

file = '/Users/aaronfeinberg/Desktop/related.bib'

with open(file) as fobj:
    fileList = str(fobj.readlines())

print(fileList)
idList = re.findall('^@,$', fileList)
print(idList)
