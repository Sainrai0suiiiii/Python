# ==========================================
# DAY 2 - PYTHON CONDITIONS
# ==========================================


# 1. Simple if statement

age = 20

if age >= 18:
    print("You are an adult.")


# 2. if - else

age = 16

if age >= 18:
    print("You can vote.")
else:
    print("You cannot vote yet.")


# 3. if - elif - else

marks = 75

if marks >= 80:
    print("Grade A")
elif marks >= 60:
    print("Grade B")
elif marks >= 40:
    print("Grade C")
else:
    print("Fail")


# 4. User Input + Conditions

age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible.")
else:
    print("You are not eligible.")


# 5. Even or Odd

number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")


# 6. Positive, Negative or Zero

number = int(input("Enter a number: "))

if number > 0:
    print("Positive number")
elif number < 0:
    print("Negative number")
else:
    print("Zero")


# 7. Comparison Operators

a = 10
b = 20

if a > b:
    print("A is greater")
elif a < b:
    print("B is greater")
else:
    print("Both are equal")


# 8. Logical AND

age = 25
has_license = True

if age >= 18 and has_license:
    print("You can drive.")
else:
    print("You cannot drive.")


# 9. Logical OR

day = "Saturday"

if day == "Saturday" or day == "Sunday":
    print("It's the weekend.")
else:
    print("It's a working day.")


# 10. Logical NOT

is_raining = False

if not is_raining:
    print("You don't need an umbrella.")
else:
    print("Take an umbrella.")


# 11. Multiple Conditions

username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "1234":
    print("Login successful")
else:
    print("Invalid username or password")


# 12. Nested if

age = int(input("Enter your age: "))

if age >= 18:

    has_id = input("Do you have an ID? (yes/no): ")

    if has_id == "yes":
        print("Entry allowed.")
    else:
        print("Please show your ID.")

else:
    print("You must be 18 or older.")