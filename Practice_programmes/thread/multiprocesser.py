import timeit
from multiprocessing import Pool
def calc_it(a,n):
    print("sdfsdf")
    start_time = timeit.default_timer()
    sum = 0
    for i in range(a,n+1):
        sum += i
    stop_time = timeit.default_timer()
    print(stop_time-start_time)
    return sum


p=Pool()
result = p.starmap(calc_it, [(1,100),(101,200),(201,300)])
print(result)
p.close()
p.join()
    
