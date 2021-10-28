import re

parcing = re.compile(r'^(\b.+\b).*\[(.+)].*\"([A-Z]+) +(/.+?)\s.*?\" (\d+) (\d+) .*$|^$')

with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    for i in f:
        print(re.findall(parcing, i))

