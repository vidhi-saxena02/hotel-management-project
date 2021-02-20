from tkinter import *
import sqlite3
import tkinter.messagebox as message
###----------------------------background-----------------------------------------------##
from webbrowser import get

BLUE = "#487e95"
ETON = "#9ECE9A"
MELON ="#FFB49A"
Purple = "#A16AE8"
Neptune = "#71A3BA"
San = "#3C64B8"
Clam = "#D0ABA9"
Thunder = "#33202E"
Edward = "#A6A8A8"
Grey = "#95979D"
Grey_1 = "#CFCDCB"
Brown="#534A43"
Orange="#DC5631"
Cold_Turkey="#CFB8B4"
Irish_Coffee="#5E2A23"
Dusty_Gray="#AE9AA6"
Casper="#A8BBCB"
Sisal="#D0C5B9"
Copper="#BC793B"
Bright_Gray="#35374D"
Pewter="#B9B7BD"
Burgundy="#4D0011"
Maroon="#914955"
Blue_Gray="#ADB3BC"
Misty_Blue="#2F5061"
Dark_Blue="#071330"
# from PIL import ImageTK,Image

root = Tk()
root.config(bg=BLUE)
back_img = PhotoImage(file="Bay.png")
# root.config(padx=50,pady=50)
# my_img=ImageTK.PhotoImage(Image.open(r"C:\Users\aseem\Desktop\image.png"))
# img=Label(image=my_image)
# img.grid(row=0,column=1)
canvas = Canvas(width=1000,height=1000, bg = BLUE,highlightthickness=0)
canvas.create_image(500, 500, image=back_img)
canvas_id = canvas.create_text(100, 10, anchor="nw")
canvas.itemconfig(canvas_id, text="Welcome to Hotel Management System ", width=900, fill = Clam, font=("courier", 30, "underline"))
canvas_id1 = canvas.create_text(300, 70, anchor="nw")
canvas.itemconfig(canvas_id1, text=" Hotel Marina", width=900, fill = "Purple", font=("Bodoni MT", 56, "bold","underline"))



# myLabel = Label(root, text="Welcome to Hotel Management System",bg=BLUE, font=("Algerian", 40, "bold", "underline"), fg="black")
# myLabel1 = Label(root,bg=BLUE, text="Hotel RENAISSANCE", font=("Castellar", 32), fg=MELON)
# canvas.create_text(252,205,text="Hotel DALLAS")
canvas.grid(row=2,column=0,columnspan=3,rowspan=3)
# myLabel.grid(row=0, column=0, columnspan=3)
# myLabel1.grid(row=1, column=1)


conn = sqlite3.connect('Staff_details.db')
c = conn.cursor()

try:
    c.execute(""" CREATE TABLE ADD_STAFF(
			Staff_name text,
			name text,
			age integer,
			gender text,
			mob text,
			adharno integer,
			address varchar,
			salary integer,
			post text
			)""")
except:
    pass

try:
    c.execute(""" CREATE TABLE ADD_CUSTOMER(
    			Room_no text,
    			Customer_name text,
    			age integer,
    			gender text,
    			mob text,
    			adharno integer,
    			address varchar
    			)""")
except:
    pass




def query():
    conn = sqlite3.connect('Staff_details.db')
    c = conn.cursor()

    c.execute("SELECT *, oid FROM ADD_STAFF")
    records = c.fetchall()
    print(records)

    print_records = ''
    for record in records:
        print_records += str(record) + "\n"

    query_label = Label(click6.top6, text=print_records)
    query_label.grid(row=2, column=0,columnspan=3)

    conn.commit()
    conn.close()

def delete():
    conn = sqlite3.connect('Staff_details.db')
    c = conn.cursor()

    c.execute(f"DELETE from ADD_STAFF WHERE Staff_name= {click7.dlte.get()}")

    click7.dlte.delete(0,END)

    conn.commit()
    conn.close()

