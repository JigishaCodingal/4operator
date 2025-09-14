# Taking total amount as input from user
amount = int(input("Please Enter Amount for Withdraw: "))

# Calculating the number of notes of different denominations
note_100 = amount // 100
note_50 = (amount % 100) // 50
note_10 = (amount % 50) // 10

# Displaying the result
print("Notes of 100 rupee:", note_100)
print("Notes of 50 rupee:", note_50)
print("Notes of 10 rupee:", note_10)
