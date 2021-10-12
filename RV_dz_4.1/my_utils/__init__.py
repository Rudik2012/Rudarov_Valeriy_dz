from requests import get, utils
from datetime import datetime

val_curs = get("http://www.cbr.ru/scripts/XML_daily.asp")
encodings = utils.get_encoding_from_headers(val_curs.headers)
content = val_curs.content.decode(encoding=encodings)


def currency_rates(valute):
    my_list = content.split("<Valute")
    for str_valute in my_list:
        if "Date=" in str_valute:
            date = []
            for i in str_valute[(str_valute.find("Date=")) + 5: (str_valute.find("Date=")) + 20]:
                if i.isdigit() or i == ".":
                    date.append(i)
            d, m, y = "".join(date).split(".")
            print(datetime(year=int(y), month=int(m), day=int(d)))
        if valute in str_valute:
            price = []
            for i in str_valute[(str_valute.find(",")) - 7:]:
                if i.isdigit() or i == ",":
                    price.append(i)
            price = float("".join(price).replace(",", "."))
            return f"{valute} = {price}"




if __name__ == "__main__":
    print(currency_rates("USD"))
    print(currency_rates("EUR"))
    print(currency_rates("Er"))