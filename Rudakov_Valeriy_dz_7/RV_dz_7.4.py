import os
from collections import defaultdict
import django

def script_inf():
    root_dir = django.__path__[0]
    #print(root_dir)
    django_files = defaultdict(int)
    #print(django_files)
    for root, dirs, files in os.walk(root_dir):
        for f in files:
            size = 10 ** len(str(os.stat(os.path.join(root, f)).st_size))
            django_files[size] += 1
    for size, nums in sorted(django_files.items()):
        print(f"{size}:{nums}")


script_inf()