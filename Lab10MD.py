#name: Metehan Dagsuyu
#lab: 10
#topic: recursion
#-------------------------------
from graphics import *

#purpose: find the first 'n'sum of the reciprocals
#syntax: sum_to(n)
#parameters: n: an integer used to loop thru
#return: sum of the firstn reciprocals
def sum_to(n):
    if n == 0:
        return 0.0
    elif n == 1:
        return 1.0
    else:
        return 1.0/n + sum_to(n-1)
    
    
#purpose: draws the Cantor set on a GraphWin object.
#syntax: drawCantor(win, start_pt, length, color)
#globals: win : the current windows object
#parameters: length: the length of the current line
#            start_pt: starting point of the line, th most left
#            color: color of the line
#return: None if cantor set length reaches 1 or less. to stop the recursion
def drawCantor(start_pt, length, color):
    if length < 1:
        return
    
    line = add_line(start_pt.x, start_pt.y, length, color)
    length = length // 3
    
    drawCantor(Point(start_pt.x, start_pt.y + 50), length, "purple")
    drawCantor(Point(start_pt.x + length * 2, start_pt.y + 50), length, "purple")
    
    
#purpose: creates a line object for the cantor set
#syntax: add_line(x, y, length, color)
#parameters: length: the length of the current line
#            x,y: the x and y location of the point
#            color: color of the line.
#return: a line object
def add_line(x, y, length, color):
    line = Line(Point(x, y), Point(x+length, y))
    line.setFill(color)
    line.setWidth(3)
    line.draw(win)
    return line

    
#purpose: shows that the program works properly
#syntax: main()
#globals: win, width: window, width of the window
def main():
    global win, width, offset
    offset = 10
    width = 900
    win = GraphWin("Cantor Set", width, 300) 
    drawCantor( Point(5, offset), width-offset*2, "purple2")     #show the cantor set   
    
    try:
        click = win.getMouse()
        win.close()
    except:
        win.close()


#purpose: find unique elements within nested lists of lists
#syntax: extract_unique_elements(nested_lists)
#parameters: nested_lists: list containing lists of nested lists and other data structures
#return: unique_elements: all the unique elements found withing lists
global all_elements
all_elements = []
def extract_unique_elements(nested_lists):
    if isinstance(nested_lists, list) or isinstance(nested_lists, tuple):  #continue recursively looping
        for each in nested_lists:
            extract_unique_elements(each)
    else:   #if it isnt a list or tuple append element to 'all_elements'
        all_elements.append(nested_lists) 
    unique_elements = set(all_elements)    
    return unique_elements

"""
#why does it not reset the return value, in the console, it works properly if you press the green arrow after each statement below
print(extract_unique_elements([[3, [3, [[3]]]]]))
print(extract_unique_elements([2, [[2, 4, 5]], 'c', [[['c', 'd']]]]))
print(extract_unique_elements([2, 2, 3, [[[3]]]]))
print(extract_unique_elements([[[[5, 5]]]]))
print(extract_unique_elements([2]))
"""