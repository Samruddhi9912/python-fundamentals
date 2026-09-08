import random

y = 0
c = 0
f = {
        "s" : "Snake",
        "w" : "Water",
        "g" : "Gun"
    }
while c<5 and y<5:
    computer = random.choice(["s", "w", "g"])
    you = input("Enter your choice: ")

    if you not in ["s","w","g"]:
        print("Invalid choices: please enter s , w or g")
        continue

    print(f"You chose {f[you]} \ncomputer chose {f[computer]}")

    if (you == computer):
        print("Its a draw")

    else:
        if (you == "s" and computer == "w"):
            print("You Won!")
            y += 1

        elif (you == "s" and computer == "g"):
            print("You Lose!")
            c += 1

        elif (you == "w" and computer == "s"):
            print("You Lose!")
            c += 1

        elif (you == "w" and computer == "g"):
            print("You Won!")
            y += 1

        elif (you == "g" and computer == "s"):
            print("You Won!")
            y += 1

        elif (you == "g" and computer == "w"):
            print("You Lose!")
            c += 1

        else:
            print("Error!!")

if y == 5:
    print(f"You won with {y} points")
else:
    print(f"Computer won with {c} points")