import json
import Inventory

def read_places_and_stuff(): # returns dictionary of places
    try:
        with open("Places and stuff.json", "r") as file:  # Prep json for reading
            Place = json.load(file)  # Read json file convert to dictionary
    except:  # Nothing in inventory: empty file
        Place = {}

    return Place


def look_around():
    Place = read_places_and_stuff()
    print("Nearby you can see: ")
    for key in Place.keys():
        print("     " + key)
    print("To head somewhere or look close at each location use 'go to placename' ")

def read_place_name(examinePlace):
    Place = read_places_and_stuff()
    placeName = examinePlace.lower()
    return Place[placeName]["name"]

def read_place_description(examinePlace):
    Place = read_places_and_stuff()
    placeName = examinePlace.lower()
    print(Place[placeName]["description"])

def read_place_items(examinePlace):
    Place = read_places_and_stuff()
    placeName = examinePlace.lower()
    items = Place[placeName]["items"]
    for key in items.keys():
        print("    " + key)


def write_places_and_stuff(Place):
    with open("Places and stuff.json", "w") as file:  # Prep json for writing
        json.dump(Place, file, indent=4, sort_keys=True)  # Rewrite

def pick_up_item(item, place):
    Place = read_places_and_stuff()
    itemName = item.lower()
    place = place.lower()
    Inventory.add_item_to_inventory(Place[place]["items"][itemName])

    del Place[place]["items"][itemName]
    write_places_and_stuff(Place)


def drop_item(item, place):
    Place = read_places_and_stuff()
    itemName = item.lower()
    place = place.lower()

    # add item back into place
    Bag = Inventory.read_inventory()

    Place[place]["items"][itemName] = Bag[itemName]
    del Bag[itemName]
    write_places_and_stuff(Place)
    Inventory.write_inventory(Bag)