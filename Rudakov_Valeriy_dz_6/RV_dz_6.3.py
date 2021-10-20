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

#С подсказкой
# from itertools import zip_longest
# from json import dump
#
# with open("users.csv", "r", encoding="utf-8") as file_1:
#     with open("hobby.csv", "r", encoding="utf-8") as file_2:
#         if len(file_1.readlines()) >= len(file_2.readlines()):
#             file_1.seek(0)
#             file_2.seek(0)
#             with open("users_hobby.json","w", encoding="utf-8") as file:
#                 all_list = zip_longest(("".join(i.split(",")) for i in file_1), file_2, fillvalue=None)
#                 my_dict = {str(el[0]).strip(): str(el[1]).strip() for el in all_list}
#
#                 dump(my_dict, file, ensure_ascii=False, indent=4)
#             print(my_dict)
#         else:
#             exit(1)