myList = ["Kishore","Hari", "Sneha", "Sravanthi"]

print ("Mylist :" + str(myList))

print ("Length of mylist : " + str(len(myList)))

print ("First Element in my List : " + myList[0])

print ("Last element in my list : " + myList[-1])

myList.append("appended name")

print ("My list after append :")

print ("Mylist :" + str(myList))

print ("Length of mylist : " + str(len(myList)))

print ("First Element in my List : " + myList[0])

print ("Last element in my list : " + myList[-1])

anotherList  = [1,2,3,4]

print ("Two lists: "+ str(myList) + str(anotherList))

myList.extend(anotherList)

print("Appended list :"+ str(myList))

myList.remove("appended name")

print ("My list after remove :")

print ("Mylist :" + str(myList))

print ("max in a list :" + str(max(anotherList)))

print ("subList : "+str(myList[3:6]))

print ("list in reverse : " , myList[::-1])

input("Press any key to exist...")
