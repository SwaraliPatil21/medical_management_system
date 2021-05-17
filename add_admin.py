from tkinter import *
import tkinter as tk
from tkinter import messagebox as mb
import re
import os
import MySQLdb

# connecting_to_the_database
db = MySQLdb.connect(host="localhost", user="root", passwd="", database="medical")
mycur = db.cursor()

root = tk.Tk()
root.title('Add Admin')
root.geometry('{}x{}+200+100'.format(1000, 500))
root.resizable('false', 'false')


# Add_admin_form
def add_admin_():
    global add_name
    global add_username
    global add_password
    global add_phone
    global add_email

add_name = StringVar()
add_username = StringVar()
add_password = StringVar()
add_phone = StringVar()
add_email = StringVar()


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
Scrollable_text = tk.Label(frame_top, textvariable=svar, height=1, width=200, font=("Helvetica", 14, "bold"), fg="White", bg="#285e5a")

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
dashoboard = Button(frame_left, text="DASHBOARD", font=("Helvetica", 11, "bold"), command=call_dashboard,
                    bg="#50aba5", width=21)
dashoboard.grid(column=1, row=0, pady=12, padx=20)


# Left_Menu1
MenuBttn = Menubutton(frame_left, text="ADMIN", font=("Helvetica", 11, "bold"), bg="#50aba5", width=23)

Menu1 = Menu(MenuBttn, tearoff=0)

Menu1.add_command(label="       Add Admin       ", font=("Helvetica", 11, "bold"))
Menu1.add_separator()
Menu1.add_command(label="       Admin List       ", font=("Helvetica", 11, "bold"), command=call_viewadmin)

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

# --------------------------------------------------------------------
# Right Frame

heading = Label(frame_right, text=" Add Admin ", font=("Times New Roman", 20, "bold"),  fg="White", bg="#285e5a")
heading.grid(padx=305, pady=40)

Label(frame_right, text="Name", font=("Times New Roman", 18, "bold"), bg="#c9d6d5").place(x=200, y=100)
e1 = Entry(frame_right, textvariable=add_name, font="Verdana 13")
e1.place(x=320, y=100, height=26, width=200)

Label(frame_right, text="Username", font=("Times New Roman", 18, "bold"), bg="#c9d6d5").place(x=200, y=150)
e2 = Entry(frame_right, textvariable=add_username, font="Verdana 13")
e2.place(x=320, y=150, height=26, width=200)

Label(frame_right, text="Password", font=("Times New Roman", 18, "bold"), bg="#c9d6d5").place(x=200, y=200)
e3 = Entry(frame_right, textvariable=add_password, font="Verdana 13", show="●")
e3.place(x=320, y=200, height=26, width=200)

Label(frame_right, text="(Use special characters, numbers for more security)",
      font=("Times New Roman", 12), bg="#c9d6d5", fg="red").place(x=320, y=230)

Label(frame_right, text="Phone", font=("Times New Roman", 18, "bold"), bg="#c9d6d5").place(x=200, y=262)
e4 = Entry(frame_right, textvariable=add_phone, font="Verdana 13")
e4.place(x=320, y=265, height=26, width=200)

Label(frame_right, text="Email", font=("Times New Roman", 18, "bold"), bg="#c9d6d5").place(x=200, y=315)
e5 = Entry(frame_right, textvariable=add_email, font="Verdana 13")
e5.place(x=320, y=315, height=26, width=200)


def add_admin():
    username = add_username.get()
    password = add_password.get()
    name = add_name.get()
    phone = add_phone.get()
    email = add_email.get()
    regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
    # test = ['!','@','#','$','%','^','&','*','(',')','<','>','?','/','|','~','{','}',':','_','-']
    test = ' !,@,#,$,%,^,&,*,(,),<,>,?,/,|,~,{,},:,_,- '

    try:
        for c in username:
            if not (c.isalnum() or c.isdigit or re.search(test, username)):
                raise Exception(" Enter proper username.")

        # for c in password:
        #     if not (c.isalnum() and c.isdigit and re.search(test, password)):
        #         raise Exception(" Enter proper password.")

        for c in name:
            if not (c.isalpha() or c.isspace()):
                raise Exception(" Name should contain alphabets only. ")

        if (phone == True):
            if len(phone) > 10 or len(phone) < 10:
                raise Exception(" Phone no. should contain 10 digits.")

        if not phone.isdigit:
            raise Exception(" Phone no. should contain only digits")

        # if (email == True):
        if re.search(regex, email):
            pass
        else:
            raise Exception(" Invalid Email.")
            # print("Name : " , name == "")

        if (name == "" or username == "" or password == "" or phone == ""):
            raise Exception("Fields are Empty.")  # or values can't be null

    except ValueError:
        print("Fields can't be empty.")
        mb.showerror("Fields are empty.")
        db.rollback()

    except Exception as e:
        print("Issue --> Value are null , ", e)
        mb.showerror("ERROR ", e)
        db.rollback()

    except Exception:
        print("Invalid data --> ")
        mb.showerror("ERROR", "Invalid Data.")
        db.rollback()

    except:
        print("Fields can't be empty.")
        mb.showerror("ERROR", "Fields are empty.")
        db.rollback()

    else:
        if not (name and username and password and phone) is None:
            try:
                sql = "INSERT INTO admin(ad_usname,ad_pass,ad_name,ad_phn,ad_email) VALUES (%s, %s, %s, %s, %s)"
                mycur.execute(sql, [username, password, name, phone, email])
                db.commit()
                print(mycur.rowcount, "record inserted.")
                mb.showinfo(
                    title='Result',
                    message='New Admin Created'
                )
                clear_fileds()
            except Exception as e:
                print(e)
                db.rollback()


def clear_fileds():
    mb.showinfo("Warning", "Data not Submitted", icon="warning")
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e5.delete(0, END)


cancel = Button(frame_right, text="CANCEL", font=("Helvetica", 13, "bold"), width=9, bg="#50aba5", border=2, cursor= "hand2",
                command=lambda: [clear_fileds()])
cancel.place(x=270, y=365, height=30)

submit = Button(frame_right, text="SUBMIT", font=("Helvetica", 13, "bold"), width=9, bg="#50aba5", border=2, cursor= "hand2",
                command=lambda: [add_admin()])
submit.place(x=400, y=365, height=30)

root.mainloop()
