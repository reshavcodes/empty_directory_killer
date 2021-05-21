import os

def remover(dirpath):
    try:
        os.rmdir(dirpath)
    except:
        print("Directory does not exist or I don't have permission to delete it")

