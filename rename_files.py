import os

def rename_files():
    #1. get file names from a folder
    file_list = os.listdir(r"/Users/dennis/projects/python/prank")
    saved_path = os.getcwd()
    print(file_list)
    os.chdir(r"/Users/dennis/projects/python/prank")
    #2. for each file, rename file
    for file_name in file_list:
        print("Old name - "+file_name)
        print("New name - "+file_name.translate(none, "0123456789"))
        os.rename(file_name, file_name.translate(none, "0123456789"))
    os.chdir(saved_path)
    
rename_files()
