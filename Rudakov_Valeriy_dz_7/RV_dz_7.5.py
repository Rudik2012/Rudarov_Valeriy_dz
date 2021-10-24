import os
import json
import django

def script_inf():
    root_dir = django.__path__[0]
    django_files = {}
    for root, dirs, files in os.walk(root_dir):
        for f in files:
            size = 10 ** len(str(os.stat(os.path.join(root, f)).st_size))
            a = f.rsplit(".", maxsplit=1)[-1].lower()
            if size in django_files:
                django_files[size][0] += 1
                if a not in django_files[size][1]:
                    django_files[size][1].append(a)
                else:
                    django_files[size] = [1, [a]]
    result = {}
    for size, nums in sorted(django_files.items()):
        result[size] = tuple(nums)
        print(f"{size}:{tuple(nums)}")

    folder = os.path.basename(os.getcwd()) + "_summary.json"
    with open(folder, "w", encoding="utf-8") as file:
        json.dump(result, file, ensure_ascii=False, indent=4)


if __name__ == "__mane__":
    script_inf()


