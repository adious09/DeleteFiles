import os
import time

target = input("Path : ")                   #Paste the path
exten_input=input("File Extension : ")      #Give File Extension to delete those files in folder
exten='.'+exten_input

for x in os.listdir(target):
    if x.endswith(exten):
        
        print(f"Deleting file : {x}")
        os.unlink(target+x)
        time.sleep(0.1)
        print(f"{x} Deleted Successfully!")
        print()
