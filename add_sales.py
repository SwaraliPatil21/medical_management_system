import tkinter as tk
from tkinter import *
import tkinter.ttk as ttk
import MySQLdb
import os
import functools
from tkinter import messagebox as mb
import random
import datetime

# connecting_to_the_database
db = MySQLdb.connect(host="localhost", user="root", passwd="", database="medical")
mycur = db.cursor()

root = tk.Tk()
root.title('Add Sales')
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

frame_top.grid_propagate(False)
frame_right.grid_propagate(False)
frame_left.grid_propagate(False)

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

Menu5.add_command(label="          Add Sales     ", font=("Helvetica", 11, "bold"))
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

# Add_customer_form
def add_cust_form():
    global cust
    global add_name, add_phone, add_city, add_email
    add_name = StringVar()
    add_phone = StringVar()
    add_city = StringVar()
    add_email = StringVar()

    cust = Toplevel(root, bg="#c9d6d5")
    cust.title("Add Customer")
    cust.geometry('{}x{}+560+170'.format(370, 360))
    Label(cust, text="Customer Details ", font=("Times New Roman", 15, "bold"), fg="White", bg="#285e5a").place(x=100,
                                                                                                                y=20)

    Label(cust, text="Name", font=("Times New Roman", 14, "bold"), bg="#c9d6d5").place(x=70, y=70)
    Entry(cust, textvariable=add_name, font="Verdana 13").place(x=150, y=73, width=150, height=25)

    Label(cust, text="Phone", font=("Times New Roman", 14, "bold"), bg="#c9d6d5").place(x=70, y=120)
    Entry(cust, textvariable=add_phone, font="Verdana 13").place(x=150, y=123, width=150, height=25)

    Label(cust, text="City", font=("Times New Roman", 14, "bold"), bg="#c9d6d5").place(x=70, y=170)
    Entry(cust, textvariable=add_city, font="Verdana 13").place(x=150, y=173, width=150, height=25)

    Label(cust, text="Email", font=("Times New Roman", 14, "bold"), bg="#c9d6d5").place(x=70, y=220)
    Entry(cust, textvariable=add_email, font="Verdana 13").place(x=150, y=223, width=150, height=25)

    Button(cust, text="CANCEL", font=("Times New Roman", 12, "bold"), fg="White", bg="#285e5a", width=8, height=1,
           command=cust_destroy).place(x=95, y=280)
    Button(cust, text="SUBMIT", font=("Times New Roman", 12, "bold"), fg="White", bg="#285e5a", width=8, height=1,
           command=cust_add).place(x=200, y=280)


def cust_add():
    name = add_name.get()
    phone = add_phone.get()
    city = add_city.get()
    email = add_email.get()

    try:
        sql = "INSERT INTO customer(cust_name, cust_phn, cust_city, cust_email) VALUES (%s, %s, %s, %s)"
        mycur.execute(sql, [(name), (phone), (city), (email)])
        db.commit()

        print(mycur.rowcount, "record inserted.")
        cust_destroy()

    except Exception as e:
        print(e)
        db.rollback()


def cust_destroy():
    cust.destroy()


# add_button_for_customer
addcust = Button(frame_right, text="+", font=("verdana", 12, "bold"), fg="White", bg="#285e5a",
                 command=lambda: [add_cust_form()], cursor="hand2")
addcust.place(x=249, y=9, height=25, width=25)

# customer
customer = Label(frame_right, text="Customer ", font=("Times New Roman", 15, "bold"), bg="#c9d6d5")
customer.grid(row=0, column=0, padx=15, pady=8, sticky="n")


# Dropdown for customer selection
def cust_name(event):
    print(customer_value.get())


# dropdown for customer
try:
    mycur.execute("SELECT cust_id,cust_name FROM customer")
    myresultcust = mycur.fetchall()
    cust_dd = []
    # fill list of meds
    for x in myresultcust:
        cust_dd.append(x[1])

    customer_value = tk.StringVar()

    customer_cb = ttk.Combobox(frame_right, textvariable=customer_value)
    customer_cb['values'] = cust_dd
    customer_cb['state'] = 'readonly'  # normal
    customer_cb.place(x=106, y=9, height=25, width=140)

    customer_cb.bind('<<ComboboxSelected>>', cust_name)
except Exception as e:
    print(e)
    db.rollback()

