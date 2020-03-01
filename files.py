import os
from os import path
from datetime import date, datetime, time, timedelta
import time

#Using contructor
class FileManager():

    def __init__(self, filename):
            self.filename = filename 

    def createFile(self):
        
        filename = self.filename

        if not os.path.isfile(filename):
            f = open(filename,"w+")
            f.close()

    def appendLine(self, newLines):
  
        filename = self.filename
        
        self.createFile()
        
        f = open(filename,"a")

        if isinstance( newLines, list):
            for row in newLines:
                f.write(row)
        else:
            f.write(newLines)
        
        f.close()

    def readFile(self):

        filename = self.filename

        if os.path.isfile(filename):
            f = open(filename,"r")
            rows = f.readlines()
            for i in rows:
                print(i)
            f.close()

    def getCreateDateTime(self):
        t = time.ctime(path.getctime(self.filename) )
        return t
    
    def getModifyDateTime(self):
        t = time.ctime(path.getmtime(self.filename) )
        return t
    
    def getFileAge(self):
        t = datetime.now() - datetime.fromtimestamp( path.getctime(self.filename) )
        return t.total_seconds()

def main():
    filename = "D:\\py_filetext.txt"
    fileManager = FileManager(filename)

    print("File created at " + fileManager.getCreateDateTime() )

    fileManager.createFile()

    for i in range(10):
        fileManager.appendLine("Valentina eu te amo! " + str(i) + "\r\n" )

    fileManager.readFile()

    print("File modified at " + fileManager.getModifyDateTime() )

    print("File age : " +  str(fileManager.getFileAge() ) )


if __name__ == "__main__":
    main()