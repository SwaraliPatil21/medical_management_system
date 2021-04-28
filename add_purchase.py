import tkinter as tk
from tkinter import *
import tkinter.ttk as ttk
import MySQLdb
import datetime
from tkcalendar import DateEntry


#connecting_to_the_database
db = MySQLdb.connect(host="localhost",user="root",passwd="",database="medical")
mycur = db.cursor()

root =tk.Tk()
root.title('Add Purchases')
root.geometry('{}x{}+200+100'.format(1000, 500))
root.resizable(False, False)

#frames
frame_right = Frame(root)
frame_right.grid()

frame_top = Frame(root, width=800, height=50, bg="#285e5a")
frame_left = Frame(root, width=240, height=405, bg="#285e5a")
frame_right = Frame(root, width=740, height=405, bg="#c9d6d5")


#grid
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)

frame_top.grid(row=0, sticky="ew")
frame_left.grid(row=1, sticky="w")
frame_right.grid(row=1, sticky="e")
frame_right.grid_propagate(False)

frame_top.grid_rowconfigure(1, weight=1)
frame_top.grid_columnconfigure(0, weight=1)

#supplier
supplier = Label(frame_right, text="Supplier ", font=("Times New Roman", 15, "bold"), bg="#c9d6d5")
supplier.grid(row=0, column=0, padx=15, pady=8, sticky="nw")

#dropdown for supomer
mycur = db.cursor()
mycur.execute("SELECT sup_name FROM supplier")
myresult = mycur.fetchall()

supplier_value = tk.StringVar()

supplier_cb = ttk.Combobox(frame_right, textvariable=supplier_value)
supplier_cb['values'] = myresult
supplier_cb['state'] = 'readonly'  # normal
supplier_cb.place(x=106, y=9, height=25, width=160)

#Current Date
curr_date = Label(frame_right, text="Date ", font=("Times New Roman", 15, "bold"), bg="#c9d6d5")
curr_date.place(x=460, y=9)

#importing _current_date
now = datetime.datetime.now()
print(now.strftime("%Y-%m-%d"))

curr_date = Label(frame_right, text=(now.strftime("%Y-%m-%d")), font=("verdana", 11, "bold"), bg="#a1abaa")
curr_date.place(x=512, y=11)


#Net_total_label
net_total = Label(frame_right, text="Net Total ", font=("Times New Roman", 15, "bold"), bg="#c9d6d5")
net_total.place(x=100, y=364)

cal_total = Label(frame_right, text="                ", font=("Times New Roman", 15, "bold"), bg="white")
cal_total.place(x=198, y=365)



# Add_supplier_form
def add_sup_form():
    global sup
    global add_name, add_agency, add_phone, add_email, add_addr
    add_name = StringVar()
    add_agency = StringVar()
    add_phone = StringVar()
    add_email = StringVar()
    add_addr = StringVar()

    sup = Toplevel(root, bg="#c9d6d5")
    sup.title("Add supplier")
    sup.geometry('{}x{}+560+170'.format(370, 390))
    Label(sup, text="Supplier Details ", font=("Times New Roman", 15, "bold"), fg="White", bg="#285e5a").place(x=110, y=20)

    Label(sup, text="Name", font=("Times New Roman", 14, "bold"), bg="#c9d6d5").place(x=70, y=70)
    Entry(sup, textvariable=add_name, font="Verdana 13").place(x=150, y=73, width=150, height=25)

    Label(sup, text="Agency", font=("Times New Roman", 14, "bold"), bg="#c9d6d5").place(x=70, y=120)
    Entry(sup, textvariable=add_agency, font="Verdana 13").place(x=150, y=123, width=150, height=25)

    Label(sup, text="Phone", font=("Times New Roman", 14, "bold"), bg="#c9d6d5").place(x=70, y=170)
    Entry(sup, textvariable=add_phone, font="Verdana 13").place(x=150, y=173, width=150, height=25)

    Label(sup, text="Email", font=("Times New Roman", 14, "bold"), bg="#c9d6d5").place(x=70, y=220)
    Entry(sup, textvariable=add_email, font="Verdana 13").place(x=150, y=223, width=150, height=25)

    Label(sup, text="Address", font=("Times New Roman", 14, "bold"), bg="#c9d6d5").place(x=70, y=270)
    Entry(sup, textvariable=add_addr, font="Verdana 13").place(x=150, y=273, width=150, height=25)

    Button(sup, text="CANCEL", font=("Times New Roman", 12, "bold"), fg="White", bg="#285e5a", width=8, height=1, command=sup_destroy).place(x=80, y=320)
    Button(sup, text="SUBMIT", font=("Times New Roman", 12, "bold"), fg="White", bg="#285e5a", width=8, height=1, command=sup_add).place(x=230, y=320)

