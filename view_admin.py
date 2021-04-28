import tkinter as tk
from tkinter import *
import tkinter.ttk as ttk
from tkinter.messagebox import *
import MySQLdb


#connecting_to_the_database
db = MySQLdb.connect(host="localhost",user="root",passwd="",database="medical")
mycur = db.cursor()

root = Tk()
root.title('View Admin')
root.geometry('{}x{}+200+100'.format(1000, 500))
root.resizable('false', 'false')

#frames
frame_top = Frame(root, width=800, height=50, bg="#285e5a")
frame_left = Frame(root, width=240, height=420, bg="#285e5a")
frame_right = Frame(root, width=740, height=420, bg="#c9d6d5")


#grid
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)

frame_top.grid(row=0, sticky="ew")
frame_left.grid(row=1, sticky="w")
frame_right.grid(row=1, sticky="e")
frame_right.grid_propagate(False)


# columns
columns = ('#1', '#2', '#3', '#4')

tree = ttk.Treeview(frame_right, selectmode="extended", columns=columns, show='headings')
style = ttk.Style()
style.configure("Treeview.Heading", font=('Verdana', 12), foreground="Black")
style.configure('Treeview.Heading', rowheight=25)
style.configure(".", font=('Helvetica', 11), foreground="Black")
style.configure('.', rowheight=25)

# define headings and column length
tree.heading('#1', text='Admin Id', anchor=W)
tree.column('#1', minwidth=50, width=100, stretch=0)

tree.heading('#2', text='Name', anchor=W)
tree.column('#2', minwidth=100, width=180, stretch=0)

tree.heading('#3', text='Phone', anchor=W)
tree.column('#3', minwidth=70, width=130, stretch=0)

tree.heading('#4', text='Email', anchor=W)
tree.column('#4', minwidth=100, width=240, stretch=0)


# add Sql data to treeview
mycur.execute("SELECT ad_id,ad_name,ad_phn,ad_email FROM `admin` ORDER BY `ad_id` ASC")
fetch = mycur.fetchall()
for data in fetch:
    tree.insert('', 'end', values=(data[0], data[1], data[2], data[3]))

# bind the select event
def item_selected(event):
    for selected_item in tree.selection():
        # dictionary
        item = tree.item(selected_item)
        # list
        record = item['values']
        print(record)

tree.bind('<<TreeviewSelect>>', item_selected)

tree.grid(padx=20, pady=120)


# add a scrollbar
scrollbar = ttk.Scrollbar(frame_right, orient=tk.VERTICAL, command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.grid(row=0, column=1, sticky='ns', pady=120)

frame_right.grid_rowconfigure(1, weight=1)
frame_right.grid_columnconfigure(0, weight=1)

root.mainloop()