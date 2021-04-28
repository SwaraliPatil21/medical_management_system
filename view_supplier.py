import tkinter as tk
from tkinter import *
import tkinter.ttk as ttk
from tkinter.messagebox import showinfo
import MySQLdb

#connecting_to_the_database
db = MySQLdb.connect(host="localhost",user="root",passwd="",database="medical")
mycur = db.cursor()

root = Tk()
root.title('supplier list')
root.geometry('{}x{}'.format(1000, 500))
root.resizable('false', 'false')

#frames
frame_top = Frame(root, width=800, height=50, bg="#285e5a")
frame_left = Frame(root, width=240, height=420, bg="#285e5a")
frame_right = Frame(root, width=740, height=420, bg="#c9d6d5")


#grid
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)

frame_top.grid(row=0,sticky="ew")
frame_left.grid(row=1,sticky="w")
frame_right.grid(row=1,sticky="e")
frame_right.grid_propagate(False)

heading = Label(frame_right, text="   Supplier List   ", font=("Times New Roman", 18, "bold"), bg="#50aba5")
heading.place(x=278, y=68, height=25, width=180)


# columns
columns = ('#1', '#2', '#3', '#4', '#5', '#6')

tree = ttk.Treeview(frame_right, selectmode="extended", columns=columns, show='headings')
style = ttk.Style()
style.configure("Treeview.Heading", font=('Verdana', 12), foreground="Black")
style.configure('Treeview.Heading', rowheight=25)
style.configure(".", font=('Helvetica', 10), foreground="Black")
style.configure('.', rowheight=25)

# define headings and column length
tree.heading('#1', text='Id', anchor=W)
tree.column('#1', minwidth=30, width=40, stretch=0)

tree.heading('#2', text='Agency Name', anchor=W)
tree.column('#2', minwidth=30, width=150, stretch=0)

tree.heading('#3', text='Name', anchor=W)
tree.column('#3', minwidth=30, width=70, stretch=0)

tree.heading('#4', text='Phone', anchor=W)
tree.column('#4', minwidth=30, width=80, stretch=0)

tree.heading('#5', text='Email', anchor=W)
tree.column('#5', minwidth=30, width=150, stretch=0)

tree.heading('#6', text='Address', anchor=W)
tree.column('#6', minwidth=30, width=220, stretch=0)


# add Sql data to treeview
mycur.execute("SELECT sup_id,sup_agency,sup_name,sup_phn,sup_email, sup_addr FROM `supplier`")
fetch = mycur.fetchall()
for data in fetch:
    tree.insert('', 'end', values=(data[0], data[1], data[2], data[3], data[4], data[5]))


# bind the select event
def item_selected(event):
    for selected_item in tree.selection():
        # dictionary
        item = tree.item(selected_item)
        # list
        record = item['values']
        #
        showinfo(title='Information',
                message=','.join(map(str,record)))


tree.bind('<<TreeviewSelect>>', item_selected)

tree.grid(padx=10, pady=100)

# add a scrollbar
scrollbar = ttk.Scrollbar(frame_right, orient=tk.VERTICAL, command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.grid(row=0, column=1, sticky='ns', pady=120)

frame_right.grid_rowconfigure(1, weight=1)
frame_right.grid_columnconfigure(0, weight=1)



root.mainloop()