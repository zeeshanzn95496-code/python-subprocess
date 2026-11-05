# NOW WE WILL delete the test 100 folder 

import os 
folder_name = "test100"

if os.path.exists(folder_name):
    os.rmdir(folder_name)
    print(f"folder'{folder_name}'deleted successfuly")
else:
    print(f"folder'{folder_name}'does not exists")


    #by this program we can delete the folder 