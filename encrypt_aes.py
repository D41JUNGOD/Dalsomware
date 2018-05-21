from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import hashlib

key = b"0123456789abcdef"
key = hashlib.sha256(key).digest()
IV = b"asdfasdfasdfasdf"
encryptor = AES.new(key,AES.MODE_CBC,IV)
ciphertext = encryptor.encrypt(b"asdfasdfasdfasdf")

print(ciphertext)

decryptor = AES.new(key,AES.MODE_CBC,IV)
print(decryptor.decrypt(ciphertext))