def click():
    top = Toplevel()
    bac_img = PhotoImage(file="lobby.png")
    # top.config(padx=100,pady=100)
    # my_img=ImageTK.PhotoImage(Image.open(r"C:\Users\aseem\Desktop\image.png"))
    # img=Label(image=my_image)
    # img.grid(row=0,column=1)
    canvas1= Canvas(top,width=1000, height=1000, bg=BLUE, highlightthickness=0)
    canvas1.create_image(500, 500, image=bac_img)
    Add_Details = Button(top, text="1.Add Staff Details", padx=50,pady=10,bg=Edward,command=click2)
    canvas1.create_window(500, 400, window=Add_Details)
    canvas1.grid(row=0, column=1)
    View = Button(top, text="2.View All Staff Details",padx=50,pady=10,bg=Grey,command=click6)
    canvas1.create_window(500, 500, window=View)
    canvas1.grid(row=0, column=1)
    Delete = Button(top, text="3.Delete Staff Details",padx=50,pady=10,bg=Grey_1,command=click7)
    canvas1.create_window(500, 600, window=Delete)
    canvas1.grid(row=0, column=1)
    main = Button(top, text="4.Exit",padx=50,pady=10,bg=Brown,command = top.quit)
    canvas1.create_window(500, 700, window=main)
    canvas1.grid(row=0, column=1)
    top.mainloop()




def click2():
    top2 = Toplevel()
    top2.title("Add Details")
    top2.config(bg=Clam)

    Staff_name = Entry(top2, width=30)
    Staff_name.grid(row=0, column=3, padx=20)
    click2.staff = Staff_name

    name = Entry(top2, width=30)
    name.grid(row=1, column=3, padx=20)
    click2.name = name
    age = Entry(top2, width=30)
    age.grid(row=2, column=3, padx=20)
    click2.age = age
    gender = Entry(top2, width=30)
    gender.grid(row=3, column=3, padx=20)
    click2.gender = gender
    mob = Entry(top2, width=30)
    mob.grid(row=4, column=3, padx=20)
    click2.mob = mob
    adharno = Entry(top2, width=30)
    adharno.grid(row=5, column=3, padx=20)
    click2.adhar = adharno
    address = Entry(top2, width=30)
    address.grid(row=6, column=3, padx=20)
    click2.address = address
    salary = Entry(top2, width=30)
    salary.grid(row=7, column=3, padx=20)
    click2.salary = salary
    post = Entry(top2, width=30)
    post.grid(row=8, column=3, padx=20)
    click2.post = post
    Staff_name_lab = Label(top2, text="Staff_ID")
    Staff_name_lab.grid(row=0, column=0)

    name_lab = Label(top2, text="Name")
    name_lab.grid(row=1, column=0)

    age_lab = Label(top2, text="Age")
    age_lab.grid(row=2, column=0)

    gender_lab = Label(top2, text="Gender")
    gender_lab.grid(row=3, column=0)

    mob_lab = Label(top2, text="Mobile Number")
    mob_lab.grid(row=4, column=0)

    adharno_lab = Label(top2, text="Adhar Number")
    adharno_lab.grid(row=5, column=0)

    address_lab = Label(top2, text="Address")
    address_lab.grid(row=6, column=0)

    salary_lab = Label(top2, text="Salary")
    salary_lab.grid(row=7, column=0)

    post_lab = Label(top2, text="Post")
    post_lab.grid(row=8, column=0)

    submit_btn = Button(top2, text="Add Details", command=submit)
    submit_btn.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=100, )
    top2.mainloop()


def submit():
    conn = sqlite3.connect('Staff_details.db')
    c = conn.cursor()

    c.execute(
        "INSERT INTO ADD_STAFF VALUES (:Staff_name, :name, :age, :gender, :mob, :adharno, :address, :salary, :post)",
        {
            'Staff_name': click2.staff.get(),
            'name': click2.name.get(),
            'age': click2.age.get(),
            'gender': click2.gender.get(),
            'mob': click2.mob.get(),
            'adharno': click2.adhar.get(),
            'address': click2.address.get(),
            'salary': click2.salary.get(),
            'post': click2.post.get()
        })
    conn.commit()
    conn.close()

    click2.staff.delete(0, END)
    click2.name.delete(0, END)
    click2.age.delete(0, END)
    click2.gender.delete(0, END)
    click2.mob.delete(0, END)
    click2.adhar.delete(0, END)
    click2.address.delete(0, END)
    click2.salary.delete(0, END)
    click2.post.delete(0, END)


