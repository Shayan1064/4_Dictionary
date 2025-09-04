dic = {"Ali": 85, "Sara": 90, "Ahmed": 78}

swapped_dic={}
for key,value in dic.items():
    swapped_dic[value]=key

print("Original : ",dic)
print("Swwapped : ",swapped_dic)