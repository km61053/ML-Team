import csv
from tkinter import *
root1 = Tk()

global rowCount


def createNewEmployee():
    with open("E:\Python Learning\employeeList.csv", 'r') as csvFile:
        empDetails = csv.reader(csvFile)
        rowCount = sum(1 for row in empDetails)
    csvFile.close()
    with open(".\employeeList.csv", 'a') as csvFile:
            employeeDetails = csv.writer(csvFile)
            if ( len (fNameE.get()) == 0 or len (lNameE.get()) == 0 or len (emailE.get()) == 0 or len (desE.get()) == 0 or len (bloodE.get()) == 0 ):
                Label (root1, text = "Must fill all fields information", font = "Helvetica 10 bold", fg = 'red').grid(row=0, column=0)
            else:
                employeeDetails.writerow([rowCount,fNameE.get(),lNameE.get(),emailE.get(),desE.get(),bloodE.get()])
                root1.destroy()
                
    csvFile.close()

root1.title("Create New Employee")

instructions = Label (root1, text = "Please fill required information")
instructions.grid(row=0, column=0)

fNameL = Label (root1, text = "First Name  : ")
lNameL = Label (root1, text = "Last Name   : ")
emailL = Label (root1, text = "Email Id    : ")
desL = Label (root1, text =   "Designation : ")
bloodL = Label (root1, text = "Blood Group : ")

fNameL.grid(row=3, column =0, sticky= W)
lNameL.grid(row=4, column =0, sticky= W)
emailL.grid(row=5, column =0, sticky= W)
desL.grid(row=6, column =0, sticky= W)
bloodL.grid(row=7, column =0, sticky= W)

fNameE = Entry(root1,  width =50)
lNameE = Entry(root1,  width =50)
emailE = Entry(root1, width =50)
desE = Entry(root1, width =50)
bloodE = Entry(root1, width =50)


fNameE.grid(row=3, column =1)
lNameE.grid(row=4, column =1)
emailE.grid(row=5, column =1)
desE.grid(row=6, column =1)
bloodE.grid(row=7, column =1)

createB = Button(root1, text ="Create", font = "Helvetica 10 bold", fg = 'Blue', command = createNewEmployee)
createB.grid(row=8, column =1)

root1.mainloop()


##label1 = Label (root1, text = "First Name ", font = 30, fg = 'Black').pack(side = LEFT)
##
##E1 = Entry(label1)
##E1.pack(side='left')
##
##label2 = Label (root1, text = "Last name ", font = 30, fg = 'Black').pack(side = LEFT)
##
##E2 = Entry(label2, bd =5).pack(side='left')
##
##label3 = Label (root1, text = "Email Id ", font = 30, fg = 'Black').pack(side = LEFT)
##
##E3 = Entry(label3, bd =5).pack(side='left')
##
##label4 = Label (root1, text = "Designation ", font = 30, fg = 'Black').pack(side = LEFT)
##
##E4 = Entry(label4, bd =5).pack(side='left')
##
##label5 = Label (root1, text = "Blood Group ", font = 30, fg = 'Black').pack(side = LEFT)
##
##E5 = Entry(label5, bd =5).pack(side='left')
##
