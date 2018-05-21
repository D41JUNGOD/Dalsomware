import os,random,struct,hashlib,binascii
from Crypto.Cipher import AES

def encrypt_file(key, in_filename, out_filename=None, chunksize=64*1024):
    if not out_filename:
        out_filename = in_filename+".enc"

    iv = bytes(''.join(chr(random.randint(0,0xFF)) for i in range(16)),encoding="utf-8")
    mode = AES.MODE_CBC
    encryptor = AES.new(key,mode,iv)
    filesize = os.path.getsize(in_filename)

    with open(in_filename,'rb') as infile:
        with open(in_filename, 'wb') as outfile:
            outfile.write(struct.pack('<Q', filesize))
            outfile.write(iv)

            while True:
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 != 0:
                    chunk += ' '*(16-len(chunk) % 16)

                outfile.write(encryptor.encrypt(chunk))

def decrypt_file(key, in_filename, out_filename=None, chunksize=24*1024):
    if not out_filename:
        out_filename = os.path.splitext(in_filename)[0]

    with open(in_filename, 'rb') as infile:
        origsize = struct.unpack('<Q',infile.read(struct.calcsize('Q')))
        iv = bytes(infile.read(16),encoding='utf-8')
        mode = AES.MODE_CBC
        decryptor = AES.new(key,mode,iv)

        with open(out_filename,'wb') as outfile:
            while True:
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break
                outfile.write(decryptor.decrypt(chunk))

            outfile.truncate(origsize)

password = b"This_is_password"
key = hashlib.sha256(password).digest()
print(binascii.hexlify(bytearray(key)))
in_filename = 'secret.hwp'
encrypt_file(key,in_filename, out_filename='output')
print("Encrypted!")

os.unlink(in_filename)

decrypt_file(key,in_filename="output",out_filename="original.hwp")
outfile = open('original.hwp')
