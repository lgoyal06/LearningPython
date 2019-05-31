def kmpfailureFunction(pattern):
    f=[]
    i=1
    j=0
    f.append(0)
    while i<len(pattern):
        if pattern[i]==pattern[j]:
            f.append(j+1)
            i+=1
            j+=1
        elif j>0:
            j=f[j-1]
        else:
            i=i+1
            f.append(0)
        
    return f

"""Solution Not working with cccccccc ccc"""
def count_substring(string,pattern):
    count=0
    f=kmpfailureFunction(pattern)
    i=0
    j=0
    while i<len(string):
        if string[i] == pattern[j]:
            if j==len(pattern)-1:
                count+=1
                j=0
                if len(pattern)==1:
                    i+=1
                continue
            i+=1
            j+=1
        elif j>0:
            j=f[j-1]
        else:
            i+=1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    count = count_substring(string, sub_string)
    print(count)
