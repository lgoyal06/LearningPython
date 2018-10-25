seconds = eval(input('Pleae enter the number of seconds'))
hour = int(seconds/3600)
seconds = seconds %3600
minute = int(seconds/60)
seconds = seconds%60
print(hour,minute,seconds)