def click1():
    top1 = Toplevel()
    ba_img = PhotoImage(file="room.png")
    # top.config(padx=100,pady=100)
    # my_img=ImageTK.PhotoImage(Image.open(r"C:\Users\aseem\Desktop\image.png"))
    # img=Label(image=my_image)
    # img.grid(row=0,column=1)
    canvas5 = Canvas(top1, width=1000, height=1000, bg=BLUE, highlightthickness=0)
    canvas5.create_image(500, 500, image=ba_img)
    canvas5.grid(row=1,column=0)
    Add_Details = Button(top1, text="1.Add Customer Details",padx=50,pady=10,bg=Orange,fg="White", command=click3)
    canvas5.create_window(500, 400, window=Add_Details)
    View = Button(top1, text="2.View All Customer Details",padx=50,pady=10,bg=Cold_Turkey, command=click11)
    canvas5.create_window(500, 500, window=View)
    Delete = Button(top1, text="3.Delete Customer Details",padx=50,pady=10,bg=Irish_Coffee,fg="White",command=click12)
    canvas5.create_window(500, 600, window=Delete)
    main = Button(top1, text="4.Exit",padx=50,pady=10,bg=Dusty_Gray,command=top1.quit)
    canvas5.create_window(500, 700, window=main)
    top1.mainloop()




def click3():
    top3 = Toplevel()
    top3.title("Add Details")
    top3.config(bg=Casper)

    Room_no = Entry(top3, width=30)
    Room_no.grid(row=0, column=3, padx=20)
    click3.room = Room_no

    Customer_name = Entry(top3, width=30)
    Customer_name.grid(row=1, column=3, padx=20)
    click3.Customer = Customer_name

    age = Entry(top3, width=30)
    age.grid(row=2, column=3, padx=20)
    click3.age = age

    gender = Entry(top3, width=30)
    gender.grid(row=3, column=3, padx=20)
    click3.gender = gender

    mob = Entry(top3, width=30)
    mob.grid(row=4, column=3, padx=20)
    click3.mob = mob

    adharno = Entry(top3, width=30)
    adharno.grid(row=5, column=3, padx=20)
    click3.adhar = adharno

    address = Entry(top3, width=30)
    address.grid(row=6, column=3, padx=20)
    click3.address = address

    room_lab = Label(top3, text="Room.No")
    room_lab.grid(row=0, column=0)

    name_lab = Label(top3, text="Customer Name")
    name_lab.grid(row=1, column=0)

    age_lab = Label(top3, text="Age")
    age_lab.grid(row=2, column=0)

    gender_lab = Label(top3, text="Gender")
    gender_lab.grid(row=3, column=0)

    mob_lab = Label(top3, text="Mobile Number")
    mob_lab.grid(row=4, column=0)

    adharno_lab = Label(top3, text="Adhar Number")
    adharno_lab.grid(row=5, column=0)

    address_lab = Label(top3, text="Address")
    address_lab.grid(row=6, column=0)

    submit_btn1 = Button(top3, text="Add Details", command=Add)
    submit_btn1.grid(row=8, column=2, columnspan=2, pady=10, padx=10, ipadx=100,)


def click4():
    top4 = Toplevel()
    img = PhotoImage(file="finc.png")
    # top.config(padx=100,pady=100)
    # my_img=ImageTK.PhotoImage(Image.open(r"C:\Users\aseem\Desktop\image.png"))
    # img=Label(image=my_image)
    # img.grid(row=0,column=1)
    canvas6 = Canvas(top4, width=1000, height=1000, bg=BLUE, highlightthickness=0)
    canvas6.create_image(500, 500, image=img)
    canvas6.grid(row=1, column=0)
    canvas6.create_text(100, 50,text=" Welcome to the Financial Department", width=900, fill=Casper,font=("FZShuTi", 36, "bold", "underline"),anchor="nw")
    canvas6.create_text(200, 150, text=" Find The Profit OR Loss", width=900, fill=Sisal,font=("Castellar", 30, "bold", "underline"), anchor="nw")

    month = Entry(top4, width=30)
    canvas6.create_window(500, 400, window=month)

    result=Label(top4,width=30)
    canvas6.create_window(500, 500, window=result)

    month_lab = Label(top4, text="Enter Month", font=("Franklin Gothic Heavy",20,"italic"))
    canvas6.create_window(300, 400, window=month_lab)

    result_lab = Label(top4, text="Result", font=("Franklin Gothic Heavy",20,"italic"))
    canvas6.create_window(300, 500, window=result_lab)
    def finc():
        x = ["January", "July", "March", "September", "May", "November"]
        y = ["February", "April", "June", "August", "October", "December"]
        if month.get() in x:
            result.config(text="Profit")
        else:
            result.config(text="Loss")



    button = Button(top4, text="Find Result", padx=50,pady=10,bg=Irish_Coffee,fg="White",command=finc)
    canvas6.create_window(500, 600, window=button)
    top4.mainloop()







def click6():
    top6 = Toplevel()
    top6.title("View")
    top6.config(bg=Pewter)
    click6.top6 = top6
    Heading = Label(top6, text="View All Staff Details", font=("Algerian", 32, "bold", "underline"), fg=Burgundy)
    Heading.grid(row=0, column=0,columnspan=3)
    Show = Button(top6, text="Show All Records", command=query)
    Show.grid(row=1, column=1)
    top6.mainloop()

def click7():
    top7 = Toplevel()
    top7.title("Delete Staff")
    top7.config(bg=Maroon)
    click7.top7 = top7
    Heading4 = Label(top7, text="Delete Staff Details",font=("Perpetua Titling MT", 32, "bold", "underline"),fg="Black")
    Heading4.grid(row=1, column=0, columnspan=3)
    dlt = Entry(top7,width=30)
    dlt.grid(row=4, column=2)
    click7.dlte = dlt
    dlt_label = Label(top7, text="Enter the Staff_Id",font=("FZShuTi", 20, "bold", "underline"))
    dlt_label.grid(row=4,column=1)
    Remove = Button(top7, text="Delete the record",padx=50,pady=10, command= delete)
    Remove.grid(row=7, column=2)

def update():
    conn = sqlite3.connect('Staff_details.db')
    c = conn.cursor()

    c.execute("""UPDATE ADD_STAFF SET
        Staff_name = :staff,
        name = :name,
        age = :age,
        gender = :gender,
        mob = :mob,
        adharno = :adharno,
        address = :address,
        salary = :salary,
        post = :post,

        WHERE oid = :oid""",
        {
        'Staff_name': click2.staff.get(),
        'name': click2.name.get(),
        'age': click2.age.get(),
        'gender': click2.gender.get(),
        'mob': click2.mob.get(),
        'adharno': click2.adhar.get(),
        'address': click2.address.get(),
        'salary': click2.salary.get(),
        'post': click2.post.get(),

        'Staff_name': click8.updt.get()
        })


    conn.commit()
    conn.close()


def update8():
    conn = sqlite3.connect('Staff_details.db')
    c = conn.cursor()

    c.execute("""UPDATE ADD_STAFF SET
            Staff_name = :staff,
            name = :name,
            age = :age,
            gender = :gender,
            mob = :mob,
            adharno = :adharno,
            address = :address,
            salary = :salary,
            post = :post,

            WHERE oid = :oid""",
              {
                  'Staff_name': click8.staff.get(),
                  'name': click8.name.get(),
                  'age': click8.age.get(),
                  'gender': click8.gender.get(),
                  'mob': click8.mob.get(),
                  'adharno': click8.adharno.get(),
                  'address': click8.address.get(),
                  'salary': click8.salary.get(),
                  'post': click8.post.get(),

                  'Staff_name': click8.updt.get()
              })

    conn.commit()
    conn.close()

    click8.top8.destroy()

    click8.staff.delete(0, END)
    click8.name.delete(0, END)
    click8.age.delete(0, END)
    click8.gender.delete(0, END)
    click8.mob.delete(0, END)
    click8.adhar.delete(0, END)
    click8.address.delete(0, END)
    click8.salary.delete(0, END)
    click8.post.delete(0, END)




