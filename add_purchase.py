import tkinter as tk
from tkinter import *
import tkinter.ttk as ttk
import MySQLdb
import datetime
import os
import functools
from tkinter import messagebox as mb
from tkcalendar import DateEntry

# connecting_to_the_database
db = MySQLdb.connect(host="localhost", user="root", passwd="", database="medical")
mycur = db.cursor()

root = tk.Tk()
root.title('Add Purchases')
root.geometry('{}x{}+200+100'.format(1000, 500))
root.resizable(False, False)

# frames
frame_right = Frame(root)
frame_right.grid()

frame_top = Frame(root, width=800, height=50, bg="#285e5a")
frame_left = Frame(root, width=240, height=405, bg="#285e5a")
frame_right = Frame(root, width=740, height=405, bg="#c9d6d5")

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

Menu6.add_command(label="     Add Purchase      ", font=("Helvetica", 11, "bold"))
Menu6.add_separator()
Menu6.add_command(label="     View Purchases    ", font=("Helvetica", 11, "bold"), command=call_viewpurchase)

MenuBttn["menu"] = Menu6
MenuBttn.grid(column=1, row=6, pady=12, padx=20)

# -----------------------------------------------------------------
# Right Frame

# supplier
supplier = Label(frame_right, text="Supplier ", font=("Times New Roman", 15, "bold"), bg="#c9d6d5")
supplier.grid(row=0, column=0, padx=15, pady=8, sticky="nw")

# importing _current_date
now = datetime.datetime.now()
date = now.strftime("%Y-%m-%d")


def call_addself():
    root.destroy()
    os.system('python3 add_purchase.py')


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
    Label(sup, text="Supplier Details ", font=("Times New Roman", 15, "bold"), fg="White", bg="#285e5a").place(x=110,
                                                                                                               y=20)

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

    Button(sup, text="CANCEL", font=("Times New Roman", 12, "bold"), fg="White", bg="#285e5a", width=8, height=1,
           command=sup_destroy).place(x=80, y=320)
    Button(sup, text="SUBMIT", font=("Times New Roman", 12, "bold"), fg="White", bg="#285e5a", width=8, height=1,
           command=lambda: [sup_add(), call_addself()]).place(x=230, y=320)


def sup_add():
    try:
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
    except Exception as e:
        print(e)
        db.rollback()


def sup_destroy():
    sup.destroy()


# add_button_for_supplier
addsup = Button(frame_right, text="+", font=("Verdana", 12, "bold"), fg="White", bg="#285e5a", command=add_sup_form)
addsup.place(x=270, y=9, height=25, width=25)

# dropdown for supplier
mycur.execute("SELECT sup_id,sup_agency FROM supplier")
myresultsup = mycur.fetchall()
sup_dd = []
# fill list of supplier
for x in myresultsup:
    sup_dd.append(x[1])

supplier_value = tk.StringVar()

supplier_cb = ttk.Combobox(frame_right, textvariable=supplier_value)
supplier_cb['values'] = sup_dd
supplier_cb['state'] = 'readonly'  # normal
supplier_cb.place(x=106, y=9, height=25, width=160)

# ===============================================BILL======================================================

item = StringVar()
Company = StringVar()
Rate = IntVar()
quantity = IntVar()
bg_color = '#c9d6d5'

global l
l = []
global pur_med
pur_med = []
global batch_details
batch_details = []

try:
    sql = "SELECT MAX(p_id) FROM `purchase_details`"
    mycur.execute(sql)
    myresultsale = mycur.fetchone()
    # converting tuple to int
    max_id = functools.reduce(lambda sub, ele: sub * 10 + ele, myresultsale)
    purchase_id = max_id + 1
    print("Max_Purchase ID:", purchase_id)
    db.commit()
except Exception as e:
    print(e)
    db.rollback()


