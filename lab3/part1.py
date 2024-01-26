#student name: Ethan Watchorn
#student number: 16538530
#Lab 3 (part 1)

def checkColumn(puzzle: list, column: int):
    """ 
        param puzzle: a list of lists containing the puzzle 
        param column: the column to check (a value between 0 to 8)

        This function checks the indicated column of the puzzle, and 
        prints whether it is valid or not. 
        
        As usual, this function must not mutate puzzle 
    """
    # In order to quickly check each column, it's easiest to gather values into one list
    buffer = []
    # Loop through every row, and put each value in the desired column into the check buffer
    for i in range(len(puzzle)):
        buffer.append(puzzle[i][column])

    # Now that we have the check buffer, check for values 1-9
        # If we detect that one of the values is missing, set the flag to false and immediately stop the loop
        # Otherwise, keep checking the rest of the values.
    is_good=1
    for i in range(1, len(buffer)+1):
        if i not in buffer:
            is_good = 0
            break

    # If the flag was never changed, then we know that each value is present in the column.
    if is_good:
        print("Column ", column, " valid")
    else:
        print("Column ", column, " not valid")

def checkRow(puzzle: list, row: int):
    """ 
        param puzzle: a list of lists containing the puzzle 
        param row: the row to check (a value between 0 to 8)

        This function checks the indicated row of the puzzle, and 
        prints whether it is valid or not. 
        
        As usual, this function must not mutate puzzle 
    """
    # Similar implementation to checkCol, but easier since each row is already a separate list
    #(therefore do not need the check buffer).
    is_good=1
    for i in range(1, len(puzzle[row])+1):
        if i not in puzzle[row]:
            is_good = 0
            break

    if is_good:
        print("Row ", row, " valid")
    else:
        print("Row ", row, " not valid")

def checkSubgrid(puzzle: list, subgrid: int):
    """ 
        param puzzle: a list of lists containing the puzzle 
        param subgrid: the subgrid to check (a value between 0 to 8)
        Subgrid numbering order:    0 1 2
                                    3 4 5
                                    6 7 8
        where each subgrid itself is a 3x3 portion of the original list
        
        This function checks the indicated subgrid of the puzzle, and 
        prints whether it is valid or not. 
        
        As usual, this function must not mutate puzzle 
    """
    # Similar implementation to checkCol, but the process of populating the check buffer is slighlty harder
    # This converts the subgrid into a 3x3 coordinate format
    subgrid_row = subgrid//3
    subgrid_col = subgrid%3
    buffer = []
    # Loop through a 3x3 grid in puzzle, but depending on the subgrid_row/col values:
    # the grid will be offset by multiples of 3
    for i in range(subgrid_row*3, 3+subgrid_row*3):
        for j in range(subgrid_col*3, 3+subgrid_col*3):
            buffer.append(puzzle[i][j])

    # Everything from here on out is the same as the other two functions.
    is_good=1
    for i in range(1, len(buffer)+1):
        if i not in buffer:
            is_good = 0
            break

    if is_good:
        print("Subgrid ", subgrid, " valid")
    else:
        print("Subgrid ", subgrid, " not valid")


if __name__ == "__main__":
    test1 = [ [6, 2, 4, 5, 3, 9, 1, 8, 7],
              [5, 1, 9, 7, 2, 8, 6, 3, 4],
              [8, 3, 7, 6, 1, 4, 2, 9, 5],
              [1, 4, 3, 8, 6, 5, 7, 2, 9],
              [9, 5, 8, 2, 4, 7, 3, 6, 1],
              [7, 6, 2, 3, 9, 1, 4, 5, 8],
              [3, 7, 1, 9, 5, 6, 8, 4, 2],
              [4, 9, 6, 1, 8, 2, 5, 7, 3],
              [2, 8, 5, 4, 7, 3, 9, 1, 6]
            ]
    test2 = [ [6, 2, 4, 5, 3, 9 , 1, 8, 7],
              [5, 1, 9, 7, 2, 8, 6, 3, 4],
              [8, 3, 7, 6, 1, 4, 2, 9, 5 ],
              [6, 2, 4, 5, 3, 9 , 1, 8, 7],
              [5, 1, 9, 7, 2, 8, 6, 3, 4],
              [8, 3, 7, 6, 1, 4, 2, 9, 5 ],
              [6, 2, 4, 5, 3, 9 , 1, 8, 7],
              [5, 1, 9, 7, 2, 8, 6, 3, 4],
              [8, 3, 7, 6, 1, 4, 2, 9, 5 ]
            ]
    
    testcase = test1   #modify here for other testcases
    SIZE = 9

    for col in range(SIZE):  #checking all columns
        checkColumn(testcase, col)
    for row in range(SIZE):  #checking all rows
        checkRow(testcase, row)
    for subgrid in range(SIZE):   #checking all subgrids
        checkSubgrid(testcase, subgrid)
