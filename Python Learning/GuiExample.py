import csv
#import CreateEmployees
from tkinter import *
root = Tk()

def searchEmployeeDetails():
    T.delete('1.0', END)
    if len (E1.get()) == 0:
        T.insert(END, "Please enter input on sarch field")
    else:
        with open(".\employeeList.csv", 'r') as csvFile:
            employeeDetails = csv.reader(csvFile, delimiter=',')
            flag = True

            for row in employeeDetails:
                for field in row:
                    if len (field) != 0:
                        if E1.get().lower() in field.lower():
                            flag = False
                            T.insert(END, row)
                            T.insert(END, "\n")
                            break
            if flag:
                T.delete('1.0', END)
                T.insert(END, "No Information available for entered search key")
        csvFile.close()

def createEmployeeInfo():
    import CreateEmployees


root.title("Employee List")
root.geometry("1350x650+0+0")
#root.configure(background='violet')

frame1 = Frame(root, width=1350, height=70, bd=8, relief='raise')
frame1.pack(side=TOP)

frame2 = Frame(root, width=1350, height=500, bd=8, relief='raise')
frame2.pack(side=BOTTOM)

label = Label (frame1, text = "Nielsen Offshore Information", font = "Helvetica 30 bold", fg = 'Black').pack()

label1 = Label (root, text = "Employee Details ", font = 10, fg = 'Black').pack(side='left')

E1 = Entry(label1, bd =5)
E1.pack(side='left')

B1 = Button(label1, text ="Search", command=searchEmployeeDetails)
B1.pack(side='left')

B2 = Button(root, text = "Add New User", bd = 5, font=30, command = createEmployeeInfo).pack(side='right')


T = Text(frame2, width = 1350)
T.pack()

root.mainloop()
