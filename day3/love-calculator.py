# love calculator exercise

print("Welcome to Love calculator.")
name1 = input("What is your name?\n")
name2 = input("What is their name?\n")

combined_string = name1 + name2
combined_string_lower = combined_string.lower()

t = combined_string_lower.count("t")
r = combined_string_lower.count("r")
u = combined_string_lower.count("u")
e = combined_string_lower.count("e")

true = t + r + u + e

l = combined_string_lower.count("l")
o = combined_string_lower.count("o")
v = combined_string_lower.count("v")
e = combined_string_lower.count("e")

love = l + o + v + e

love_score = str(true) + str(love)
love_score = int(love_score)

if (love_score < 10) or (love_score > 90):
    print(f"Your love score is {love_score},you go together like coke and mentos.")
elif (love_score >= 40) and (love_score <= 50):
    print(f"Your love score is {love_score}, you are alright together.")
else:
    print(f"Your love score is {love_score}.")
