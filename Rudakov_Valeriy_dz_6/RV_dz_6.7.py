from sys import argv

with open("bakery.csv", "r+", encoding="utf-8") as f:
    a, val = argv[1:]
    val = round(float(val.replace(",", ".")), 3)
    for line in range(int(a)):
        p = f.tell()
        n = f.readline().strip()
        if n == "":
            exit("Error")

    if "," in str(val) or "." in str(val):
        if val <= 99999.999:
            f.seek(p)
            f.write(f"{val:>010}")
        else:
            print("Число должно быть меньше 99999,999")
