import os

def search(default_path,ext_list):
    file_list = []
    dir_list = []
    for (path,dir,files) in os.walk(default_path):
        dir_list.append(path)
        for filename in files:
            ext = os.path.splitext(filename)[-1]
            if ext in ext_list:
                file_list.append(path+"\\"+filename)

    return file_list,dir_list

'''
default_path = "C:\\Users\\oonja\\Desktop\\Ransomware"
ext_list = [".hwp"]
file, directory = search(default_path,ext_list)
for i in file:
    print(i)
'''
