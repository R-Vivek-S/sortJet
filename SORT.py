import os,shutil,tkinter
from tkinter import filedialog
folders={'videos':['mp4','mkv','avi',],
    'audios':['wav','mp3'],
    'images':['jpg','png','dng','psd'],
    'documents':['doc','xlsx','xls','pdf','txt'],
    'programs':['c','py','exe','msi']}
def sort(path):
    # print("Enter directory path:",end="")

    os.chdir(path)#input())
    
    for file in os.listdir():
        for j in folders:
            if file.split(".")[-1] in folders[j]:
                try:
                    os.mkdir(j)
                except FileExistsError as e:
                    pass
                shutil.move(file,f"./{j}")
                
    print("Sorted Successfully.")
print("Select a folder to sort.")
path = filedialog.askdirectory()
# print("Select destination folder.")
# dest = filedialog.askdirectory()
sort(path)