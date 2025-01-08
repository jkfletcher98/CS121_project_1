userName = input("What is your name?")
print(f"Hi, {userName}")
if userName.upper() == "ANDY":
    print("I'm looking forward to this semester with you")

keepGoing = True
while keepGoing:
    response = input("Do you think I'm going to do well in CS 121?")
    response = response.upper ()
    if response.startswith ("Y"):
        print("Thanks for the vote of confidence!")
        keepGoing = False
    elif response.startswith ("N"):
        print("Honestly, that's fair.")
        keepGoing = False
    else:
        print("I'm not sure I understand. Please answer 'yes' or 'no'.")

print("Thanks for talking with me!")
