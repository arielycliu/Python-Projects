import Inventory
import Look

cur_place = "town"

while True:
    print("\nWhat would you like to do now?")

    command = input().split()
    cmd = command[0].lower()
    if cmd == "i" or cmd == "inventory":
        print("Currently in your bag you hold: ")
        Inventory.print_inventory()
    elif cmd == "x" or cmd == "examine":
        try:
            Inventory.examine_item_in_inventory(command[1])
        except:
            print("Huh, make sure to indicate which object to examine (e.g, x apple)")
    elif cmd == "l" or cmd == "look":
        print("Currently you are at: " + cur_place)
        Look.read_place_description(cur_place)
        Look.look_around(cur_place)
    elif cmd == "gt" or cmd == "go":
        try:
            print("You have arrived at: ")
            Look.read_place_description(command[2])
            cur_place = Look.read_place_name(command[2])
        except:
            print("Huh I can't find that place")
        try:
            print("You see a few rocks and... ")
            Look.read_place_items(command[2])
        except:
            print("You see nothing out of the ordinary")
    elif cmd == "pick":
        try:
            Look.pick_up_item(command[2], cur_place)    # since pick up is two words
            print("You successfully picked up: " + command[2])
        except:
            print("Huh, I can't find that item here")
    elif cmd == "drop":
        try:
            Look.drop_item(command[1], cur_place)
            print("You have successfully dropped: " + command[1])
        except:
            print("Huh, I can't drop that item here")
    elif cmd == "help":
        print("i: check inventory, x: examine something (must be in inventory), l: look around, gt: go to")
        print("You can also pick up and drop items")
    elif cmd == "swear":
        print("You let out a string of curses that would make your Uncle Rogers proud")