def hello_fuction():
    print("Hello from functions.py!")


def add(a,b):
    return a+b

hello_fuction()

import sys
print ("Command line arguments:", sys.argv)
print(f"add 2 numbers: {add(int(sys.argv[1]),int(sys.argv[2]))}")
print(f"add 2 numbers: {add(b=20,a=10)}")


def default_arg_example(x,y=5):
    return x+y
print(f"default arg example: {default_arg_example(10)}")
print(f"default arg example: {default_arg_example(10,15)}")

def var_length_arg_example(*x):
    sum=0
    for i in x:
        sum+=i
    return sum
print(f"var length arg test: {var_length_arg_example(1,2,3,4,5)}")
print(f"var length arg test: {var_length_arg_example(10)}")


#mutiple keyworodl arguemnts
def vra_lenght_ketworld_args(**x):
    for key, values in x.items():
        print(f"key: {key}, value : {values}")


vra_lenght_ketworld_args( job="Develoepr",name="Abhay", age=39)

## Lambda function
sqaure = lambda y:y*y
print(f"sqaur of 5 is :{sqaure(5)}")

doublevalue=lambda z:z*2
print(f"double value of 7 is :{doublevalue(7)}")







()
