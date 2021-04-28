from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo, showwarning
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

heading = Label(frame_right, text=" Add Admin ", font=("Times New Roman", 18, "bold"),  fg="White", bg="#285e5a")
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


def submit_clicked():
    """ callback when the submit button clicked
    """
    msg = f'You entered name: {add_username.get()}, password: {add_password.get()}, name: {add_name.get()}, phone: {add_phone.get()}, email: {add_email.get()}'
    showinfo(
        title='Result',
        message='New Admin Created'
    )


def add_admin():
    username = add_username.get()
    password = add_password.get()
    name = add_name.get()
    phone = add_phone.get()
    email = add_email.get()

    sql = "INSERT INTO admin(ad_usname,ad_pass,ad_name,ad_phn,ad_email) VALUES (%s, %s, %s, %s, %s)"
    mycur.execute(sql, [username, password, name, phone, email])
    db.commit()

    print(mycur.rowcount, "record inserted.")


def cancel_clicked():
    """ callback when the cancel button clicked
    """
    msg = f'You entered name: {add_username.get()}, password: {add_password.get()}, name: {add_name.get()}, phone: {add_phone.get()}, email: {add_email.get()}'
    showwarning(
        title='Warning',
        message='Data not Submitted'
    )


def clear_fileds():
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e5.delete(0, END)


cancel = Button(frame_right, text="CANCEL", font=("Verdana 13", 13, "bold"), bg="#50aba5", border=2, cursor="hand2",
                command=lambda: [cancel_clicked(), clear_fileds()])
cancel.place(x=270, y=365, height=30)

submit = Button(frame_right, text="SUBMIT", font=("Verdana 13", 13, "bold"), bg="#50aba5", border=2, cursor="hand2",
                command=lambda: [add_admin(), submit_clicked(), clear_fileds()])
submit.place(x=400, y=365, height=30)

root.mainloop()
