print("Welcome to the Tip Calculator!")

bill = input("What is the total bill?? Rs ")
bill_as_float = float(bill)

tip = int(input("How much tip would you like to give?? 10,12,15?  "))
people = int(input("How many people to split the bill?  "))

bill_with_tip = (tip / 100) * bill_as_float + bill_as_float
split_bill = bill_with_tip / people
final_bill = "{:.2f}".format(split_bill)

print(f"Each person should pay Rs {final_bill} ")
