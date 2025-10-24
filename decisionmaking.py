from scipy.stats import false_discovery_control

num=20
## Type your code here
divisible=False
if(num%7==0):
    divisible=True
else:
    divisible=False
#####################
print(divisible )
print(27%10)
print("#####################whiele loop")
i=6
while (i>0):
    print(i)
    i-=1
    if(i==3):
        break
print("while loop ended")

while True:
    print ("infinite loop")
    break

i=10
while i>=1:
    print("i",i)
    i-=1
else:
    print("else block")
print("while loop ended")

while True: print("infinite loop"); break
print("while loop ended")

#for loop
lst=[1,2,3,4]
for i in lst:
    print(i)

str="Abhay pratap singh"
for s in str:
    print(s)
    
lst1=["abh",5,6.4,"pratap"]

for i in range(len(lst1)):
    print(i, lst1[i])
else:
    print("else block")

i=5
while i>0:
    print("outside while for nested:", i)
    i-=1
    while True:
        print("inner while",i)
        break


tp=(1,2,3,4)
for i in tp:
    print ("in tp:",i)
    break
j=6
while j>2:
   print("j",j)
   j-=1
   if j>2:
      continue
print(f"j after while: {j}")

print(f"####Even Odd number check for given number")
i=24
lst=[22,33,44,55,66]
print("last element removal",lst.pop())
for i in lst:
    if i%2==0:
            print(f"Even number: {i}")
    else:
            print(f"Odd number: {i}")


print(f"####################Add even numbers from 0 to 9 in a list and print the list")
lst2=[]
given_num=10
#for i in range(0,given_num+1):
for i in range(given_num+1):
    if i%2==0:
       lst2.append(i)
print(f"Using for loop Even numbers from 0 to 9:{lst2}")


print(f"####################Add even numbers from 0 to 9 in a list and print the list in reverse order")
lst3=[]
while given_num>=0:
    if given_num%2==0:
        lst3.append(given_num)
    given_num-=1
lst3.reverse()
print(f"Using while  loop Even numbers from 0 to 9:{lst3}")

print(lst3.pop())
print(lst3)

num=300
for i in range(1,num+1):
    if i%3==0 and i%5==0:
        print(f"{i} is divisible by both 3 and 5")
        break

lst4=[]
for i in range(1,num+1):
    if i%3==0 and i%5==0:
        lst4.append(i)
print(f"{lst4[0]} is divisible by both 3 and 5")

counter=0
for i in range(1,num+1):
    if i%3==0 and i%5==0 and counter<5:
        counter+=1
        if counter==4:
            print(f"{i} is second divisible by both 3 and 5")





inoutnumber=10
for i in range(inoutnumber):
    for j in range(i+1):
        print("*",end="")
    print()
name=input("Enter your number: ")
print(f"You entered and multiply valur: {int(name) * 2 }")









