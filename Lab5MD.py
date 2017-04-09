#name - Mete Dagsuyu
#celticaMD.py   -lab 5
#-------------------------


#purpose:       create the Celtica board
#Syntax:        setup_game()
#Return value:  board = list of characters representing the colour on the Celtica game board
def setup_game():
    board = ["G"] * 8 + ["R"] * 8 + ["Y"] * 8 + ["B"] * 8 + ["X"]
    return board


#purpose:       print the board, 
#               each print statement prints the section thats one below. top to bottom
#Syntax:        displayText(board)
#Parameter:     board: a list of characters representing the Celtica game board
#Return value:  None
def displayText(board):
    boardFormat = []
    
    boardFormat.append("".join(board[27:32]+ board[:4]))
    
    for repeat in range(3):
        boardFormat.append("".join([board[26-repeat]]+ [" "] *7 + [board[4+repeat]]))
        
    boardFormat.append("".join([board[23]] + [" "]*3 + [board[32]] + [" "]*3 + [board[7]]))  
    
    for repeat in range(3):
        boardFormat.append("".join([board[22-repeat]] + [" "]*7 + [board[8+repeat]]))
         
    boardFormat.append("".join(board[19:10:-1]))
    return boardFormat
    
#board = setup_game()
#displayText(board)
    


#Purpose:        swap the char in one location with the other
#Syntax:         exchange(board, first, second)
#Parameters:     board:    Celtica game board where the exchange takes place on
#                first:    index of the first marble being exchanged
#                second:   index of the second marble being exchanged
#Return value:   None
def exchange(board, first, second):
    locationOne = board[first]
    board[first] = board[second]
    board[second] = locationOne
    
    return board


#Purpose:       check if game is over by comparing the current board to the winning board
#Syntax:        is_game_over(board)
#Parameter:     board: Celtica game board
#Return value:  True if the board contains the winning configuration, False otherwise
def is_game_over(board):
    if board == ["G"] * 8 + ["R"] * 8 + ["Y"] * 8 + ["B"] * 8 + ["X"]:
        return True
    else:
        return False
    