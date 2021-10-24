import yaml
import os

with open("config.yaml", "r") as f:
    cont = yaml.safe_load(f)
    #print(cont)

def skript(val, prefix=""):
    for d, p in val.items():
        dir_path = os.path.join(prefix, d)
        os.makedirs(dir_path, exist_ok=True)
        if isinstance(p, dict):
            skript(p, dir_path)
        else:
            for i in p:
                if isinstance(i, dict):
                    skript(i, dir_path)
                elif isinstance(i, str):
                    with open(os.path.join(dir_path, f"{i}"), "w") as d:
                        pass
skript(cont)
