import tkinter as tk
from tkinter import *
import tkinter.ttk as ttk
from tkinter import messagebox as mb
from tkinter.messagebox import showinfo
import MySQLdb
import os

# connecting_to_the_database
db = MySQLdb.connect(host="localhost", user="root", passwd="", database="medical")
mycur = db.cursor()

root = Tk()
root.title('View Purchase')
root.geometry('{}x{}+200+100'.format(1000, 500))
root.resizable('false', 'false')
# grid
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)

# frames
frame_top = Frame(root, width=800, height=50, bg="#285e5a")
frame_left = Frame(root, width=240, height=420, bg="#285e5a")
frame_right = Frame(root, width=740, height=420, bg="#c9d6d5")

frame_right.grid_rowconfigure(1, weight=1)
frame_right.grid_columnconfigure(0, weight=1)
frame_top.grid_rowconfigure(1, weight=1)
frame_top.grid_columnconfigure(0, weight=1)

frame_top.grid(row=0, sticky="ew")
frame_left.grid(row=1, sticky="w")
frame_right.grid(row=1, sticky="e")

frame_top.grid_propagate(False)
frame_left.grid_propagate(False)
frame_right.grid_propagate(False)

# ----------------------------------------------------------------------------------------------------------
# Top_Frame
# Scrollable text
svar = tk.StringVar()
Scrollable_text = tk.Label(frame_top, textvariable=svar, height=1, width=200, font=("Helvetica", 14, "bold"),
                           fg="White", bg="#285e5a")


def shif():
    deli = 195
    shif.msg = shif.msg[1:] + shif.msg[0]
    svar.set(shif.msg)
    root.after(deli, shif)


shif.msg = '  Welcome  To  Medical  Store  Management  System!  Wear  Mask,  Stay  Safe!!  '
shif()
Scrollable_text.grid(column=0, row=1, pady=12, padx=50)


# -------------------------------------------------------------------------------------
# Left Dashboard
# calling pages
def call_dashboard():
    root.destroy()
    os.system('python3 dashboard.py')


def call_addadmin():
    root.destroy()
    os.system('python3 add_admin.py')


def call_viewadmin():
    root.destroy()
    os.system('python3 view_admin.py')


def call_addmedicine():
    root.destroy()
    os.system('python3 add_medicine.py')


def call_viewmedicine():
    root.destroy()
    os.system('python3 view_medicines.py')


def call_viewcustomer():
    root.destroy()
    os.system('python3 view_customer.py')


def call_viewsupplier():
    root.destroy()
    os.system('python3 view_supplier.py')


def call_addsales():
    root.destroy()
    os.system('python3 add_sales.py')


def call_viewsales():
    root.destroy()
    os.system('python3 view_sales.py')


def call_addpurchase():
    root.destroy()
    os.system('python3 add_purchase.py')


# Left_button_Dashboard
dashboard = Button(frame_left, text="DASHBOARD", font=("Helvetica", 11, "bold"),
                   bg="#50aba5", width=21, command=call_dashboard)
dashboard.grid(column=1, row=0, pady=12, padx=20)

# Left_Menu1
MenuBttn = Menubutton(frame_left, text="ADMIN", font=("Helvetica", 11, "bold"), bg="#50aba5", width=23)

Menu1 = Menu(MenuBttn, tearoff=0)
Menu1.add_command(label="           Add Admin        ", font=("Helvetica", 11, "bold"), command=call_addadmin)
Menu1.add_separator()
Menu1.add_command(label="           Admin List       ", font=("Helvetica", 11, "bold"), command=call_viewadmin)

MenuBttn["menu"] = Menu1
MenuBttn.grid(column=1, row=1, pady=12, padx=20)

# Left_Menu2
MenuBttn = Menubutton(frame_left, text="MEDICINES", font=("Helvetica", 11, "bold"), bg="#50aba5", width=23)

Menu2 = Menu(MenuBttn, tearoff=0)
Menu2.add_command(label="       Add Medicine      ", font=("Helvetica", 11, "bold"), command=call_addmedicine)
Menu2.add_separator()
Menu2.add_command(label="       Medicine List      ", font=("Helvetica", 11, "bold"), command=call_viewmedicine)

MenuBttn["menu"] = Menu2
MenuBttn.grid(column=1, row=2, pady=12, padx=20)

# Left_Menu3
MenuBttn = Menubutton(frame_left, text="CUSTOMERS", font=("Helvetica", 11, "bold"), bg="#50aba5", width=23)

Menu3 = Menu(MenuBttn, tearoff=0)
Menu3.add_command(label="       Customer List      ", font=("Helvetica", 11, "bold"), command=call_viewcustomer)

MenuBttn["menu"] = Menu3
MenuBttn.grid(column=1, row=3, pady=12, padx=20)

# Left_Menu4
MenuBttn = Menubutton(frame_left, text="SUPPLIERS", font=("Helvetica", 11, "bold"), bg="#50aba5", width=23)

Menu4 = Menu(MenuBttn, tearoff=0)
Menu4.add_command(label="       Supplier List       ", font=("Helvetica", 11, "bold"), command=call_viewsupplier)

MenuBttn["menu"] = Menu4
MenuBttn.grid(column=1, row=4, pady=12, padx=20)

# Left_Menu5
MenuBttn = Menubutton(frame_left, text="SALES", font=("Helvetica", 11, "bold"), bg="#50aba5", width=23)

