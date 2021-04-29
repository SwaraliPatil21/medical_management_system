from tkinter import *
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.messagebox import showinfo
from tkinter.messagebox import *
import MySQLdb

#connecting_to_the_database
db = MySQLdb.connect(host="localhost",user="root",passwd="",database="medical")
mycur = db.cursor()

root = Tk()
root.title('View Medicine List')
root.geometry('{}x{}+200+100'.format(1000, 500))

#frames
frame_top = Frame(root, width=800, height=50, bg="#285e5a")

frame_left = Frame(root, width=240, height=420, bg="#285e5a")
frame_left.grid_propagate(False)

frame_right = Frame(root, width=740, height=420, bg="#c9d6d5")

# click event handler
def confirm():
    answer = askyesno(title='confirmation',
                    message='Are you sure that you want to logout?')
    if answer:
        root.destroy()

#Top_Admin name label
admin_name = Label(frame_top, text="Admin name", font=("Times New Roman", 13, "bold"), bg="#50aba5")
admin_name.place(x=23, y=14, height=25, width=190)

#Top_log out button
log_out = Button(frame_top, text=" Log Out ", bg="#50aba5", command=confirm)
#log_out.grid(row=0, column=3, pady=7, padx=15)
log_out.place(x=860,y=14,height=25,width=100)

#-------------------------------------------------------------------------------------------------------------

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

#--------------------------------------------------------------------------------------------------------------------

#Right_frame
#grid
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)

frame_top.grid(row=0,sticky="ew")
frame_left.grid(row=1,sticky="w")
frame_right.grid(row=1,sticky="e")
frame_right.grid_propagate(False)

#label for medicine list
med_list = Label(frame_right, text=" Medicine List ", font=("Times New Roman", 22, "bold"), fg="White", bg="#285e5a")
med_list.place(x=28, y=30, height=38, width=250)

#Search-button
global med_verify
med_verify = StringVar()
Label(frame_right, text="Search :", font=("Times New Roman", 19, "bold"),bg = "#c9d6d5" ).place(x=400, y=70)
Entry(frame_right, textvariable=med_verify, font="Verdana 13").place(x=500, y=75, height=26, width=200)

# columns
columns = ('#1', '#2', '#3', '#4' ,'#5')

tree = ttk.Treeview(frame_right, selectmode="extended", columns=columns, show='headings')
style = ttk.Style()
style.theme_use("clam") #can also give default
style.configure("Treeview.Heading", font=('Verdana',12,"bold"), background ="#50aba5",foreground="Black")
style.configure('Treeview.Heading', rowheight=25)
style.configure(".", font=('Helvetica', 11), foreground="Black")
style.configure('.', rowheight=25)

# define headings and column length
tree.heading('#1', text='Medicine Name', anchor=W)
tree.column('#1', minwidth=50, width=160, stretch=0)

tree.heading('#2', text='Company Name', anchor=W)
tree.column('#2', minwidth=100, width=230, stretch=0)

tree.heading('#3', text='Unit Price', anchor=W)
tree.column('#3', minwidth=70, width=100, stretch=0)

tree.heading('#4', text='Quantity', anchor=W)
tree.column('#4', minwidth=100, width=95, stretch=0)

tree.heading('#5', text='Action', anchor=W)
tree.column('#5', minwidth=100, width=90, stretch=0)

# add Sql data to treeview
mycur.execute("SELECT med_name,med_comp,med_price,SUM(curr_qty) FROM `med_details` as A LEFT join med_batch_details as B ON A.med_id = B.med_id GROUP by med_name,med_comp,med_price")
fetch = mycur.fetchall()
for data in fetch:
    tree.insert('', 'end', values=(data[0], data[1], data[2] , data[3]))

# bind the select event
def item_selected(event):
    for selected_item in tree.selection():
        # dictionary
        item = tree.item(selected_item)
        # list
        record = item['values']
        #
        showinfo(title='Information',
                message=', '.join(map(str, record)))

#to stop column movement
def handle_click(event):
    if tree.identify_region(event.x, event.y) == "separator":
        return "break"
tree.bind('<Button-1>', handle_click)


tree.bind('<<TreeviewSelect>>', item_selected)

tree.grid(padx=20, pady=120)

# add a scrollbar
scrollbar = ttk.Scrollbar(frame_right, orient=tk.VERTICAL, command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.grid(row=0, column=1, sticky='ns', pady=120)

frame_right.grid_rowconfigure(1, weight=1)
frame_right.grid_columnconfigure(0, weight=1)

root.mainloop()