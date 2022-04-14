""" Adding data to Treeview, If the textbox is empty,
    press the button to retrieve all data."""
import sqlite3
import tkinter
import tkinter as tk
from tkinter import ttk

def connect():
    con1 = sqlite3.connect("data/company.db")
    cur1 = con1.cursor()
    cur1.execute("CREATE TABLE IF NOT EXISTS table1(id INTEGER PRIMARY KEY, First TEXT, Surname TEXT)")
    con1.commit()
    con1.close()


def View():
    t_string = ''
    for item in tree.get_children():
        tree.delete(item)
    selection = str(sel())
    if selection == '1':
        name = "first_name"
    else:
        name = "last_name"
    t_str = text_box.get("1.0","end-1c")
    con1 = sqlite3.connect("data/company.db")
    cur1 = con1.cursor()
    if t_str != '':
        like = ("'"+"%"+t_str+"%"+"'")
        sql_string = "SELECT * FROM employees WHERE "+name+" LIKE "+like
    else:
        sql_string = "SELECT * FROM employees"
    cur1.execute(sql_string)
    rows = cur1.fetchall()

    for row in rows:
        tree.insert("", tk.END, values=row)

    con1.close()

# connect to the database

connect()
root = tk.Tk()
root.configure(bg='light blue')
root.geometry('625x275')
s = ttk.Style()
s.theme_use('clam')

# Configure the style of Heading in Treeview widget
s.configure('Treeview.Heading', background="light blue")

tree = ttk.Treeview(root, column=("c1", "c2", "c3"), show='headings')
tree.column("#1", anchor=tk.CENTER)
tree.heading("#1", text="ID")
tree.column("#2", anchor=tk.CENTER)
tree.heading("#2", text="FIRST NAME")
tree.column("#3", anchor=tk.CENTER)
tree.heading("#3", text="LAST NAME")
tree.pack()

def sel():
   selection = str(var.get())
   return selection


button1 = tk.Button(root, text="Display data", command=View)
btn_exit = tk.Button(
    root, text="Exit",
    width=7,
    height=1,
    command=quit)
text_box = tk.Text(root, height=1,
    width=30)

var = tk.IntVar()
radi_button = tk.Radiobutton(root, text='by First Name', variable=var, value=1, command=sel)
radi_button1 = tk.Radiobutton(root, text='by Last Name', variable=var, value=2, command=sel)
radi_button1.pack( side=tkinter.LEFT)
radi_button.pack(side=tkinter.LEFT)
button1.pack(side=tkinter.LEFT)
text_box.pack(side=tkinter.LEFT)
btn_exit.pack(side=tkinter.RIGHT)
root.mainloop()