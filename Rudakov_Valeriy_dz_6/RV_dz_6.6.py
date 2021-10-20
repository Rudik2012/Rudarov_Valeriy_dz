# С подсказкой

from sys import argv

with open("bakery.csv","r", encoding="utf-8") as f:
    if 1 < len(argv) < 4 and [i for i in argv[1:] if i.isdigit()]:
        if len(argv) == 3:
            start, finish = map(int, argv[1:])
            print(*(v for i, v in enumerate(f) if start - 1 <= i < finish), sep="")
        else:
            print(*(v for i, v in enumerate(f) if i >= int(argv[1]) - 1), sep="")
    else:
        print(f.read())



from sys import argv

with open("bakery.csv","a", encoding="utf-8") as f_a:
    with open("bakery.csv", "r", encoding="utf-8") as f_b:
        if len(argv) > 1 and [i for i in argv[1:] if "." in i and i.replace(".", "").isdigit()]:
            if round(float(argv[1]), 3)<= 99999.999:
                print(f"{round(float(argv[1]), 3):>010}", file=f_a)
            else:
                print("Число должно быть меньше 99999,999")
        else:
            print(f_b.read())