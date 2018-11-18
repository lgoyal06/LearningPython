#n!/(n-k)!
#n - number of elements
#k - number of possible permutation of k objects
#if n , k = 4 then 24 possible combinations
#TODO resume on 13th Nov 2018
import copy
def permutation(list, startIndex, endIndex):
    if startIndex == endIndex:
        print(list)
        return 
    else:        
            j = startIndex
            while j < endIndex+1:
                #print("swap- ",list[startIndex],"with",list[j])
                #Swapping
                list[startIndex], list[j]=list[j], list[startIndex]
                permutation(list, startIndex+1, endIndex)
                #Backtracking
                list[startIndex], list[j]=list[j], list[startIndex]
                j=j+1
                                   
def main():
    #string ="ABCD"
    list=['A','B','C','D']
    permutation(list,0,len(list)-1)

main()
