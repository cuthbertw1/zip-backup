#!/usr/bin/python3
import os
import subprocess
import glob
import zipfile
import time


def backupDir(path, backupPath):
    if(os.path.exists(path) and os.path.exists(backupPath)):        # input validation
        mainpath=path
        files=os.listdir(path)
        for file in files:                      # loop through files
            currentPath=mainpath+'/'+file
            subprocess.run(['cp',currentPath,backupPath])
    else:
        print('Error main path or backup path not found')
def archiveDir(path, type):
    type=type.lower()
    validTypes=['zip','gztar','tar','bztar','xztar']

    if os.path.exists(path):
        if type not in validTypes:
            print("Error: invalid file type entered ")
        elif type == "zip":
            subprocess.call(['zip','-r','/home/student/archiveddir.zip',path])
        elif type=="tar":
           os.chdir(path)
           items=glob.glob('*')
           subprocess.run(['tar','-cf','/home/student/archiveddir.tar']+items)
        elif type=="gztar":
            os.chdir(path)
            items=glob.glob('*')
            subprocess.run(['tar','-czf','/home/student/archiveddir.tar.gz']+items)
        elif type=="bztar":
            os.chdir(path)
            items = glob.glob('*')
            subprocess.run(['tar', '-cjf', '/home/student/archiveddir.tar.bz2'] + items)
        elif type=="xztar":
            os.chdir(path)
            items = glob.glob('*')
            subprocess.run(['tar', '-cJf', '/home/student/archiveddir.tar.xz'] + items)


def archiveSize(path):
    # getting threshold
    threshold = input("What is the threshold for the size of the files: ")
    # input validation
    try:
        path = os.path.expanduser(path)
        # open zip file
        with zipfile.ZipFile(path) as filePntr:
            # checking files in the zip file
            for file in filePntr.infolist():
                if file.create_system == 0:                     # os detection
                    system = "windows"
                elif file.create_system == 3:
                    system = "Unix"
                else:
                    system = "UNKNOWN"
                # checking if the file is within the threshold
                if file.file_size / 1024 > float(threshold):
                    # if so print
                    print("OS:", system, ",", "File name:", file.filename, ",",
                          "KB:", "{:.2f}".format(file.file_size / 1024), ",",                 # /1024 to account for kb
                          "Compressed KB:", "{:.2f}".format(file.compress_size / 1024))
                # otherwise don't print
                else:
                    continue
            # close the file
            filePntr.close()
    except:
        print("Not a zip file or file does not exists")


def whenModded(path):
    try:
        path = os.path.expanduser(path)
        curentTime=time.time()
        oneMonthAgo=curentTime(30*24*3600)
        for file in os.listdir(path):
            if os.path.getmtime(file)<oneMonthAgo:
                print(file)

    except:
        print("Error: directory not found")


def main():
    print("Welcome user. What would you like to do?")
    print("1. back up directory contents to new directory")         # initial choices
    print("2. Archive the contents of a given directory")
    print("3. view information about given archive ")
    print("5. Exit this menu")
    userChoice=input()
    if userChoice =="1":
        path=input("enter path")
        backuppath=input("enter backup path")       # runs backupDir function
        backupDir(path,backuppath)
    if userChoice=="2":
        path=input("Enter path: ")
        type=input("Enter archive type: ")
        archiveDir(path,type)
    if userChoice=="3":
        path=input("Enter path: ")
        archiveSize(path)
    if userChoice=="5":
        pass                                        # exit condition

main()
