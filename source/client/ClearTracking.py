import subprocess


def clearEventlog():
    # cmd = ['runas', '/noprofile', '/user:ThanhNX','ipconfig']
    cmd = ['wevtutil', 'clear-log', 'Application']
    cmd2 = ['wevtutil', 'clear-log', 'Security']
    cmd3 = ['wevtutil', 'clear-log', 'Setup']
    cmd4 = ['wevtutil', 'clear-log', 'System']

    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                         shell=True)
    p = subprocess.Popen(cmd2, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                         shell=True)
    p = subprocess.Popen(cmd3, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                         shell=True)
    p = subprocess.Popen(cmd4, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                         shell=True)
    return "[+] Clear tracking successful!"


clearEventlog()
