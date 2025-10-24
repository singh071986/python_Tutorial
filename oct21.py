#shopping cart program
def shopping_cart(budget=1000):
    budget  =1000
    balance_left=budget
    item_name = ""
    lst_items={}
    lstitem1=[]
    lstprice1=[]
    decimalvalue=False
    item_price=0.0
    while item_name.upper()!="DONE":
        item_name =input("Enter the item name you want to buy or DONE to finish: ")
        if item_name=="DONE":
            break
        item_price=(input(f"Enter the price of {item_name}: "))
       # while != item_price.isdecimal():
        #item_price=(input(f"Enter the price of {item_name}: "))
            #item_price= input(f"Invalid price. Please enter a numeric value for {item_name}: ")
        item_price=float(item_price)
        if item_price<=balance_left:
            balance_left=balance_left-item_price
            print(f"Item {item_name} Total:{item_price} Balance left:{balance_left}" )
            lstitem1.append(item_name)
            lstprice1.append(item_price)

        elif item_price>balance_left:
            print(f"Cannot  but buy {item_name}. Exceeds budget by {item_price-balance_left}.")

    print("Final Cart:")
    for i in range (len (lstitem1)):
        print(f"{lstitem1[i]}: {lstprice1[i]}")

    print(f"Total spent: {budget - balance_left}")
    print(f"Balance left: {balance_left}")


#count vowels and given character in a string
def count_vowels_and_character():
    input_string=input("Enter a string: ")
    given_string=input("Enter a charter to be counted: ")
    vowel_count=0
    given_string_count=0
    for i in range(len(input_string)):
        if input_string[i].lower()==given_string.lower():
            given_string_count+=1
        if input_string[i].lower() in ['a','e','i','o','u']:
            vowel_count+=1

    print(f"Number of times '{given_string}' appears in the string: {given_string_count}")
    print(f"Number of vowels in the string: {vowel_count}")

#print(f"Fibonacci series of n terms: {fibonacci_series(10)}")
def generate_fibonacci_series(n=3):
    first=1
    second=2
    temp=0
    counter=1
    print("Fibonacci series: ")
    while(counter<=n):
        print(first,end=" ")
        temp=first+second
        first=second
        second=temp
        counter+=1
    print()

#print(f"Fibonacci series of n terms wiht return: {fibonacci_series(10)}")
def generate_fibonacci_series_return(n=3):
    first=1
    second=2
    temp=0
    counter=1
    lst_fib=[]
    print("Fibonacci series: ")
    while(counter<=n):
        lst_fib.append(first)
        temp=first+second
        first=second
        second=temp
        counter+=1
    return lst_fib

#shopping_cart(2000)
#count_vowels_and_character()
#generate_fibonacci_series(3)
if __name__ == "__main__":
    result =generate_fibonacci_series_return(3)
    print (f"Fibonacci series of n terms with return: {result}")
    for val in result:print(val,end=" ")
    print()