# ===============================================BILL======================================================

item = StringVar()
Company = StringVar()
Rate = StringVar()
quantity = IntVar()
bill_no = StringVar()
x = random.randint(1000, 9999)
bill_no.set(str(x))
bg_color = '#c9d6d5'
global sale_id
global l
l = []
all_med = []



# importing _current_date
now = datetime.datetime.now()

date = now.strftime("%Y-%m-%d")
print(date)
try:
    sql = "SELECT MAX(s_id) FROM `sale_details`"
    mycur.execute(sql)
    myresultsale = mycur.fetchone()
    # converting tuple to int
    max_id = functools.reduce(lambda sub, ele: sub * 10 + ele, myresultsale)
    sale_id = max_id + 1
    print("Max_SALE ID:", sale_id)
    db.commit()
except Exception as e:
    print(e)
    db.rollback()


def additm():
    unit_med = []
    n = int(Rate.get())
    q = int(quantity.get())
    m = quantity.get() * n
    l.append(m)
    if item.get() != '':
        textarea.insert((10.0 + float(len(l) - 1)), f"{item.get()}\t\t\t{n}\t{q}\t{m}\n")
        for t in myresult:
            if t[1] == m_name:
                print('MED ID:', t[0])
                med_id = t[0]

        for c in myresultcust:
            if c[1] == c_name:
                print('Cust ID:', c[0])
                cust_id = c[0]

        print("Sale ID : ", sale_id)
        print("Med ID :", med_id)
        print("Cust ID", cust_id)
        print("Qty", q)
        print("Total Amt", m)

        unit_med.insert(1, sale_id)
        unit_med.insert(2, med_id)
        unit_med.insert(3, cust_id)
        unit_med.insert(4, date)
        unit_med.insert(5, q)
        unit_med.insert(6, m)

        print("Sale ID,Med ID,Cust ID,date,Qty,Total Amt:", unit_med)
        all_med.append(unit_med)
    else:
        mb.showerror('Error', 'Please Enter item')


def gbill():
    textAreaText = textarea.get(10.0, (10.0 + float(len(l))))
    welcome()
    print(all_med)
    textarea.insert(END, textAreaText)
    textarea.insert(END, f"\n=========================================")
    textarea.insert(END, f"\nTotal Paybill Amount :\t\t  {sum(l)}")
    textarea.insert(END, f"\n\n=========================================")
    save_bill()


def clear():
    # bill_no.set('')
    # date.set('')
    customer_value.set('')
    item.set('')
    Company.set('')
    Rate.set('')
    quantity.set(0)
    welcome()


def save_bill():
    op = mb.askyesno("Save bill", "Do you want to save the Bill?")
    if op > 0:
        bill_details = textarea.get('1.0', END)
        f1 = open("salesbills/" + str(sale_id) + ".txt", "w")
        f1.write(bill_details)
        f1.close()
        try:
            # Sale_Details
            allmed_len = len(all_med)
            sql1 = "INSERT INTO sale_details(s_id, s_med_id, s_cust_id, s_date, s_qty, s_totalamt) " \
                  "VALUES (%s, %s, %s, %s, %s, %s)"

            sql3 = "UPDATE med_batch_details SET curr_qty = curr_qty - %s WHERE med_batch_details.med_id = %s and med_batch_details.batch_id = %s"

            for i in range(0, allmed_len, 1):
                mycur.execute(sql1,( all_med[i][0],all_med[i][1],all_med[i][2],all_med[i][3],all_med[i][4],all_med[i][5]))

                # batch
                sql2 = ("SELECT MIN(batch_id) FROM `med_batch_details` WHERE med_status= 'AVAILABLE' and med_id = '" + str(all_med[i][1]) + "'")
                mycur.execute(sql2)
                myresultbatch = mycur.fetchall()
                # converting tuple to int
                batch_id = myresultbatch
                print("=====Batch ID=====:", batch_id)

                # updating curr_qty
                mycur.execute(sql3, (all_med[i][4], all_med[i][1], batch_id))

                sql = "SELECT MAX(s_id) FROM `sale_details`"
                mycur.execute(sql)
            db.commit()

        except Exception as e:
            print(e)
            db.rollback()
        mb.showinfo("Saved", f"Bill no, {sale_id} Saved Successfully")
        clear()
    else:
        return


