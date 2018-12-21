from stopwatch import Stopwatch

class CountingClockWatch (Stopwatch):
    def __init__(self):
        super(CountingClockWatch, self).__init__()
        self.__count=0
        
    def start(self):
        super(CountingClockWatch,self).start()
        self.__count+=1

    def reset(self):
        super(CountingClockWatch,self).reset()
        self.__count=0

    def count():
        return self.__count
