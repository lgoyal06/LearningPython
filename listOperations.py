list = []

def insert(index, element):
        global list
        if len(list)-1<index:
            list = list + [element]
        else:
            listCopy = []
            for i in range(len(list)):
                if i < index or i > index:
                    listCopy=listCopy + [list[i]]
                elif i == index:
                    listCopy=listCopy + [element]
                    listCopy=listCopy + [list[i]]                    
            list=listCopy

def printList():
    print(list)

def remove(element):
    global list
    listCopy = []
    isElementFirstOccuranceFound = False
    for i in range(len(list)):
        if list[i] != element or isElementFirstOccuranceFound == True:
            listCopy=listCopy + [list[i]]
        else:
            isElementFirstOccuranceFound = True
    list=listCopy

def removeIndex(index):
    global list
    listCopy = []
    for i in range(len(list)):
        if i < index or i > index:
            listCopy=listCopy + [list[i]]
    list=listCopy
    
def append(element):
    global list
    list=list+[element]

def sort():
    for i in range(len(list)-1):
        for j in range(i+1,len(list)):
            if list[i]>list[j]:
                tmp=list[i]
                list[i]=list[j]
                list[j]=tmp
def reverse():
    for i in range(int(len(list)/2)):
                tmp=list[i]
                list[i]=list[len(list)-1-i]
                list[len(list)-1-i]=tmp

def pop():
    removeIndex(len(list)-1)
    
def operation(inputList):
    if inputList[0] == 'insert':
        insert(int(inputList[1]), int(inputList[2]))
    elif inputList[0] == 'print':
        printList()
    elif inputList[0] == 'remove':
        remove(int(inputList[1]))
    elif inputList[0] == 'append':
        append(int(inputList[1]))
    elif inputList[0] == 'sort':
        sort()
    elif inputList[0] == 'pop':
        pop()
    elif inputList[0] == 'reverse':
        reverse()
    else:
        print("Invalid Operation")


def main():
    #N = int(input())
    lis = ['append 1','append 6','append 10','append 8','append 9','append 2','append 12','append 7','append 3','append 5','insert 8 66','insert 1 30','insert 6 75','insert 4 44','insert 9 67','insert 2 44','insert 9 21','insert 8 87','insert 1 75','insert 1 48','print','reverse','print','sort','print','append 2','append 5','remove 2','print']
    for i in range(29):
        operation(lis[i].split( ))
main()
    
    
    
