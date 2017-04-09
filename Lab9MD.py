#name - Mete Dagsuyu
#celticaMD.py   -lab 9
#-------------------------
import CelticaMDLab5 as C1
from graphics import *

global size, sHalf, board, boardformat

size = 500    #size of height and width, can be changed; minimum of 100
sHalf = size//2    #half of size
board = C1.setup_game()    #board: game board in list form
boardformat = C1.displayText(board)    #board in printable state


#purpose:     displays the Celtica game board in a graphical form
#syntax:      display(board)
#parameters:  board: game board in list form
#globals:     boardformat:check top of code
def display(board):
    global win, boardformat
    win = GraphWin("Celtica by BRB", size, size)
    sD20 = size/20
    
    topLeft = Rectangle(Point(10, 10), Point(sHalf-sD20, sHalf-sD20))
    topLeft.setFill("turquoise")
    
    topRight = Rectangle(Point(sHalf+sD20, 10), Point(size-10, sHalf-sD20))
    topRight.setFill("green") 
    
    bottomLeft = Rectangle(Point(10, sHalf+sD20), Point(sHalf-sD20, size-10))
    bottomLeft.setFill("orange2") 
    
    bottomRight = Rectangle(Point(sHalf+sD20, sHalf+sD20), Point(size-10, size-10))
    bottomRight.setFill("red3")  

    lineVertical = Rectangle(Point(sHalf-sD20, 0), Point(sHalf+sD20, size))
    lineVertical.setFill("navyblue")
    lineVertical.setOutline("navyblue")
    
    lineHorizontal = Rectangle(Point(0, sHalf-sD20), Point(size, sHalf+sD20))
    lineHorizontal.setFill("navyblue")
    lineHorizontal.setOutline("navyblue") 
    
    lineAround = Rectangle(Point(0, 0), Point(size, size))
    lineAround.setFill("navyblue")
    lineAround.setOutline("navyblue")        
    
    lineAround.draw(win)
    topLeft.draw(win)
    topRight.draw(win)
    bottomLeft.draw(win)
    bottomRight.draw(win)
    lineVertical.draw(win)
    lineHorizontal.draw(win)    
    
    circleList = [[0]*9]*9  
    circleColorList = [[""]*9]*9 
    for lines in range(9):   
        for marble in range(9):  
            boardLocation = boardformat[lines][marble]
            
            if boardLocation != " ":
                color = {boardLocation == "B": "blue",
                         boardLocation == "G": "lightgreen",
                         boardLocation == "Y": "yellow",
                         boardLocation == "R": "red",
                         boardLocation == "X": "black"
                        }[True] 
                
                circleColorList[lines][marble] = color
                
                x = (size//9)*marble+size/16.6
                y = (size//9)*lines+size/16.6
                circleList[lines][marble] = Circle(Point(x, y), size/21.4)
                circleList[lines][marble].setFill(color)
                circleList[lines][marble].setWidth(2)
                circleList[lines][marble].setOutline("white")
                circleList[lines][marble].draw(win)
            else:
                circleColorList[lines][marble] = " "
    return circleList


#Purpose:      check if move made is legal
#Syntax:       legalMove = is_legal_move(board, index)
#Parameters:   board = Celtica game board
#              index = index of the marble being clicked on
#Return value: True if the move is legal, False otherwise
def is_legal_move(board, index):
    if index in (7,15,23,31): 
        if board[32] == "X":
            return True
        elif board[index-1] == "X" or board[index+1] == "X":
            return True 
    elif index == 32:
        if "X" in [board[31],board[23],board[15],board[7]] :
            return True
        else:
            return False
    elif index != 32 and board[index+1] =="X":
        return True
    elif index != 0 and board[index-1] == "X":
        return True
    else:
        return False
        
    
#Purpose:      find the index of a marble with the help of global cx, cy
#Syntax:       index = find_Index()
#Globals:      cx, cy = x and y location of a click
#Return value: integer index in variable 'board' that holds the marble clicked
def find_Index():
    sD20 = size/20
    quadrant = {cy <= sHalf+sD20 and cx >= sHalf+sD20: 0,    #"green"
                cy >= sHalf+sD20 and cx >= sHalf-sD20: 8,    #"red"                
                cy >= sHalf-sD20 and cx <= sHalf-sD20: 16,   #"orange"
                cy <= sHalf-sD20 and cx <= sHalf+sD20: 24,   #"blue"
                cy >= sHalf-sD20 and cy <= sHalf+sD20 and 
                cx >= sHalf-sD20 and cx <= sHalf+sD20: 32    #"black"
                }[True]  
    
    xMarbleSize = cx//(size//9)
    yMarbleSize = cy//(size//9)
    
    if quadrant == 0 :
        if yMarbleSize == 0 : 
            return quadrant-5+xMarbleSize
        else:   
            return quadrant+3+yMarbleSize           
        
    elif quadrant ==8:
        if yMarbleSize == 8 : 
            return quadrant+11-xMarbleSize
        else:   
            return quadrant-5+yMarbleSize 
            
    elif quadrant ==16:
        if yMarbleSize == 8: 
            return quadrant+3-xMarbleSize
        else:   
            return quadrant+11-yMarbleSize  
            
    elif quadrant ==24:
        if yMarbleSize == 0 : 
            return quadrant+3+xMarbleSize
        else:   
            return quadrant+3-yMarbleSize
    else:
        return 32

#purpose: control the Celtica game
#syntax: main()
#globals: win: game window
def main():
    
    display(board)
    for i in range(100):  #later, change this to = while not gameOver:
        try:
            
            click = win.getMouse()        
            global cx, cy   #location x of click, location y of click
            cx = click.getX()
            cy = click.getY()
            
            #find index of marble thats clicked, print if its a legal move
            index = find_Index()
            print(is_legal_move(board, index))
            
        except:    #if X on window is clicked
            win.close()
            return    
            
    win.close()  

main()