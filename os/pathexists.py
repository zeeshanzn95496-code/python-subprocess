import os 

path= "os.py"

if os.path.exists(path):
    print("path exists")
else:
    print("path does not exists")


    # to check whether path is file or not

    print(os.path.isfile("os.py"))

    #to check whether file is directory 

    print(os.path.isdir("os.py"))

    #to convert relative path into an absolute path 
    
    # path = "os.py"

    #print(os.path.abspath(path))


    # to join directory and file names correctly 

#  folder = "projects"
#  filename = "main.py"
#  path = os.path.join(folder,filename)
#  print(path)