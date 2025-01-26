print("Welcome to Treasure Island.\n Your mission is to find the treasure.")
direction = input("Choose direction: Left or Right? ")
if direction.upper() == "LEFT":
    second_stage = input("Choose: Swim or Wait ")
    if second_stage.upper()  == "WAIT":
        chosen_door = input("Find the treasure door: choose a single option between Red, Blue or Yellow ")
        if chosen_door.upper() == "YELLOW":
            print("You Win!!!!")
        else:
            print("Game Over")
    else:
        print("Game Over")
else:
    print("Game Over")