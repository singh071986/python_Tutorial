def cal_coffee_price(size, type, size_needed, type_needed):
    if size_needed in size and type_needed in type:
        total_price = size[size_needed] + type[type_needed]
        print(f"The price of a {size_needed} {type_needed} coffee is: ${total_price:.2f}")
    else:
        print("Invalid size or type. Please try again.")
size_prices = {"small": 2.0, "medium": 3.0, "large": 4.0}
type_prices = {"regular": 0.0, "cappuccino": 1.0, "latte": 1.5}
#size_needed=input("Enter coffee size (small, medium, large): ").lower()
#type_needed=input("Enter coffee type (regular, cappuccino, latte): ").lower()
#cal_coffee_price(size_prices,type_prices,size_needed,type_needed)


def calculate_discounted_price(original_price, discount_percentage):
    #discounted_price=original_price
    if discount_percentage <= 0 or discount_percentage >= 100:
        print("Discount percentage must be between 0 and 100.")
        return original_price
    else:
        discount_amount = (discount_percentage / 100) * original_price
        discounted_price = original_price - discount_amount
        return discounted_price
print(f"discounted price: {calculate_discounted_price(200,100)}")
print(f"discounted price: {calculate_discounted_price(200,15)}")



