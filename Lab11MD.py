

#name - Mete Dagsuyu
#celticaMD.py   -lab 9
#things added for bonus:
#                       - checks if the a circle is clicked, not just around it 
#                       celtica board is now a circle not a square, like the original
#                       outline of the clicked circle is changed briefly
#                       animation while switched marbles
#                       random isnt random cuz if it is then game might be unsolvable
#                                   instead computer moves the balck marble and swaps a certain number of times
#                       something cool when you win game
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
    
#Purpose:      draw the circles of the board on the window
#Syntax:       draw_circle()
#Globals:      board_format = formated text display version of the board
#Return value: circleList, circleColorList : list to hold circle objects, list to hold colors of those circle objects 
def draw_circle():
    circleList = [0]*(len(board)+1)         
    circleColorList = [" "]*(len(board)+1)   
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
                
                
                x = (size//9)*marble+size/16.6
                y = (size//9)*lines+size/16.6
                index = find_Index(x, y, marble, lines)
            
        
                circleColorList[index] = color
                circleList[index] = Circle(Point(x, y), size/21.4)
                circleList[index].setFill(color)
                circleList[index].setWidth(2)
                circleList[index].setOutline("white")
                circleList[index].draw(win)
            else:
                continue
    return circleList, circleColorList


#Purpose:      check if move made is legal
#Syntax:       legalMove = is_legal_move(board, index)
#Parameters:   board = Celtica game board
#              index = index of the marble being clicked on
#Return value: True if the move is legal, False otherwise
def is_legal_move(board, index):
    if index != None:
        if index in (7,15,23,31):  
            if board[32] == "X":
                return True
            elif board[index-1] == "X" or board[index+1] == "X":
                return True 
            elif index ==31  and board[0] == "X":
                return True
        elif index == 32:
            if "X" in [board[31],board[23],board[15],board[7]] :
                return True
            else:
                return False
        elif index == 0 and board[31] == "X":
            return True
        elif index != 32 and board[index+1] =="X":
            return True
        elif index != 0 and board[index-1] == "X":
            return True
        else:
            return False
    else:
        return False #click location isnt a circle
       
       
#Purpose:      check if click is in the closest circle
#Syntax:       in_Circle()
#Globals:      cx, cy = x and y location of a click
#              xMarbleLocation, = column of click
#              yMarbleLocation = row of click
#Return value: True if the click was in a circle, False otherwise      
def in_Circle():
    circleX = (size//9)*xMarbleLocation+size/16.6
    circleY = (size//9)*yMarbleLocation+size/16.6
    
    if xMarbleLocation ==0 or xMarbleLocation ==8 or yMarbleLocation == 0 or yMarbleLocation == 8: #edge of board
        return ((cx-circleX)**2 + (cy-circleY)**2 <= (size/21.4)**2)
    elif xMarbleLocation == 4 and yMarbleLocation == 4 :  #center of board        
        return ((cx-circleX)**2 + (cy-circleY)**2 <= (size/21.4)**2)
    else:
        return False
        

#Purpose:      find the index of a marble with the help of global cx, cy
#Syntax:       index = find_Index()
#Globals:      cx, cy = x and y location of a click
#              xMarbleLocation, = column of click
#              yMarbleLocation = row of click
#Return value: integer index in variable 'board' that holds the marble clicked
def find_Index(cx, cy, xMarbleLocation, yMarbleLocation):
    sD20 = size/20
    quadrant = {cy <= sHalf+sD20 and cx >= sHalf+sD20: 0,    #"green"
                cy >= sHalf+sD20 and cx >= sHalf-sD20: 8,    #"red"                
                cy >= sHalf-sD20 and cx <= sHalf-sD20: 16,   #"orange"
                cy <= sHalf-sD20 and cx <= sHalf+sD20: 24,   #"blue"
                cy >= sHalf-sD20 and cy <= sHalf+sD20 and 
                cx >= sHalf-sD20 and cx <= sHalf+sD20: 32    #"black"
                }[True]  
    
    
    if quadrant == 0 :
        if yMarbleLocation == 0 : 
            return quadrant-5+xMarbleLocation
        else:
            return quadrant+3+yMarbleLocation
    elif quadrant ==8:
        if yMarbleLocation == 8 : 
            return quadrant+11-xMarbleLocation
        else: 
            return quadrant-5+yMarbleLocation 
    elif quadrant ==16:
        if yMarbleLocation == 8: 
            return quadrant+3-xMarbleLocation
        else:   
            return quadrant+11-yMarbleLocation
    elif quadrant ==24:
        if yMarbleLocation == 0 : 
            return quadrant+3+xMarbleLocation
        else:  
            return quadrant+3-yMarbleLocation      
    else:
        return 32


#purpose: control the Celtica game
#syntax: main()
#globals: win: game window
def main():
    
    display(board)    
    circleList, circleColorList = draw_circle()
    #print(circleList)
    #print(circleColorList) 
    for i in range(100):  #later, change this to = while not gameOver:
        #try:
            
        click = win.getMouse() 
        #location x of click, location y of click
        global cx, cy
        cx = click.getX()
        cy = click.getY()
        
        #location of column of click, location row of click
        global xMarbleLocation, yMarbleLocation
        xMarbleLocation = cx//(size//9)
        yMarbleLocation = cy//(size//9)           
        
        #find index of marble thats clicked, print if its a legal move
        index = find_Index(cx, cy, cx//(size//9), cy//(size//9) )
        print("\nindex:" , index)
        print("black marble:", board.index("X"))
        if in_Circle():
            if is_legal_move(board, index):
                 
                color_of_clicked_circle = circleColorList[index] 
                location_of_black_marble = board.index("X")
                
                circleList[location_of_black_marble].setFill(color_of_clicked_circle)
                circleList[index].setFill("black")
                
                circleColorList[location_of_black_marble] = color_of_clicked_circle            
                circleColorList[index] = "black"
                board[board.index("X")], board[index] = board[index] , board[board.index("X")] #swap locations            
                print("move was succesfull")
            else:
                print("not a legal move")
        
        else:
            print("not a circle") 
            
            
            
            
            
            
            
           
            
        #except:    #if X on window is clicked, most likely
        #    win.close()
        #    return    
            
    win.close()  

main()