def click8():
    top8 = Toplevel()
    click8.top8 = top8


    updt = Entry(top8, width=30)
    updt.grid(row=1, column=0)
    click8.updt = updt



    Heading8 = Label(top8, text="Update Staff Details")
    Heading8.grid(row=0, column=0, columnspan=3)

    Staff_name_ed = Entry(top8, width=30)
    Staff_name_ed.grid(row=2, column=3, padx=20)
    click8.staff= Staff_name_ed

    name_ed = Entry(top8, width=30)
    name_ed.grid(row=3, column=3, padx=20)
    click8.name= name_ed

    age_ed = Entry(top8, width=30)
    age_ed.grid(row=4, column=3, padx=20)
    click8.age= age_ed


    gender_ed = Entry(top8, width=30)
    gender_ed.grid(row=5, column=3, padx=20)
    click8.gender= gender_ed

    mob_ed = Entry(top8, width=30)
    mob_ed.grid(row=6, column=3, padx=20)
    click8.mob= mob_ed

    adharno_ed = Entry(top8, width=30)
    adharno_ed.grid(row=7, column=3, padx=20)
    click8.adharno= adharno_ed

    address_ed = Entry(top8, width=30)
    address_ed.grid(row=8, column=3, padx=20)
    click8.address= address_ed
    salary_ed = Entry(top8, width=30)
    salary_ed.grid(row=9, column=3, padx=20)
    click8.salary= salary_ed
    post_ed = Entry(top8, width=30)
    post_ed.grid(row=10, column=3, padx=20)
    click8.post= post_ed

    Staff_name_lab = Label(top8, text="Staff_ID")
    Staff_name_lab.grid(row=2, column=1)

    name_lab = Label(top8, text="Name")
    name_lab.grid(row=3, column=1)

    age_lab = Label(top8, text="Age")
    age_lab.grid(row=4, column=1)

    gender_lab = Label(top8, text="Gender")
    gender_lab.grid(row=5, column=1)

    mob_lab = Label(top8, text="Mobile Number")
    mob_lab.grid(row=6, column=1)

    adharno_lab = Label(top8, text="Adhar Number")
    adharno_lab.grid(row=7, column=1)

    address_lab = Label(top8, text="Address")
    address_lab.grid(row=8, column=1)

    salary_lab = Label(top8, text="Salary")
    salary_lab.grid(row=9, column=1)

    post_lab = Label(top8, text="Post")
    post_lab.grid(row=10, column=1)


    upd_label = Label(top8, text="Enter the Staff_Id")
    upd_label.grid(row=1, column=1)

    upd = Button(top8, text="Search Record", command=search)
    upd.grid(row=11, column=1)

    edit = Button(top8, text="Edit Record", command=update8)
    edit.grid(row=12, column=1)


    top8.mainloop()

def search():
    conn = sqlite3.connect('Staff_details.db')
    c = conn.cursor()
    r = click8.updt.get()
    c.execute(f"SELECT * from ADD_STAFF WHERE Staff_name = {r}")
    records = c.fetchall()
    print(records)


    list1=[]
    for record in records:
        for i in range(len(record)):
            list1.append(record[i])


        click8.staff.insert(0, list1[0])
        click8.name.insert(0, list1[1])
        click8.age.insert(0, list1[2])
        click8.gender.insert(0, list1[3])
        click8.mob.insert(0, list1[4])
        click8. adharno.insert(0, list1[5])
        click8.address.insert(0, list1[6])
        click8. salary.insert(0, list1[7])
        click8.post.insert(0, list1[8])



def Add():
    conn = sqlite3.connect('Staff_details.db')
    c= conn.cursor()

    c.execute(
        "INSERT INTO ADD_CUSTOMER VALUES (:Room_no, :Customer_name, :age, :gender, :mob, :adharno, :address)",
        {
            'Room_no': click3.room.get(),
            'Customer_name': click3.Customer.get(),
            'age': click3.age.get(),
            'gender': click3.gender.get(),
            'mob': click3.mob.get(),
            'adharno': click3.adhar.get(),
            'address': click3.address.get(),
        })
    conn.commit()
    conn.close()

    click3.room.delete(0, END)
    click3.Customer.delete(0, END)
    click3.age.delete(0, END)
    click3.gender.delete(0, END)
    click3.mob.delete(0, END)
    click3.adhar.delete(0, END)
    click3.address.delete(0, END)


