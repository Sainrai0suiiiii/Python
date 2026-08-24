# ==========================================
# DAY 4 - PYTHON LISTS
# ==========================================


# 1. CREATE A LIST

fruits = ["Apple", "Banana", "Mango", "Orange"]

print(fruits)


# 2. ACCESS LIST ITEMS

print(fruits[0])   # Apple
print(fruits[1])   # Banana
print(fruits[-1])  # Orange


# 3. MODIFY A LIST ITEM

fruits[1] = "Grapes"

print(fruits)


# 4. ADD ITEMS TO A LIST

fruits.append("Watermelon")

print(fruits)


# 5. INSERT AN ITEM

fruits.insert(1, "Papaya")

print(fruits)


# 6. REMOVE AN ITEM

fruits.remove("Mango")

print(fruits)


# 7. REMOVE LAST ITEM

fruits.pop()

print(fruits)

# 8. LIST LENGTH

print("Total fruits:", len(fruits))


# 9. LOOP THROUGH A LIST

for fruit in fruits:
    print(fruit)


# 10. CHECK IF AN ITEM EXISTS

if "Apple" in fruits:
    print("Apple is available")
else:
    print("Apple is not available")


# 11. NUMBERS LIST

numbers = [10, 20, 30, 40, 50]

print("First:", numbers[0])
print("Last:", numbers[-1])


# 12. ADD ALL NUMBERS

total = 0

for number in numbers:
    total += number

print("Total:", total)


# 13. FIND THE LARGEST NUMBER

numbers = [12, 45, 7, 89, 23]

print("Largest:", max(numbers))


# 14. FIND THE SMALLEST NUMBER

print("Smallest:", min(numbers))


# 15. SORT A LIST

numbers = [50, 10, 30, 20, 40]

numbers.sort()

print(numbers)


# 16. REVERSE A LIST

numbers.reverse()

print(numbers)


# 17. LIST SLICING

numbers = [10, 20, 30, 40, 50, 60]

print(numbers[1:4])
# Output: [20, 30, 40]


# 18. COPY A LIST

new_numbers = numbers.copy()

print(new_numbers)


# 19. CLEAR A LIST

temp = [1, 2, 3]

temp.clear()

print(temp)


# 20. SIMPLE STUDENT MARKS

marks = [70, 85, 90, 65, 80]

print("Marks:", marks)
print("Highest:", max(marks))
print("Lowest:", min(marks))
print("Total:", sum(marks))
print("Average:", sum(marks) / len(marks))
