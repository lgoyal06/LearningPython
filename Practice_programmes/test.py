def stringDisplay():
    while True:
        s = yield
        print(s*3)


c = stringDisplay()
c.send('Hi!!')