def sup_add():
    name = add_name.get()
    agency = add_agency.get()
    phone = add_phone.get()
    email = add_email.get()
    address = add_addr.get()

    sql = "INSERT INTO supplier(sup_name, sup_agency, sup_phn, sup_email, sup_addr) VALUES (%s, %s, %s, %s, %s)"
    mycur.execute(sql, [(name), (agency), (phone), (email), (address)])
    db.commit()

    print(mycur.rowcount, "record inserted.")
    sup_destroy()

def sup_destroy():
    sup.destroy()

#add_button_for_supplier
addsup = Button(frame_right, text="+", font=("Verdana", 12, "bold"), fg="White", bg="#285e5a", command=add_sup_form)
addsup.place(x=270, y=9, height=25, width=25)



def addbox():
    frame = Frame(frame_right, width=650, height=30, bg="White")
    frame.grid(padx=6)

    # Item
    if len(all_entries) < 1:
        Label(frame, text="Medicine""\n""Name", font=("Times New Roman", 11, "bold"), bg="#c9d6d5").grid(row=1, column=0, padx=10, pady=10)
        Label(frame, text="Medicine""\n""Company", font=("Times New Roman", 11, "bold"), bg="#c9d6d5").grid(row=1, column=1, padx=10, pady=10)
        Label(frame, text="Price", font=("Times New Roman", 11, "bold"), bg="#c9d6d5").grid(row=1, column=2, padx=10, pady=10)
        Label(frame, text="Quantity", font=("Times New Roman", 11, "bold"), bg="#c9d6d5").grid(row=1, column=3, padx=10, pady=10)
        Label(frame, text="Manufacture""\n""Date", font=("Times New Roman", 11, "bold"), bg="#c9d6d5") \
            .grid(row=1, column=4, padx=10, pady=10)
        Label(frame, text="Expiry""\n""Date", font=("Times New Roman", 11, "bold"), bg="#c9d6d5") \
            .grid(row=1, column=5, padx=10, pady=10)

    # Medicine_Name_combobox
    mycur = db.cursor()
    mycur.execute("SELECT med_name FROM med_details")
    myresult = mycur.fetchall()

    selected_value = tk.StringVar()

    name_cb = ttk.Combobox(frame, textvariable=selected_value)
    name_cb['values'] = myresult
    name_cb['state'] = 'readonly'  # normal
    name_cb.place(x=425, y=100, height=30, width=160)

    name_cb.bind('<<ComboboxSelected>>')
    name_cb.grid(row=2, column=0, padx=10, pady=7)

    # Medicine_Company_combobox
    mycur = db.cursor()
    mycur.execute("SELECT med_comp FROM med_details")
    myresult = mycur.fetchall()

    selected_value = tk.StringVar()

    comp_cb = ttk.Combobox(frame, textvariable=selected_value)
    comp_cb['values'] = myresult
    comp_cb['state'] = 'readonly'  # normal
    comp_cb.place(x=425, y=100, height=30, width=160)

    comp_cb.bind('<<ComboboxSelected>>')
    comp_cb.grid(row=2, column=1, padx=10, pady=7)

    # Price
    price = Entry(frame, width=10)
    price.grid(row=2, column=2, padx=10, pady=7)

    # Quantity
    quantity = Entry(frame, width=10)
    quantity.grid(row=2, column=3, padx=10, pady=7)

    # manufacture_date
    mfg_date = DateEntry(frame, values="Text", year=2021, state="readonly", date_pattern="yyyy-mm-dd")
    mfg_date.grid(row=2, column=4, padx=10, pady=7)

    # expiry_date
    exp_date = DateEntry(frame, values="Text", year=2021, state="readonly", date_pattern="yyyy-mm-dd")
    exp_date.grid(row=2, column=5, padx=10, pady=7)

    all_entries.append((name_cb, comp_cb, price, quantity, mfg_date, exp_date))

#------------------------------------
#Save_button
save = Button(frame_right, text="SAVE", font=("Times New Roman", 13, "bold"), fg="White", bg="#285e5a")
save.place(x=440, y=365, height=30, width=100)

all_entries = []
addbox = Button(frame_right, text="Add Medicine Details", font=("Times New Roman", 11, "bold"), fg="White", bg="#285e5a", command=addbox)
addbox.grid(sticky="w", padx=260)



root.mainloop()