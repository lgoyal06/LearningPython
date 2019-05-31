import os

class IterateDirectory:
    count=0
    def iterate(self, filePath):
        os.chdir(filePath)      
        listDir = os.listdir()
        for dir1 in listDir:
           if os.path.isdir(os.path.abspath(dir1)):
                self.iterate(os.path.abspath(dir1))
                os.chdir(filePath)
           elif(dir1.endswith(".py")):
                self.count+=1
                print(dir1)
           
id1 = IterateDirectory()
id1.iterate("C:\\Users\\lalit goyal\\Desktop\\python")
print(id1.count)
        
