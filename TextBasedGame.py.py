# =========================
# Developer: Mohamed Hassan
# =========================


rooms = {
    'Great Hall': {'South': 'Basement', 'North': 'Dining room', 'East': 'Living room', 'West': 'Bedroom'},
    'Basement': {'North': 'Great Hall', 'East': 'Bathroom', 'item': 'pistol'},
    'Dining room': {'South': 'Great Hall', 'East': 'Kitchen', 'item': 'bulletproof'},
    'Living room': {'West': 'Great Hall', 'North': 'Storeroom', 'item': 'handcuffs'},
    'Bathroom': {'West': 'Basement', 'item': 'flashlight'},
    'Bedroom': {'East': 'Great Hall', 'item': 'cellphone'},
    'Kitchen': {'West': 'Dining room', 'item': 'knife'},
    'Storeroom': {'South': 'Living room', 'item': 'Thief'}
}


# show player location.
def show_player_location(location):
    if 'item' in rooms[location]:
        print(f"You are in {location}")
    else:
        print(f"You are in {location} and it is a empty.")

    directions(location)


def directions(location):
    print("Directions you can go:", end=' ')
    for direction in rooms[location].keys():
        if direction != 'item':
            print(direction, end=' ')
    print()


def get_user_direction(directions):
    user_input = input().title()
    direction = user_input[3:] if ' ' in user_input else user_input
    while direction not in directions and direction != 'Exit':
        print(f'You cannot go that way. Please go one of that available directions.')
        user_input = input().title()
        direction = user_input[3:] if ' ' in user_input else user_input

    return direction


def update_player_location(user_command, player_location, container):
    return rooms[player_location][user_command]


def retrieve_item(location, item_container):
    # Check item is in the room.
    if 'item' in rooms[location]:
        item = rooms[location]["item"]
        print(f'You are in {location}')
        print(f'You see {item}\nType \'get {item}\' to retrieve the item"')
        user_input = input()
        if item in user_input:
            print(f'{item} is retrieved.')
            item_container.append(rooms[location]['item'])
            print(item_container)
            # remove item from rooms.
            del rooms[location]['item']


def main_menu():
    player_location = 'Great Hall'
    user_command = ''
    item_container = []

    while True:
        show_player_location(player_location)
        user_command = get_user_direction(rooms[player_location].keys())

        if user_command == 'Exit':
            print('Thanks for playing. Please come back')
            break
        else:
            player_location = update_player_location(user_command, player_location, item_container)

        if player_location == 'Storeroom':
            print('Take your last breathe, you fool.\nGame over!')
            break
        else:
            retrieve_item(player_location, item_container)

        if len(item_container) == 6:
            print("Congrtulations! You caught the thief.")
            break


main_menu()
