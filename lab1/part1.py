# student name: Ethan Watchorn
# student number: 16538530

# A command-line 2048 game

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

def addANewTwoToBoard() -> None:
    """ 
        adds a new 2 at an available randomly-selected cell of the board
    """

    # If no empty spaces, no point in adding a 2
    if isFull():
        return

    while True:
        # Generates a random coordinate on the board
        rand_x = random.randint(0, 3)
        rand_y = random.randint(0, 3)

        # If that random coordinate is empty, add the 2 and break the loop.
        # Otherwise, start again and look for a new space.
        if not board[rand_y][rand_x]:
            board[rand_y][rand_x] = 2
            break

def isFull() -> bool:
    """ 
        returns True if no empty cell is left, False otherwise 
    """

    # Loops through every space in the board.
    # If any space has no value, return false right away.
    for i in range(len(board)):
        for j in range(len(board)):
            if not board[i][j]:
                return False

    # Otherwise, the board is full.
    return True

def getCurrentScore() -> int:
    """ 
        calculates and returns the current score
        the score is the sum of all the numbers currently on the board
    """

    score: int = 0

    # Loops through every position on the board,
    # adds the value in the position to the sum.
    for i in range(len(board)):
        for j in range(len(board)):
            if(board[j][i]): # This checks to see if it's an empty space or not (can't add '' to an integer value)
                score += board[j][i]

    return score

def updateTheBoardBasedOnTheUserMove(move: str) -> None:
    """
        updates the board variable based on the move argument by sliding and merging
        the move argument is either 'W', 'A', 'S', or 'D'
        directions: W for up; A for left; S for down, and D for right
    """

    buffer = [] # Line buffer

    if move == 'W' or move == 'A':
        direction = 0 # Up (direction decides which way to squish the line, more on that later)
    else:
        direction = 1 # Down
    for y in range(len(board)):
        buffer = []
        for x in range(len(board[y])):
            
            # Adds values in one line to a buffer so we can squish it
            if move == 'A' or move == 'D':
                buffer.append(board[y][x]) # for left-right
            else:
                # Admittedly, this is messy. I'm switching rows and columns here,
                # so doing board[x][y] instead of board[y][x]. This is essentially transposing the board,
                # and that allows us to loop through colums rather than rows.
                buffer.append(board[x][y]) # for up-down, note the transposed [x][y] instead of [y][x]

            if len(buffer) == 4: # Once we know that we've iterated through the whole line, sqush the buffer.
                buffer = squish(buffer, direction) # squishes the given line in the corresponding direction
                for i in range(len(board[y])):
                    if move == 'A' or move == 'D':
                        board[y][i] = buffer[i] # Replaces the line in board by the squished buffer.
                    else:
                        board[i][y] = buffer[i]

#up to two new functions allowed to be added (if needed)
#as usual, they must be documented well
#they have to be placed below this line

def squish(input: list, direction: int) -> list:
    """
        Takes an input line and returns a 1x4 list that's been "squished"
        to one side depending on direction, adds any adjacent identical numbers.
        input: list = either a column or a row passed from the board
        direction: int = 0: squish to first index
                       = 1: squish to last index
        return value: list = squished row/column to replace values on the board
    """
    original_len = len(input) # Added this in case I wanted to mess around with different board sizes
    squish_buf = []

    # To make things easy on me, I only sqush the buffer in one direction.
    # If we indicate a reversed direction, we just flip the input and flip
    # it again after the  suish before returning the value.
    if direction:
        input.reverse()

    # Only add non-empty values to the squish_buffer
    for i in input:
        if i:
            squish_buf.append(i)

    i = 0
    while i < len(squish_buf):
        if i >= len(squish_buf) - 1: # If we've reached the end of the values, break out of the loop.
            break
        if squish_buf[i] == squish_buf[i+1]: # If the next value in the buffer is the same:
            squish_buf[i] = squish_buf[i]*2 # Multiply the current value by 2, 
            squish_buf = squish_buf[:i+1] + squish_buf[i+2:] # and remove that next value from the buffer entirely (so we don't end up adding it twice).
        i += 1 # move on to the next value in the buffer

    # Make sure the input is the same length as it was originally
    input = squish_buf
    for i in range(original_len-len(squish_buf)):
        input.append('')
    if direction:
        input.reverse() # Undo the direction swap

    return input # We done :)

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
        addANewTwoToBoard()
        displayGame()

        if isFull(): #game is over once all cells are taken
            print("Game is Over. Check out your score.")
            print("Thanks for playing!")
            break