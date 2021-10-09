# write your code here
figures = ('X', 'O')
empty_cell = " "


def init_grid_state():
    return [[empty_cell for _ in range(3)] for _ in range(3)]


# # Functions to analyze the game state


def is_full_grid(grid_state):
    for row in grid_state:
        for square in row:
            if square not in figures:
                return False

    return True


def is_victory(grid_state, figure):
    # check rows:
    for row in grid_state:
        counter = 0
        for square in row:
            if square != figure:
                break
            counter += 1
        if counter == 3:
            return True

    # check columns:
    col_index = 0
    while col_index <= 2:
        row_index = 0
        while row_index <= 2:
            if grid_state[row_index][col_index] != figure:
                break
            row_index += 1
        if row_index == 3:
            return True
        col_index += 1

    # Check 1-5-9 diagonal:
    col_index = 0
    row_index = 0
    while col_index <= 2 and row_index <= 2:
        if grid_state[row_index][col_index] != figure:
            break
        row_index += 1
        col_index += 1
    if col_index == 3:  # o row_index, da igual.
        return True

    # Check 7-5-3 diagonal:
    col_index = 0
    row_index = 2
    while col_index <= 2 and row_index >= 0:
        if grid_state[row_index][col_index] != figure:
            break
        col_index += 1
        row_index -= 1
    if col_index == 3:  # o row_index == -1, da igual.
        return True

    return False


def is_impossible(grid_state):
    if is_victory(grid_state, figures[0]) and is_victory(grid_state, figures[1]):
        return True

    num_fig_0 = 0
    num_fig_1 = 0
    for row in grid_state:
        num_fig_0 += row.count(figures[0])
        num_fig_1 += row.count(figures[1])
    if abs(num_fig_0 - num_fig_1) >= 2:
        return True

    return False


def analyze_state(grid_state):
    if is_impossible(grid_state):
        return 'Impossible'

    for figure in figures:
        if is_victory(grid_state, figure):
            return figure + ' wins'

    if is_full_grid(grid_state):
        return 'Draw'
    else:
        return 'OK'

# # END Functions to analyze the game state


def is_free_cell(grid_state, x, y):
    return grid_state[x-1][y-1] == empty_cell


def analyze_move_input(move_input, grid_state):
    if len(move_input.split()) != 2:
        return "You should enter two numbers between 1 and 3 separated by one space!"

    x_string, y_string = move_input.split()

    try:
        x = int(x_string)
        y = int(y_string)
    except ValueError:
        return "You should enter numbers!"

    if x > 3 or x < 1 or y > 3 or y < 1:
        return "Coordinates should be from 1 to 3!"

    if is_free_cell(grid_state, x, y):
        return 'OK'
    else:
        return "This cell is occupied! Choose another one!"


def extract_coordinates(move_input):
    x, y = list(map(int, move_input.split()))
    return x, y


def update_grid_state(grid_state, xy, current_figure):
    x, y = xy
    grid_state[x-1][y-1] = current_figure
    return grid_state


def change_current_figure(current_figure):
    if current_figure == figures[0]:
        return figures[1]
    else:
        return figures[0]


def print_grid(grid_state):
    print("---------")
    for row in grid_state:
        print('|', end=" ")
        for char in row:
            print(char, end=" ")
        print('|')
    print("---------")


gridState = init_grid_state()
currentFigure = figures[0]
print_grid(gridState)

while True:
    moveInput = input("Enter the coordinates: ")
    result = analyze_move_input(moveInput, gridState)
    if result == 'OK':
        gridState = update_grid_state(gridState, extract_coordinates(moveInput), currentFigure)
        stateResult = analyze_state(gridState)
        if stateResult == 'OK':
            currentFigure = change_current_figure(currentFigure)
            print_grid(gridState)
        else:
            print_grid(gridState)
            print(stateResult)
            break
    else:
        print(result)
