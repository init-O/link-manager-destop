from tkinter import *
from tkinter import messagebox
from tkinter.font import Font
from db import Database
import webbrowser as chrome

db = Database('bookmarks.db')
selectedLink = ''

def openLink():
    print('selected chutiyap',selectedLink)
    chrome.open(selectedLink)

def populate_bookmarks():
    link_list.delete(0,END)
    space = "-"*10
    for row in db.fetch():
        link_list.insert(END, (row[0], row[1],space,row[2]))

def selectLink(event):
    index = link_list.curselection()[0]
    global selectedLink
    selectedLink = link_list.get(index)[3]
    selectedLabel.config(text=selectedLink)

def addLink():
    if(part_text.get()=='' or link_text.get()==''):
        messagebox.showerror('Requires Field', 'Please enter Title and Link')
        return 
    db.insert(part_text.get(),link_text.get())
    link_list.delete(0,END)
    populate_bookmarks()

def removeLink():
    if(link_list.curselection()):
        index = link_list.curselection()[0]
        db.remove(link_list.get(index)[0])
        populate_bookmarks()
    else:
        messagebox.showerror('Requires Field', 'Please Select A Link')

app = Tk()
app.geometry('900x700')
app.title('Link Manager')
app.configure(bg="#151516")
helv36 = Font(family="Adobe Garamond Pro",size=12)

frame1 = Frame(app, bg="#151516")

part_text = StringVar()
part_label = Label(frame1, text="Title", font=('bold',16), bg="#151516", fg="white", pady=20)
part_label.grid(row=0, column=0, sticky=W)
part_entry = Entry(frame1, text=part_text, width=30)
part_entry.grid(row=0, column=1)

link_text = StringVar()
link_label = Label(frame1, text="Link", font=('bold',16),  bg="#151516", fg="white")
link_label.grid(row=0, column=2, sticky=W)
link_entry = Entry(frame1, text=link_text, width=50)
link_entry.grid(row=0, column=3,columnspan=2)


link_list = Listbox(frame1, height=25, width=60, bg="#151516", fg="white", bd=0, font=helv36, activestyle="none", highlightthickness=0, selectbackground="#6495ed")
link_list.grid(row=3, column=0, columnspan=3, rowspan=6, pady=20, padx=20)

scrollbar = Scrollbar(frame1)
scrollbar.grid(row=3, column=3)

link_list.configure(yscrollcommand=scrollbar.set)
link_list.bind('<<ListboxSelect>>', selectLink)
scrollbar.configure(command=link_list.yview)

addBtn = Button(frame1, text="Add New link", command=addLink)
addBtn.grid(row=2, column=0)

removeBtn = Button(frame1, text="Delete", bg="red", command=removeLink)
removeBtn.grid(row=2, column=1)


selectedLabel = Label(frame1, text='', font=('bold',14),  bg="#151516", fg="white")
selectedLabel.grid(row=10, column=0, columnspan=3)

gotoBtn = Button(frame1, text="Go", bg="red", command=openLink, width=10)
gotoBtn.grid(row=10, column=4)

populate_bookmarks()

frame1.pack(fill='both', expand=True)

app.resizable(True,True)
app.mainloop()

