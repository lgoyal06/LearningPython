def listContainsOnlyTrue(list):
    for k in range(len(list)):
        if list[k] is False:
            return False
    return True

def containsCheck(string):
    list=[False,False,False,False,False]
    for k in range(0,len(string)):
        #digit value
        if list[2] !=True and ord(string[k]) >=48 and ord(string[k]) <=57:
            list[2]=True
            list[0]=True
            if listContainsOnlyTrue(list):
                break
            continue
        #Upper Character
        elif list[4]!=True and ord(string[k]) >=65 and ord(string[k]) <=90:
            list[4]=True
            list[1]=True
            list[0]=True
            if listContainsOnlyTrue(list):
                break
            continue
        #Lower Character
        elif list[3]!=True and ord(string[k]) >=97 and ord(string[k]) <=122:
            list[3]=True
            list[1]=True
            list[0]=True
            if listContainsOnlyTrue(list):
                break
            continue
    return list

list = containsCheck("qA2")
for k in range(0,len(list)):
    print(list[k])
