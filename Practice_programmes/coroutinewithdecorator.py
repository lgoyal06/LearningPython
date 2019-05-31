def coroutine_decorator(coroutine_func):
    def inner(a,b):
        c=coroutine_func(a,b)
        next(c)
        return c
    return inner
# Define coroutine 'linear_equation' as specified in previous exercise
@coroutine_decorator
def linear_equation(a, b):
    while True:
        x=yield
        print('Expression, %s*x^2 + %s, with x being %s equals %s' % (a,b,x,(a*(x**2)+b)))