def welcome():
    textarea.delete(1.0, END)
    textarea.insert(END, "\t  Medical Management System")
    textarea.insert(END, f"\n\nBill Number:\t{sale_id}")
    textarea.insert(END, f"\nCustomer Name:\t{customer_value.get()}")
    textarea.insert(END, f"\nDate: {date}")
    textarea.insert(END, f"\n\n============================================")
    textarea.insert(END, "\nMedicines\t\t\tRate\tQty\tPrice")
    textarea.insert(END, f"\n============================================\n")
    textarea.configure(font='arial 12 bold')


def select_name(event):
    global m_name
    global c_name

    # print("ComboNumber", cb_number, "SelectedValue",  selected_name.get())
    m_name = str(item.get())
    c_name = str(customer_value.get())

    try:
        # for price
        mycur.execute("SELECT med_price FROM med_details where med_name = '" + m_name + "'")
        myresultprice = mycur.fetchall()

        for unit_price in myresultprice:
            print(unit_price)
            rate_txt.config(state=NORMAL)
            rate_txt.delete(0, END)
            rate_txt.insert(END, unit_price[0])
            rate_txt.config(state=DISABLED)

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


F2 = Label(frame_right, text='Medicine Details', font=('times new roman', 15, 'bold'), fg="White", bg="#285e5a")
F2.place(x=50, y=50, height=25, width=180)

# Medicine_Name_combobox
mycur = db.cursor()
mycur.execute("SELECT med_id,med_name FROM med_details GROUP BY med_name")
myresult = mycur.fetchall()
print(myresult)
meds_dd = []
# fill list of meds
for x in myresult:
    meds_dd.append(x[1])

itm_txt = ttk.Combobox(frame_right, textvariable=item, font=('times new roman', 12))
itm_txt['values'] = meds_dd
itm_txt['state'] = 'readonly'  # normal
itm_txt.place(x=100, y=90)

itm_txt.bind('<<ComboboxSelected>>', select_name)

itm = Label(frame_right, text='Name', font=('times new roman', 15, 'bold'), bg=bg_color, fg='Black')
itm.place(x=15, y=90)

comp = Label(frame_right, text='Company', font=('times new roman', 15, 'bold'), bg=bg_color, fg='Black')
comp.place(x=15, y=130)
comp_txt = Entry(frame_right, width=22, textvariable=Company, font=('times new roman', 12, 'bold'))
comp_txt.place(x=100, y=130)

rate = Label(frame_right, text='Rate', font=('times new roman', 15, 'bold'), bg=bg_color, fg='Black')
rate.place(x=15, y=170)
rate_txt = Entry(frame_right, width=22, textvariable=Rate, font=('times new roman', 12, 'bold'))
rate_txt.place(x=100, y=170)

n = Label(frame_right, text='Quantity', font=('times new roman', 15, 'bold'), bg=bg_color, fg='Black')
n.place(x=15, y=210)
n_txt = Entry(frame_right, width=22, textvariable=quantity, font=('times new roman', 12, 'bold'))
n_txt.place(x=100, y=212)

# ========================Bill area================
Bill_frame = Frame(frame_right, relief=GROOVE, bd=10)
Bill_frame.place(x=293, y=10, width=442, height=385)

bill_title = Label(Bill_frame, text='Bill Area', font='arial 15 bold', bd=7, relief=GROOVE)
scrol_y = Scrollbar(Bill_frame, orient=VERTICAL)
textarea = Text(Bill_frame, yscrollcommand=scrol_y)
scrol_y.pack(side=RIGHT, fill=Y)
scrol_y.config(command=textarea.yview)
textarea.pack()
welcome()
# =========================Buttons======================
btn1 = Button(frame_right, text='Add Medicines', font='arial 12 bold', width=15, bg="#50aba5", border=2, cursor="hand2", command=additm)
btn1.place(x=60, y=280)
btn2 = Button(frame_right, text='Generate Bill', font='arial 12 bold', padx=10, bg="#50aba5", border=2, cursor="hand2", command=gbill)
btn2.place(x=15, y=330)
btn3 = Button(frame_right, text='Delete Bill', font='arial 12 bold', padx=10, bg="#50aba5", border=2, cursor="hand2", command=clear)
btn3.place(x=160, y=330)

root.mainloop()
