import zipfile

def writeTo(filename, input_text):
    with open(filename, 'w') as fp:
        fp.write(input_text)
        
def archive(zfile, filename):
        with zipfile.ZipFile(zfile,'w') as zip:
            zip.write(filename)

writeTo('C:\\Users\\lalit goyal\\Desktop\\Testing1.txt','Hello1')
archive('C:\\Users\\lalit goyal\\Desktop\\Testing1.zip', 'C:\\Users\\lalit goyal\\Desktop\\Testing1.txt')
