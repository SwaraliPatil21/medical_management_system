from tkinter import *
from tkinter.messagebox import *
from tkinter import messagebox as mb
import MySQLdb
import tkinter as tk
import os

# connecting_to_the_database
db = MySQLdb.connect(host="localhost", user="root", passwd="", database="medical")
mycur = db.cursor()

root = Tk()
root.title('Dashboard')
root.geometry('{}x{}+200+100'.format(1000, 500))
root.resizable('false', 'false')

frame_top = Frame(root, width=800, height=50, bg="#285e5a")
frame_right = Frame(root, width=740, height=420, bg="#c9d6d5")
frame_left = Frame(root, width=240, height=420, bg="#285e5a")

# grid
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)

frame_top.grid(row=0, sticky="ew")
frame_left.grid(row=1, sticky="w")
frame_right.grid(row=1, sticky="e")

frame_top.grid_rowconfigure(1, weight=1)
frame_top.grid_columnconfigure(0, weight=1)

frame_left.grid_propagate(False)
frame_right.grid_propagate(False)
frame_top.grid_propagate(False)

# Logout event handler
def confirm():
    answer = askyesno(title='confirmation',
                      message='Are you sure that you want to logout?')
    if answer:
        root.destroy()
        os.system('python3 login.py')

# change password
def change_pass_destroy():
    chg.destroy()

def change_pasword():
    global chg
    global new_pass
    global curr_pass

    curr_pass = StringVar()
    new_pass = StringVar()

    chg = Toplevel(frame_right, bg="#c9d6d5")
    chg.title("Change Password")
    chg.geometry('{}x{}+590+250'.format(370, 180))
    l1 = Label(chg, text="Current Password",font=("Verdana", 11,'bold'), bg="#c9d6d5").place(x=20, y=30)
    e1 = Entry(chg, textvariable=curr_pass, font=("Verdana", 9,'bold'), show="*").place(x=185, y=30, width=150, height=25)
    l2 = Label(chg, text="New Password",font=("Verdana", 11,'bold'),bg="#c9d6d5").place(x=20, y=70)
    e2 = Entry(chg, textvariable=new_pass, font=("Verdana", 9,'bold'), show="*").place(x=185, y=70, width=150,
                                                                                            height=25)

    Button(chg, text="CHANGE",font=("Verdana", 11,'bold'), bg="#50aba5", border=2, cursor= "hand2", command=change_pass_verify).place(x=210, y=120)
    Button(chg, text="CANCEL",font=("Verdana", 11,'bold'), bg="#50aba5", border=2, cursor= "hand2", command=change_pass_destroy).place(x=80, y=120)
    chg.mainloop()


def change_pass_verify():
    curr_pass_verify = curr_pass.get()
    new_pass_verify = new_pass.get()
    try:
        sql = "UPDATE admin SET ad_pass = %s WHERE ad_pass = '" + curr_pass_verify + "'"
        mycur.execute(sql, [(new_pass_verify)])
        db.commit()
        mb.showinfo("Success", "New Password Submitted")
        change_pass_destroy()
    except Exception as e:
        print(e)
        db.rollback()

# Admin name menu
MenuBttn = Menubutton(frame_top, text="ADMIN", font=("Helvetica", 11, "bold"),
                      bg="#50aba5", width=10)

admin = Menu(MenuBttn, tearoff=0)

admin.add_command(label="Change Password", font=("Helvetica", 10, "bold"), command=change_pasword)
admin.add_separator()
admin.add_command(label="Log Out", font=("Helvetica", 10, "bold"), command=confirm)

MenuBttn["menu"] = admin
MenuBttn.grid(column=1, row=1, pady=12, padx=70)


# Scrollable text
svar = tk.StringVar()
Scrollable_text = tk.Label(frame_top, textvariable=svar, height=1, width=200, font=("Helvetica", 14, "bold"), fg="White", bg="#285e5a")

def shif():
    deli = 195
    shif.msg = shif.msg[1:] + shif.msg[0]
    svar.set(shif.msg)
    root.after(deli, shif)

shif.msg = '  Welcome  To  Medical  Store  Management  System!  Wear  Mask,  Stay  Safe!!  '
shif()
Scrollable_text.grid(column=0, row=1, pady=12, padx=50)

# ----------------------------------------------------------------------
# Left Dashboard
# calling pages
import time

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

def call_viewpurchase():
    root.destroy()
    os.system('python3 view_purchase.py')

# Left_button_Dashboard
dashoboard = Button(frame_left, text="DASHBOARD", font=("Helvetica", 11, "bold"), bg="#50aba5", width=21)
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


# ---------------------------------------------------------------------------------
# updating database
try:
    mycur.execute("Update med_batch_details SET "
                  "med_status='EXPIRED' "
                  "WHERE med_batch_details.med_exp <= NOW()")
except Exception as e:
    print(e)
    db.rollback()


# Right_labels
# Sales of month
try:
    mycur.execute("SELECT COUNT(DISTINCT s_id) from sale_details "
                  "WHERE month(s_date)= MONTH(CURDATE()) GROUP BY month(s_date)")
    myresult_sales = mycur.fetchall()
    for myresult_sales in mycur:
        print("Sales of Month", myresult_sales)
except Exception as e:
    print(e)
    db.rollback()

label = Label(frame_right, text=(str("Sales Of Month"'\n'"%s " % myresult_sales)), font=("Helvetica", 20, "bold"), bg="#4d9653", width=15,
              height=3)
label.grid(column=1, row=0, pady=30, padx=40)


# Expired Medicines
try:
    mycur.execute("SELECT COUNT(med_id) from med_batch_details WHERE med_batch_details.med_exp <= NOW()")
    myresult_exp = mycur.fetchall()
    for myresult_exp in mycur:
        print("Expired Products", myresult_exp)
except Exception as e:
    print(e)
    db.rollback()

label = Label(frame_right, text=(str("Expired Products"'\n'"%s " % myresult_exp)), font=("Helvetica", 20, "bold"),
              bg="#e02626", width=15, height=3)
label.grid(column=1, row=3, pady=30, padx=40)

# Stock shortage
try:
    mycur.execute(
        "SELECT COUNT(med_id) from med_batch_details WHERE med_batch_details.curr_qty <= 20 and med_batch_details.med_status ='AVAILABLE'")
    myresult_stckshortage = mycur.fetchall()
    for myresult_stckshortage in mycur:
        print("Stock Shortage", myresult_stckshortage)
except Exception as e:
    print(e)
    db.rollback()

label = Label(frame_right, text=(str("Stock Shortage"'\n'"%s " % myresult_stckshortage)), font=("Helvetica", 20, "bold"),
              bg="#4d8096", width=15, height=3)
label.grid(column=4, row=0, pady=30, padx=40)

# Near Expiry Medicines
try:
    mycur.execute(
        "SELECT COUNT(med_id) from med_batch_details where med_exp between now() and adddate(now(), INTERVAL 10 DAY)")
    myresult_nearexp = mycur.fetchall()
    for myresult_nearexp in mycur:
        print("Near Expiry", myresult_nearexp)
except Exception as e:
    print(e)
    db.rollback()

label = Label(frame_right, text=(str("Near Expiry"'\n'"%s " % myresult_nearexp)), font=("Helvetica", 20, "bold"),
              bg="#e3932b", width=15, height=3)
label.grid(column=4, row=3, pady=30, padx=40)

root.mainloop()
