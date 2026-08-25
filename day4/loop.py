# ==========================================
# PYTHON DAY 5 - LOOPS
# ==========================================

print("===== PYTHON DAY 5 =====")


# ------------------------------------------
# 1. FOR LOOP
# ------------------------------------------

print("\n1. FOR LOOP")

for number in range(1, 6):
    print("Number:", number)


# ------------------------------------------
# 2. LOOP THROUGH A LIST
# ------------------------------------------

print("\n2. LOOP THROUGH A LIST")

fruits = ["Apple", "Banana", "Mango", "Orange"]

for fruit in fruits:
    print(fruit)


# ------------------------------------------
# 3. RANGE FUNCTION
# ------------------------------------------

print("\n3. RANGE FUNCTION")

print("Numbers from 1 to 10:")

for number in range(1, 11):
    print(number)

# ------------------------------------------
# 4. EVEN NUMBERS
# ------------------------------------------

print("\n4. EVEN NUMBERS")

for number in range(1, 21):
    if number % 2 == 0:
        print(number)


# ------------------------------------------
# 5. ODD NUMBERS
# ------------------------------------------

print("\n5. ODD NUMBERS")

for number in range(1, 21):
    if number % 2 != 0:
        print(number)


# ------------------------------------------
# 6. WHILE LOOP
# ------------------------------------------

print("\n6. WHILE LOOP")

count = 1

while count <= 5:
    print("Count:", count)
    count += 1


# ------------------------------------------
# 7. SUM OF NUMBERS
# ------------------------------------------

print("\n7. SUM OF NUMBERS")

total = 0

for number in range(1, 11):
    total += number

print("Total:", total)


# ------------------------------------------
# 8. MULTIPLICATION TABLE
# ------------------------------------------

print("\n8. MULTIPLICATION TABLE")

number = int(input("Enter a number: "))

for i in range(1, 11):
    print(number, "x", i, "=", number * i)


# ------------------------------------------
# 9. BREAK
# ------------------------------------------

print("\n9. BREAK STATEMENT")

for number in range(1, 11):

    if number == 6:
        print("Loop stopped at:", number)
        break

    print(number)


# ------------------------------------------
# 10. CONTINUE
# ------------------------------------------

print("\n10. CONTINUE STATEMENT")

for number in range(1, 11):

    if number == 5:
        continue

    print(number)


# ------------------------------------------
# 11. FIND EVEN NUMBERS FROM USER INPUT
# ------------------------------------------

print("\n11. EVEN NUMBERS")

limit = int(input("Enter a limit: "))

for number in range(1, limit + 1):

    if number % 2 == 0:
        print(number)


# ------------------------------------------
# 12. SIMPLE COUNTDOWN
# ------------------------------------------

print("\n12. COUNTDOWN")

countdown = 5

while countdown > 0:
    print(countdown)
    countdown -= 1

print("Blast Off! 🚀")


# ------------------------------------------
# 13. SIMPLE PASSWORD CHECK
# ------------------------------------------

print("\n13. PASSWORD CHECK")

correct_password = "python123"
password = ""

while password != correct_password:
    password = input("Enter password: ")

    if password != correct_password:
        print("Wrong password! Try again.")

print("Access Granted!")


# ------------------------------------------
# 14. SUM FROM USER INPUT
# ------------------------------------------

print("\n14. SUM OF NUMBERS")

user_number = int(input("Enter a number: "))

total = 0

for i in range(1, user_number + 1):
    total += i

print("Sum from 1 to", user_number, "=", total)


# ------------------------------------------
# 15. MINI CHALLENGE
# ------------------------------------------

print("\n15. MINI CHALLENGE - NUMBER CHECKER")

number = int(input("Enter a number: "))

if number > 0:
    print("Positive Number")

elif number < 0:
    print("Negative Number")

else:
    print("Zero")

if number % 2 == 0:
    print("Even Number")

else:
    print("Odd Number")


# ==========================================
# END OF DAY 5
# ==========================================

print("\nCongratulations! You completed Python Day 5! 🎉")
