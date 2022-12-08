# ========================
# Developer: Mohamed Hassan
# =========================
container = []
commands = []

print(
    'Welcome To Thief Catching Game\nYou will need to collect Six items from'
    '\nsix different rooms to catch the thief or you will be defeated.')
print('\n-----------------------------------------------------')

player_location = 'Great Hall'
possible_moves = ''


def nCharacter(chars, length):
    characters = ''
    for num in range(0, length):
        characters += chars
    return characters


def show_instructions():
    command_char_length = 0

    possible_moves = rooms[player_location].keys()
    print(f'You are in: {player_location}')
    print('Move Commands: ', end='')
    for key in rooms[player_location].keys():
        command = ('Go ' + key).title()
        print(command, end=' ')
        commands.append(command)
        command_char_length += len(command) + 1  # each word's length plus 1, which is for the length for each
        # space for between words.
    print()
    print( nCharacter('-', command_char_length + 14))
    print("Enter your move:\n")
    command = input()
    return command.title()


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



# main game loop

if __name__ == '__main__':
    user_command = show_instructions()
    print(user_command)
    while user_command != 'Exit':

        if user_command in commands:  # check if user entered valid a move.

            player_location = rooms[player_location][user_command[3:]]  # if user entered valid move, update user
            # location.
            # directions = rooms[player_location].keys()  # show the direction a user can go to.

            if player_location == 'Storeroom' and len(container) != 6:
                print('Take your last breathe, you fool.\nGame over!')
                break  # game ends if user enters thief's room without collecting all items.

            elif 'item' not in rooms[player_location]:  # if the key 'item' isn't in player's, it meas the room is
                # empty.
                print(f'You are in: {player_location}')
                print('The room you are in is empty.')
                user_command = show_instructions()

            else:
                # show the room user is in and item in the room.
                print(f'You are in: {player_location}\nYou see {rooms[player_location]["item"]}')
                # prompt user to get the item or move on .
                action = input(
                    'Type \'get {}\' if you to take it or \'exit\' to move on:\n'.format(
                        rooms[player_location]['item'])).strip().lower()

                item = ('get {}'.format(rooms[player_location]['item']))

                # This inner loop is responsible for user's item command. user has the choice to get the item or not.
                while True:
                    if action == 'exit':
                        break  # exit inner loop.

                    elif action != item:
                        print('Item name is incorrect.')
                        action = input(
                            'Type \'get {}\' if you to take or \'exit\' to move on:\n'.format(
                                rooms[player_location]['item']))

                    elif item == action:
                        container.append(rooms[player_location]['item'])
                        print(rooms[player_location]['item'], ' is retrieved')
                        print(f'Inventory: {container}')
                        del rooms[player_location]['item']
                        break  # get out inner loop.
                if len(container) == 6:
                    print('Congratulations! You defeated the thief.\nThanks for playing. Hope you enjoyed it')
                    break  # player won. end of game.

                    #  remove 'item' from the list possible directions because item isn't a direction.
                if 'item' in possible_moves:
                    print(f'Directions you can go:', commands[:-1])
                    user_command = show_instructions()
                else:
                    user_command = show_instructions()
        else:
            print('You can not go that way.')

            if 'item' in rooms[player_location]:  # remind the user the item, if user enters invalid direction
                user_command = show_instructions()

            else:  # if user already retrieved the item that was in the room the player is in it,
                # remind that the room is empty.
                print('It is empty room.')
                user_command = show_instructions()
