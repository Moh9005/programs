#!/usr/bin/python
import math
import os


def add(a, b):
   return a + b

# This function subtracts two numbers
def subtract(a, b):
   return a - b

# This function multiplies two numbers
def multiply(a, b):
   return a * b

# This function divides two numbers
def divide(a, b):
   return a / b

def squareRoot(a):
   return math.sqrt(a)

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
def modulus(a,b):
    return a%b


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Squareroot")
print("6.Factorial")
print("7.Modulus")
#choice = input("Enter choice(1/2/3/4/5/6/7): ")
choice = input("Enter choice(1/2/3/4/5/6/7): ")
while(choice!=0):
# Take input from the user
    os.system('clear')
    choice = input("Enter choice(1/2/3/4/5/6/7): ")

    if choice == '1':
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        print(num1,"+",num2,"=", add(num1,num2))

    elif choice == '2':
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        print(num1,"-",num2,"=", subtract(num1,num2))

    elif choice == '3':
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        print(num1,"*",num2,"=", multiply(num1,num2))

    elif choice == '4':
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        print(num1,"/",num2,"=", divide(num1,num2))

    elif choice == '5':
        num1 = int(input("Enter  number: "))
        print("squareRoot of number = " , squareRoot(num1))

    elif choice == '6':
        num1 = int(input("Enter  number: "))
        print(num1,"!","=", factorial(num1))

    elif choice == '7':
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        print(num1,"%",num2,"=", modulus(num1,num2))
    else:
        print("Invalid input")
