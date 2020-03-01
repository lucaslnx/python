import os
import shutil
from os import path
from shutil import make_archive
from zipfile import ZipFile

def main():

    filename = "D:\\py_filetext.txt"
    destination_file = "D:\\py_filetext_bak.txt"

    if path.exists(filename):
        shutil.copy(filename, destination_file)

    root_dir, tail = path.split(filename)

#    shutil.make_archive("archive","zip", root_dir=)

    with ZipFile("D:\\test.zip","w") as newZip:
        newZip.write(filename)
        newZip.write(destination_file)

if __name__ == "__main__":
    main()