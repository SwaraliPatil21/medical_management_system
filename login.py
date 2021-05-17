from tkinter import *
from PIL import ImageTk, Image
import MySQLdb
import os


#connecting_to_the_database
db = MySQLdb.connect(host="localhost",user="root",passwd="",database="medical")
mycur = db.cursor()


def login():
    global root
    root = Tk()
    root.geometry('{}x{}+200+100'.format(1000, 500))
    root.title('Medical Store Management System')
    root.resizable(0, 0)

    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)

    path = "E:/SEM_4/MiniProject/bg4.jpg"
    img = ImageTk.PhotoImage(Image.open(path))
    panel = Label(root, image=img)
    panel.photo = img
    panel.place(x=0, y=0)

    #frame
    frame_centre = Frame(root, width=600, height=350, bg="#285e5a")

    frame_centre.grid(column=0, row=0, padx=200, pady=50)
    frame_centre.grid_propagate(False)

    path = "E:/SEM_4/MiniProject/ad.png"
    img = ImageTk.PhotoImage(Image.open(path))
    panel = Label(root, image=img)
    panel.photo = img
    panel.place(x=450, y=140)

    #inside frame
    global username_verify
    global password_verify
    username_verify = StringVar()
    password_verify = StringVar()

    heading = Label(frame_centre, text="Welcome to Medical Store Management System", font=("Times New Roman", 15, "bold"), bg="#50aba5")
    heading.grid(padx=94, pady=20)

    Label(frame_centre, text="Username", font=("Times New Roman", 19, "bold"), bg="#285e5a").place(x=130, y=164)
    Entry(frame_centre, textvariable=username_verify, font="Verdana 13").place(x=260, y=170, height=26, width=160)

    Label(frame_centre, text="Password", font=("Times New Roman", 19, "bold"), bg="#285e5a").place(x=130, y=224)
    Entry(frame_centre, textvariable=password_verify, font="Verdana 13", show="●").place(x=260, y=230, height=26, width=160)

    Button(frame_centre, text="LOGIN", bg='#50aba5',font=("Times New Roman", 11, "bold"),command=login_verify).place(x=240, y=300, height=28, width=100)
    Label(frame_centre, text="")



#functinalities
def logg_destroy():
    logg.destroy()
    root.destroy()
    os.system('python3 dashboard.py')


def fail_destroy():
    fail.destroy()

def logged():
    global logg
    logg = Toplevel(root)
    logg.title("Welcome")
    logg.geometry('{}x{}+540+285'.format(280, 95))
    Label(logg, text="Successful Login"'\n'"Welcome {}".format(username_verify.get()), fg="green", font="bold").pack()
    Button(logg, text="OK", bg="lightgrey", width=8, height=1, command=logg_destroy).pack()



def failed():
    global fail
    fail = Toplevel(root)
    fail.title("Invalid Login")
    fail.geometry(('{}x{}+540+285'.format(280, 95)))
    Label(fail, text="Failed Login"'\n'"Check Username and Password", fg="red", font="bold").pack()
    Label(fail, text="").pack()
    Button(fail, text="OK", bg="lightgrey", width=8, height=1, command=fail_destroy).pack()


def login_verify():
    user_verify = username_verify.get()
    pas_verify = password_verify.get()
    sql = "select * from admin where ad_usname = %s and ad_pass = %s"
    mycur.execute(sql,[(user_verify),(pas_verify)])
    results = mycur.fetchall()
    if results:
        for i in results:
            logged()

            break
    else:
        failed()

login()
root.mainloop()