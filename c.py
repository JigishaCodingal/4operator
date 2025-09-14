# Take marks as input from user
print("Enter Marks Obtained in 4 Subjects:")
math = int(input("Maths: "))
english = int(input("English: "))
science = int(input("Science: "))
hindi = int(input("Hindi: "))

# Calculate the total and percentage
total = math + english + science + hindi
print("Sum of Maths, English, Science and Hindi =", total)

percentage = (total / 400) * 100
print("Percentage Marks =", percentage)
