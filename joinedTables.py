"""the INNER JOIN clause matches each row from the employees table
with every row from the depatments table based on the join condition
(departments.department_id = employees.department_id)
specified after the ON keyword."""

import sqlite3
import tkinter as tk
from tkinter import ttk

def connect():
    con1 = sqlite3.connect("data/company.db")
    cur1 = con1.cursor()
    con1.commit()
    con1.close()


def view():
    """In this function, the treeview is populated with sql query data."""
    sql_string = """SELECT employees.employee_id, employees.first_name, employees.last_name, 
                  departments.department_name
                  FROM departments
                  INNER JOIN employees ON 
                  departments.department_id = employees.department_id"""
    con1 = sqlite3.connect("data/company.db")
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

"""Python Tkinter Treeview gives an improved look to the data columns.
Python Tkinter Treeview is derived from tkinter.ttk module."""
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
tree.heading("#4 ", text="DEPART. NAME")
tree.pack()

view()
root.mainloop()