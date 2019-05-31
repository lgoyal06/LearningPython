def bind(func):
    func.data = 9
    return func

@bind
def add(x, y):
    return x + y

print(add(3, 10))
print(add.data)
