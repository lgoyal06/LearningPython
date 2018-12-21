value = 0
print("Enter number")
value = eval(input())
start = 0
if(value <=4):
    end = value
else:
    end = value/2
while start < end :
    mid = (start+end)/2
    squaredValue= mid * mid
    diff = value-squaredValue
    if diff > 0.00000000000001 or diff < -0.000000000000001:
        if value < squaredValue:
            end = mid
        else:
            start = mid   
    else:
            print(mid)
            break
