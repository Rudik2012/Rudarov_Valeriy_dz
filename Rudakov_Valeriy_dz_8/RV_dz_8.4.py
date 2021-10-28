from functools import wraps

def val_checker(a):
    def _val_checker(b):

        @wraps(b)
        def wrapper(num):
            if a(num):
                print(b(num))
            else:
                raise ValueError(f'Не верное значение {num}')

        return wrapper

    return _val_checker

@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3

try:
    a = calc_cube(5)
    print(help(calc_cube))
except (ValueError, TypeError) as err:
    print(err)