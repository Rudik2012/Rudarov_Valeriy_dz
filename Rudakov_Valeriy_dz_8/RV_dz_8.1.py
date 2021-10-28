import re


def email_parse(email_adress):
    RE_EMAIL = re.compile(r'(?P<username>([\w]+))@(?P<domain>[^&]+\.\w+)', re.IGNORECASE)
    if not RE_EMAIL.match(email_adress):
        raise ValueError(f'не верный адресс: {email_adress}')
    print(RE_EMAIL.match(email_adress).groupdict())


email_parse('someonegeekbrains.ru')
