import Inventory
import Look

cur_place = ""

while True:
    print("\nWhat would you like to do now?")
    print("i: check inventory, x: examine something (must be in inventory), l: look around, gt: go to")
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
        Look.look_around()
    elif cmd == "gt" or cmd == "go":
        print("You have arrived at: ")
        Look.read_place_description(command[1])
        print("You see a few rocks and... ")
        Look.read_place_items(command[1])
        cur_place = Look.read_place_name(command[1])
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