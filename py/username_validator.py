'''
Problem Statement:
Take a username from the user.

Your program must check:

Length must be between 5 and 15
First character must be a letter
It must contain at least one number
It must not contain spaces
It must not contain special characters

'''

username = input("Enter a username: ")

if (len(username) < 5) :
    print("Username must have atleast 5 characters")
elif (len(username) > 15) :
    print("Username must not exceed 15 characters")
else:
    if not(username[0].isalpha()):
        print("Username must start with a letter")
    else:
        num = False
        for char in username:
            if char.isdigit():
                num = True
                break
        if (num == False):
            print("Username must contain atleast one number")
        else:
            if " " in username:
                print("Username must not contain spaces")
            else:
                if(username.isalnum() == False):
                    print("Username must not contain any special characters")
                else:
                    print(f"{username} is accepted")
