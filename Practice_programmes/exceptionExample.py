try:
    a = 2; b = 'hello'
    if not (isinstance(a, int)
            and isinstance(b, int)):
        raise TypeError('Two inputs must be integers.')
    c = a**b
except TypeError as e:
    print(e)
finally:
    print("God is great.")
