from tkinter import *
from tkinter import ttk


root = Tk()
root.title('') # Title of app
root.geometry("300x300") # Size of sccreen
root.iconbitmap("")  # Icon at to left of screen
root.configure(background="white") 
ttk.Frame(root, padding=10)


#Label(root, text="Hello world").pack()
#Button(root, text="Hello world", padx=30, pady=10).pack() 
# 
# padx = width, pady = height
# works on most
# 
# .pack(padx = move from left, pady = move down)
# # .grid(column=0, row=0) can be used instead of .pack()


root.mainloop()
