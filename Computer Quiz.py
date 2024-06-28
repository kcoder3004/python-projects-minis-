score = 0
print("Welcome to my Computer Quiz! ")

playing = input("Do you want to play? \n")

if playing.lower() != "yes":
    print("Okay See Ya!")
    quit()
print("Okay, Lets Play! :D")
answer = input("What does CPU stand for? \n")
if answer.lower() == "central processing unit":
    print("Correct! ")
    score += 1
else:
    print("Wrong! The correct answer is central processing unit!")

answer = input("What does GPU stand for? \n")
if answer.lower() == "graphics processing unit":
    print("Correct! ")
    score += 1
else:
    print("Wrong! The correct answer is graphics processing unit!")

answer = input("What does RAM stand for? \n")
if answer.lower() == "random access memory":
    print("Correct! ")
    score += 1
else:
    print("Wrong! The correct answer is random access memory!")

answer = input("What does PSU stand for? \n")
if answer.lower() == "power supply unit":
    print("Correct! ")
    score += 1
else:
    print("Wrong! The correct answer is power supply unit!")

if score < 2:
    performance = "Poorly"
elif score == 2:
    performance = "Average"
else:
    performance = "Excellent"

percentage = score/4 * 100
print(f"You got {score}/4 questions right! You did {performance} with {percentage}% accuracy!")
