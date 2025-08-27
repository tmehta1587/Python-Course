
number = int(input("Enter your number"))

original_number = number
reversed_number = 0

while number>0:
    digit = number % 10
    reversed_number = reversed_number * 10 + digit
    number = number //10

if original_number == reversed_number:
    print("It is a palindrome")

else: 
    print("This is not a palindrome")