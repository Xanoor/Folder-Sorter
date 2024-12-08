import os
import json

print("""
  _____     _     _           ____             _            
 |  ___|__ | | __| | ___ _ __/ ___|  ___  _ __| |_ ___ _ __ 
 | |_ / _ \| |/ _` |/ _ \ '__\___ \ / _ \| '__| __/ _ \ '__|
 |  _| (_) | | (_| |  __/ |   ___) | (_) | |  | ||  __/ |   
 |_|  \___/|_|\__,_|\___|_|  |____/ \___/|_|   \__\___|_|   
                                                   by Xanoor
""")

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

f = open('extensions.json')
extensions = json.load(f)  # IMPORT EXTENSIONS


def updateExtensions(msg: str) -> None:
    """
    Update the extensions.json file with the current content of the extensions variable.
    Params:
        msg : str (message to display if successful)
    """
    try:
        with open("extensions.json", "w+") as f:
            json_object = json.dumps(extensions, indent=4)
            f.write(json_object)
            print(f"{bcolors.OKGREEN}{msg}{bcolors.ENDC}")
    except:
        print(f"{bcolors.FAIL}Cannot update the extensions.json file!{bcolors.ENDC}")

def FolderSorter():
    path = input("""Help
-ae : Add extension to extensions.json
-re : Remove extension from extensions.json
-le : List all saved extensions from extensions.json
Path : path to sort

Command:
""")

    match path:
        case "-ae":
            extension = input("Enter the name of the extension: ")
            if extension != "":
                if extension.startswith('.'):
                    extension = extension.removeprefix('.')
                if extension in extensions:
                    print(f"{bcolors.FAIL}This extension already exists in extensions.json. Use -re to remove it first!{bcolors.ENDC}")
                else:
                    folderName = input(f"In which folder do you want to place the .{extension} files? ")
                    if folderName != "":
                        extensions[extension] = folderName
                        updateExtensions(f".{extension} will now be placed in {folderName}!")
        case "-re":
            extension = input("Enter the name of the extension you want to remove: ")
            if extension in extensions:
                del extensions[extension]
                updateExtensions(f".{extension} extension successfully removed!")
        case "-le":
            print(extensions)
        case _:
            try:
                files = os.listdir(path)
                for i in files:
                    list = i.split('.')
                    ext = (list[len(list)-1]).lower()
                    print(ext, "ext")

                    if i.__contains__('.') and ext in extensions:
                        if not os.path.exists(f"{path}/{extensions[ext]}"):
                            os.makedirs(f"{path}/{extensions[ext]}")

                        os.replace(f'{path}/'+i, f'{path}/{extensions[ext]}/'+i)
                print('Folder sorted!')
            except:
                print(f"{bcolors.FAIL}Invalid path!{bcolors.ENDC}")

FolderSorter()
