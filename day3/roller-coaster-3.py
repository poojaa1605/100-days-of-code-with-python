# roller coaster exercise 3

print("Welcome to the roller coaster!!!")
height = int(input("What is your height in cm ?    "))

bill = 0
if height > 120:
    print("You can ride the roller coaster.")
    age = int(input("What is your age?  "))
    if age < 12:
        bill = 5
        print("Child tickets are $5")
    elif age <= 18:
        bill = 7
        print("Your tickets are $7")
    else:
        bill = 10
        print("Adult tickets are $10")
    wants_photo = input("Do you want a photo taken?Y or N    ").upper()
    if wants_photo == "Y":
        bill += 2
    print(f"Your final bill is $ {bill}")
else:
    print("Sorry,you have to grow taller before you can ride.")
