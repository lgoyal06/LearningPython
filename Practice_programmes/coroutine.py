def stringDisplay():
    while True:
        s = yield
        print(s*3)


c = stringDisplay()
next(c)
c.send('Hi!!')
