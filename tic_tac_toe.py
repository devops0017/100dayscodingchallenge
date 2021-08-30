import sys

def print_pattern(dict):
    print(
        f"{dict.get('7', ' ')}|{dict.get('8', ' ')}|{dict.get('9', '')}")
    print(f'-+-+-')
    print(
        f"{dict.get('4', ' ')}|{dict.get('5', ' ')}|{dict.get('6', '')}")
    print(f'-+-+-')
    print(
        f"{dict.get('1', ' ')}|{dict.get('2', ' ')}|{dict.get('3', '')}")

def restart_game(restart):
    if restart == 'y':
        total_slots = 9
        data_store.clear()
        print_pattern(data_store)
        return True
    else:
        sys.exit(1)


users = ['x','o']
data_store = {}

print_pattern(data_store)

total_slots = 9
while total_slots > 1:
    for user in users:
        while True:
            inp_1 = input(f'Enter your position {user}: ')
            if 1 > int(inp_1) or int(inp_1) > 9:
                print('Invalid choice','\n','Enter Number between 1-9')
                continue
            break
        if inp_1 not in data_store:
            data_store[inp_1] = user
            print_pattern(data_store)
        if data_store.get(inp_1) == data_store.get('1') == data_store.get('2') == data_store.get('3'):
            print(f'Game over..{user} has won the Game')
            restart = input(f'Do you want to play again y/n: ')
            if restart_game(restart):
                break
        elif data_store.get(inp_1) == data_store.get('4') == data_store.get('5') == data_store.get('6'):
            print(f'Game over..{user} has won the Game')
            restart = input(f'Do you want to play again y/n: ')
            if restart_game(restart):
                break
        elif data_store.get(inp_1) == data_store.get('7') == data_store.get('8') == data_store.get('8'):
            print(f'Game over..{user} has won the Game')
            restart = input(f'Do you want to play again y/n: ')
            if restart_game(restart):
                break
        elif data_store.get(inp_1) == data_store.get('7') == data_store.get('5') == data_store.get('3'):
            print(f'Game over..{user} has won the Game')
            restart = input(f'Do you want to play again y/n: ')
            if restart_game(restart):
                break
        elif data_store.get(inp_1) == data_store.get('1') == data_store.get('5') == data_store.get('9'):
            print(f'Game over..{user} has won the Game')
            restart = input(f'Do you want to play again y/n: ')
            if restart_game(restart):
                break
        elif data_store.get(inp_1) == data_store.get('1') == data_store.get('7') == data_store.get('4'):
            print(f'Game over..{user} has won the Game')
            restart = input(f'Do you want to play again y/n: ')
            if restart_game(restart):
                break
        elif data_store.get(inp_1) == data_store.get('2') == data_store.get('5') == data_store.get('8'):
            print(f'Game over..{user} has won the Game')
            restart = input(f'Do you want to play again y/n: ')
            if restart_game(restart):
                break
        elif data_store.get(inp_1) == data_store.get('3') == data_store.get('6') == data_store.get('9'):
            print(f'Game over..{user} has won the Game')
            restart = input(f'Do you want to play again y/n: ')
            if restart_game(restart):
                break
        total_slots = total_slots - 1
