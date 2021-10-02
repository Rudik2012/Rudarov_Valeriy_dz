# Практическое задание 1

duration = int(input("Введите продолжительность времени в секундах: "))
sec = duration % 60
min = duration // 60 % 60
hour = duration // 3600 % 24
day = duration // 86400

# 1a
if min == 0:
    print( sec, "сек")
# 1b
elif hour == 0:
   # min = min % 60
    print(min, "мин", sec, "сек.")
#1c
elif day == 0:
    #hour = hour % 24
   # min = min % 60
    print(hour, "час", min, "мин", sec, "сек.")
#1d
elif day > 0:
    print(day, "дн", hour, "час", min, "мин", sec, "сек.")






