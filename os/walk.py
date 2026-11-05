 # walkpath()
#1 root =:current directory path
#2 dirs = list of subdirectries
#3 files = list of files inside that directory

import os

for root, dirs, files in os.walk("."):
    print("current directory:",root)
    print("folders",dirs)
    print("files",files)
    print("-----------------------")

    print(os.getcwd())
    print(os.listdir())
