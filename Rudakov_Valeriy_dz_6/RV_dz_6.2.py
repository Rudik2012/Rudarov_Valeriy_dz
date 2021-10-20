import collections

with open("nginx_logs.txt", "r", encoding="utf-8") as file_1:
    list_spamer = []
    dict_spamer = {}
    for line in file_1:
        line_log = ((line.split()[0], line.split()[5].replace('"', ""), line.split()[6]))
        list_spamer.append(line_log[0])
    for i in list_spamer:
        dict_spamer[i] = dict_spamer.get(i,0) + 1

    dict_spamer = collections.Counter(dict_spamer)
    spamer, req = dict_spamer.most_common(1)[0][0], dict_spamer.most_common(1)[0][1]
    print(f"Спамер = {spamer}, количество запросов = {req}")

    # a = {}
    # for i, b in dict_spamer:
    #     a.append()
    #     for v in range(len(a)):
    #         if list(dict_spamer.values())[v] < list(dict_spamer.values())[v-1]:
