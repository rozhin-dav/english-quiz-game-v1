# English Quiz Game V1
# Created by Rozhin
# Python Beginner Project

print("===== English Quiz Game =====")

score = 0

# Question 1
answer1 = input("How many days are there in a week? ")

if answer1 == "7":
    print("Correct!")
    score += 1
else:
    print("Wrong!")
    print("The correct answer is 7.")

# Question 2
answer2 = input("What is the capital of England? ")

if answer2.lower() == "london":
    print("Correct!")
    score += 1
else:
    print("Wrong!")
    print("The correct answer is London.")

# Question 3
answer3 = input("How many months are there in a year? ")

if answer3 == "12":
    print("Correct!")
    score += 1
else:
    print("Wrong!")
    print("The correct answer is 12.")

print("\n===== Result =====")
print(f"Your score is {score} out of 3.")

if score == 3:
    print("Excellent!")
elif score == 2:
    print("Good job!")
elif score == 1:
    print("Keep practicing!")
else:
    print("Better luck next time!")
