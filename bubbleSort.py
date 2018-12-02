if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))    
    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):
            if arr[i]<arr[j]:
                tmp=arr[i]
                arr[i]=arr[j]
                arr[j]=tmp
    uniqueElementIndex=1
    previousVal=arr[0]
    elementPositionToFind=2
    for i in range(1,len(arr)):
      if arr[i] != previousVal:
          uniqueElementIndex+= 1
          previousVal = arr[i]
          if uniqueElementIndex == elementPositionToFind:
              print(arr[i])
              break
