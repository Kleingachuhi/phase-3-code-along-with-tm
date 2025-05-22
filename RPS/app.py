import random

my_hand_can_be = ['Rock', 'Paper', 'Scissors']
my_hand  = random.choice(my_hand_can_be)

while True:
    my_input = input('What do you have on your hand:')
    if my_input == my_hand:
        confirmatory_input =input("Are you sure?(y/n)")
        print("Congratulations You have won!")
        if confirmatory_input =='n':
            break
        elif confirmatory_input != 'y':
            print("Unfortunately invalid, try again.")
            break
        break
    else:
        just_confirming = input("Are you sure?(y/n)")
        if just_confirming == 'n':
            break
        elif just_confirming != 'y':
            print("Unfortunately invalid, try again.")
            break
        print("Sorry try again!")
        break
