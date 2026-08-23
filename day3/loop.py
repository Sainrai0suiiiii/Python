# ==========================================
# DAY 3 - PYTHON LOOPS
# ==========================================


# 1. FOR LOOP

for i in range(5):
    print(i)


# Output:
# 0
# 1
# 2
# 3
# 4


# 2. RANGE WITH START AND END

for i in range(1, 6):
    print(i)


# 3. RANGE WITH STEP

for i in range(0, 11, 2):
    print(i)


# 4. LOOP THROUGH A STRING

name = "Python"

for letter in name:
    print(letter)


# 5. PRINT MULTIPLICATION TABLE

number = int(input("Enter a number: "))

for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")


# 6. WHILE LOOP

count = 1

while count <= 5:
    print(count)
    count += 1


# 7. SUM OF NUMBERS USING WHILE

number = 1
total = 0

while number <= 5:
    total += number
    number += 1

print("Total:", total)


# 8. BREAK STATEMENT

for i in range(1, 10):

    if i == 5:
        break

    print(i)


# 9. CONTINUE STATEMENT

for i in range(1, 6):

    if i == 3:
        continue

    print(i)


# 10. SKIP EVEN NUMBERS

for i in range(1, 11):

    if i % 2 == 0:
        continue

    print(i)

# 11. FIND A NUMBER

numbers = [10, 20, 30, 40, 50]

search = int(input("Enter a number to search: "))

for number in numbers:

    if number == search:
        print("Number found!")
        break

else:
    print("Number not found!")


# 12. SIMPLE LOGIN ATTEMPTS

attempts = 0

while attempts < 3:

    password = input("Enter password: ")

    if password == "python123":
        print("Login successful!")
        break

    else:
        print("Incorrect password!")
        attempts += 1

else:
    print("Too many attempts!")
