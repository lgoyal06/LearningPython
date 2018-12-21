from inheritance import CountingClockWatch
from time import sleep

timer=CountingClockWatch()
timer.start()
sleep(10)
timer.stop()
print(timer.elapsed())
