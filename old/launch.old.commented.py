from tkinter import *
from pandas import *
from datetime import *
from numpy import *
def issue():
    file = read_excel('database.xlsx')
    serial_no=sne.get()
    roll=rne.get()
    name=ne.get()
    if (file.loc[file['Sr No.']==serial_no,'issued'].to_string(index=False) ==" Yes"):
        print("\nAlready Issued\n")
        return
    # roll="BT19CSE004"
    # name="Vedant"
    # print(file)
    # print("'"+file.loc[file['Sr No.']==serial_no,'issued'].to_string(index=False)+"'")
    file.loc[file['Sr No.']==serial_no,'issued_by'] = roll
    file.loc[file['Sr No.']==serial_no,'issue_date'] = (datetime.now().date())
    file.loc[file['Sr No.']==serial_no,'return_date'] = (datetime.now().date()+ timedelta(days=14))
    file.loc[file['Sr No.']==serial_no,'issuer_name'] = name
    file.loc[file['Sr No.']==serial_no,'issued'] = "Yes"
    # file.loc[file['Sr No.']==serial_no,'issue_date'] = datetime.timestamp(datetime.now())
    # file.loc[file['Sr No.']==serial_no,'return_date'] = datetime.timestamp(datetime.now()+ timedelta(days=14))
    # print((datetime.now().date()+ timedelta(days=14)) - datetime(2020-5-17).date() )
    # print(file)
    file.to_excel('database.xlsx', index=False)
    # file2 = read_excel('database.xlsx')
    # print(file2)
    # bookid=str(input("Enter Book ID : "))
    # print(file["Sr No."]==1)
    # df.to_excel(r'database.xlsx', index = False)
    messagebox.showinfo("Done")
def rturn():
    file = read_excel('database.xlsx')
    serial_no=sne.get()
    # roll=str(input("Enter Roll No. of Issuer :"))
    # name=str(input("Enter Name of Issuer :"))
    # print(file.loc[file['Sr No.']==serial_no,'issued_by'])
    delta = datetime.strptime(file.loc[file['Sr No.']==serial_no,'return_date'].to_string(index=False), '%Y-%m-%d') - datetime.now()
    delta = int(delta.days)
    fine = abs(delta*10)
    # print(delta)
    if (delta<0):
        print("\nLate Return Fine : " + str(fine) + " Rs")
    file.loc[file['Sr No.']==serial_no,'issued_by'] = nan
    file.loc[file['Sr No.']==serial_no,'issue_date'] = nan
    file.loc[file['Sr No.']==serial_no,'return_date'] = nan
    file.loc[file['Sr No.']==serial_no,'issuer_name'] = nan
    file.loc[file['Sr No.']==serial_no,'issued'] = "No"
    file.to_excel('database.xlsx', index=False)
    # file2 = read_excel('database.xlsx')
    # print(file2)
    messagebox.showinfo("Done")
def adnew():
    # bookid=string(input("Enter Book ID : "))
    file = read_excel('database.xlsx')
    serial_no=sne.get()
    book=bne.get()
    if(len(file.index[file['Sr No.'] == serial_no].values)!=0):
        print("\nSerial Number Already Exists\n")
        return
    new_row = {'Sr No.':serial_no, 'book_name':book,'issued':"No"}
    file = file.append(new_row, ignore_index=True)
    file.to_excel('database.xlsx', index=False)
    # print(file)
    messagebox.showinfo("Done")
def rmold():
    # bookid=string(input("Enter Book ID : "))
    file = read_excel(r'database.xlsx')
    serial_no=sne.get()
    # print(file.index[file['Sr No.'] == serial_no].values)
    file = file.drop(index=file.index[file['Sr No.'] == serial_no].values)
    file.to_excel(r'database.xlsx', index=False)
    messagebox.showinfo("Done")

