from itertools import zip_longest


tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А'
]

gen_t_k = (n for n in zip_longest(tutors, klasses))
print(*gen_t_k, type(gen_t_k), sep="\n")
