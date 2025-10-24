def calculate_percentage(degree, totalnumber):
    assert (degree>=0,totalnumber>=0), "degree and total numebr shoudl be grater than zero"
    calculate_percentage=(degree/totalnumber)*100
    print(f"totla perctage:{calculate_percentage} ")
    return calculate_percentage

degree1=float(input("enter degree :"))
totalnumber1=float(input("enter total number:"))
calculate_percentage(degree1,totalnumber1)

