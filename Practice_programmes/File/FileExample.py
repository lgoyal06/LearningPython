with open("C:\\Users\\lalit goyal\\Desktop\\python\\Practice_programmes\\File\\Sample_File.txt","r") as File1:
    print(File1.name)
    print(File1.mode)

	print("----------read file as a whole-----")
    print(File1.read())
	
	
    print("----------File read lines as list-----")
    FileasList=File1.readlines()
    print(FileasList)

    print("----------File read line by line-----")
    file_stuff=File1.readline()
    print(file_stuff)

    print("----------File read by Iterating-----")
    for line in File1:
        print(line)
        print(type(line))

print(File1.closed)
