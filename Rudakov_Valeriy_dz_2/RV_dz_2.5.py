#5a
prices = [57.08, 46.51, 97, 51, 1.76, 20, 25.08, 76, 23.34, 98.90, 70.01, 63, 39,
          91, 18.34, 13, 64.80, 78, 93, 88.08]
new_prices = []
print(id(new_prices))
for i in prices:
    if type(i) == float:
        i = str(i).split(".")
        new_prices.append(f"{i[0]} руб {i[1]} коп")
    else:
        i = str(float(i)).split(".")
        i[1] = "00"
        new_prices.append(f"{i[0]} руб {i[1]} коп")
for i in new_prices:
    print(i, end= ", ")
print(id(new_prices))
#5b
new_prices.sort()
for i in new_prices:
    print(i, end = ", ")
print(id(new_prices))
#5c
new_prices_2 = new_prices[:]
new_prices_2.sort(reverse=True)
for i in new_prices_2:
    print(i, end = ", ")
print(id(new_prices_2))

#5d
exp_goods = new_prices[0:5]
exp_goods.sort()
for i in exp_goods:
    if i == exp_goods[4] :
        print(i, end = ". ")
    else:
        print(i, end=",")




