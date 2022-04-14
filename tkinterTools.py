from tkinter import *
from tkinter import messagebox
main_window = Tk()

# function creates a messagebox for warning or confirmation
def msg(title, text):
    messagebox.showinfo(title, text)

# definitions of main window
def window(size, title):
    main_window.geometry(size)
    main_window.resizable(False, False)
    main_window.title(title)

# create a textbox
def txtbox():
    text_box = Text(
    main_window,
    height=1,
    width=30
    ).place(x=50, y=30)

"""These buttons can display text or images that convey the purpose of the buttons.
You can attach a function or a method to a button which is called automatically 
when you click the button."""
def buton(txt):
    btn2 = Button(
        main_window,
        text=txt,
        command=lambda: msg('Warning', 'the name will be deleted, are you sure?')
    ).place(x=100, y=60)

def btn_exit(txt):
    btn2 = Button(
        main_window,
        width=10,
        text=txt,
        command=lambda: quit()
    ).place(x=100, y=100)