# frame = Frame(root , width=400, height=100 , background="red")
def renIssue(): 
    if len(root.winfo_children()) > 4:
        root.winfo_children()[4].destroy()
    frame = Frame(root)
    frame.grid(row = 2, column = 0, columnspan = 4, sticky = W, pady = 2)
    
    snl = Label(frame, text = "Serial No.")
    sne = Entry(frame)
    snl.grid(row = 0, column = 0, sticky = W, pady = 2)
    sne.grid(row = 0, column = 1, sticky = W, pady = 2)
    
    rnl = Label(frame, text = "Roll No.") 
    rne = Entry(frame) 
    rnl.grid(row = 1, column = 0, sticky = W, pady = 2)
    rne.grid(row = 1, column = 1, sticky = W, pady = 2)

    nl = Label(frame, text = "Name") 
    ne = Entry(frame) 
    nl.grid(row = 2, column = 0, sticky = W, pady = 2)
    ne.grid(row = 2, column = 1, sticky = W, pady = 2)

    ok = Button(frame, text="OK",command = issue)
    ok.grid(row = 3, column = 0, columnspan = 4 ,sticky = W, pady = 2)
def renRet():
    if len(root.winfo_children()) > 4:
        root.winfo_children()[4].destroy()
    frame = Frame(root)
    frame.grid(row = 2, column = 0, columnspan = 4, sticky = W, pady = 2)
    snl = Label(frame, text = "Serial No.")
    sne = Entry(frame)
    snl.grid(row = 0, column = 0, sticky = W, pady = 2)
    sne.grid(row = 0, column = 1, sticky = W, pady = 2)
    
    ok = Button(frame, text="OK",command = rturn)
    ok.grid(row = 1, column = 0, columnspan = 4 ,sticky = W, pady = 2)
def renNew():
    if len(root.winfo_children()) > 4:
        root.winfo_children()[4].destroy()
    frame = Frame(root)
    frame.grid(row = 2, column = 0, columnspan = 4, sticky = W, pady = 2)
    snl = Label(frame, text = "Serial No.")
    sne = Entry(frame)
    snl.grid(row = 0, column = 0, sticky = W, pady = 2)
    sne.grid(row = 0, column = 1, sticky = W, pady = 2)
    
    bnl = Label(frame, text = "Book Name")
    bne = Entry(frame) 
    bnl.grid(row = 1, column = 0, sticky = W, pady = 2)
    bne.grid(row = 1, column = 1, sticky = W, pady = 2)

    ok = Button(frame, text="OK",command = adnew)
    ok.grid(row = 2, column = 0, columnspan = 4 ,sticky = W, pady = 2)
 
def renDel():
    if len(root.winfo_children()) > 4:
        root.winfo_children()[4].destroy()
    frame = Frame(root)
    frame.grid(row = 2, column = 0, columnspan = 4, sticky = W, pady = 2)
    snl = Label(frame, text = "Serial No.")
    sne = Entry(frame)
    snl.grid(row = 0, column = 0, sticky = W, pady = 2)
    sne.grid(row = 0, column = 1, sticky = W, pady = 2)

    ok = Button(frame, text="OK",command = rmold)
    ok.grid(row = 1, column = 0, columnspan = 4 ,sticky = W, pady = 2)
root = Tk()
button1 = Button(root, text="Issue Book",command = renIssue)
button2 = Button(root, text="Return Book",command = renRet)
button3 = Button(root, text="Add New Books",command = renNew)
button4 = Button(root, text="Delete Books",command = renDel)
button1.grid(row = 0, column = 0, sticky = W, pady = 2)
button2.grid(row = 0, column = 1, sticky = W, pady = 2)
button3.grid(row = 0, column = 2, sticky = W, pady = 2)
button4.grid(row = 0, column = 3, sticky = W, pady = 2)
# button1.pack(fill=BOTH,side = LEFT, anchor=N)
# button2.pack(fill=BOTH,side = LEFT, anchor=N)
# button3.pack(fill=BOTH,side = LEFT, anchor=N)
# button4.pack(fill=BOTH,side = LEFT, anchor=N)
root.mainloop()