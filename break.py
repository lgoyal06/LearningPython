entry =0
sum =0
print("Enter number to sum")
while True:
    entry=eval(input())
    if entry <0:
        break
    sum=sum+entry
print("Sum=",sum)
