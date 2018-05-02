from Tkinter import *
from PIL import ImageTk,Image
import Tkinter
import tkMessageBox
import Pmw, sys
count = 0
root = Tk()
root.geometry('1050x580+160+100')
root.title('LIBRARY MANAGEMENT SYSTEM')

# Top frame color
Top = Frame(root, width=1050, height=100, bg="#ff0040")
Top.pack(side=TOP)

#MAIN LEFT FRAME
frame1 = Frame(root, width=600, height=450, bg="#016f82")
frame1.pack(padx = 14,pady = 10,side=LEFT)

#MAIN RIGHT FRAME
frame2 = Frame(root, width=420, height=450, bg="#016f89")
frame2.pack(padx=14,pady=10,side=RIGHT)

#Button(frame2, text='Quit', command=root.destroy).pack(pady=15)

# MAIN LABEL
infoLabel = Label(Top, font=('Times New Roman', 50), text="LIBRARY MANAGEMENT SYSTEM",bg="#ff0040")
infoLabel.place(x=190,y=16)
# VARIABLES
bookid = StringVar()
bookname = StringVar()
isbn = StringVar()
sub = StringVar()
quantity = StringVar()

label_i = Label(frame1, text='BookID' ,font=('aerial',20,'bold'),bg = "#016f82")
label_i.place(x=10,y=30)
entry_i = Entry(frame1,font=('aerial',20,'bold'),textvariable=bookid,width=29,justify='right')
entry_i.place(x=165,y=30)

label_b = Label(frame1, text='Book Name',font=('aerial',20,'bold'),bg = "#016f82")
label_b.place(x=10,y=80)
entry_b = Entry(frame1,font=('aerial',20,'bold'),textvariable=bookname,width=29,justify='right')
entry_b.place(x=165,y=80)

label_isbn = Label(frame1, text='ISBN' ,font=('aerial',20,'bold'),bg = "#016f82")
label_isbn.place(x=10,y=130)
entry_isbn = Entry(frame1,font=('aerial',20,'bold'),textvariable=isbn,width=29,justify='right')
entry_isbn.place(x=165,y=130)

label_sub = Label(frame1, text='Subject',font=('aerial',20,'bold'),bg = "#016f82")
label_sub.place(x=10,y=180)
entry_sub = Entry(frame1,font=('aerial',20,'bold'),textvariable=sub,width=29,justify='right' )
entry_sub.place(x=165,y=180)

label_quantity = Label(frame1, text='Quantity',font=('aerial',20,'bold'),bg = "#016f82")
label_quantity.place(x=10,y=230)
entry_quantity = Entry(frame1,font=('aerial',20,'bold'),textvariable=quantity,width=29,justify='right' )
entry_quantity.place(x=165,y=230)

##################################################
def error():
    bookid.set("")
    bookname.set("")
    isbn.set("")
    sub.set("")
    quantity.set("")
    l8 = Label(frame1, text='**Error**ALL FIELDS ARE NECESSARY')
    l8.grid(row=20, columns=3)


###############################################
def display(event):
    filename = "librarymanagement.txt"
    text = Pmw.ScrolledText(frame2,
                            borderframe=5,
                            vscrollmode='dynamic',
                            hscrollmode='dynamic',
                            labelpos='n',
                            label_text='Book ID     Book Name     ISBN         Subject       Quantity',
                            text_width=420,
                            text_height=450,
                            text_wrap='none',
                            )
    text.pack()

    text.insert('end', open(filename, 'r').read())


    data = open('librarymanagement.txt', 'r')
    data_list = []
    j = 0
    s = data.readlines()
    for i in s:
        l = s[j].split()
        j += 1
        data_list.append(l)
    print(data_list)
    global count
    print count
    if count <= len(data_list) - 1:
        bookid.set(data_list[count][0])
        bookname.set(data_list[count][1])
        isbn.set(data_list[count][2])
        sub.set(data_list[count][3])
        quantity.set(data_list[count][4])
        count += 1
        data.close()
    else:
        count = 0

def addBook(event):
    text =  bookid.get()
    text2 = bookname.get()
    text3 = isbn.get()
    text4 = sub.get()
    text5 = quantity.get()
    text5=str(text5)

    for i in range(len(text), 11):
        text = text + " "
    for i in range(len(text2), 16):
        text2 = text2 + " "
    for i in range(len(text3), 11):
        text3 = text3 + " "
    for i in range(len(text4), 11):
        text4 = text4 + " "
    for i in range(len(text5), 14):
        text5 = text5 + " "

    TEXT = "\n"+text + " " + text2 +" " + text3+ " "+text4+" "+text5
    print (TEXT)
    if text == "" or text2 == "" or text3 == "" or text4 == "" or text5 == "" :
        error()
    INFO = open("librarymanagement.txt", "a")
    INFO.writelines(text + " " + text2 +" " + text3+ " "+text4+" "+text5+"\n")
    bookid.set("")
    bookname.set("")
    isbn.set("")
    sub.set("")
    quantity.set("")
    INFO.close()

def display_first(event):
    import re
    data = open('librarymanagement.txt', 'r')
    s = data.readline()
    string = re.sub(' +', ' ', s)
    l = string.split()
    bookid.set(l[0])
    bookname.set(l[1])
    isbn.set(l[2])
    sub.set(l[3])
    quantity.set(l[4])
    data.close()


########################################################
def display_last(event):
    data = open('librarymanagement.txt', 'r')

    for i in data:
        s = i
    string = re.sub(' +', ' ', s)
    l = string.split()
    bookid.set(l[0])
    bookname.set(l[1])
    isbn.set(l[2])
    sub.set(l[3])
    quantity.set(l[4])
    data.close()

def deletebook(event) :
    id = bookid.get()
    INFO = open("librarymanagement.txt" ,"r")
    lines = INFO.readlines()
    INFO.close()
    INFO = open("librarymanagement.txt","w")

    for i in lines :
        x = i.split()
        if ( x[0] != id) :
            INFO.write(i)


    bookid.set("")
    INFO.close()


button_sub = Button(frame1, fg='black',height=1,width=11,text='Add',bg="#016FA2")
button_sub.place(x=200,y=280)
button_cancel = Button(frame1, text='Close', fg='Red', bg='white', height=1,width=11, command=root.destroy)
button_cancel.place(x=395,y=280)

button_display=Button(frame1, fg='black',height=1,width=11,text='Display',bg="#016FA2")
button_display.place(x=200,y=330)

button_delete=Button(frame1, fg='black',height=1,width=11,text='Delete',bg="#016FA2")
button_delete.place(x=395,y=330)


first = Button(frame1, text="First_Rec", fg='red',height=1,width=11)
first.place(x=200,y=380)
last = Button(frame1, text='Last_Rec', fg='red',height=1,width=11)
last.place(x=395,y=380)



button_sub.bind('<Button-1>', addBook)
button_display.bind('<Button-1>',display)
first.bind('<Button-1>', display_first)
last.bind('<Button-1>', display_last)
button_delete.bind('<Button-1>',deletebook)

root.mainloop()
