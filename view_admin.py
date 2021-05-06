import tkinter as tk
from tkinter import *
import tkinter.ttk as ttk
from tkinter import messagebox as mb
import MySQLdb
import os


#connecting_to_the_database
db = MySQLdb.connect(host="localhost",user="root",passwd="",database="medical")
mycur = db.cursor()

root = Tk()
root.title('View Admin')
root.geometry('{}x{}+200+100'.format(1000, 500))
root.resizable('false', 'false')

root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)

#frames
frame_top = Frame(root, width=800, height=50, bg="#285e5a")
frame_left = Frame(root, width=240, height=420, bg="#285e5a")
frame_right = Frame(root, width=740, height=420, bg="#c9d6d5")


frame_top.grid(row=0, sticky="ew")
frame_left.grid(row=1, sticky="w")
frame_right.grid(row=1, sticky="e")

frame_top.grid_rowconfigure(1, weight=1)
frame_top.grid_columnconfigure(0, weight=1)
frame_right.grid_rowconfigure(1, weight=1)
frame_right.grid_columnconfigure(0, weight=1)

frame_top.grid_propagate(False)
frame_left.grid_propagate(False)
frame_right.grid_propagate(False)

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


# -------------------------------------------------------------------------------------
# Left Dashboard
# calling pages
def call_dashboard():
    root.destroy()
    os.system('python3 dashboard.py')


def call_addadmin():
    root.destroy
    os.system('python3 add_admin.py')


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
dashoboard = Button(frame_left, text="DASHBOARD", font=("Helvetica", 11, "bold"),
                    bg="#50aba5", width=21, command=call_dashboard)
dashoboard.grid(column=1, row=0, pady=12, padx=20)

# Left_Menu1
MenuBttn = Menubutton(frame_left, text="ADMIN", font=("Helvetica", 11, "bold"), bg="#50aba5", width=23)

Menu1 = Menu(MenuBttn, tearoff=0)
Menu1.add_command(label="       Add Admin       ", font=("Helvetica", 11), command=call_addadmin)
Menu1.add_separator()
Menu1.add_command(label="       Admin List      ", font=("Helvetica", 11))

MenuBttn["menu"] = Menu1
MenuBttn.grid(column=1, row=1, pady=12, padx=20)

# Left_Menu2
MenuBttn = Menubutton(frame_left, text="MEDICINES", font=("Helvetica", 11, "bold"), bg="#50aba5", width=23)

Menu2 = Menu(MenuBttn, tearoff=0)
Menu2.add_command(label="   Add Medicine    ", font=("Helvetica", 11), command=call_addmedicine)
Menu2.add_separator()
Menu2.add_command(label="   Medicine List   ", font=("Helvetica", 11), command=call_viewmedicine)

MenuBttn["menu"] = Menu2
MenuBttn.grid(column=1, row=2, pady=12, padx=20)

# Left_Menu3
MenuBttn = Menubutton(frame_left, text="CUSTOMERS", font=("Helvetica", 11, "bold"), bg="#50aba5", width=23)

Menu3 = Menu(MenuBttn, tearoff=0)
Menu3.add_command(label="       Customer List       ", font=("Helvetica", 11), command=call_viewcustomer)

MenuBttn["menu"] = Menu3
MenuBttn.grid(column=1, row=3, pady=12, padx=20)

# Left_Menu4
MenuBttn = Menubutton(frame_left, text="SUPPLIERS", font=("Helvetica", 11, "bold"), bg="#50aba5", width=23)

Menu4 = Menu(MenuBttn, tearoff=0)
Menu4.add_command(label="       Supplier List       ", font=("Helvetica", 11), command=call_viewsupplier)

MenuBttn["menu"] = Menu4
MenuBttn.grid(column=1, row=4, pady=12, padx=20)

# Left_Menu5
MenuBttn = Menubutton(frame_left, text="SALES", font=("Helvetica", 11, "bold"), bg="#50aba5", width=23)

Menu5 = Menu(MenuBttn, tearoff=0)
Menu5.add_command(label="       Add Sales     ", font=("Helvetica", 11), command=call_addsales)
Menu5.add_separator()
Menu5.add_command(label="       View Sales    ", font=("Helvetica", 11), command=call_viewsales)

MenuBttn["menu"] = Menu5
MenuBttn.grid(column=1, row=5, pady=12, padx=20)

# Left_Menu6
MenuBttn = Menubutton(frame_left, text="PURCHASES", font=("Helvetica", 11, "bold"), bg="#50aba5", width=23)

Menu6 = Menu(MenuBttn, tearoff=0)
Menu6.add_command(label="   Add Purchase    ", font=("Helvetica", 11), command=call_addpurchase)
Menu6.add_separator()
Menu6.add_command(label="   View Purchases  ", font=("Helvetica", 11), command=call_viewpurchase)

MenuBttn["menu"] = Menu6
MenuBttn.grid(column=1, row=6, pady=12, padx=20)

# --------------------------------------------------------------------------------------------------------------------
# Right_frame

global add_name
global add_phone
global add_email
add_name = tk.StringVar()
add_phone = tk.StringVar()
add_email = tk.StringVar()

# label for admin list
admin_list = Label(frame_right, text=" Admin List ", font=("Times New Roman", 20, "bold"), fg="White", bg="#285e5a")
admin_list.place(x=250, y=24, height=35, width=200)

# columns
columns = ('#1', '#2', '#3', '#4')

