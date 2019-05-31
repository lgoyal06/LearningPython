def factory(n=0):
    def counter():
        return n+1
    def current():
        return n
    return counter,current
f_current, f_counter = factory(int(input()))
print(f_current())
print(f_counter())
