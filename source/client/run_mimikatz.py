import subprocess
import sys
import os


def demo():
    path = "C:\Users\ThanhNX\Desktop\Thanh-win\mimikatz.exe"
    return subprocess.Popen(path, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE,
                            shell=True)

