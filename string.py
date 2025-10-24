s="RoboGarden"

print(s[2:4])  # prints bo (2nd and 3rd index)
print(s[0:5])   # prints RoboG (0th to 4th
print(s[5:])    # prints arden (5th to end)
print(s[:5])    # prints RoboG (start to 4th)
print(s[-1])    # prints d (last character)
print(s[-2:])   # prints den (last 3 characters)

print(s*3)  # prints RoboGardenRoboGardenRoboGarden
print(s+"123")  # prints RoboGarden123
print("123"+s)  # prints 123RoboGarden
print("-----------")
print(s+"\n"+s)
print("-----------")
print(s+"\t"+s)
print("-----------")
print(s+"\r"+s)
print("-----------")


print(s.upper())
print(s.lower())
print(s.replace("Robo","Techno"))
print(s.find("Garden"))  # prints 4 (starting index of substring)
print(s.index("Garden")) # prints 4 (starting index of substring)
print(s.split("o"))      # prints ['R', 'b', 'Garden']


age=10
marks=10.3
degree=-10
name="robogardenoo"
str1="hi %s"%(name)
print(str1)

print("hey %s, my age is%u"%(name,age))
print("hey%s, my marks is %f"%(name, marks))
print("hey%s, my age is %u, my marks is %f, degree is %d"%(name,age,marks,degree))

print(name.capitalize())
print(name.upper())
print(name.count("o",2,len(name)))
print(name.find("y",0,len(name)))
print(name.find("o",0,len(name)))
print(name.index("o",0,len(name)))
#print(name.index("y",0,len(name)))
name1="ROBo123"
print(name1.isdigit())
print(age.is_integer())
print(name1.islower())
print(name1.isupper())
print(name1.join("abh"))
#print(name1.join(["a","b","c"]))
print(name1.join("1234"))
print(name1.split(","))
print(name1[2:-1])
name1=name
print(name1)
name1=name[0:3]+"Abhay"
print(name1)
name2="abhayyuvaankiaan"
print(name2[-1:-4])
#conda craete -n octmlaibootcamp python=3.7
#conda env list


st="Kindly check your code. your code looks interesting"

## Type your code here

st_out= (st[0:2]+st[-2:])
print(st_out*2)


