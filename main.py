import os #importing the os module to interact with operating system
import shutil #importing the shutil module to perform file operations

path = input("Enter the path of the directory you want to organize: ") #taking user input for required directory path

if os.path.exists(path): #checking if the provided path exists
    files_list = os.listdir(path) #listing all files in the provided directory
    for file in files_list: #looping through each file in the directory
        filename, extension = os.path.splitext(file) #splitting the file name and its extension
        extension = extension[1:] #removing the dot from the extension
        if extension == "":
            extension = "Null" #if there is no extension, assigning "Null" as the extension
        if os.path.exists(path+"/"+extension): #checking if a directory with the name of the extension already exists
            shutil.move(path+"/"+file, path+"/"+extension+"/"+file) #moves the file to the corresponding extension directory
        else:
            os.makedirs(path+"/"+extension) #create a new directory with the name of the extension
            shutil.move(path+"/"+file, path+"/"+extension+"/"+file) #moves the file to the newly created extension directory