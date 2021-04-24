from tkinter import *
from pandas import *
from datetime import *
from numpy import *
def issue():
    file = read_excel('database.xlsx')
    serial_no=int(input("Enter Serial No. of book to issue :"))
    if (file.loc[file['Sr No.']==serial_no,'issued'].to_string(index=False) ==" Yes"):
        print("\nAlready Issued\n")
        return
    roll=str(input("Enter Roll No. of Issuer :"))
    name=str(input("Enter Name of Issuer :"))
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
def rturn():
    file = read_excel('database.xlsx')
    serial_no=int(input("Enter Serial No. of book to return :"))
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
def adnew():
    # bookid=string(input("Enter Book ID : "))
    file = read_excel('database.xlsx')
    serial_no=int(input("Enter Serial No. of book to Add :"))
    if(len(file.index[file['Sr No.'] == serial_no].values)!=0):
        print("\nSerial Number Already Exists\n")
        return
    book=str(input("Enter Name of book to Add :"))
    new_row = {'Sr No.':serial_no, 'book_name':book,'issued':"No"}
    file = file.append(new_row, ignore_index=True)
    file.to_excel('database.xlsx', index=False)
    # print(file)
def rmold():
    # bookid=string(input("Enter Book ID : "))
    file = read_excel('database.xlsx')
    serial_no=int(input("Enter Serial No. of book to Delete :"))
    # print(file.index[file['Sr No.'] == serial_no].values)
    file = file.drop(index=file.index[file['Sr No.'] == serial_no].values)
    file.to_excel('database.xlsx', index=False)
issue()
file2 = read_excel('database.xlsx')
print(file2)
rturn()
file2 = read_excel('database.xlsx')
print(file2)
rmold()
file2 = read_excel('database.xlsx')
print(file2)
adnew()
file2 = read_excel('database.xlsx')
print(file2)