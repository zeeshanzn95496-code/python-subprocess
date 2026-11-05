import os

os.chdir('/users/zeeshan/oneDrive/Desktop/subprocess')

folder_name = "test100"

if not os.path.exists(folder_name):
    os.mkdir(folder_name)
    print(f"folder'{folder_name}'created")
else:
    print(f"folder'{folder_name}'already exists")

print(os.listdir())


#this creates a folder in in the subprocess folder which has been created with name test100