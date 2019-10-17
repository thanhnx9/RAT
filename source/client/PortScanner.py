import subprocess


# network = raw_input("Input network subnet: ")
def scanner(host, port):
    try:
        cmd = [r"C:\Program Files (x86)\Nmap\nmap.exe", host, "-p", port]
        p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return p.stdout.read() + p.stderr.read()
    except Exception:
        return "[-] Error when scan network! Try again..."
