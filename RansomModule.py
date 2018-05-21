import os,struct
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def encrypt_file(key, in_filename, chunksize=65536):
    out_filename = in_filename+".dal"
    iv = get_random_bytes(16)
    mode = AES.MODE_CBC
    encryptor = AES.new(key,mode,iv)
    filesize = os.path.getsize(in_filename)

    with open(in_filename,'rb') as infile:
        with open(out_filename, 'wb') as outfile:
            outfile.write(struct.pack('<Q', filesize))
            outfile.write(iv)

            while True:
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 != 0:
                    chunk += b' '*(16-len(chunk) % 16)

                outfile.write(encryptor.encrypt(chunk))

    os.unlink(in_filename)

def decrypt_file(key, in_filename, chunksize=24*1024):
    out_filename = os.path.splitext(in_filename)[0]
    with open(in_filename, 'rb') as infile:
        origsize = struct.unpack('<Q',infile.read(struct.calcsize('Q')))
        iv = infile.read(16)
        mode = AES.MODE_CBC
        decryptor = AES.new(key,mode,iv)

        with open(out_filename,'wb') as outfile:
            while True:
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break
                outfile.write(decryptor.decrypt(chunk))
            outfile.truncate(origsize[0])

    print(out_filename)
    os.unlink(in_filename)
