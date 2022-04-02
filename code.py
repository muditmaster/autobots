import os
import shutil

path = input('enter the name of the folder you want to organize : ')

list_of_files = os.listdir(path)


for file in list_of_files:
    name , ext = os.path.splitext(file)
    ext = ext[1:]
    if ext == '' :
        continue
#png
    if os.path.exists(path+ '/' + ext ):
        shutil.move(path + '/' + file , path+'/'+ext+'/' + file)
    # folder - directory
    else:
        os.makedirs(path+ '/' + ext)
        shutil.move(path + '/' + file , path+'/'+ext+'/' + file)









