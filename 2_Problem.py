# Taking input from user and then print the dic

dic={}
item=int(input("How many Items Do You Want In Dic : "))

for i in range(item):
    key=(input("Enter Your Name : "))
    value=int(input("Enter Marks : "))

    dic[key]=value

print("Your Names and Marks ")
for  i ,k in dic.items():
    print(i," ",k)

highest=max(dic.values())
for name,score in dic.items():
    if(score==highest):
        print("Highest marks : ",score," by:",name)