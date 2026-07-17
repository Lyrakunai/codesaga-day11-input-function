# ===============================
# Codesaga Day 11
# Topic : input() Function
# ===============================

# Program 1 : Name Input
name = input("Enter your name: ")
print("Welcome,", name)



# Program 2 : Next Year Age
age = int(input("Enter your age: "))
next_year = age + 1
print("Next year you will be", next_year)



# Program 3 : Sum of Two Numbers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("Sum =", num1 + num2)



# Program 4 : Multiplication
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Multiplication =", a * b)



# Program 5 : Square
num = int(input("Enter a number: "))
print("Square =", num * num)



# Program 6 : Double Triple Half
num = int(input("Enter a number: "))
print("Double =", num * 2)
print("Triple =", num * 3)
print("Half =", num / 2)


# Program 7 : Square and Cube
num = int(input("Enter a number: "))
print("Square =", num ** 2)
print("Cube =", num ** 3)



# Program 8 : Birth Year
name = input("Enter your name: ")
birth_year = int(input("Enter your birth year: "))
age = 2026 - birth_year
print(name, "is", age, "years old")



# Program 9 : Simple Interest Calculator
principal = int(input("Enter principal: "))
rate = int(input("Enter rate: "))
time = int(input("Enter time: "))
si = (principal * rate * time) / 100
amount = principal + si
print("Simple Interest =", si)
print("Total Amount =", amount)