def click11():
    top11 = Toplevel()
    top11.title("View")
    top11.config(bg=Blue_Gray)
    click11.top11 = top11
    Heading = Label(top11, text="View All Customer Details", font=("Algerian", 32, "bold", "underline"), fg=Misty_Blue)
    Heading.grid(row=0, column=0,columnspan=3)
    Show = Button(top11, text="Show All Records", padx=50,pady=10,bg=Maroon,fg="White",command=query1)
    Show.grid(row=1, column=1)

def query1():
    conn = sqlite3.connect('Staff_details.db')
    c = conn.cursor()

    c.execute("SELECT *, oid FROM ADD_CUSTOMER")
    records = c.fetchall()
    print(records)

    print_records = ''
    for record in records:
        print_records += str(record) + "\n"

    query_label = Label(click11.top11, text=print_records)
    query_label.grid(row=2, column=0,columnspan=3)

    conn.commit()
    conn.close()

def click12():
    top12 = Toplevel()
    top12.title("Delete")
    top12.config(bg=Dark_Blue)
    click12.top12 = top12
    Heading4 = Label(top12, text="Delete Customer Details",font=("Tw Cen MT Condensed Extra Bold", 32, "bold", "underline"),fg="Black")
    Heading4.grid(row=0, column=0, columnspan=3)
    dlt = Entry(top12,width=30)
    dlt.grid(row=3, column=2)
    click12.dlte = dlt
    dlt_label = Label(top12, text="Enter the Room Number",font=("Comic Sans MS", 12, "italic"), fg=Misty_Blue)
    dlt_label.grid(row=3,column=1)
    Remove = Button(top12, text="Delete the record",padx=30,pady=10,bg=Clam,command= delete_1)
    Remove.grid(row=7, column=2)
    top12.mainloop()


def delete_1():
    conn = sqlite3.connect('Staff_details.db')
    c = conn.cursor()

    c.execute(f"DELETE from ADD_CUSTOMER WHERE Room_no= {click12.dlte.get()}")

    click12.dlte.delete(0, END)

    conn.commit()
    conn.close()




def click13():
    top13=Toplevel()
    ba_img = PhotoImage(file="rename.png")
    # top.config(padx=100,pady=100)
    # my_img=ImageTK.PhotoImage(Image.open(r"C:\Users\aseem\Desktop\image.png"))
    # img=Label(image=my_image)
    # img.grid(row=0,column=1)
    canvas3 = Canvas(top13, width=500, height=500, bg=BLUE, highlightthickness=0)
    canvas3.create_image(250, 250, image=ba_img)
    canvas3.grid(row=0, column=1,rowspan=16)

    var1 = IntVar()
    var2 = IntVar()
    var3 = IntVar()
    var4 = IntVar()
    var5 = IntVar()
    var6 = IntVar()
    var7 = IntVar()
    var8 = IntVar()
    var9 = IntVar()
    var10 = IntVar()
    var11 = IntVar()
    var12= IntVar()
    var13= IntVar()
    var14= IntVar()
    var15= IntVar()



    li=[var1,var2,var3,var4,var5,var6,var7,var8,var9,var10,var11,var12,var13,var14,var15]

    kab=Label(top13, text="What would you like to order?", font=("Edwardian Script ITC",32, "bold","underline"),fg=BLUE)
    kab.grid(row=0, column=0)
    menu = {
        'Paella Valenciana':1,
        "Bistro Salad":2,
        "Lasanga":3,
        'Ddukbokki':4,
        'Sushi':5,
        'Hotpot':6,
        'Irish Stew':7,
        'Kabuli Palaw':8,
        'Saimin':10,
        'Pierogi':11,
        'Khuzi':12,
        'Fish Curry':13,
        'Butter Chicken':14,
        'Gatsby':15


    }


    i=0
    for item,val in menu.items():

        Radiobutton(top13,text=item,value = val,variable=li[i]).grid(row=i+1,column=0)
        i+=1

    def order():
        final = []
        ans = ""
        for food,value in menu.items():
            for q in li:
                if q.get() == value:
                    final.append(food)
        for items in final:
            ans += f"{items},"
        message.showinfo("Order Recieved", f"We have received your order for {ans}. Thanks for ordering!")

    #     bill = {item:value for item,value in menu.}
    #     # message.showinfo("Order Recieved", f"We have received your order for {click13.var.get()}. Thanks for ordering!")
    mybutton = Button(top13, text="Place Order", command= order)
    mybutton.grid(row=16, column=0)
    top13.mainloop()

