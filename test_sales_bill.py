# Importing Required Module
from reportlab.pdfgen import canvas
import tkinter as tk
from tkinter import *
import tkinter.ttk as ttk
import MySQLdb
import datetime

global cb_number
cb_number = 0
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
frame_right.grid_propagate(False)

frame_top.grid_rowconfigure(1, weight=1)
frame_top.grid_columnconfigure(0, weight=1)

# customer
customer = Label(frame_right, text="Customer ", font=("Times New Roman", 15, "bold"), bg="#c9d6d5")
customer.grid(row=0, column=0, padx=15, pady=8, sticky="nw")

def comando(event):
    print(customer_value.get())

# dropdown for customer
mycur = db.cursor()
mycur.execute("SELECT cust_name FROM customer")
myresult = mycur.fetchall()

customer_value = tk.StringVar()

customer_cb = ttk.Combobox(frame_right, textvariable=customer_value)
customer_cb['values'] = myresult
# customer_cb['state'] = 'readonly'  # normal
customer_cb.place(x=106, y=9, height=25, width=160)

customer_cb.bind('<<ComboboxSelected>>', comando)

# Current Date
curr_date = Label(frame_right, text="Date ", font=("Times New Roman", 15, "bold"), bg="#c9d6d5")
curr_date.place(x=460, y=9)

# importing _current_date
now = datetime.datetime.now()
print(now.strftime("%Y-%m-%d"))

curr_date = Label(frame_right, text=(now.strftime("%Y-%m-%d")), font=("verdana", 11, "bold"), bg="#a1abaa")
curr_date.place(x=512, y=11)

# Net_total_label
net_total = Label(frame_right, text="Net Total ", font=("Times New Roman", 15, "bold"), bg="#c9d6d5")
net_total.place(x=100, y=364)

cal_total = Label(frame_right, text="                ", font=("Times New Roman", 15, "bold"), bg="white")
cal_total.place(x=198, y=365)


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

    sql = "INSERT INTO customer(cust_name, cust_phn, cust_city, cust_email) VALUES (%s, %s, %s, %s)"
    mycur.execute(sql, [(name), (phone), (city), (email)])
    db.commit()

    print(mycur.rowcount, "record inserted.")
    cust_destroy()


def cust_destroy():
    cust.destroy()


# add_button_for_customer
addcust = Button(frame_right, text="+", font=("verdana", 12, "bold"), fg="White", bg="#285e5a",
                 command=add_cust_form, cursor="hand2")
addcust.place(x=270, y=9, height=25, width=25)



def select_name(event):
    print("ComboNumber", cb_number, "SelectedValue",  selected_name.get())


def addbox():
    global cb_number

    frame = Frame(frame_right, width=650, height=30, bg="White")
    frame.grid(padx=50)

    # Item
    if len(all_entries) < 1:
        Label(frame, text="Medicine Name", font=("Times New Roman", 11, "bold"), bg="#c9d6d5").grid(row=1, column=0,
                                                                                                    padx=20, pady=10)
        Label(frame, text="Medicine Company", font=("Times New Roman", 11, "bold"), bg="#c9d6d5").grid(row=1, column=1,
                                                                                                       padx=20, pady=10)
        Label(frame, text="Price", font=("Times New Roman", 11, "bold"), bg="#c9d6d5").grid(row=1, column=2, padx=20,
                                                                                            pady=10)
        Label(frame, text="Quantity", font=("Times New Roman", 11, "bold"), bg="#c9d6d5").grid(row=1, column=3, padx=20,
                                                                                               pady=10)

    # Medicine_Name_combobox
    mycur = db.cursor()
    mycur.execute("SELECT med_name FROM med_details")
    myresult = mycur.fetchall()

    # Medicine_Name_combobox



    global selected_name
    selected_name = tk.StringVar()

    name_cb = ttk.Combobox(frame, textvariable=selected_name)
    name_cb['values'] = myresult
    name_cb['state'] = 'readonly'  # normal
    name_cb.place(x=425, y=100, height=30, width=160)
    name_cb.current()

    name_cb.bind('<<ComboboxSelected>>', select_name)
    name_cb.grid(row=2, column=0, padx=20, pady=7)


    # Medicine_Company_combobox
    global selected_comp
    mycur = db.cursor()
    mycur.execute("SELECT med_comp FROM med_details")
    myresult = mycur.fetchall()

    selected_comp = tk.StringVar()

    comp_cb = ttk.Combobox(frame, textvariable=selected_comp)
    comp_cb['values'] = myresult
    comp_cb['state'] = 'readonly'  # normal
    comp_cb.place(x=425, y=100, height=30, width=160)

    comp_cb.bind('<<ComboboxSelected>>', selected_comp)
    comp_cb.grid(row=2, column=1, padx=20, pady=7)

    # Price
    price = Entry(frame, width=10)
    price.grid(row=2, column=2, padx=20, pady=7)

    # Quantity
    quantity = Entry(frame, width=10)
    quantity.grid(row=2, column=3, padx=20, pady=7)

    all_entries.append((name_cb, comp_cb, price, quantity))

    cb_number = cb_number + 1


