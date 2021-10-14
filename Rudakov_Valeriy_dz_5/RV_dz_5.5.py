src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 2, 11]
#result = [23, 1, 3, 10, 4, 11]


# result = [i for i in src if src.count(i) == 1]
# print(result)

result = set()
tmp = set()
for i in src:
    if i not in tmp:
        result.add(i)
    else:
        result.discard(i)
    tmp.add(i)

result = [i for i in src if i in result]
print(result)

