"""The max, min, average, sum, and count of a set of values were determined
   by SQLite aggregate functions. After determining values, to catch staff min salary and max salary,
   WHERE clause was used. User can select options to find min, max, average values by radio buttons"""
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
    for item in tree.get_children():
        tree.delete(item)
    selection = str(sel())
    if selection == '1':
        sql_string = "SELECT MIN(salary) FROM employees"
    elif selection == '2':
        sql_string = "SELECT MAX(salary) FROM employees"
    else:
        sql_string = "SELECT AVG(salary) FROM employees"
    con1 = sqlite3.connect("data/company.db")
    cur1 = con1.cursor()
    cur1.execute(sql_string)
    rows = cur1.fetchall()
    val = str(rows[0][0])
    if selection == '3':
        avg_salary = tk.Label(text='average of salaries : $'+val)
        avg_salary.pack(side=tkinter.LEFT)
    else:
        sql_string = "SELECT employee_id, first_name, last_name, salary FROM employees WHERE salary="+val
        cur1 = con1.cursor()
        cur1.execute(sql_string)
        rows = cur1.fetchall()
        print(rows)
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

tree = ttk.Treeview(root, column=("c1", "c2", "c3", "c4"), show='headings')
tree.column("#1", anchor=tk.CENTER, width=4)
tree.heading("#1", text="ID")
tree.column("#2", anchor=tk.CENTER)
tree.heading("#2", text="FIRST NAME")
tree.column("#3", anchor=tk.CENTER)
tree.heading("#3", text="LAST NAME")
tree.column("#4", anchor=tk.CENTER)
tree.heading("#4 ", text="SALARY")
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


var = tk.IntVar()

radi_button = tk.Radiobutton(root, text='Min Salary', variable=var, value=1, command=sel)
radi_button1 = tk.Radiobutton(root, text='Max Salary', variable=var, value=2, command=sel)
radi_button2 = tk.Radiobutton(root, text='Avg Salary', variable=var, value=3, command=sel)
radi_button1.pack( side=tkinter.LEFT)
radi_button.pack(side=tkinter.LEFT)
radi_button2.pack( side=tkinter.LEFT)
button1.pack(side=tkinter.LEFT)
btn_exit.pack(side=tkinter.RIGHT)
root.mainloop()