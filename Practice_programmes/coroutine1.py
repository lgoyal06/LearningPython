def linear_equation(a, b):
    while True:
        x=yield
        print('Expression, %s*x^2 + %s, with x being %s equals %s' % (a,b,x,(a*(x**2)+b)))

equation1 = linear_equation(3,4)    
next(equation1)    
equation1.send(6)
    
    
