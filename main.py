import os #importing the os module to interact with operating system
import shutil #importing the shutil module to perform file operations


def file_sort(path, log):
    if not os.path.exists(path): #checking if the provided path exists
        log(f"Path '{path}' does not exist.")
        return
    
    files_list = os.listdir(path) #listing all files in the provided path

    for file in files_list: #iterating through each file in the list
        full_path = path+"/"+file #creating the full path of the file
        if not os.path.isfile(full_path): #checking if the path is a file (not a directory)
            continue #skipping if it's not a file
        filename, extension = os.path.splitext(file) #splitting the file name and extension
        extension = extension[1:].lower() #removing the dot and converting to lowercase
        if extension == "":
            extension = "Null" #if there is no extension, set it to "Null"
        destination_dir = path + "/" + extension #creating the destination directory path
        if not os.path.exists(destination_dir): #checking if the destination directory exists
            os.makedirs(destination_dir) #creating the destination directory if it does not exist
        shutil.move(full_path, destination_dir + "/" + file) #moving the file to the destination directory
        log(f"Moved '{file}' to '{destination_dir}'") #logging the file movement
    log("File sorting completed.") #completion of the sorting process