class NumberGusser:
    def __init__(self):
        pass
    def guess_number(self, low, high):
        if low > high:
            return None
        mid = (low + high) // 2
        feedback = input(f"Is  number {mid}?  (h/l/c) from your number :::: h for higher from , l for lower, c for correct.: ").lower()
        if feedback == 'c':
            return mid
        elif feedback == 'h':
            return self.guess_number(low, mid - 1)
        elif feedback == 'l':
            return self.guess_number(mid + 1, high)
        else:
            print("Invalid input! Please enter 'h', 'l', or 'c'. h for higher, l for lower, c for correct.")
            return self.guess_number(low, high)
if __name__ == "__main__":
    ng = NumberGusser()
    print("Think of a number between 1 and 1000.")
    result = ng.guess_number(1, 1000)
    if result is not None:
        print(f"Yay! I guessed your number: {result}")
    else:
        print("Hmm, something went wrong.")


