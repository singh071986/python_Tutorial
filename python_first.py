from operator import truediv

print("Hello World Yuvaana Kiaan")

a=1
b=2.0
c="hi"
d=True
e=None
f=[1,2,3] #list
g=(1,2,3)  #touple
h={1,2,3} #set
i= {"name":"yuvaan","Age":12} #dictionary
j=range(5)
print("a type:",type(a))
print("b type:",type(b))
print("c type:",type(c))
print("d type:",type(d))
print("e type:",type(e))
print("f type:",type(f))
print("g type:",type(g))
print("h type:",type(h))
print("i type:",type(i))
print("j type:",type(j))
print(a,b,c,d,e,f,g,h,i,j)

print(f[0])
print(f[0:2])
print(f[0:])
f[2]=12
print(f)
f.append(4)
print(f)
f.remove(2)
print(f)
f.pop()
print(f)
f.insert(1,22)
print(f)
f.sort()
print(f)
f.reverse()
print(f)
f.clear()
print(f)
f=[1,2,3]
print(len(f))
for item in f:
    print(item)

g=(11,22,33)
print([0])
print(g[0:2])
print(g[0:])
# g[2]=12 #touple is immutable
# print(g)
# g.append(4) #touple is immutable
# print(g)
# g.remove(2) #touple is immutable
# print(g)
# g.pop() #touple is immutable
# print(g)
# g.insert(1,22) #touple is immutable
# print(g)
# g.sort() #touple is immutable
# print(g)
# g.reverse() #touple is immutable
# print(g)
# g.clear() #touple is immutable
# print(g)
print(len(g))
for item in g:
    print(item)

h={44,55,66}
print(h)
# print(h[0]) #set is unordered
# print(h[0:2]) #set is unordered
# print(h[0:]) #set is unordered
# h[2]=12 #set is unordered
# print(h)
# h.append(4) #set is unordered
# print(h)
# h.remove(2) #set is unordered
# print(h)
# h.pop() #set is unordered
# print(h)
# h.insert(1,22) #set is unordered
# print(h)
# h.sort() #set is unordered
# print(h)
# h.reverse() #set is unordered
# print(h)
# h.clear() #set is unordered
# print(h)
print(len(h))
for item in h:
    print(item)


var1 = "Hello"
var2 = "World"
var3 = var1 + " " + var2
print(var3)
var4 = f"{var1} {var2}"
print(var4)
var5 = "{} {}".format(var1, var2)
print(var5)
var6 = "%s %s" % (var1, var2)
print(var6)
var7 = var1 * 3
print(var7)
del var7,var6

a=b=c=10
print(a,b,c)

if a>b:
    print("a is greateht than b")
elif a==b:
    print("boh are equal")
else:
    print("else at last")
print("if else is over")

x='This is a multi-line string.'
print(type(x))

def my_fuction():
    print("this is first fucniton")
my_fuction()

y=3+4j
print(type(y))
print(y.real)
print(y.imag)
print(y.conjugate())
print(abs(y))
print(pow(3,4))
print(divmod(10,3))
print(10//3)
print(10%3)

ls1=[1,2,"Abhay"]
ls2=[4,5,6]
ls3=ls1+ls2
print(ls3)

dt={}
dt["name"]="yuvaan"
dt["age"]=12
print(dt)
print(dt["age"])
print(dt.keys())
print(dt.values())
bool1=True
bool2=False
print(bool1 and bool2)
print(bool1 or bool2)
print(not bool2)
print(a==b)
print(type(None))

a=1.2
print (type(a))
b=int(a)
print(b)
print (type(b))
c=str(a)
print(c)
print (type(c))