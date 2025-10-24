def check_perfect_sqaure(num):
    import math as ma
    if ma.sqrt(num)%1==0:
        print (f"{num} is a perfect square")
    else:
        print (f"{num} is not a perfect square")
check_perfect_sqaure(9)

def check_perfect_sqaurewihtoutlibrary(num):
    if num**0.5 %1==0:
        print (f"{num} is a perfect square")
    else:
        print (f"{num} is not a perfect square")
check_perfect_sqaurewihtoutlibrary(7)


def findmax_number(ls):
    max_number=ls[0]
    for num in ls:
        if num>max_number:
            max_number=num
    return max_number
print(f"find max number in list:{findmax_number([-5,-4,-3,-2,-1])}")

def list_sort(ls):  #bubble sorting
    for i in range(len(ls)):

        for j in range(i+1,len(ls)):
            temp=ls[i]
            if ls[i]>ls[j]:
                ls[j]=temp
                ls[i]=ls[j]
    return ls
print(f"list sort:{list_sort([3,2,1,5,4])}")
print(f"list sort:{list_sort([3,2,1,-1,-5,5,4])}")
