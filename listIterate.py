num = [2,4,6,8]
for i in range(len(num)-1,-1,-1):
    print(num[i])
num = num + [10,12,14]
print("List after append")
for i in range(len(num)-1,-1,-1):
    print(num[i])
print(num)
