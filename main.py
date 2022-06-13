import random

while True:
    choice = input("Enter a choice (R, P, S): ")
    while choice != "R" and choice != "P" and choice != "S":
	    choice = (input("enter valid input: "))
    possible_choices = ["R", "P", "S"]
    computer_choice = random.choice(possible_choices)
    print(f"\nPlayer ({choice}): CPU ({computer_choice}).\n")
    
    if choice == computer_choice:
        print(f"Both players selected {choice}. It's a tie!")
    elif choice == "R":
        if computer_choice == "S":
            print("Rock smashes scissors! User wins!")
            break
        else:
            print("Paper covers rock! User loses.")
    elif  choice == "P":
        if computer_choice == "R":
            print("Paper covers rock! User wins!")
            break
        else:
            print("Scissors cuts paper! User lose.")
    elif choice == "S":
        if computer_choice == "P":
            print("Scissors cuts paper! User wins!")
            break
        else:
            print("Rock smashes scissors! User loses.")

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break
