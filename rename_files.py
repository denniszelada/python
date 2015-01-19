import os

def rename_files():
    #1. get file names from a folder
    file_list = os.listdir(r"/Users/dennis/projects/python/prank")
    print(file_list)
    #2. for each file, rename file
    for file_name in file_list:
        os.rename(file_name, file_name.translate(none, "0123456789"))
rename_files()
