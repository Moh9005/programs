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
    try:
       return a/b

    except ZeroDivisionError:
        print(" Infinty",a ,"cannot be divided by ",b)

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




while True:
    # main program
    while True:
        answer = input('Run / Run again? (y/n): ')
        if answer in ('y', 'n'):
            break
    if answer == 'y':
        os.system('clear')
        choice = input("Enter choice(1/2/3/4/5/6/7): ")

        if choice == '1':
            print("-------ADDITION FUNCTION-------- ")
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print("-------SUBTRACTION FUNCTION-------- ")
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print("-------MULTIPLICATION FUNCTION-------- ")
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print("-------DIVISION FUNCTION-------- ")
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
            print(num1, "/", num2, "=", divide(num1, num2))

        elif choice == '5':
            print("-------SQUAREROOT FUNCTION-------- ")
            num1 = int(input("Enter  number: "))
            print("squareRoot of number = ", squareRoot(num1))

        elif choice == '6':
            print("-------FACTORIAL FUNCTION-------- ")
            num1 = int(input("Enter  number: "))
            print(num1, "!", "=", factorial(num1))

        elif choice == '7':
            print("-------MODULUS FUNCTION-------- ")
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
            print(num1, "%", num2, "=", modulus(num1, num2))
        else:
            print("Invalid input")
        continue
    else:
        print ('Goodbye')
        break