def primeFinder(range1):
    import math
    list1=[]
    for i in range(range1):
        list1+=[True]
    divider = 2
    while divider <= int(math.sqrt(range1)):
        firstPerfectDividee = 0
        for j in range(divider+1,range1+1):
            if j%divider  == 0:
                list1[j-1] = False
            else:
                if firstPerfectDividee == 0:
                    firstPerfectDividee = j
        divider = firstPerfectDividee
    return list1

def main():
    listResultant = primeFinder(100)
    prime = 1
    for i in listResultant:
        if(i):
            print(prime)
            prime = prime +1;
        else:
            prime=prime+1

main()
