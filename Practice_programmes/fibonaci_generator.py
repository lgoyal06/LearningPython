def fib_gen(a,b) :
    while True:
        c=a+b
        yield c
        if c == 0:
            a=0
            b=1
        elif c == 1:
            yield 1
            a=1
            b=1
        else:
            a=b
            b=c

fs = fib_gen(0,0)
print(fs.next())
print(fs.next())
print(fs.next())
print(fs.next())