def additm():
    unit_med = []
    unit_batch = []
    n = int(Rate.get())
    q = int(quantity.get())
    m = quantity.get() * n
    l.append(m)
    if item.get() != '':
        textarea.insert((10.0 + float(len(l) - 1)), f"{item.get()}\t\t{n}\t{q}\t{m}\n")

        for t in myresult:
            if t[1] == m_name:
                print('MED ID:', t[0])
                med_id = t[0]

        for c in myresultsup:
            if c[1] == s_name:
                print('Cust ID:', c[0])
                sup_id = c[0]

        mycur.execute("SELECT max(batch_id) FROM med_batch_details WHERE med_id = '" + str(med_id) + "'")
        myresultbatch = mycur.fetchone()
        # converting tuple to int
        maxbatch = functools.reduce(lambda sub, ele: sub * 10 + ele, myresultbatch)
        print('MAX BATCH: ', maxbatch)
        newbatch = maxbatch + 1
        status = "AVAILABLE"

        print("Purchase ID : ", purchase_id)
        print("Med ID :", med_id)
        print("Supp ID", sup_id)
        print("Rate", n)
        print("Qty", q)
        print("Total Amt", m)
        print("MFG", mfg_date.get_date())
        print("EXP", exp_date.get_date())

        unit_med.insert(1, purchase_id)
        unit_med.insert(2, med_id)
        unit_med.insert(3, sup_id)
        unit_med.insert(4, date)
        unit_med.insert(5, n)
        unit_med.insert(6, q)
        unit_med.insert(7, m)

        unit_batch.insert(1, med_id)
        unit_batch.insert(2, newbatch)
        unit_batch.insert(3, mfg_date.get_date())
        unit_batch.insert(4, exp_date.get_date())
        unit_batch.insert(5, status)
        unit_batch.insert(6, q)

        print("UNIT MDES:", unit_med)
        pur_med.append(unit_med)
        print("UNIT BATCH", unit_batch)
        batch_details.append(unit_batch)
    else:
        mb.showerror('Error', 'Please Enter item')


def gbill():
    textAreaText = textarea.get(10.0, (10.0 + float(len(l))))
    welcome()
    textarea.insert(END, textAreaText)
    textarea.insert(END, f"\n=========================================")
    textarea.insert(END, f"\nTotal Paybill Amount :\t  {sum(l)}")
    textarea.insert(END, f"\n\n=========================================")
    save_bill()


def clear():
    # bill_no.set('')
    # date.set('')
    supplier_value.set('')
    item.set('')
    Company.set('')
    Rate.set(0)
    quantity.set(0)
    welcome()


def exit():
    op = mb.askyesno("Exit", "Do you really want to exit?")
    if op > 0:
        root.destroy()


def save_bill():
    op = mb.askyesno("Save bill", "Do you want to save the Bill?")
    if op > 0:
        bill_details = textarea.get('1.0', END)
        f1 = open("purchasebills/" + str(purchase_id) + ".txt", "w")
        f1.write(bill_details)
        f1.close()
        try:
            # Purchase_Details
            allmed_len = len(pur_med)
            sql = "INSERT INTO `purchase_details` (`p_id`,`p_med_id`,`p_sup_id`, `p_date`, `p_price`, `p_qty`, `p_totalamt`) " \
                  "VALUES (%s, %s, %s, %s, %s, %s, %s)"
            for i in range(0, allmed_len, 1):
                mycur.execute(sql, (
                pur_med[i][0], pur_med[i][1], pur_med[i][2], pur_med[i][3], pur_med[i][4], pur_med[i][5],
                pur_med[i][6]))
            db.commit()
            print(mycur.rowcount, "record inserted.")

            # Med_Batch_Details
            batch_details_len = len(batch_details)
            sql = "INSERT INTO `med_batch_details` (`med_id`, `batch_id`, `med_mfg`, `med_exp`, `med_status`, `curr_qty`)" \
                  "VALUES (%s, %s, %s, %s, %s, %s)"
            for i in range(0, batch_details_len, 1):
                mycur.execute(sql, (batch_details[i][0], batch_details[i][1], batch_details[i][2], batch_details[i][3],
                                    batch_details[i][4], batch_details[i][5]))
            db.commit()
            print(mycur.rowcount, "record inserted.")

        except Exception as e:
            print(e)
            db.rollback()
        mb.showinfo("Saved", f"Bill no, {purchase_id} Saved Successfully")
        clear()
    else:
        return


def welcome():
    textarea.delete(1.0, END)
    textarea.insert(END, "\t   Medical Management System")
    textarea.insert(END, f"\n\nBill Number:\t{purchase_id}")
    textarea.insert(END, f"\nSupplier Name:\t{supplier_value.get()}")
    textarea.insert(END, f"\nDate:\t{date}")
    textarea.insert(END, f"\n\n=========================================")
    textarea.insert(END, "\nMedicines\t\tRate\tQty\tPrice")
    textarea.insert(END, f"\n=========================================\n")
    textarea.configure(font='arial 12 bold')


