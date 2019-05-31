import timeit

myListCode ='''def f1():
    return [x*x for x in range(20)]'''
    
myGeneratorCode='''def f2():
    return (x*x for x in range(20))'''

print(timeit.timeit(stmt = myListCode, 
                    number = 20000))
print(timeit.timeit(stmt = myGeneratorCode, 
                    number = 20000))
