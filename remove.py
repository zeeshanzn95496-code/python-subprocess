# to remove sngle file 

import os 

filename= "example.txt"

if os.path.exists(filename):
    os.remove(filename)
    print(f"file'{filename}'removed successfully")
else:
    print(f"file'{filename}'does not exists")


    #the file example.text has been deleted 