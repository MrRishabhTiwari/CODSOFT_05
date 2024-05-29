from tkinter import *

root = Tk()
root.geometry('400x500')
root.config(bg = 'pink')
root.title('DataFlair-AddressBook')

contactlist = []

Name = StringVar()
Number = StringVar()
Email = StringVar()
Address = StringVar()

def Selected():
    return int(select.curselection()[0])

def AddContact():
    contactlist.append([Name.get(), Number.get(), Email.get(), Address.get()])
    Select_set()

def EDIT():
    contactlist[Selected()] = [Name.get(), Number.get(), Email.get(), Address.get()]
    Select_set()

def DELETE():
    del contactlist[Selected()]
    Select_set()

def VIEW():
    NAME, NUMBER, EMAIL, ADDRESS = contactlist[Selected()]
    Name.set(NAME)
    Number.set(NUMBER)
    Email.set(EMAIL)
    Address.set(ADDRESS)

def EXIT():
    root.destroy()

def RESET():
    Name.set('')
    Number.set('')
    Email.set('')
    Address.set('')

def Select_set() :
    contactlist.sort()
    select.delete(0,END)
    for name,phone,email,address in contactlist :
        select.insert (END, name)

frame = Frame(root)
frame.pack(side = BOTTOM)

scroll = Scrollbar(frame, orient=VERTICAL)
select = Listbox(frame, yscrollcommand=scroll.set, height=12,width=50)
scroll.config (command=select.yview)
scroll.pack(side=RIGHT, fill=Y)
select.pack(side=LEFT,  fill=BOTH, expand=1)

Label(root, text = "Name").place(x= 50, y= 50)
Entry(root, textvariable = Name,width=42).place(x= 100, y= 50)

Label(root, text = "Phone").place(x= 50, y= 100)
Entry(root, textvariable = Number,width=42).place(x= 100, y= 100)

Label(root, text = "Email").place(x= 50, y= 150)
Entry(root, textvariable = Email,width=42).place(x= 100, y= 150)

Label(root, text = "Address").place(x= 50, y= 200)
Entry(root, textvariable = Address,width=42).place(x= 100, y= 200)

Button(root, text="Add", command = AddContact).place(x= 50, y= 250)
Button(root, text="Edit", command = EDIT).place(x= 100, y= 250)
Button(root, text="Delete", command = DELETE).place(x= 150, y= 250)
Button(root, text="View", command = VIEW).place(x= 200, y= 250)
Button(root, text="Exit", command = EXIT).place(x= 250, y= 250)
Button(root, text="Reset", command = RESET).place(x= 300, y= 250)

Select_set()

root.mainloop()
