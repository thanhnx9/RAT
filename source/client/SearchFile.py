import os
import string

def searchFile(command):
    path, ext = command.split('*')
    list = ''  # here we define a string where we will append our result on it
    for dirpath, dirname, files in os.walk(path):
        for file in files:
            if file.endswith(ext):
                list = list + '\n' + os.path.join(dirpath, file)
    return list
#print searchFile("C:\\*.jpg")