names = ["Иван", "Мария", "Петр", "Илья"]



def thesaurus(my_list):
    names_peaple = {}
    for i in my_list:
        first = i[0]
        if first in names_peaple:
            names_peaple[first] += [i]
        else:
            names_peaple[first] = [i]
    return names_peaple

print(thesaurus(names))
