#copying a all the city files into one common file with python

import os
import shutil

dest = "C:/Users/ASUS/Desktop/New folder/"
os.chdir(dest)
#print(os.listdir())
dest_files = os.listdir()
for filename in dest_files:
    shutil.copy(filename, "all_city_list.txt")







#ignore thie comented code..... trash code
'''
src_files = os.listdir()
dest = "C:/Users/ASUS/Desktop/New folder"
src = "all_city_list.txt"
for file_name in src_files:
    full_file_name = os.path.join(src, file_name)
    if os.path.isfile(full_file_name):
        shutil.copy(full_file_name, dest) 
'''
#os.chdir('C:\\Users\\ASUS\\Desktop')
#os.popen('copy 1.txt 2.txt')
'''
dest = "C:/Users/ASUS/Desktop/New folder/*.txt"
src = "all_city_list.txt"
for filename in glob.glob(os.path.join(dest, "*.txt")):
    shutil.copy(filename, dest)
'''
