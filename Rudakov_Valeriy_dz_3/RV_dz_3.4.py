names_surnames = ["Иван Петров", "Петр Сергеев", "Мария Смирнова", "Илья Анисимов"]

def thesaurus_adv(my_list):
    peaple = {}
    for i in my_list:
        name, surname = i.split()
        a = peaple.setdefault(surname[0], {name[0]: [i]})
        b = a.setdefault(name[0], [i])
        if i not in b:
            b.append(i)
    return peaple


print(thesaurus_adv(names_surnames))