from os import  path, walk, listdir
import shutil

dir = "my_project"


try:
    for root, dirs, files in walk(dir):
        #print(root, dirs, files)
        if "templates" in dirs and root != dir:
            for i in listdir(path.join(root, "templates")):
                #print(i)
                shutil.copytree(path.join(root, "templates", i), path.join(dir, "templates", i))
except FileExistsError:
    print("Уже отработано")