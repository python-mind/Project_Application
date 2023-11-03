import random

def Rules(Robot, You):
    if Robot == You:
        return None
    elif Robot == "r":
        if You == "p":
            return True
        elif You=="s":
            return False

    elif Robot == "p":
        if You == "s":
            return True
        elif You=="r":
            return False

    elif Robot == "s":
        if You == "r":
            return True
        elif You=="p":
            return False


print("Robot  : Rock(R)\t Paper(P)\t Scissors(S) ?")
robot_random =  random.randint(1,3)

if robot_random == 1:
    Robot = "r"

elif robot_random == 2:
    Robot = "p"

elif robot_random == 3:
    Robot = "s"
q = True
while q:
    You = input("You\t   : Rock(R)\t Paper(P)\t Scissors(S) ?")
    You = You.lower()
    if You == "r" or You == "p" or You == "s":
        a = Rules(Robot,You)

        print(f"Robot Choice : {Robot}")
        print(f"You Choice: {You}")

        if a == None:
            print("*********** It's a Tie ! ***********")
        elif a:
            print("*********** You Win! ***********")
        else:
            print("*********** You Lose! ***********")
        p = input("\n\nPress 'y' to continue or Press 'q' to Quite")
        if p == "q":
            q = False
        elif p == 'Y':
            q = True
            continue
        else:
            print("Wrong Input... !")

    else:
        print("***Wrong Choice!***\n\n")
