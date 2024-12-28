from tkinter import *
from tkinter import ttk
from db import DataBase
from tkinter import messagebox


db = DataBase("QADESIA.db")




root = Tk()
root.title('QADESIA')
root.geometry('1590x800+0+0')
root.resizable(True,True)
root.configure(bg='#2c3e50')

name = StringVar()
age = StringVar()
cat = StringVar()
nots = StringVar()
#tarekh = StringVar()
#baqi = StringVar()
#me3ad= StringVar()

#logo = PhotoImage(file='')
#lbl_logo = Label(root,image=logo,bg='#2c3e50')
#lbl_logo.place(x=80,y=520)



# =================| Entries Frame |=======================

entries_frame = Frame(root, bg='#2c3e50')
entries_frame.place(x=1,y=1,width=360,height=510)
Title = Label(entries_frame,text='QADESIA',font=('Calibri',18,'bold'),bg='#2c3e50',fg='white')
Title.place(x=20,y=15)

lblPersonName = Label(entries_frame,text='الاسم',font=('Calibri',16),bg='#2c3e50',fg='white')
lblPersonName.place(x=20,y=90)
txtPersonName = Entry(entries_frame,textvariable=name,width=30,font=('Calibri',16)) 
txtPersonName.place(x=120,y=90)

lblProAge = Label(entries_frame,text='مواليد',font=('Calibri',16),bg='#2c3e50',fg='white')
lblProAge.place(x=20,y=150)
txtProAge = Entry(entries_frame,textvariable=age,width=30,font=('Calibri',16)) 
txtProAge.place(x=120,y=150)

lblProCat= Label(entries_frame,text='الصفه',font=('Calibri',16),bg='#2c3e50',fg='white')
lblProCat.place(x=20,y=210)
txtProCat= Entry(entries_frame,textvariable=cat,width=30,font=('Calibri',16)) 
txtProCat.place(x=120,y=210)

lblNots = Label(entries_frame,text='ملاحظات',font=('Calibri',16),bg='#2c3e50',fg='white')
lblNots.place(x=20,y=270)
txtNots = Entry(entries_frame,textvariable=nots,width=30,font=('Calibri',16)) 
txtNots.place(x=120,y=270)

#lblTarekh = Label(entries_frame,text='بتاريخ',font=('Calibri',16),bg='#2c3e50',fg='white')
#lblTarekh.place(x=10,y=210)
#txtTarekh = Entry(entries_frame,textvariable=tarekh,width=20,font=('Calibri',16)) 
#txtTarekh.place(x=120,y=210)

#lblBaqi = Label(entries_frame,text='الباقى',font=('Calibri',16),bg='#2c3e50',fg='white')
#lblBaqi.place(x=10,y=250)
#txtBaqi = Entry(entries_frame,textvariable=baqi,width=20,font=('Calibri',16)) 
#txtBaqi.place(x=120,y=250)

#lblMe3ad = Label(entries_frame,text='ميعاد التسليم',font=('Calibri',16),bg='#2c3e50',fg='white')
#lblMe3ad.place(x=10,y=290)
#txtMe3ad = Entry(entries_frame,textvariable=me3ad,width=20,font=('Calibri',16)) 
#txtMe3ad.place(x=120,y=290)

# =================| Defines |=============================

def hide():
    root.geometry("360x510")

def show():
    root.geometry('1590x800+0+0')
    

btnHide = Button(entries_frame,text='اخفاء',bg='white',bd=1,relief=SOLID,cursor='hand2',command=hide)
btnHide.place(x=270,y=20)

btnShow = Button(entries_frame,text='اظهار',bg='white',bd=1,relief=SOLID,cursor='hand2',command=show)
btnShow.place(x=310,y=20)

def getData(event):
    selected_row = tv.focus()
    data = tv.item(selected_row)
    global row
    row = data["values"]
    name.set(row[1])
    age.set(row[2])
    cat.set(row[3])
    nots.set(row[4])
    #tarekh.set(row[5])
    #baqi.set(row[6])
    #me3ad.set(row[7])

