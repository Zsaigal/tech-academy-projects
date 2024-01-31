# Import necessary modules
import tkinter as tk
from tkinter import *
import webbrowser

# Define a class for the main application window
class ParentWindow(Frame):
    # Constructor method
    def __init__(self,master):
        # Call the constructor of the superclass (Frame)
        Frame.__init__(self,master)
        # Set the title of the window
        self.master.title("Web Page Generator")

        # Create and place a label widget for instruction
        self.lbl=Label(self.master,text="Enter custom text or click the Default HTML Page button",width=50,height=6)
        self.lbl.grid(row=1,column=1,columnspan=5,padx=(10,0),pady=(10,0))

        # Create and place an entry widget for user input
        self.entry=Entry(width=100)
        self.entry.grid(row=2,column=2,columnspan=10,padx=(20,10),pady=(20,10))

        # Create and place a button widget to submit custom text
        self.btn=Button(self.master,text="Submit Custom Text",width=30,height=2,command=self.CustomText)
        self.btn.grid(row=8,column=10,padx=(20,10),pady=(20,10))

        # Create and place a button widget to generate default HTML page
        self.btn=Button(self.master,text="Default HTML Page",width=30,height=2,command=self.defaultHTML)
        self.btn.grid(row=8,column=7,padx=(20,10),pady=(20,10))

    # Method to generate default HTML page
    def defaultHTML(self):
        # Default HTML text
        htmlText="Stay tuned for our amazing summer sale"
        # Open/create a file named index.html in write mode
        htmlFile=open("index.html","w")
        # HTML content to be written into the file
        htmlContent="<html>\n<body>\n<h1>"+htmlText+"</h1>\n</body>\n</html>"
        # Write HTML content into the file
        htmlFile.write(htmlContent)
        # Close the file
        htmlFile.close()
        # Open the generated HTML file in a new browser tab
        webbrowser.open_new_tab("index.html")

    # Method to generate custom HTML page
    def CustomText(self):
        # Get custom text from the entry widget
        customText=self.entry.get()
        # Open/create a file named index.html in write mode
        htmlFile=open("index.html","w")
        # HTML content with custom text to be written into the file
        htmlContent="<html>\n<body>\n"+customText+"\n</body>\n</html>"
        # Write HTML content into the file
        htmlFile.write(htmlContent)
        # Close the file
        htmlFile.close()
        # Open the generated HTML file in a new browser tab
        webbrowser.open_new_tab("index.html")

# Main program entry point
if __name__== "__main__":
    # Create a Tkinter root window
    root=tk.Tk()
    # Instantiate the ParentWindow class with the root window
    App=ParentWindow(root)
    # Start the Tkinter event loop
    root.mainloop()
