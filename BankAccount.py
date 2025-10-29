class BankAccount:

    total_balance=0
    def __init__(self,name,accountType, balance=0):
        import random as rd
        self.name=name
        self.accountType=accountType
        self.balance=balance
        self.account_number=rd.randint(1000000000,9999999999)
        self.file_name=str(self.account_number)+"_"+self.accountType+"_"+self.name+".txt"
        files2=open(self.file_name,"a+")
        files2.write(f"{self.account_number},{self.name},{self.accountType},{self.balance}\n")
        print(f"Account created successfully for {self.name} with account number {self.account_number} and balance {self.balance}")

# Create account method
    def create_account(self):
        print(f"Account details saved in file: {self.file_name}")
# Deposit method
    def deposit(self,account_number, name,accountType,depositbalance,filename):
        deposit_file=open(filename,"a+")
        deposit_file.write(f"{account_number},{name},{accountType},{depositbalance}\n")
# Withdraw method
    def wihtdraw(self,account_number, name,accountType,wihtdraw_amount,filename):
        file = self.account_baalnce(filename)
        print(f"Total balance before withdrawal: { BankAccount.total_balance}")
        if  BankAccount.total_balance<wihtdraw_amount:
            print(f"Insufficient balance for withdrawal.Available balance: { BankAccount.total_balance}$ , Withdrawal amount: {wihtdraw_amount}$")
        else:
            file.write(f"{account_number},{name},{accountType},{-wihtdraw_amount}\n")
# Account balance method
    def account_baalnce(self, filename):
        file = open(filename, "r+")
        BankAccount.total_balance=0
        # content=file.readline()
        for line in file:
            lst1 = line.split(",")
            BankAccount.total_balance = BankAccount.total_balance + int(lst1[len(lst1) - 1])
        print(f"Total balance in account: {BankAccount.total_balance}$")
        return file
# Find user details methods
    def find_user_id(self):
        print(f"Customer Account number :{self.account_number}")
# Find user details methods
    def find_user_name(self):
        print(f"Customer user_name:{self.name}")
# Find user details methods
    def find_account_type(self):
        print(f"Customer account_type:{self.accountType}")
# Print account statement method
    def print_statement(self,filename):
        file = open(filename, "r+")
        print("***Account Statement start**:")
        for line in file:
            print(line)
        print("***Account Statement end ***:")


print("-------First object  Creation start-------")
bc1=BankAccount("Yuvaan", "Savings", 17000)
bc1.create_account()
bc1.deposit(8955473943,"Abhay","Savings",40000,bc1.file_name)
bc1.wihtdraw(8955473943,"Abhay","Savings",10000,bc1.file_name)
bc1.account_baalnce(bc1.file_name)
bc1.find_user_id()
bc1.find_user_name()
bc1.find_account_type()
bc1.print_statement(bc1.file_name)
print("-------First object  Creation end-------")


print("-------Second object  Creation start-------")
bc=BankAccount("Abhay", "Checking", 5000)
bc.create_account()
bc.deposit(8955473943,"Abhay","Savings",10000,"8955473943_Savings_Abhay.txt")
bc.wihtdraw(8955473943,"Abhay","Savings",10000,"8955473943_Savings_Abhay.txt")
bc.account_baalnce("8955473943_Savings_Abhay.txt")
bc.find_user_id()
bc.find_user_name()
bc.find_account_type()
bc.print_statement("8955473943_Savings_Abhay.txt")
print("-------Second object  Creation end-------")





