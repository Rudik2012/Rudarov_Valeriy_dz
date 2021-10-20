with open("users.csv", "r", encoding="utf-8") as file_1:
    with open("hobby.csv", "r", encoding="utf-8") as file_2:
        a = {}
        key = file_1.readline().replace(",", " ").replace("\n", "")
        value = file_2.readline().replace("\n", "")
        while key:
            if key:
                a.setdefault(key, value)
                key = file_1.readline().replace(",", " ").replace("\n", "")
                value = file_2.readline().replace("\n", "")
            if not value:
                value = None
            if not key and value:
                exit(1)
        print(a)

        with open("users_hobby.txt", "w", encoding="utf-8") as f:
            for i, b in a.items():
                print(f"{i}: {b}", file=f)