#  GUI VERSION OF QR CODE CREATOR  #
from tkinter import *
from tkinter import messagebox
import pyqrcode
import os

window = Tk()
window.title("QR CODE CREATOR")


# noinspection PyGlobalUndefined,PyBroadException
def create():
    if len(subject.get()) != 0:
        global Qr
        Qr = pyqrcode.create(subject.get())
        img = Qr.xbm(scale=6)
        global pic
        pic = BitmapImage(data=img)
    else:
        messagebox.showinfo("Error...", "Please Enter The Subject")
    try:
        getcode()
    except:
        pass


# Code Display
# noinspection PyGlobalUndefined
def getcode():
    global pic
    notificationLabel.config(image=pic)
    subLabel.config(text="Showing QR code for: " + subject.get())


# noinspection PyBroadException
def save():
    # Location to save Generated code image
    path = os.getcwd() + "\\QR Codes"
    # Create a folder if not exist
    if not os.path.exists(path):
        os.mkdir(path)
    try:
        if len(name.get()) != 0:
            img = Qr.png(os.path.join(path, name.get() + ".png"), scale=6)
        else:
            messagebox.showinfo("Error...", "Please enter file name..")
    except:
        messagebox.showinfo("Error...", "Please generate before saving")


l1 = Label(window, text="Enter Something", font=("Helvetica", 12))
l1.grid(row=0, column=0, sticky=N + S + E + W)

l2 = Label(window, text="Enter file name", font=("Helvetica", 12))
l2.grid(row=1, column=0, sticky=N + S + E + W)

subject = StringVar()
subjectEntry = Entry(window, textvariable=subject, font=("Helvetica", 12))
subjectEntry.grid(row=0, column=1, sticky=N + S + E + W)

name = StringVar()
nameEntry = Entry(window, textvariable=name, font=("Helvetica", 12))
nameEntry.grid(row=1, column=1, sticky=N + S + E + W)

createBtn = Button(window, text="Create QR", font=("Helvetica", 12), width=15, command=create)
createBtn.grid(row=0, column=3, sticky=N + S + E + W)
notificationLabel = Label(window)
notificationLabel.grid(row=2, column=1, sticky=N + S + E + W)

subLabel = Label(window, text="")
subLabel.grid(row=3, column=1, sticky=N + S + E + W)

showBtn = Button(window, text="Save as PNG", font=("Helvetica", 12), width=15, command=save)
showBtn.grid(row=1, column=3, sticky=N + S + E + W)
# Making responsive layout:
totalRows = 3
totalCols = 3
for row in range(totalRows + 1):
    window.grid_rowconfigure(row, weight=1)
for col in range(totalCols + 1):
    window.grid_columnconfigure(col, weight=1)
# looping the GUI
window.mainloop()
