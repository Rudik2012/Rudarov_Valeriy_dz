#2a
my_list = []
for i in range(1,1001):
    if i % 2 != 0 :
        i = i ** 3
        my_list.append(i)
all_sum = 0
for idx in my_list:
    m = idx
    sum_num = 0
    while m > 0:
        a = m % 10
        m = m // 10
        sum_num = sum_num + a
    if sum_num % 7 == 0:
        all_sum = all_sum + idx
print(all_sum)

#2b
my_list = []
for i in range(1,1001):
    if i % 2 != 0 :
        i = i ** 3
        my_list.append(i + 17)
all_sum = 0
for idx in my_list:
    m = idx
    sum_num = 0
    while m > 0:
        a = m % 10
        m = m // 10
        sum_num = sum_num + a
    if sum_num % 7 == 0:
        all_sum = all_sum + idx
print(all_sum)

# #2c
my_list = []
for i in range(1,1001):
    if i % 2 != 0 :
        i = i ** 3
        my_list.append(i)
all_sum = 0

for idx in my_list:
    idx = idx + 17
    m = idx
    sum_num = 0
    while m > 0:
        a = m % 10
        m = m // 10
        sum_num = sum_num + a
    if sum_num % 7 == 0:
        all_sum = all_sum + idx
print(all_sum)