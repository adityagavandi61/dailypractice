list_1 = [1,2,3,4,5,5,3,4,6,8,1]
list_2=[]
for i in list_1:
    if i not in list_2:
        list_2.append(i)
    
print(list_2)