from tkinter import *
from tkinter.messagebox import *
import tkinter.ttk as ttk
import MySQLdb
import datetime

# connecting_to_the_database
db = MySQLdb.connect(host="localhost", user="root", passwd="", database="medical")
mycur = db.cursor()

root = Tk()
root.title('Dashboard')
root.geometry('{}x{}+200+100'.format(1000, 500))
root.resizable('false', 'false')

#Top_Frame
frame_top = Frame(root, width=800, height=50, bg="#285e5a")

# Logout event handler
def confirm():
    answer = askyesno(title='confirmation',
                    message='Are you sure that you want to logout?')
    if answer:
        root.destroy()

# Logout event handler
# def chng_pass_wind():
#     global window
#     global pass_chng
#     pass_chng = StringVar()
#     window.destroy()
#     window = Tk()
#     Label(window,text="Enter new password:").pack()
#     passn = Entry(window,width=15)
#     passn.pack()
#     Button(window,text="CHANGE", command=chng_pass).pack()
#
# def chng_pass():
#     user_verify = username_verify.get()
#     pas_verify = password_verify.get()
#     sql = "INSERT INTO customer"
#     mycur.execute(sql,[(user_verify),(pas_verify)])
#     results = mycur.fetchall()
#     if results:
#         for i in results:
#             logged()
#             break
#     else:
#         failed()

#Admin name menu
MenuBttn = Menubutton(frame_top, text="Admin Name", font=("Helvetica", 11, "bold"), bg="#50aba5", width=10)

admin = Menu(MenuBttn,  tearoff=0)

admin.add_command(label="Change"'\n'" Password", font=("Helvetica", 9))
admin.add_separator()
admin.add_command(label="Log Out", font=("Helvetica", 9), command=confirm)

MenuBttn["menu"] = admin
MenuBttn.grid(column=1, row=1, pady=12, padx=70)

#Left_Frame
frame_left = Frame(root, width=240, height=420, bg="#285e5a")
frame_left.grid_propagate(False)

#Left_button_Dashboard
dashoboard = Button(frame_left, text="DASHBOARD", font=("Helvetica", 11, "bold"), bg="#50aba5", width=21)
dashoboard.grid(column=1, row=0, pady=12, padx=20)


#Left_Menu1
MenuBttn = Menubutton(frame_left, text="ADMIN", font=("Helvetica", 11, "bold"), bg="#50aba5", width=23)

Menu1 = Menu(MenuBttn, tearoff=0)

Menu1.add_command(label="Add Admin", font=("Helvetica", 11))
Menu1.add_separator()
Menu1.add_command(label="Admin List", font=("Helvetica", 11))

MenuBttn["menu"] = Menu1
MenuBttn.grid(column=1, row=1, pady=12, padx=20)

#Left_Menu2
MenuBttn = Menubutton(frame_left, text="MEDICINES", font=("Helvetica", 11, "bold"), bg="#50aba5", width=23)

Menu2 = Menu(MenuBttn, tearoff=0)

Menu2.add_command(label="Add Medicine", font=("Helvetica", 11))
Menu2.add_separator()
Menu2.add_command(label="Medicine List", font=("Helvetica", 11))

MenuBttn["menu"] = Menu2
MenuBttn.grid(column=1, row=2, pady=12, padx=20)

#Left_Menu3
MenuBttn = Menubutton(frame_left, text="CUSTOMERS", font=("Helvetica", 11, "bold"), bg="#50aba5", width=23)

Menu3 = Menu(MenuBttn, tearoff=0)

Menu3.add_command(label="Customer List", font=("Helvetica", 11))

MenuBttn["menu"] = Menu3
MenuBttn.grid(column=1, row=3, pady=12, padx=20)

#Left_Menu4
MenuBttn = Menubutton(frame_left, text="SUPPLIERS", font=("Helvetica", 11, "bold"), bg="#50aba5", width=23)

Menu4 = Menu(MenuBttn, tearoff=0)

Menu4.add_command(label="Supplier List", font=("Helvetica", 11))

MenuBttn["menu"] = Menu4
MenuBttn.grid(column=1, row=4, pady=12, padx=20)

#Left_Menu5
MenuBttn = Menubutton(frame_left, text="SALES", font=("Helvetica", 11, "bold"), bg="#50aba5", width=23)

Menu5 = Menu(MenuBttn, tearoff=0)

Menu5.add_command(label="Add Sales", font=("Helvetica", 11))
Menu5.add_separator()
Menu5.add_command(label="View Sales", font=("Helvetica", 11))

MenuBttn["menu"] = Menu5
MenuBttn.grid(column=1, row=5, pady=12, padx=20)

#Left_Menu6
MenuBttn = Menubutton(frame_left, text="PURCHASES", font=("Helvetica", 11, "bold"), bg="#50aba5", width=23)

Menu6 = Menu(MenuBttn, tearoff=0)

Menu6.add_command(label="Add Purchase", font=("Helvetica", 11))
Menu6.add_separator()
Menu6.add_command(label="View Purchases", font=("Helvetica", 11))

MenuBttn["menu"] = Menu6
MenuBttn.grid(column=1, row=6, pady=12, padx=20)




#Right_Frame
frame_right = Frame(root, width=740, height=420, bg="#c9d6d5")
frame_right.grid_propagate(False)


# Right_labels


label = Label(frame_right, text="Sales Of Month""\n""50", font=("Helvetica", 20, "bold"), bg="#4d9653", width=15, height=3)
label.grid(column=1, row=0, pady=30, padx=40)

# Expired Medicines
mycur.execute("SELECT COUNT(med_id) from med_batch_details WHERE med_batch_details.med_exp <= NOW()")
myresult_exp = mycur.fetchall()
for myresult_exp in mycur:
    print ("Expired Products", myresult_exp)

label = Label(frame_right, text=(str("Expired Products"'\n'"%s " % myresult_exp)), font=("Helvetica", 20, "bold"), bg="#e02626",
                  width=15, height=3)
label.grid(column=1, row=3, pady=30, padx=40)

# Stock shortage
label = Label(frame_right, text="Stock Shortage""\n""2", font=("Helvetica", 20, "bold"), bg="#4d8096", width=15,
              height=3)
label.grid(column=4, row=0, pady=30, padx=40)

# Near Expiry Medicines
mycur.execute("SELECT COUNT(med_id) from med_batch_details where med_exp between now() and adddate(now(), INTERVAL 10 DAY)")
myresult_nearexp = mycur.fetchall()
for myresult_nearexp in mycur:
    print ("Expired Products", myresult_nearexp)

label = Label(frame_right, text=(str("Near Expiry"'\n'"%s " % myresult_nearexp)), font=("Helvetica", 20, "bold"), bg="#e3932b", width=15, height=3)
label.grid(column=4, row=3, pady=30, padx=40)



#grid
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)

frame_top.grid(row=0,sticky="ew")
frame_left.grid(row=1,sticky="w")
frame_right.grid(row=1,sticky="e")

frame_top.grid_rowconfigure(1, weight=1)
frame_top.grid_columnconfigure(0, weight=1)

root.mainloop()