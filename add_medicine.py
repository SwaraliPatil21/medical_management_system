from tkinter import *
from tkinter import messagebox
import MySQLdb
from tkinter.messagebox import showinfo, showwarning

# connecting_to_the_database
db = MySQLdb.connect(host="localhost", user="root", passwd="", database="medical")
mycur = db.cursor()

root = Tk()
root.title('Add Medicine')
root.geometry('{}x{}'.format(1000, 500))
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

heading = Label(frame_right, text="  Add Medicine  ", font=("Times New Roman", 18, "bold"), fg="White", bg="#285e5a")
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

    clear_fileds()


def clear_fileds():
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)


def submit_clicked():
    """ callback when the submit button clicked
    """
    msg = f'You entered name: {add_name.get()}, company: {add_company.get()}, price: {add_price.get()}'
    showinfo(
        title='Result',
        message='New Medicine added!!'
    )


cancel = Button(frame_right, text="CANCEL", font=("Verdana", 13, "bold"), bg="#50aba5", border=2, cursor="hand2",
                command=clear_fileds).place(x=190, y=300, height=35, width=150)

submit = Button(frame_right, text="SUBMIT", font=("Verdana", 13, "bold"), bg="#50aba5", border=2, cursor="hand2",
                command=lambda: [medicine_add(), submit_clicked(), clear_fileds()]).place(x=380, y=300, height=35, width=150)

root.mainloop()
