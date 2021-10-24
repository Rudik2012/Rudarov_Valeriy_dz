import os

dir_list = {"my_project": ["setting", "mainapp", "adminapp", "authapp"]}

for k, v in dir_list.items():
    if not os.path.exists(k):
        for i in v:
            os.makedirs(os.path.join(k, i))
