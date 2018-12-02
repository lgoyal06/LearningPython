arr=[]
if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        arr.insert(_,[name,score])
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i][1] > arr[j][1]:
                tmp=arr[i]
                arr[i]=arr[j]
                arr[j]=tmp
            elif arr[i][1] == arr[j][1] and arr[i][0] > arr[j][0]:
                tmp=arr[i]
                arr[i]=arr[j]
                arr[j]=tmp
    uniqueValueCounter = 1
    previousVal = arr[0][1]
    elementPositionToFind=2
    for i in range(1,len(arr)):
      if arr[i][1] != previousVal:
          uniqueValueCounter+= 1
          previousVal = arr[i][1]
      if uniqueValueCounter == elementPositionToFind:
          print(arr[i][0])
      elif uniqueValueCounter > elementPositionToFind:
          break
