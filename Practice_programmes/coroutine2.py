# Define the function 'coroutine_decorator' below
def coroutine_decorator(coroutine_func):
    def inner(*args, **kwdargs):
        c = coroutine_func(*args, **kwdargs)
        next(c)
        return c
    return inner
    
# Define the coroutine function 'linear_equation' below
@coroutine_decorator
def linear_equation(a, b):
    while True:
        x=yield
        print('Expression, %s*x^2 + %s, with x being %s equals %s' % (a,b,x,(a*(x**2)+b)))


    
# Define the coroutine function 'numberParser' below
@coroutine_decorator
def numberParser():
    equation1 = linear_equation(3, 4)
    equation2 = linear_equation(2, -1)
    # code to send the input number to both the linear equations
    while True:
        x = yield
        equation1.send(x)
        equation2.send(x)
    
def main(x):
    n = numberParser()
    n.send(x)

main(4.5)
