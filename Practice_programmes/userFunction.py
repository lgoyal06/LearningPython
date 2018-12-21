def gcd(m,n):
    min =0;
    if m>n :
        min = n
    else :
        min = m
    largestCommonDivider = 1
    counter = 2
    while(counter <= min):
        if(m%counter == 0 and n%counter== 0):
            largestCommonDivider = counter
            print("A",largestCommonDivider)
        counter +=counter
        print("COUNTER",counter)
    return largestCommonDivider

def main1():
    print(gcd(10,4))

main1()
    
    
