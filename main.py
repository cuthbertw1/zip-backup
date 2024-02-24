#!/usr/bin/python3
import os
import subprocess


def backupDir(path, backupPath):
    if(os.path.exists(path) and os.path.exists(backupPath)):
        subprocess.run(['cp','-r',path,backupPath])
    else:
        print('Error main path or backup path not found')