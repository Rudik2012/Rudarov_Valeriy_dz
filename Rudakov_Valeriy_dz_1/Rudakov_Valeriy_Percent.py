for i in range(1, 101):
    if i == 1 or i % 10 == 1 and i != 11:
        print(i, "процент")
    elif 2 <= i % 10 <= 4 and not 12 <= i <= 14 :
        print(i, "процента")
    else:
        print(i, "процентов")