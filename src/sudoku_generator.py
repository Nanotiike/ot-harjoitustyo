from random import shuffle, sample

def generate_sudoku():
    # Generate a random sudoku board
    # Return a 9x9 list
    # start with a fully made sudoku board
    board=[[1,2,3,4,5,6,7,8,9],
            [4,5,6,7,8,9,1,2,3],
            [7,8,9,1,2,3,4,5,6],
            [2,3,1,5,6,4,8,9,7],
            [5,6,4,8,9,7,2,3,1],
            [8,9,7,2,3,1,5,6,4],
            [3,1,2,6,4,5,9,7,8],
            [6,4,5,9,7,8,3,1,2],
            [9,7,8,3,1,2,6,4,5]]
    
    # shuffle the numbers. So for example 1 becomes 5, 2 becomes 9, etc.
    temp_board=[]
    numbers=[1,2,3,4,5,6,7,8,9]
    shuffled_numbers=sample(numbers, len(numbers))
    for i in range(9):
        temp_board.append([])
        for j in range(9):
            for k in numbers:
                if board[i][j]==k:
                    position_number=numbers.index(k)
                    temp_board[i].append(shuffled_numbers[position_number])

    board=temp_board
    temp_board=[]

    # shuffle the rows
    rows1 = sample([0,1,2], 3)
    rows2 = sample([3,4,5], 3)
    rows3 = sample([6,7,8], 3)
    rows = rows1+rows2+rows3
    for i in rows:
        temp_board.append(board[i])
    
    board=temp_board
    temp_board=[[],[],[],[],[],[],[],[],[]]

    # shuffle the columns
    columns1 = sample([0,1,2], 3)
    columns2 = sample([3,4,5], 3)
    columns3 = sample([6,7,8], 3)
    columns = columns1+columns2+columns3
    for i in columns:
        for j in range(9):
            temp_board[j].append(board[j][i])
    
    board.append(temp_board)
    temp_board=[]

    # shuffle the 3x rows
    rows=sample([0,3,6], 3)
    for i in rows:
        for j in range(3):
            temp_board.append(board[i+j])

    board=temp_board
    temp_board=[[],[],[],[],[],[],[],[],[]]

    # shuffle the 3x columns
    columns=sample([0,3,6], 3)
    for i in columns:
        for j in range(3):
            for k in range(9):
                temp_board[k].append(board[k][i+j])

    board=temp_board

    return board

generate_sudoku()