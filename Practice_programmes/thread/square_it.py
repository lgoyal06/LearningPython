import threading
import time

rv=""
def square_it(n):
    square = n * n
    time.sleep(1)
    global rv
    rv=rv+str(square)+"\n"
    

def do_it(a,b):
    t1= threading.Thread(target=square_it,args=(a,))
    t2= threading.Thread(target=square_it,args=(b,))
    t1.start()
    t1.join()
    t2.start()
    t2.join()
    
do_it(5,23)
print(rv)
    
