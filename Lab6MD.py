#name - Mete Dagsuyu
#celticaMD.py
#purpose: create a timer gui
#-------------------------

from graphics import *
import time


#Purpose: creates, draws, and returns a Text object
#         that can be used as a label within a window. 
#Syntax: label = add_label(window, x, y, text)
#Parameter: window - GraphWin object: the window
#           x, y - int values: location for centre of label
#           text - str object: text to use for label
#Return value: label - Text object used for the label
def add_label(window, x, y, text):
    text = Text(Point(x,y),text)
    if y > 90:
        text.setSize(36)
    text.draw(win)
    return text


#Purpose:  creates and draws a button.
#Syntax: button = add_button(window, x, y, text)
#Parameter: window - GraphWin object: the window
#           x, y : int values: location for centre of button
#           text : str object: text to use for button's label
#Return value: button : Rectangle object used for the button
def add_button(window, x, y, text):
    rect = Rectangle(Point(x-50, y-15), Point(x+50, y+15))
    rect.setFill("grey")
    rect.draw(win)
    label = Text(Point(x, y), text)
    label.draw(win)
    return rect
    
    
# Purpose: Check if a point is within the bounding box of button
# Syntax: bool = is_clicked(point, button)
# Parameters: point - Point object
#             button - Rectangle object 
# Return value: True if point is within the bounding box of button;
#               False, otherwise
def is_clicked(point, button):
    top_left = button.getP1()
    bottom_right = button.getP2()
    return (point.x >= top_left.x and point.x <= bottom_right.x and
            point.y >= top_left.y and point.y <= bottom_right.y)
    
#Purpose: creates, draws, and returns an entery box    
#Syntax: entry = add_entry(win, x, y, width)
#Parameter: win - GraphWin object: the window
#           x, y - int values: location for centre of entry
#           width - int value: width (in characters) of object
#Return value: entry - Entry object
def add_entry(win, x, y, width):
    entry = Entry(Point(x,y),width)
    entry.draw(win)
    return entry


#Pupose: flash the window for certain amount of times when timer reachers 0
#syntax: flash(win, times)
#Parameter: win - the window that everything takes place
#           times- the amount of times it will flash the window
#return None
def flash(win, times):
    for flashes in range(times):
        win.setBackground("black")
        time.sleep(.1)
        win.setBackground("white")
        time.sleep(.1)


#Purpose: converts the given time into seconds
#Syntax: convert_to_seconds(timeMid)
#Parameters: timeMid- the time given by user
#globals : msgAtTop : label above the entry box used to show msgs
#Return: totalSeconds- time in seconds
def convert_to_seconds(timeMid):
    totalSeconds = 0
    global msgAtTop
    try:
        if ":" in timeMid:
            timeNew = timeMid.split(":")
            if int(timeNew[0]) > 999: 
                return totalSeconds
            if timeNew[0] == "":
                return int(timeNew[1])
            else:
                totalSeconds += int(timeNew[0])*60 + int(timeNew[1])
                return totalSeconds
    
        else:
            return totalSeconds
        
    except:
        return totalSeconds
    return


#Purpose: converts the given seconds to clock time to display
#Syntax: convert_to_clock(secondsLeft)
#Parameters: secondsLeft- the seconds left on clock
#Return: secondsLeftClock - seconds left in clock time
def convert_to_clock(secondsLeft):
    try:
        minutes = int(secondsLeft) // 60
        seconds = int(secondsLeft) % 60
        if seconds < 10 and seconds >=0:
            seconds =  "0"+str(seconds)
        
        return str(minutes)+":"+ str(seconds)
    
    except:
        return "0:00"
    
    
#Purpose:  main creates the main graphics window, adds button
#          to it, and then begins a loop where it detects mouse clicks
#parameters: None
#syntax: main()
#globals: win: windows object
#         msgAtTop : label above the entry box used to show msgs
#Return None
def main():
    
    global win, msgAtTop
    #set up GUI
    win = GraphWin("Lab6",300,200)
    win.setBackground("white")
    timeMid = add_label(win,150,100, "0:00")
    msgAtTop = add_label(win,150,20,"Time (MMM:SS)")
    start = add_button(win,100,150, "Start/Restart")
    start.setFill("green")
    start.setOutline("green")
    exit = add_button(win,200,150, "Exit")
    exit.setFill("red")
    exit.setOutline("red")
    width = 20
    timeBox = add_entry(win,150,50,width)

    #'now' resets to proper time.time() value when start button is clicked
    now = 1000000000000000000000000000000    
    while True:
        try:
            timePast = abs(int(now-time.time()))
            if timePast < 60000:    #60000 is 1000 minutes, the max allowed
                displayTime = newTime - int(timePast)
                timeClock = convert_to_clock(displayTime)
                if displayTime <= 0:
                    timeMid.setText("0:00")
                    flash(win, 3)
                    now = 1000000000000000000000000000000                    
                else:
                    timeMid.setText(timeClock)
            point = win.checkMouse()
                
        except GraphicsError:
            return
        
        if point == None:
            continue    
        
        if is_clicked(point, start):
            timeEntered = timeBox.getText() 
            if timeEntered.strip() =="" or timeEntered.isalpha() or convert_to_seconds(timeEntered) == 0:
                msgAtTop.setText("Please enter proper time\nTime (MMM:SS)")
                msgAtTop.setSize(10)               
            else:
                msgAtTop.setText("Time (MMM:SS)")
                msgAtTop.setSize(12)                
                timeMid.setText(timeEntered)
                newTime = convert_to_seconds(timeMid.getText())
                timeMid.setText(newTime)
                now = time.time()
            
        elif is_clicked(point, exit):
            win.close()
            return     
main()