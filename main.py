import os
from time import sleep,time
from rm_dir import remover


#Function to scan and put empty directories in an dictionary
def dir_scanner(path):
    emptys=[]
    for paths,dirs,files in os.walk(path):
        if len(files)<=0 and len(dirs)<=0:
            emptys.append(paths)
    print("\n***Empty directory scan complete***\n")
    return emptys
        


#Deleting empty folders
def removeing(empty_list):
    
    for dirs_path in empty_list:
        k=dirs_path.split("\\")
        remover(dirs_path)
        item=k.pop()
        print(f"Removed \"{item}\" folder")
    print("\nDeletion Complete")


#Execution starts here
if __name__=="__main__":
    print("""\n
    ^___________________________________________________________________^
    |           Welcome to empty directory cleaner!                     |
    | Run me and I will clean all the blank folders from your device    |
    |  **Please don't mess up with the code before running or           |
    |    I'm not responsible if it malfunctioned**                      |
    |                                                                   |
    |     Checkout my github http://www.github.com/reshavcodes          |
    |                                                                   |
    |___________________________________________________________________|
    """)

    print("#____Enter the directory path to start scanning___#\n")
    path=input()
    scan=True

#Checking if given path exists
    if os.path.exists(path):
        print("Scanning.......")
        t1=time()

#Getting the empty directories
        try:
            emptys=dir_scanner(path)
        except:
            print("Got error while Scanning please scan again")
            scan=False

#Checking if scanner got any emoty directories stops execution if found 0
        if len(emptys)>=1 and scan:
            print(f"Found {len(emptys)} empty directories/folders")
            sleep(2)
            print("***Starting to delete empty folders***\n")

#Deleting those empty directories
            removeing(emptys)
            print(f"Process complete in {round((time()-t1),2)}s time")

        else:
            print("Found 0 empty folders\nStopping program")
    
    else:
        print("Wrong Path Entered, Please try entering correct path!!!")