Menu5 = Menu(MenuBttn, tearoff=0)
Menu5.add_command(label="          Add Sales     ", font=("Helvetica", 11, "bold"), command=call_addsales)
Menu5.add_separator()
Menu5.add_command(label="         View Sales         ", font=("Helvetica", 11, "bold"), command=call_viewsales)

MenuBttn["menu"] = Menu5
MenuBttn.grid(column=1, row=5, pady=12, padx=20)

# Left_Menu6
MenuBttn = Menubutton(frame_left, text="PURCHASES", font=("Helvetica", 11, "bold"), bg="#50aba5", width=23)

Menu6 = Menu(MenuBttn, tearoff=0)
Menu6.add_command(label="     Add Purchase      ", font=("Helvetica", 11, "bold"), command=call_addpurchase)
Menu6.add_separator()
Menu6.add_command(label="     View Purchases    ", font=("Helvetica", 11, "bold"))

MenuBttn["menu"] = Menu6
MenuBttn.grid(column=1, row=6, pady=12, padx=20)

# --------------------------------------------------------------------------------------------------------------------
# Right_frame
# Search Function
def search():
    m_comp.delete(0, END)
    m_name.delete(0, END)

    global myresult
    med_id = m_id.get()
    med_comp = m_comp.get()
    med_name = m_name.get()
    try:
        print("med_ID --> ", med_id)
        if med_id == "":
            raise Exception("Medicine ID can't be empty.")

    except Exception as e:
        mb.showerror("ERROR", e)
        print("ERROR --> ", e)
        db.rollback()

    else:
        # try:

        mycur.execute("SELECT med_comp,med_name,med_price FROM med_details where med_id = '" + med_id + "'")
        myresult = mycur.fetchall()

        for x in myresult:
            print(x)

            m_comp.insert(END, x[0])
            m_name.insert(END, x[1])


Label(frame_right, text="Medicine ID", bg="#c9d6d5", font=("Verdana", 11, 'bold')).place(x=50, y=20)
Button(frame_right, text="SEARCH", bg="#50aba5", font=("Verdana", 10, 'bold'), command=search, height=1, width=8).place(
    x=110, y=55)
Label(frame_right, text="Medicine Company", bg="#c9d6d5", font=("Verdana", 11, 'bold')).place(x=300, y=20)
Label(frame_right, text="Medicine Name", bg="#c9d6d5", font=("Verdana", 11, 'bold')).place(x=300, y=53)

m_id = Entry(frame_right, font=("Verdana", 10, 'bold'), width=10)
m_id.place(x=155, y=21)

m_comp = Entry(frame_right, font=("Verdana", 10, 'bold'), width=20)
m_comp.place(x=460, y=21)

m_name = Entry(frame_right, font=("Verdana", 10, 'bold'), width=20)
m_name.place(x=460, y=55)

# Purchase List Label
purchase_lst = Label(frame_right, text="Purchases List", font=("Times New Roman", 18, "bold"), fg="White", bg="#285e5a")
purchase_lst.place(x=285, y=110, height=25, width=180)

# Table_ columns
columns = ('#1', '#2', '#3', '#4', '#5', '#6')

tree = ttk.Treeview(frame_right, selectmode="extended", columns=columns, show='headings')
style = ttk.Style()
style.theme_use("clam")  # can also give default
style.configure("Treeview.Heading", font=('Verdana', 11, "bold"), background="#50aba5", foreground="Black")
style.configure('Treeview.Heading', rowheight=25)
style.configure(".", font=('Helvetica', 12), foreground="Black")
style.configure('.', rowheight=20)

# define headings and column length
tree.heading('#1', text='P_ID', anchor=W)
tree.column('#1', minwidth=50, width=60, stretch=0)

tree.heading('#2', text='Supplier Name', anchor=W)
tree.column('#2', minwidth=130, width=135, stretch=0)

tree.heading('#3', text='Purchase Date', anchor=W)
tree.column('#3', minwidth=100, width=132, stretch=0)

tree.heading('#4', text='Medicine ID', anchor=W)
tree.column('#4', minwidth=50, width=110, stretch=0)

tree.heading('#5', text='Medicine Qty', anchor=W)
tree.column('#5', minwidth=60, width=115, stretch=0)

tree.heading('#6', text='Total Amt', anchor=W)
tree.column('#6', minwidth=60, width=90, stretch=0)

# add Sql data to treeview
try:
    mycur.execute(
        "SELECT purchase_details.p_id, supplier.sup_name, purchase_details.p_date, purchase_details.p_med_id, "
        "purchase_details.p_qty, purchase_details.p_totalamt FROM purchase_details "
        "INNER JOIN supplier ON purchase_details.p_sup_id=supplier.sup_id Order BY purchase_details.p_id DESC")
    fetch = mycur.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data[0], data[1], data[2], data[3], data[4], data[5]))
except Exception as e:
    print(e)
    db.rollback()


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


# to stop column movement
def handle_click(event):
    if tree.identify_region(event.x, event.y) == "separator":
        return "break"


tree.bind('<Button-1>', handle_click)
tree.bind('<<TreeviewSelect>>', item_selected)

tree.grid(padx=10, pady=150)

# add a scrollbar
scrollbar = ttk.Scrollbar(frame_right, orient=tk.VERTICAL, command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.grid(row=0, column=1, sticky='ns', pady=150)

root.mainloop()