def displayAll():
    tv.delete(*tv.get_children())
    for row in db.fetch():
        tv.insert("",END,values=row)



def delete():
    db.remove(row[0])
    clear()
    displayAll()
    

def clear():
    name.set("")
    age.set("")
    cat.set("")
    nots.set("")
    #tarekh.set("")
    #baqi.set("")
    #me3ad.set("")

def add_emoloyee():
    if txtPersonName.get() == "" or txtProAge.get() == "" or txtProCat.get() == "" or  txtNots.get() == "" :
        messagebox.showerror("Error","من فضلك قم بملىء كافة الحقول")
        return
    db.insert(
        txtPersonName.get(),
        txtProAge.get(),
        txtProCat.get(),
        txtNots.get())
        #txtTarekh.get(),
        #txtBaqi.get(),
        #txtMe3ad.get()
    #messagebox.showinfo("Success"," هل تريد اضافة خدمه جديده")
    clear()
    displayAll()

def update():
    if txtPersonName.get() == "" or txtProAge.get() == "" or txtProCat.get() == "" or  txtNots.get() == "" :
        messagebox.showerror("Error","من فضلك قم بملىء كافة الحقول")
        return
    db.update(row[0],
    txtPersonName.get(),
    txtProAge.get(),
    txtProCat.get(),
    txtNots.get())
   # txtTarekh.get(),
   # txtBaqi.get(),
   # txtMe3ad.get())
    #messagebox.showinfo("Success","هل تريد تعديل هذه الخدمه ؟")
    clear()
    displayAll()

# ============================| Buttons Frame |===========================================================

btn_frame = Frame(entries_frame,bg='#2c3e50',bd=1,relief=SOLID)
btn_frame.place(x=10,y=400,width=335,height=100)

btnAdd = Button(btn_frame,text='اضافة شخص',width=14,height=1,font=('Calibri',16),fg='white',bg='#16a085',bd=0,command=add_emoloyee).place(x=4,y=5)
btnUpdate = Button(btn_frame,text='تعديل شخص',width=14,height=1,font=('Calibri',16),fg='white',bg='#2980b9',bd=0,command=update).place(x=4,y=50)
btnDelete = Button(btn_frame,text='حذف شخص',width=14,height=1,font=('Calibri',16),fg='white',bg='#c0392b',bd=0,command=delete).place(x=170,y=5)
btnClear = Button(btn_frame,text='مسح الحقول',width=14,height=1,font=('Calibri',16),fg='white',bg='#f39c12',bd=0,command=clear).place(x=170,y=50)

# ============================| Table Frame |===========================================================

tree_Frame = Frame(root,bg='white')
tree_Frame.place(x=365,y=1,width=1230,height=795)
style = ttk.Style()
style.configure("mystyle.Treeview",font=('Calibri',13),rowheight=50)
style.configure("mystyle.Treeview.Heading",font=('Calibri',13))

tv = ttk.Treeview(tree_Frame,columns=(1,2,3,4,5),style="mystyle.Treeview")

tv.heading("1",text="مسلسل")
tv.column("1",width="60")

tv.heading("2",text="الاسم")
tv.column("2",width="120")

tv.heading("3",text="مواليد")
tv.column("3",width="120")

tv.heading("4",text="الصفه")
tv.column("4",width="60")

tv.heading("5",text="ملاحظات")
tv.column("5",width="60")

#tv.heading("6",text="بتاريخ")
#tv.column("6",width="90")

#tv.heading("7",text="الباقى")
#tv.column("7",width="60")

#tv.heading("8",text="ميعاد التسليم")
#tv.column("8",width="90")

tv['show'] = 'headings'

tv.bind("<ButtonRelease-1>",getData)

tv.place(x=1,y=1,height=794,width=1230)





displayAll()

root.mainloop()