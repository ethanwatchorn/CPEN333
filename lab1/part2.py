# student name: Ethan Watchorn
# student number: 16538530

# A command-line 2048 game
"""
    Note: Doesn't continue if there's still possible moves left... Double check that that's not part of p2...
"""
import random

board: list[list] = []  # a 2-D list to keep the current status of the game board

def init() -> None:  # Use as is
    """ 
        initializes the board variable
        and prints a welcome message
    """
    # initialize the board cells with ''
    for _ in range(4):     
        rowList = []
        for _ in range(4):
            rowList.append('')
        board.append(rowList)
    # add two starting 2's at random cells
    twoRandomNumbers = random.sample(range(16), 2)   # randomly choose two numbers between 0 and 15   
    # correspond each of the two random numbers to the corresponding cell
    twoRandomCells = ((twoRandomNumbers[0]//4,twoRandomNumbers[0]%4),
                      (twoRandomNumbers[1]//4,twoRandomNumbers[1]%4))
    for cell in twoRandomCells:  # put a 2 on each of the two chosen random cells
        board[cell[0]][cell[1]] = 2

    print(); print("Welcome! Let's play the 2048 game."); print()


def displayGame() -> None:  # Use as is
    """ displays the current board on the console """
    print("+-----+-----+-----+-----+")
    for row in range(4): 
        for column in range(4):
            cell = board[row][column] 
            print(f"|{str(cell).center(5)}", end="")
        print("|")
        print("+-----+-----+-----+-----+")


def promptGamerForTheNextMove() -> str: # Use as is
    """
        prompts the gamer until a valid next move or Q (to quit) is selected
        (valid move direction: one of 'W', 'A', 'S' or 'D')
        returns the user input
    """
    print("Enter one of WASD (move direction) or Q (to quit)")
    while True:  # prompt until a valid input is entered
        move = input('> ').upper()
        if move in ('W', 'A', 'S', 'D', 'Q'): # a valid move direction or 'Q'
            break
        print('Enter one of "W", "A", "S", "D", or "Q"') # otherwise inform the user about valid input
    return move

def addANew2Or4ToBoard() -> None:
    """ 
        adds a new 2 at an available randomly-selected cell of the board
    """

    added = 0
    is4 = random.random()
    while True and not added:
        is_empty_space = 0
        for i in range(len(board)):
            for j in range(len(board)):
                if not board[i][j]:
                    is_empty_space = 1
        if not is_empty_space:
            break

        rand_x = random.randint(0, 3)
        rand_y = random.randint(0, 3)

        # Look for rows/colums with only 1 empty space, just to make my life harder :)
        for y in range(len(board)):
            if board[y].count('') == 1:
                rand_y = y
        for x in enumerate(zip(board)):
            if x[1].count('') == 1:
                rand_x = x[0]

        if not board[rand_y][rand_x]:
            board[rand_y][rand_x] = 2 if is4 < 0.66 else 4
            added = 1
        else:
            pass

def isFullAndNoValidMove() -> bool:
    """ 
        returns True if no empty cell is left or there is no possible new move, False otherwise 
    """

    for i in range(len(board)):
        for j in range(len(board)):
            if not board[i][j]:
                return False
            if i > 0:
                if board[i][j] == board[i-1][j]:
                    return False
            if j > 0:
                if board[i][j] == board[i][j-1]:
                    return False


    return True

def getCurrentScore() -> int:
    """ 
        calculates and returns the current score
        the score is the sum of all the numbers currently on the board
    """

    score: int = 0

    for i in range(len(board)):
        for j in range(len(board)):
            if(board[j][i]):
                score += board[j][i]

    return score

def updateTheBoardBasedOnTheUserMove(move: str) -> None:
    """
        updates the board variable based on the move argument by sliding and merging
        the move argument is either 'W', 'A', 'S', or 'D'
        directions: W for up; A for left; S for down, and D for right
    """

    buffer = []

    # For up-down functionality
    if move == 'W' or move == 'S':
        if move == 'W':
            direction = 0 # Up
        else:
            direction = 1 # Down
        for y in range(len(board)):
            buffer = []
            for x in range(len(board[y])):
                buffer.append(board[x][y])
                
                if len(buffer) == 4:
                    buffer = squish(buffer, direction)
                    for i in range(len(board[y])):
                        board[i][y] = buffer[i]

    # For left-right funcitonality
    elif move == 'A' or 'D':
        if move == 'D':
            direction = 1 # Right
        else:
            direction = 0 # Left
        for y in range(len(board)):
            buffer = []
            for x in range(len(board[y])):
                buffer.append(board[y][x])
                
                if len(buffer) == 4:
                    buffer = squish(buffer, direction)
                    for i in range(len(board[y])):
                        board[y][i] = buffer[i]

    pass #to implement

#up to two new functions allowed to be added (if needed)
#as usual, they must be documented well
#they have to be placed below this line

def squish(input: list, direction: int) -> list:
    """
        Takes an input line and returns a 1x4 list that's been "squished"
        to one side depending on direction, adds any adjacent identical numbers.
        direction == 0: squish to first index
                  == 1: squish to last index
    """
    original_len = len(input)

    squish_buf = []

    if direction:
        input.reverse()

    for i in input:
        if i:
            squish_buf.append(i)

    i = 0

    while i < len(squish_buf):
        if i == len(squish_buf) - 1:
            break
        if squish_buf[i] == squish_buf[i+1]:
            squish_buf[i] = squish_buf[i]*2
            squish_buf = squish_buf[:i+1] + squish_buf[i+2:]
        i += 1

    input = squish_buf
    for i in range(original_len-len(squish_buf)):
        input.append('')
    if direction:
        input.reverse()

    return input

if __name__ == "__main__":  # Use as is  
    init()
    displayGame()
    while True:  # Super-loop for the game
        print(f"Score: {getCurrentScore()}")
        userInput = promptGamerForTheNextMove()
        if(userInput == 'Q'):
            print("Exiting the game. Thanks for playing!")
            break
        updateTheBoardBasedOnTheUserMove(userInput)
        addANew2Or4ToBoard()
        displayGame()

        if isFullAndNoValidMove(): #game is over once all cells are taken
            print("Game is Over. Check out your score.")
            print("Thanks for playing!")
            break