tree = ttk.Treeview(frame_right, selectmode="extended", columns=columns, show='headings')
style = ttk.Style()
style.theme_use("clam") #can also give default
style.configure("Treeview.Heading", font=('Verdana',12,"bold"), background ="#50aba5", foreground="Black")
style.configure('Treeview.Heading', rowheight=25)
style.configure(".", font=('Helvetica', 11), foreground="Black")
style.configure('.', rowheight=25)

# define headings and column length
tree.heading('#1', text='Admin Id', anchor=W)
tree.column('#1', minwidth=50, width=100, stretch=0)

tree.heading('#2', text='Name', anchor=W)
tree.column('#2', minwidth=100, width=180, stretch=0)

tree.heading('#3', text='Phone', anchor=W)
tree.column('#3', minwidth=70, width=130, stretch=0)

tree.heading('#4', text='Email', anchor=W)
tree.column('#4', minwidth=100, width=240, stretch=0)


# add Sql data to treeview
try:
    mycur.execute("SELECT ad_id,ad_name,ad_phn,ad_email FROM `admin` ORDER BY `ad_id` ASC")
    fetch = mycur.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data[0], data[1], data[2], data[3]))
except Exception as e:
    print(e)
    db.rollback()

# bind the select event
def item_selected(event):
    for selected_item in tree.selection():
        # dictionary
        item = tree.item(selected_item)
        # list
        record = item['values']
        print(record)


#to stop column movement
def handle_click(event):
    if tree.identify_region(event.x, event.y) == "separator":
        return "break"




tree.bind('<Button-1>', handle_click)
tree.bind('<<TreeviewSelect>>', item_selected)

tree.grid(padx=20, pady=80)

# add a scrollbar
scrollbar = ttk.Scrollbar(frame_right, orient=tk.VERTICAL, command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.grid(row=0, column=1, sticky='ns', pady=80)

# delete_table_selection
deletebutton = tk.Button(frame_right, text="DELETE", command=lambda: (delete_data(tree), item_selected))
deletebutton.configure(font=('Verdana', 12, 'bold'), bg="#318781", cursor="hand2")
deletebutton.place(x=250, y=375)


def delete_data(tree):
    try:
        selected_item = tree.selection()[0]
        print(tree.item(selected_item)['values'])
        uid = tree.item(selected_item)['values'][0]
        del_query = "DELETE FROM admin WHERE ad_id=%s"
        sel_data = (uid,)
        mycur.execute(del_query, sel_data)
        db.commit()
        tree.delete(selected_item)
    except Exception as e:
        print(e)
        db.rollback()
    mb.showinfo("success", "ADMIN data deleted!")



# Update_table_selection
updatebutton = tk.Button(frame_right, text="EDIT", command=lambda: (select_data(tree)))
updatebutton.configure(font=('Verdana', 12, 'bold'), bg="#318781", cursor="hand2")
updatebutton.place(x=420, y=375)


def select_data(tree):
    f = Toplevel(root, bg="#c5dedd")
    f.title("Modify Details")
    f.geometry('{}x{}+635+220'.format(370, 300))
    curItem = tree.focus()
    values = tree.item(curItem, "values")
    print(values)

    head = Label(f, text="Update Admin",width=15, font=("Times New Roman", 14, "bold"), fg="White", bg="#285e5a")
    head.place(x=110, y=20)

    l1 = Label(f, text="Name",font=("Times New Roman", 14, "bold"), bg="#c5dedd")
    l1.place(x=55, y=80)
    e1 = Entry(f, textvariable=add_name, width=17, font="Verdana 11")
    e1.place(x=130, y=80)
    e1.delete(0, END)

    l2 = Label(f, text="Phone", font=("Times New Roman", 14, "bold"), bg="#c5dedd")
    l2.place(x=55, y=125)
    e2 = Entry(f, textvariable=add_phone, width=17, font="Verdana 11")
    e2.place(x=130, y=125)
    e2.delete(0, END)

    l3 = Label(f, text="Email", font=("Times New Roman", 14, "bold"), bg="#c5dedd")
    l3.place(x=55, y=170)
    e3 = Entry(f, textvariable=add_email, width=17, font="Verdana 11")
    e3.place(x=130, y=170)
    e3.delete(0, END)
    e1.insert(0, (values[1]))
    e2.insert(0, (values[2]))
    e3.insert(0, (values[3]))

    def update_data():
        nonlocal e1, e2, e3, curItem, values
        try:
            e1 = add_name.get()
            e2 = add_phone.get()
            e3 = add_email.get()
            tree.item(curItem, values=(values[0], e1, e2, e3))
            print("Admin id",values[0])
            mycur.execute("UPDATE admin SET ad_name=%s, ad_phn=%s, ad_email=%s WHERE ad_id=%s",
                          (e1, e2, e3, values[0]))
            db.commit()
        except Exception as e:
            print(e)
            db.rollback()
        mb.showinfo("Success", "Admin data Updated")
        f.destroy()

    cancelbutton = tk.Button(f, text="CANCEL",font=("Times New Roman", 12, "bold"), bg="#50aba5", width=8,
                             command=f.destroy)
    cancelbutton.place(x=100, y=230)
    savebutton = tk.Button(f, text="SAVE",font=("Times New Roman", 12, "bold"), bg="#50aba5", width=8,
                            command=update_data)
    savebutton.place(x=200, y=230)






root.mainloop()