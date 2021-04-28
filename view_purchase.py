import tkinter as tk
from tkinter import *
import tkinter.ttk as ttk
from tkinter.messagebox import showinfo
import MySQLdb

# connecting_to_the_database
db = MySQLdb.connect(host="localhost", user="root", passwd="", database="medical")
mycur = db.cursor()

root = Tk()
root.title('View Sales')
root.geometry('{}x{}+200+100'.format(1000, 500))
root.resizable('false', 'false')

# frames
frame_top = Frame(root, width=800, height=50, bg="#285e5a")
frame_left = Frame(root, width=240, height=420, bg="#285e5a")
frame_right = Frame(root, width=740, height=420, bg="#c9d6d5")

# grid
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)

frame_top.grid(row=0, sticky="ew")
frame_left.grid(row=1, sticky="w")
frame_right.grid(row=1, sticky="e")
frame_right.grid_propagate(False)


# Search Function
def search():
    global myresult
    med_id = m_id.get()
    med_comp = m_comp.get()
    med_name = m_name.get()

    try:
        mycur.execute("SELECT med_comp,med_name,med_price FROM med_details where med_id = '" + med_id + "'")
        myresult = mycur.fetchall()

        for x in myresult:
            print(x)
        m_comp.delete(0, END)
        m_comp.insert(END, x[0])
        m_name.delete(0, END)
        m_name.insert(END, x[1])

    except Exception as e:
        print(e)


Label(frame_right, text="Medicine ID", bg="#c9d6d5", font=("Verdana", 10, 'bold')).place(x=50, y=20)
Button(frame_right, text="SEARCH", bg="#50aba5", font=("Verdana", 10, 'bold'), command=search, height=1, width=8).place(
    x=110, y=55)
Label(frame_right, text="Medicine Company", bg="#c9d6d5", font=("Verdana", 10, 'bold')).place(x=300, y=20)
Label(frame_right, text="Medicine Name", bg="#c9d6d5", font=("Verdana", 10, 'bold')).place(x=300, y=53)

m_id = Entry(frame_right, font=("Verdana", 10), width=15)
m_id.place(x=145, y=21)

m_comp = Entry(frame_right, font=("Verdana", 10), width=22)
m_comp.place(x=445, y=21)

m_name = Entry(frame_right, font=("Verdana", 10), width=22)
m_name.place(x=445, y=55)


# Purchase List Label
purchase_lst = Label(frame_right, text="Purchases List", font=("Times New Roman", 15, "bold"), fg="White", bg="#285e5a")
purchase_lst.place(x=285, y=132, height=25, width=180)

# Table_ columns
columns = ('#1', '#2', '#3', '#4', '#5', '#6')

tree = ttk.Treeview(frame_right, selectmode="extended", columns=columns, show='headings')
style = ttk.Style()
style.configure("Treeview.Heading", font=('Verdana', 11), foreground="black", bg='#285e5a')
style.configure('Treeview.Heading', rowheight=50)
style.configure(".", font=('Helvetica', 11), foreground="Black")
style.configure('.', rowheight=20)

# define headings and column length
tree.heading('#1', text='P_ID', anchor=W)
tree.column('#1', minwidth=50, width=70, stretch=0)

tree.heading('#2', text='Supplier Name', anchor=W)
tree.column('#2', minwidth=130, width=150, stretch=0)

tree.heading('#3', text='Purchase Date', anchor=W)
tree.column('#3', minwidth=100, width=120, stretch=0)

tree.heading('#4', text='Medicine ID', anchor=W)
tree.column('#4', minwidth=50, width=110, stretch=0)

tree.heading('#5', text='Medicine Qty', anchor=W)
tree.column('#5', minwidth=60, width=110, stretch=0)

tree.heading('#6', text='Total Amt', anchor=W)
tree.column('#6', minwidth=60, width=90, stretch=0)

# add Sql data to treeview
mycur.execute(
    "SELECT purchase_details.p_id, supplier.sup_name, purchase_details.p_date, purchase_details.p_med_id,"
    "purchase_details.p_qty, purchase_details.p_totalamt "
    "FROM purchase_details INNER JOIN supplier "
    "ON purchase_details.p_sup_id=supplier.sup_id")
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
                 message=', '.join(map(str, record)))


tree.bind('<<TreeviewSelect>>', item_selected)

tree.grid(padx=10, pady=165)

# add a scrollbar
scrollbar = ttk.Scrollbar(frame_right, orient=tk.VERTICAL, command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.grid(row=0, column=1, sticky='ns', pady=165)

frame_right.grid_rowconfigure(1, weight=1)
frame_right.grid_columnconfigure(0, weight=1)

root.mainloop()
