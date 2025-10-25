__aPrivateVar = "private variable by appending __" #__ to private variable
_aProtectedVar = "protected variables by appending _ "

# class MyClass:
#     def __init__(self):
#         self.__private_var = "I am private"
#     def show_private(self):
#         return self.__private_var
    
# obj = MyClass()
# print(obj.show_private())

# Name Mangling for private variables
# class MyClass:
#     def __init__(self):
#         self.__private_var = "Name Mangling"
#     def display_private(self):
#         return self.__private_var
# obj = MyClass()
# print(obj._MyClass__private_var)

# class MyClass:
#     def __init__(self):
#         self.__private_var = "I am Private variable"

#     def __private_method(self):
#         return "This is a private method"

#     def show_private(self):
#         return self.__private_var + " and " + self.__private_method()
        
    
# obj = MyClass()
# print(obj.show_private())
# # print(obj.__private_method())
# print(obj._MyClass__private_method())

class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        return self.__balance
    
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        return self.__balance
    
    def get_balance(self):
        return self.__balance
    
account = BankAccount("12345", 1000)

try:
    account.__balance += 500
except AttributeError:
    print('Direct access to private variable failed')

print("Your account balance is: ", account.get_balance())

account.deposit(500)
print("Your account balance after deposit is: ", account.get_balance())
        