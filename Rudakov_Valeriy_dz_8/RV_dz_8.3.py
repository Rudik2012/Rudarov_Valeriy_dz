from  functools import wraps

def type_logger(a):
    @wraps(a)
    def wrapper(*args, **kwargs):
        num_list = [el for el in (*args, *kwargs.values())]
        n = [f'{a.__name__}({el}: {type(el)})' for el in num_list]
        print(*n, a(*args, ** kwargs), sep=",\n")

    return wrapper

@type_logger
def calc_cube(*x,**y):
    num_list = [el for el in (*x, *y.values()) if isinstance(el, int) or isinstance(el, float)]
    return [i ** 3 for i in num_list]
a = calc_cube(5)