def click14():
    top14 = Toplevel()
    img1 = PhotoImage(file="kiri.png")
    # top.config(padx=100,pady=100)
    # my_img=ImageTK.PhotoImage(Image.open(r"C:\Users\aseem\Desktop\image.png"))
    # img=Label(image=my_image)
    # img.grid(row=0,column=1)
    canvas7 = Canvas(top14, width=600, height=600, bg=BLUE, highlightthickness=0)
    canvas7.create_image(300, 300, image=img1)
    canvas7.grid(row=0, column=1, rowspan=10)
    lab = Label(top14, text="Choose Your Requirements", font=("STKaiti", 32, "bold", "underline"),fg=Copper)
    lab.grid(row=0, column=0)

    radio_var = IntVar()
    r1 = IntVar()
    r2 = IntVar()
    r3 = IntVar()
    r6 = IntVar()
    r7 = IntVar()
    r8 = IntVar()
    r4 = IntVar()
    r5 = IntVar()



    radio = Radiobutton(top14,text="Shirt", variable = radio_var, value=1)
    radio1 = Radiobutton(top14, text="Pant", variable= r1, value=2)
    radio2 = Radiobutton(top14, text="Coat", variable=r2, value=3)
    radio3 = Radiobutton(top14, text="Jacket", variable=r3, value=4)
    radio4 = Radiobutton(top14, text="Jeans", variable=r4, value=5)
    radio5 = Radiobutton(top14, text="Sweater", variable=r5, value=6)
    radio6 = Radiobutton(top14, text="Dry Clean", variable=r6, value=7)
    radio7 = Radiobutton(top14, text="Steam-Pressing", variable=r7, value=8)
    radio8 = Radiobutton(top14, text="Wash", variable=r8, value=9)
    radio.grid(row=1, column=0)
    radio1.grid(row=2, column=0)
    radio2.grid(row=3, column=0)
    radio3.grid(row=4, column=0)
    radio4.grid(row=5, column=0)
    radio5.grid(row=6, column=0)
    radio6.grid(row=7, column=0)
    radio7.grid(row=8, column=0)
    radio8.grid(row=9, column=0)
    print(radio_var.get())
    def test():

        price = 0
        if radio_var.get() == 1:
            price+= 50
        if r1.get()==2:
            price+= 50
        if r2.get()==3:
            price+= 100
        if r3.get()==4:
            price+= 100
        if r4.get()==5:
            price+= 75
        if r5.get()==6:
            price+= 100
        if r6.get()==7:
            price+= 40
        if r7.get()==8:
            price+= 30
        if r8.get()==9:
            price+= 30
        message.showinfo(message=f"The Total Amount to be paid is {price}")


    button = Button(top14,text="Total Amount",padx=50,pady=10,bg=Bright_Gray,fg="White",command=test)
    button.grid(row=10,column=0)

    top14.mainloop()




staff_detail_button = Button(root, text="1.Staff Detail", command=click, highlightthickness=0, padx=50,pady=10,bg=Neptune,relief=FLAT)
customer_detail_button = Button(root, text="2.Customer Detail", command=click1, highlightthickness=0,padx=50,pady=10, bg=San, relief=FLAT)
finance_dep_button = Button(root, text="3.Finance Department", command=click4, highlightthickness=0,padx=50,pady=10, bg=Clam, relief=FLAT)
laundary_dep_button = Button(root, text="4.Laundary Department",command= click14, highlightthickness=0,padx=50,pady=10,bg=Neptune, relief=FLAT)




hotel_dep_button = Button(root, text="5.Hotel Resturant Department",command =click13, highlightthickness=0,padx=50,pady=10,bg=San, relief=FLAT)
exit_button = Button(root, text="6.Exit",highlightthickness=0, command = root.quit,padx=50,pady=10, bg=Clam, relief=FLAT)
canvas.create_window(500,400,window=staff_detail_button)
canvas.create_window(500,500,window=customer_detail_button)
canvas.create_window(500,600,window=finance_dep_button)
canvas.create_window(500,700,window=laundary_dep_button)
canvas.create_window(500,800,window=hotel_dep_button)
canvas.create_window(500,900,window=exit_button)

conn.commit()
conn.close()
root.mainloop()
