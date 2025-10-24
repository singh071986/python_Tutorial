list=["abhay",12,12.3,True,12]
print(type(list))
print(list)
print(set(list))
list1=[11,22,33,44,55]
print(type(list1))
print(list+list1)
print((list+list1)*3)

print(list[0:3])
print(list[-1])
print(list[-1:])
print(list1[-3:-1])
list2=list1.copy()
del list2[len(list2)-1]
print(list2)
list2.remove(11)
print(list2)

print(7 in list2)
print(22 in list2)
print (7 not in list2)
print(22 not in list2 )

list2.append(66)
print(list2)
list2.insert(1,77)
print(list2)
print(max(list2))
print(min(list2))
print(list.count(22))
list2.extend([77])
print(list2)
print(list2.index(77))
#print(list2.sort(key=NONE , reverse=True))
list2.sort()
print(list2)

tp1=(11,22,33,44,55)
print(type(tp1))
print(tp1)
print(tp1[0:3])
print(tp1[-1])
print(tp1[-1:])
print(tp1[-3:-1])
print(tp1.count(22))
print(tp1.index(22))
#tp1[0]=100 #touple is immutable
tp2=(66,77,88)
tp3=tp1+tp2
print(tp3)
print (tp3*2)
print(max(tp3))
print(min(tp3))
print(11 in tp3)
print(10 in tp3)
print(11 not in tp3)
print(10 not  in tp3)
#tp3.append(99) #touple is immutable
#tp3.remove(11) #touple is immutable
#tp3.insert(1,100) #touple is immutable
#tp3.sort() #touple is immutable
#tp3.reverse() #touple is immutable
#tp3.clear() #touple is immutable
#print(len(tp3))
#for item in tp3:
   # print(item)
#
#dict={"name":"abhay","age":12,"marks":12.3,"name":"yuvaan"}
dict1={"name":"abhay","age":12,"marks":12.3}
print(dict1["name"])
print(dict1.get("name"))
#print(dict1["name11"])
print(dict1.get("name11"))
print(dict1.keys())
print(dict1.values())
dict1["address"]="Toronto"
print(dict1)
dict2={"school":"RoboGarden","city":"Toronto"}
dict3={**dict1,**dict2}
print(dict3)
dict4=dict1 | dict2
print(dict4)
dict4["job details"]={"company":"CIBC","positon":"consultnat"}
print(dict4)

dict4[123]=12131
print(dict4)
del dict4[123]
print(dict4)
#print(dict4.clear())
#del dict4
#print(dict4)
print(str(dict4))
print(dict4.items())



for i in range(5):
    for j in range(5):
        print( j,end="")
    print()




num=30
ls = []
check=True
i=1
#while(check):
while(i<=num):
    if(i%3==0 and i%5==0):
        check=False
        ls.append(i)
    i+=1
print(f"number divisabel by 2 and 5:{ls}")


available_copies=3
boorowed_copies=1
Available_for_boorow=available_copies-boorowed_copies
while(Available_for_boorow<=available_copies):
    askfor_boorow=input("Do you want to borrow money? (YES/NO or yes/no): ")
    if (askfor_boorow).upper()=="YES" and Available_for_boorow>0:
        print(f"Available copies for boorowing:{Available_for_boorow}")
        Available_for_boorow=Available_for_boorow-boorowed_copies
        boorowed_copies+=1
    else:
        print(f"No book available for boorowing")
        break

passowrd="admin123"
max_attempts=3
attempts=0
while(attempts<max_attempts):
    user_input=input("Enter your password:")
    if user_input==passowrd:
        print("Login successful!")
        break
    else:
        attempts+=1
        if attempts<max_attempts:
         print(f"Incorrect password. You have {max_attempts - attempts} attempts left.")
if attempts>=max_attempts:
   print("Account locked due to too many failed attempts.")
