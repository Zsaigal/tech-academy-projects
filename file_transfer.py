import tkinter as tk
from tkinter import *
import tkinter.filedialog
import os
import shutil
import datetime
from datetime import datetime, timedelta

# Define a class for the GUI window
class ParentWindow(Frame):
    def __init__(self, master):
        # Initialize the parent window
        self.master = master
        self.master.title("File Transfer")
        Frame.__init__(self)

        # Create buttons and entry widgets for selecting source and destination directories
        self.sourceDir_btn = Button(text="Select Source", width=20, command=self.sourceDir)
        self.sourceDir_btn.grid(row=0, column=0, padx=(20, 10), pady=(30, 0))

        self.source_dir = Entry(width=75)
        self.source_dir.grid(row=0, column=1, columnspan=2, padx=(20, 10), pady=(30, 0))

        self.destDir_btn = Button(text="Select Destination", width=20, command=self.destDir)
        self.destDir_btn.grid(row=1, column=0, padx=(20, 10), pady=(15, 10))

        self.destination_dir = Entry(width=75)
        self.destination_dir.grid(row=1, column=1, columnspan=2, padx=(20, 10), pady=(15, 10))
        
        # Create buttons for file transfer and exiting the program
        self.transfer_btn = Button(text="Transfer Files", width=20, command=self.transferFiles)
        self.transfer_btn.grid(row=2, column=1, padx=(200, 0), pady=(0, 15))

        self.exit_btn = Button(text="Exit", width=20, command=self.exit_program)
        self.exit_btn.grid(row=2, column=2, padx=(10, 40), pady=(0, 15))

    # Method to select source directory
    def sourceDir(self):
        selectsourceDir = tkinter.filedialog.askdirectory()
        self.source_dir.delete(0, END)
        self.source_dir.insert(0, selectsourceDir)

    # Method to select destination directory
    def destDir(self):
        selectDestDir = tkinter.filedialog.askdirectory()
        self.destination_dir.delete(0, END)
        self.destination_dir.insert(0, selectDestDir)

    # Method to transfer files from source to destination directory
    def transferFiles(self):
        source = self.source_dir.get()
        destination = self.destination_dir.get()
        source_files = os.listdir(source)
        current_time = datetime.now()
        time_threshold = current_time - timedelta(hours=24)

        # Iterate over each file in the source directory
        for file_name in source_files:
            file_path = os.path.join(source, file_name)
            time_modified = datetime.fromtimestamp(os.path.getmtime(file_path))
            # Check if the file has been modified within the last 24 hours
            if time_modified > time_threshold:
                # Transfer the file to the destination directory
                shutil.move(file_path, destination)
                print(f'{file_name} was successfully transferred.')
            else:
                print(f"{file_path} is not new/modified.")

    # Method to exit the program
    def exit_program(self):
        root.destroy()

# Main function to create the Tkinter root window and run the application
if __name__=="__main__":
    root=tk.Tk()
    App=ParentWindow(root)
    root.mainloop()
