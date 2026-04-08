import tkinter as tk
from tkinter import filedialog, scrolledtext
from main import file_sort  # importing the logic from main.py

def browse_folder():
    folder = filedialog.askdirectory()  # opening a dialog to select a folder
    if folder:
        folder_path.set(folder)

def sort_button_clicked():
    file_sort(folder_path.get(), log)  # calling the file sorting function

def log(message):
    output.insert(tk.END, message + "\n")  # inserting log messages into the output text area
    output.see(tk.END)  # scrolling to the end of the text area

#--- Setting up the GUI ---
root = tk.Tk() #creating the main application window
root.title("File Sorter") #setting the title of the window
root.geometry("500x400") #setting the size of the window

folder_path = tk.StringVar() #creating a StringVar to hold the folder path

tk.Label(root, text="Select Folder:").pack(pady=5) #adding a label to the window
tk.Entry(root, textvariable=folder_path, width=50).pack(pady=0) #adding an entry widget to display the selected folder path
tk.Button(root, text="Browse", command=browse_folder).pack(pady=5) #adding a button to browse for folders
tk.Button(root, text="Sort Files", command=sort_button_clicked).pack(pady=5) #adding a button to start sorting files

output = scrolledtext.ScrolledText(root, width=60, height=15) #adding a scrolled text area to display logs
output.pack(pady=10) #packing the text area into the window

root.mainloop() #starting the main event loop of the application