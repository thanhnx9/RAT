import urllib
import zipfile
import os.path
import sys
import base64


# def response(path):
#     response=urllib.urlopen("http://www.google.com")
#     return  response.read()
def download_file(path, file_name):
        return urllib.urlretrieve(path, file_name)


def unzip(path_to_zip_file, directory_to_extract_to):
    try:
        if os.path.exists(path_to_zip_file) is False | os.path.exists(directory_to_extract_to) is False:
            return "[-] Path file is not exist! Check Again!"
        else:
            with zipfile.ZipFile(path_to_zip_file, 'r') as zip_ref:
                zip_ref.extractall(directory_to_extract_to)
            return "[+] Unzip file successful"
    except:  # handle other exceptions such as attribute errors
        return "[-] Unexpected error:", sys.exc_info()[0]


def read_file(path):
    try:
        if os.path.exists(path) is False:
            return "[-] Path file is not exist! Check Again!"
        else:
            with open(path, "rb") as file_object:
                file_content = file_object.read()
                # return file_object.read()
            return "[+] READ from file " + path + ": " + file_content
    except:  # handle other exceptions such as attribute errors
        return "[-] Unexpected error:", sys.exc_info()[0]


def write_file(path, content):
    try:
        with open(path, "wb") as file:
            file.write(content)
        return "[+] WRITE " + content + " to file " + path + "SUCCESSFUL!!"
    except:  # handle other exceptions such as attribute errors
        return "[-] Unexpected error:", sys.exc_info()[0]
# print unzip("C:\Users\ThanhNX\Desktop\window 7\SysinternalsSuite.zip","C:\Users\ThanhNX\Desktop\demo")