def select_name(event):
    global m_name
    global s_name

    m_name = str(item.get())
    s_name = str(supplier_value.get())

    try:

        # for company
        mycur.execute("SELECT med_comp FROM med_details where med_name = '" + m_name + "'")
        print(m_name)
        myresultcomp = mycur.fetchall()

        for x in myresultcomp:
            print(x)
            comp_txt.config(state=NORMAL)
            comp_txt.delete(0, END)
            comp_txt.insert(END, x[0])
            comp_txt.config(state=DISABLED)

    except Exception as e:
        print(e)


F2 = Label(frame_right, text='Medicine Details', font=('times new roman', 14, 'bold'), fg="White", bg="#285e5a")
F2.place(x=50, y=47, height=22, width=180)

# Medicine_Name_combobox
mycur = db.cursor()
mycur.execute("SELECT med_id,med_name FROM med_details GROUP BY med_name")
myresult = mycur.fetchall()
meds_dd = []
# fill list of meds
for x in myresult:
    meds_dd.append(x[1])

itm_txt = ttk.Combobox(frame_right, textvariable=item, font=('times new roman', 12))
itm_txt['values'] = meds_dd
itm_txt['state'] = 'readonly'  # normal
itm_txt.place(x=120, y=82)

itm_txt.bind('<<ComboboxSelected>>', select_name)

itm = Label(frame_right, text='Name', font=('times new roman', 15, 'bold'), bg=bg_color, fg='Black')
itm.place(x=25, y=82)

comp = Label(frame_right, text='Company', font=('times new roman', 15, 'bold'), bg=bg_color, fg='Black')
comp.place(x=25, y=122)
comp_txt = Entry(frame_right, width=22, textvariable=Company, font=('times new roman', 12, 'bold'))
comp_txt.place(x=120, y=122)

rate = Label(frame_right, text='Rate', font=('times new roman', 15, 'bold'), bg=bg_color, fg='Black')
rate.place(x=25, y=162)
rate_txt = Entry(frame_right, width=22, textvariable=Rate, font=('times new roman', 12, 'bold'))
rate_txt.place(x=120, y=162)

n = Label(frame_right, text='Quantity', font=('times new roman', 15, 'bold'), bg=bg_color, fg='Black')
n.place(x=25, y=202)
n_txt = Entry(frame_right, width=22, textvariable=quantity, font=('times new roman', 12, 'bold'))
n_txt.place(x=120, y=202)

mfg = Label(frame_right, text='Mfg Date', font=('times new roman', 14, 'bold'), bg=bg_color, fg='Black')
mfg.place(x=25, y=242)
mfg_date = DateEntry(frame_right, values="Text", year=2021, state="readonly", date_pattern="yyyy-mm-dd", width=26)
mfg_date.place(x=120, y=242)

exp = Label(frame_right, text='Exp Date', font=('times new roman', 14, 'bold'), bg=bg_color, fg='Black')
exp.place(x=25, y=282)
exp_date = DateEntry(frame_right, values="Text", year=2021, state="readonly", date_pattern="yyyy-mm-dd", width=26)
exp_date.place(x=120, y=282)

# ========================Bill area================
Bill_frame = Frame(frame_right, relief=GROOVE, bd=10)
Bill_frame.place(x=320, y=10, width=410, height=385)

bill_title = Label(Bill_frame, text='Bill Area', font='arial 15 bold', bd=7, relief=GROOVE)
scrol_y = Scrollbar(Bill_frame, orient=VERTICAL)
textarea = Text(Bill_frame, yscrollcommand=scrol_y)
scrol_y.pack(side=RIGHT, fill=Y)
scrol_y.config(command=textarea.yview)
textarea.pack()
welcome()
# =========================Buttons======================
btn1 = Button(frame_right, text='Add Medicines', font='arial 11 bold', width=15, bg="#50aba5", border=2, cursor="hand2",
              command=additm)
btn1.place(x=85, y=320)
btn2 = Button(frame_right, text='Generate Bill', font='arial 11 bold', padx=10, bg="#50aba5", border=2, cursor="hand2",
              command=gbill)
btn2.place(x=25, y=360)
btn3 = Button(frame_right, text='Delete Bill', font='arial 11 bold', padx=10, bg="#50aba5", border=2, cursor="hand2",
              command=clear)
btn3.place(x=180, y=360)

root.mainloop()
