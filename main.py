# This is a simple program to calculate how much each person in a group needs to pay, if you know the total bill and tip percentage.

print("Welcome to the tip calculator.")

#Get the total bill amount
total_bill = float(input("What was the total bill ($)? "))

#Get the total number of people in the group
people = int(input("How many people to split the bill? "))

#Get the tip percentage
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))

#Calculate the bill per person
bill_per_person = round(total_bill * (1+tip/100) / people,2)

#Print the result
print(f"Each person should pay: ${bill_per_person}")