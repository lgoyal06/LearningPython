FileWriteList=["line 1\n","line 2\n", "line 3\n"]
with open("C:\\Users\\lalit goyal\\Desktop\\python\\Practice_programmes\\File\\Sample_File.txt","w") as File1:
    File1.write("This is writing file using Python\n")
    for line in FileWriteList:
        File1.write(line)
