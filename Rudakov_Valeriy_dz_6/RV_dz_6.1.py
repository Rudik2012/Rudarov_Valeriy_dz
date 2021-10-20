with open("nginx_logs.txt", "r", encoding="utf-8") as file_1:
    for line in file_1:
        line_log = ((line.split()[0], line.split()[5].replace('"', ""), line.split()[6]))
        print(line_log)
    #     # a = line.split()[0]
    #     # b = line.split()[5].replace('"', "")
    #     # c = line.split()[6]
    #     # line_log = (a, b, c)

#с помощью подсказки
# with open(r"C:\Users\User\PycharmProjects\pythonProject1\Rudakov_Valeriy_dz_6\nginx_logs.txt", "r", encoding="utf-8") as file_1:
#     line_log = ((line.split()[0], line.split()[5].replace('"', ""), line.split()[6]) for line in file_1)
#     for i in line_log:
#         print(i)