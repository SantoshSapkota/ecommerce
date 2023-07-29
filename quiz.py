print("Welcome my quiz game")
playing=input("Do you want to play game?" )
if playing !="yes":
    quit()
score=0
print("Okay i want to play")
answer=input("What does CPU Stand for?")
if answer=="central processing unit":
    print("Correct!")
    score+=1

else:
    print("Incorrect your answer!")
answer=input("What does MB stand for?")
if answer=="mega byte":
    print("Correct!")
    score+=1
else:
    print("Incorrect your answer!")
answer=input("What does GB Stand for ?")
if answer=="Giga byte":
    print("Correct!")
    score+=1
else:
    print("Incorrect your answer!")
answer=input("What does IC Stand for?")
if answer=="Intergrated Circuit":
    print("Correct!")
    score+=1
else:
    print("Incorrect your answer!")
print("You got " + str(score) + " Question correct!")
print("You got " + str((score/4) * 100) + "%")
