#2.2
my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
print(id(my_list))
new_list = []

for i in my_list:
    if i.isdigit() == False:
        for n in i:
            if n.isdigit() == True:
                new_list.append('"')
                i = i[0] + "0" + i[1:]
                new_list.append(i)
                new_list.append('"')
        new_list.append(i)
    elif i.isdigit() == True:
        if int(i) / 10 < 1:
            new_list.append('"')
            new_list.append("0" + i)
            new_list.append('"')
        elif int(i) / 10 > 1:
            new_list.append('"')
            new_list.append(i)
            new_list.append('"')
new_list.pop(-2)
new_list = " ".join(new_list)
new_list = new_list.replace('" 05 "', '"05"')
new_list = new_list.replace('" 17 "', '"17"')
new_list = new_list.replace('" +05 "', '"+05"')

print(new_list)

print(id(new_list))