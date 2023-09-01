import os
print("""
###########################################
###############FOLDER SORTER###############
###############  BY XANOOR1 ###############
###########################################
""")

print('Folder path:')
path = input()


# EXTENSIONS THAT WILL BE SORTED
extensions = {"exe": "Executables", 
             "png": "Images", 
             "jpg": "Images", 
             "jpeg": "Images", 
             "zip": "Archives", 
             "rar": "Archives", 
             "mkv": "Videos", 
             "mp4": "Videos",
             "gif": "Videos",
             "pdf": "PDFs",
             "json": "Data",
             "csv": "Data",
             "xlsx": "Data",
             "doc": "Documents",
             "docx": "Documents",
             "txt": "Documents",
             "jar": "Programming",
             "py": "Programming"
             }


try:
    files = os.listdir(path)
    for i in files:
        list = i.split('.')
        ext = (list[len(list)-1]).lower()

        if (i.__contains__('.') & extensions.__contains__(ext)):
            if (os.path.exists(f"{path}/{extensions[ext]}") == False):
                os.makedirs(f"{path}/{extensions[ext]}")

            os.replace(f'{path}/'+i, f'{path}/{extensions[ext]}/'+i)
    print('Folder sorted !')
except:
    print("Incorrect path !")


