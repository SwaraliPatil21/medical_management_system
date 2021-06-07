from tkinter import *
import os
import MySQLdb
import tkinter as tk
from tkinter.messagebox import showinfo, showwarning

# connecting_to_the_database
db = MySQLdb.connect(host="localhost", user="root", passwd="", database="medical")
mycur = db.cursor()

root = Tk()
root.title('Add Medicine')
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

frame_top.grid_rowconfigure(1, weight=1)
frame_top.grid_columnconfigure(0, weight=1)

frame_right.grid_propagate(False)
frame_left.grid_propagate(False)
frame_top.grid_propagate(False)

# -------------------------------------------------------------------------------------------------------------
# top frame

# Scrollable Text
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


# -------------------------------------------------------------------------------------------------------------
# left dashboard

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


def call_viewpurchase():
    root.destroy()
    os.system('python3 view_purchase.py')


# Left_button_Dashboard
dashoboard = Button(frame_left, text="DASHBOARD", font=("Helvetica", 11, "bold"), command=call_dashboard,
                    bg="#50aba5", width=21)
dashoboard.grid(column=1, row=0, pady=12, padx=20)

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

Menu2.add_command(label="       Add Medicine      ", font=("Helvetica", 11, "bold"))
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

Menu4.add_command(label="        Supplier List       ", font=("Helvetica", 11, "bold"), command=call_viewsupplier)

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
Menu6.add_command(label="     View Purchases    ", font=("Helvetica", 11, "bold"), command=call_viewpurchase)

MenuBttn["menu"] = Menu6
MenuBttn.grid(column=1, row=6, pady=12, padx=20)
# --------------------------------------------------------------------------------------------------------------------
# Right Design

heading = Label(frame_right, text="  Add Medicine  ", font=("Times New Roman", 20, "bold"), fg="White", bg="#285e5a")
heading.grid(padx=270, pady=40)

global add_name
global add_company
global add_price

add_name = StringVar()
add_company = StringVar()
add_price = StringVar()

Label(frame_right, text="Name", font=("Times New Roman", 18, "bold"), bg="#c9d6d5").place(x=140, y=130)
e1 = Entry(frame_right, textvariable=add_name, font="Verdana 13")
e1.place(x=260, y=130, height=26, width=270)

Label(frame_right, text="Company", font=("Times New Roman", 18, "bold"), bg="#c9d6d5").place(x=140, y=180)
e2 = Entry(frame_right, textvariable=add_company, font="Verdana 13")
e2.place(x=260, y=180, height=26, width=270)

Label(frame_right, text="Price", font=("Times New Roman", 18, "bold"), bg="#c9d6d5").place(x=140, y=230)
e3 = Entry(frame_right, textvariable=add_price, font="Verdana 13")
e3.place(x=260, y=230, height=26, width=270)


def medicine_add():
    name = add_name.get()
    company = add_company.get()
    price = add_price.get()

    try:
        sql = "INSERT INTO med_details(med_name,med_comp,med_price) VALUES (%s, %s, %s)"
        mycur.execute(sql, [name, company, price])
        db.commit()
        print(mycur.rowcount, "record inserted.")
    except Exception as e:
        print(e)
        db.rollback()
    clear_fileds()


def clear_fileds():
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)


def submit_clicked():
    showinfo(
        title='Result',
        message="New Medicine Added."
    )


cancel = Button(frame_right, text="CANCEL", font=("Verdana", 13, "bold"), bg="#50aba5", border=2, cursor="hand2",
                command=clear_fileds).place(x=190, y=300, height=35, width=150)

submit = Button(frame_right, text="SUBMIT", font=("Verdana", 13, "bold"), bg="#50aba5", border=2, cursor="hand2",
                command=lambda: [medicine_add(), submit_clicked(), clear_fileds()]).place(x=380, y=300, height=35,
                                                                                          width=150)

# ------------------------------------------------------------------------------------------------
root.mainloop()
