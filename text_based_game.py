import time

def start_game():
    print("Welcome to the Text Adventure Game!")
    time.sleep(1)
    print("You find yourself in a mysterious room.")
    time.sleep(1)
    print("There are two doors in front of you. Which one do you choose?")
    time.sleep(1)
    door_choice = input("Enter '1' for the left door or '2' for the right door: ")
    
    if door_choice == '1':
        enter_left_door()
    elif door_choice == '2':
        enter_right_door()
    else:
        print("Invalid input. Try again.")
        start_game()

def enter_left_door():
    print("You open the left door and find a treasure chest!")
    time.sleep(1)
    print("Congratulations! You have won the game.")

def enter_right_door():
    print("You open the right door and encounter a fierce dragon.")
    time.sleep(1)
    fight_choice = input("Do you want to 'fight' or 'run' away? ")
    
    if fight_choice.lower() == 'fight':
        print("You bravely fight the dragon but unfortunately get defeated. Game over.")
    elif fight_choice.lower() == 'run':
        print("You wisely choose to run away and escape the dragon. You survive!")
        time.sleep(1)
        print("You exit the room and find yourself in a corridor.")
        time.sleep(1)
        print("There are three more doors in front of you. Which one do you choose?")
        time.sleep(1)
        door_choice = input("Enter '1', '2', or '3': ")
        if door_choice == '1':
            enter_corridor_door1()
        elif door_choice == '2':
            enter_corridor_door2()
        elif door_choice == '3':
            enter_corridor_door3()
        else:
            print("Invalid input. Try again.")
            enter_right_door()
    else:
        print("Invalid input. Try again.")
        enter_right_door()

def enter_corridor_door1():
    print("You open the door and find a room filled with puzzles.")
    time.sleep(1)
    puzzle_choice = input("Do you want to 'solve' the puzzles or 'skip' them? ")
    
    if puzzle_choice.lower() == 'solve':
        print("You successfully solve all the puzzles and find a key.")
        time.sleep(1)
        print("You exit the room and find another corridor.")
        time.sleep(1)
        print("There are two more doors in front of you. Which one do you choose?")
        time.sleep(1)
        door_choice = input("Enter '1' or '2': ")
        if door_choice == '1':
            enter_final_door()
        elif door_choice == '2':
            enter_corridor_door2()
        else:
            print("Invalid input. Try again.")
            enter_corridor_door1()
    elif puzzle_choice.lower() == 'skip':
        print("You choose to skip the puzzles and proceed.")
        time.sleep(1)
        print("Unfortunately, a trap is triggered, and you get trapped. Game over.")
    else:
        print("Invalid input. Try again.")
        enter_corridor_door1()

def enter_corridor_door2():
    print("You open the door and find a room full of treasures.")
    time.sleep(1)
    print("You collect as many treasures as you can and feel rich.")
    time.sleep(1)
    print("You exit the room and find another corridor.")
    time.sleep(1)
    print("There are two more doors in front of you. Which one do you choose?")
    time.sleep(1)
    door_choice = input("Enter '1' or '2': ")
    if door_choice == '1':
        enter_corridor_door1()
    elif door_choice == '2':
        enter_final_door()
    else:
        print("Invalid input. Try again.")
        enter_corridor_door2()

def enter_corridor_door3():
    print("You open the door and find a room with a sleeping giant.")
    time.sleep(1)
    action_choice = input("Do you want to 'sneak' past the giant or 'fight' it? ")
    
    if action_choice.lower() == 'sneak':
        print("You successfully sneak past the giant and enter another corridor.")
        time.sleep(1)
        print("There are two more doors in front of you. Which one do you choose?")
        time.sleep(1)
        door_choice = input("Enter '1' or '2': ")
        if door_choice == '1':
            enter_corridor_door1()
        elif door_choice == '2':
            enter_final_door()
        else:
            print("Invalid input. Try again.")
            enter_corridor_door3()
    elif action_choice.lower() == 'fight':
        print("You try to fight the giant but get crushed. Game over.")
    else:
        print("Invalid input. Try again.")
        enter_corridor_door3()

def enter_final_door():
    print("You open the door and find a shining portal.")
    time.sleep(1)
    print("You step into the portal and are transported to another world.")
    time.sleep(1)
    print("Congratulations! You have completed the game!")

start_game()
