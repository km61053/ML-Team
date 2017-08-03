import csv

with open("E:\Python Learning\employeeList.csv", 'r') as csvFile:
    employeeDetails = csv.reader(csvFile, delimiter=',')
    id = input("Enter employee id : ")
    index = True
    for row in employeeDetails:
        if id == row[0]:
            index = False
            print ("Full Name   : ",row[1]+" "+row[2])
            print ("Email Id    : ",row[3])
            print ("Designation : ",row[4])
            print ("Blood Group : ",row[5])
            break

    if index:
        print ("No info available")

        
input("Press Enter to go next program")

with open("E:\Python Learning\employeeList.csv", 'r') as csvFile:
    employeeDetails = csv.reader(csvFile, delimiter=',')
    searchKey = input("Enter employee id : ")
    index = True
    for row in employeeDetails:
        for field in row:
            if searchKey in field:
                print (row)
