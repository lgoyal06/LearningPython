with open("C:\\Users\\lalit goyal\\Desktop\\python\\Practice_programmes\\File\\Sample_File_Read.txt","r") as File1:
    with open("C:\\Users\\lalit goyal\\Desktop\\python\\Practice_programmes\\File\\Sample_File.txt","a") as File2:
        for line in File1:
            File2.write(line)
with open("C:\\Users\\lalit goyal\\Desktop\\python\\Practice_programmes\\File\\Sample_File.txt","r") as testwritefile:
    print(testwritefile.read())

