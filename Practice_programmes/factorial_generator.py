def factorial_gen() :
    count=0   
    while True:
        fact =1
        if count == 0:
            yield fact
            count =count+1
        else:
            for x in range(count):
                fact=fact * (x+1)
            yield fact
            count=count+1

fs = factorial_gen()
print(fs.next())
print(fs.next())
print(fs.next())
print(fs.next())
