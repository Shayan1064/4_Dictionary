dic={}

items=int(input("Enter Items : "))
for i in range(items):
    key=input("Enter name: ")
    value=int(input("Enter Marks: "))
    dic[key]=value

print("The length of dic is : ",len(dic))