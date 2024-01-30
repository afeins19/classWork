#reading files with python

fileName = '/Users/aaronfeinberg/PycharmProjects/Playground/text_files/compsci_course'

#best method to handle files
#send open() the a+ param to specifiy that you are appending
with open(fileName, 'a+') as fileObj:
    fileObj.write("i have appended this part ")
    lines=fileObj.readlines()
    print(len(lines))

