# Tic-tac-toe project.


# Greeting message
def greeting():
    print('──────────────────')
    print(' Tic-tac-toe game ')
    print('──────────────────')
    print(' Type coordinates ')
    print(" in 'x y' format  ")
    print(' where x is column')
    print(' and y is raw     ')
    print('──────────────────')


# Prints game field with coordinates
def print_field(fld):
    print(f'    0   1   2')
    print(f'  ┌───┬───┬───┐')
    for i in range(3):
        row = ' │ '.join(fld[i])
        print(f'{i} │ {row} │')
        if i < 2:
            print(f'  ├───┼───┼───┤')
    print(f'  └───┴───┴───┘')


# Request player for coordinates
def input_coords():
    while True:
        coords = input('Enter coordinates x y: ').split()
        # Pair check
        if len(coords) != 2:
            print('Enter two coordinates')
            continue

        _x, _y = coords
        # Digit check
        if not(_x.isdigit()) or not(_y.isdigit()):
            print('Enter digits')
            continue

        _x, _y = int(_x), int(_y)
        # Correct coordinates range check
        if 0 > _x or _x > 2 or 0 > _y or _y > 2:
            print('Coordinates out of range')
            continue
        # Correct cell for making move check
        if field[_y][_x] != ' ':
            print('Cell is already taken')
            continue

        return _x, _y


# Check game field for win conditions based on player move coordinates
def win_condition(_x, _y):
    player = field[_y][_x]
    # Check for X/O in picked cell
    if player == ' ':
        return False
    # Check field row
    line = set(field[_y])
    if len(line) == 1 and player in line:
        return True
    line.clear()
    # Check field column
    for i in range(3):
        line.add(field[i][_x])
    if len(line) == 1 and player in line:
        return True
    line.clear()
    # Check diagonals if picked cell is on diagonal position
    if _x == _y or _x + _y == 2:
        for i in range(3):
            line.add(field[i][i])
        if len(line) == 1 and player in line:
            return True
        line.clear()
        for i in range(3):
            line.add(field[i][2-i])
        if len(line) == 1 and player in line:
            return True
    return False


# Create empty initial field
field = [[' '] * 3 for i in range(3)]
# Counter of total turns left
counter = 9
# Turn flag. False is X turn, True is O turn
turn = False
# Print greeting message
greeting()
# Print initial field
print_field(field)

# Game process cycle. Game lasts while there's possible turns left
while counter > 0:
    if not turn:
        print("It's X's turn")
    else:
        print("It's O's turn")
    # Receive correct coordinates
    x, y = input_coords()
    # Add coordinates into game field
    if not turn:
        field[y][x] = 'X'
    else:
        field[y][x] = 'O'
    # Print new field
    print_field(field)
    # Check field state with current coordinates for winning conditions
    if win_condition(x, y):
        print(f'Player {"O" if turn else "X"} won!')
        break
    # Inverts player turn
    turn ^= True
    # Decrements game turns left
    counter -= 1

# If there is no turns left, then declares draw
if not counter:
    print('No cells left. Draw')
