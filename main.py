#!/usr/bin/python3
import os
import subprocess
import glob
import zipfile


def backupDir(path, backupPath):
    if(os.path.exists(path) and os.path.exists(backupPath)):
        mainpath=path
        files=os.listdir(path)
        for file in files:
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
    if os.path.exists(path):
        fileStats=os.stat(path)
        size=fileStats.st_size

        if size>=1024:
            size=size/1024
            size=str(size)+" Kilobytes"
        else:
            print(str(size)+" Bytes")
    else:
        print("Error: invalid path given")
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