# ------------------------------------
# Save_button


save = Button(frame_right, text="SAVE", font=("Times New Roman", 13, "bold"), bg="#50aba5", border=2, cursor="hand2")
save.place(x=440, y=364, height=30, width=100)

all_entries = []
addbox = Button(frame_right, text="Add Medicine Details", font=("Times New Roman", 11, "bold"), fg="White",
                bg="#285e5a", command=addbox)
addbox.grid(sticky="w", padx=260)

root.mainloop()













# Creating Canvas
c = canvas.Canvas("invoice.pdf",pagesize=(200,250),bottomup=0)
# Logo Section
# Setting th origin to (10,40)
c.translate(10,40)
# Inverting the scale for getting mirror Image of logo
c.scale(1,-1)
# Inserting Logo into the Canvas at required position
c.drawImage("E:/SEM_4/MiniProject/pharmacy.png",0,0,width=50,height=30)
# # Title Section
# # Again Inverting Scale For strings insertion
c.scale(1,-1)
# # Again Setting the origin back to (0,0) of top-left
c.translate(-10,-40)
# Setting the font for Name title of company
c.setFont("Helvetica-Bold",10)
# Inserting the name of the company
c.drawCentredString(125,20,"MEDICAL STORE")
# For under lining the title
c.line(70,22,180,22)
# Changing the font size for Specifying Address
c.setFont("Helvetica-Bold",5)
c.drawCentredString(125,30,"Block No. 101, Triveni Apartments, Pitam Pura,")
c.drawCentredString(125,35,"Mumbai - 210034, India")
# Changing the font size for Specifying GST Number of firm
c.setFont("Helvetica-Bold",6)
c.drawCentredString(125,42,"GSTIN : 07AABCS1429B1Z")
# Line Seprating the page header from the body
c.line(5,45,195,45)
# Document Information
# Changing the font for Document title
c.setFont("Courier-Bold",8)
c.drawCentredString(100,55,"INVOICE")
# This Block Consist of Costumer Details
c.roundRect(15,63,170,40,10,stroke=1,fill=0)
c.setFont("Times-Bold",5)


c.drawRightString(70,70,"INVOICE No. :")

c.drawRightString(70,80,"DATE :")
c.drawRightString(95,80,(now.strftime("%Y-%m-%d")))

c.drawRightString(70,90,"CUSTOMER NAME :")
c.drawRightString(95,90,(str("%s " % customer_value.get())))

c.drawRightString(70,100,"PHONE No. :")

# This Block Consist of Item Description
c.roundRect(15,108,170,130,10,stroke=1,fill=0)
c.line(15,120,185,120)

while (True):
    if cb_number == 1:
        c.drawRightString(30,130,(str("%s " % cb_number)))
        c.drawRightString(80, 130, (str("%s " % selected_name.get())))
    elif cb_number == 2:
        c.drawRightString(30, 140, (str("%s " % cb_number)))
        c.drawRightString(80, 140, (str("%s " % selected_name.get())))
    elif cb_number == 3:
        c.drawRightString(30, 150, (str("%s " % cb_number)))
        c.drawRightString(80, 150, (str("%s " % selected_name.get())))
    elif cb_number == 4:
        c.drawRightString(30, 160, (str("%s " % cb_number)))
        c.drawRightString(80, 160, (str("%s " % selected_name.get())))
    elif cb_number == 5:
        c.drawRightString(30, 170, (str("%s " % cb_number)))
        c.drawRightString(80, 170, (str("%s " % selected_name.get())))
    elif cb_number == 6:
        c.drawRightString(30, 180, (str("%s " % cb_number)))
        c.drawRightString(80, 180, (str("%s " % selected_name.get())))
    elif cb_number == 7:
        c.drawRightString(30, 190, (str("%s " % cb_number)))
        c.drawRightString(80, 190, (str("%s " % selected_name.get())))
    else:
        print("No Medicines"'\n'"Purchased!!")


c.drawCentredString(25,118,"SR No.")
c.drawCentredString(75,118,"GOODS DESCRIPTION")

# ("ComboNumber", cb_number, "SelectedValue",  selected_name.get())

c.drawCentredString(125,118,"RATE")
c.drawCentredString(148,118,"QTY")
c.drawCentredString(173,118,"TOTAL")
# Drawing table for Item Description
c.line(15,210,185,210)
c.line(35,108,35,220)
c.line(115,108,115,220)
c.line(135,108,135,220)
c.line(160,108,160,220)
# Declaration and Signature
c.line(15,220,185,220)
c.line(100,220,100,238)
c.drawString(20,225,"We declare that above mentioned")
c.drawString(20,230,"information is true.")
c.drawString(20,235,"(This is system generated invoive)")
c.drawRightString(180,235,"Authorised Signatory")
# End the Page and Start with new
c.showPage()
# Saving the PDF
c.save()