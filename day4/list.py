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


