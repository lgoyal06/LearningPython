def sum(list):
    sum =0
    for i in list:
        sum += i
    return sum

def clear(list):
    for i in range(len(list)):
        list[i]= 0

def random_list(n):
    import random
    result = []
    for i in range(n):
        rand = random.randrange(1000)
        result+=[rand]
    return result
    
def main():
    print(sum([34,45,44,34]))
    list=[3445,45,23,34]
    print(list)
    clear(list)
    print(list)
    list = random_list(10)
    print(list)

main()
    
