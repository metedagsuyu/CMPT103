#name: mete
#lab: 12
#purpose: OOP
#-------------------------------------------------------------------------

#*********
#right num1, left num2, right num3


#purpose: sets up the lock so its ready for input
#parameters:
#return: 
class ComboLock:
    
    #------------------------------------------------------------------
    #purpose: initilize the variables that will be used
    #parameter: numeEntered1,2,3 are the ints for the combonation of the lock
    #return:    none 
    def __init__(self, num1, num2, num3):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3
        self.winning_Combo = ["r",num1,"l",num2,"r",num3]
        self.guessed_Combo = []
    #-----------------------------------------------------------------
    #purpose:  create string repr of class
    #parameter: none
    #return:    comboEntered: the 3 ints that make up the combonation
    def __repr__(self):
        comboEntered = 'ComboLock({}, {}, {})'.format(self.num1, self.num2, self.num3)
        return comboEntered

    #-----------------------------------------------------------------
    #purpose: sets up the lock so its ready for input
    #parameter: none
    #return:    none
    def reset(self):
        self.guessed_Combo = []
    
    #-----------------------------------------------------------------
    #purpose: turns absurd numbers into proper numbers
    #parameters: current_Num: a number thats the amount we will turn  
    #return : adjusted_Num: proper int between 0-59        
    def properNum(self, current_Num, right_left):
        if right_left == "left" and len(self.guessed_Combo) == 2:
            current_Num = self.guessed_Combo[1] - current_Num
        elif right_left == "right" and len(self.guessed_Combo) == 2:
            current_Num = self.guessed_Combo[1] + current_Num
        elif right_left == "left" and len(self.guessed_Combo) == 4:
            current_Num = self.guessed_Combo[3] - current_Num
        elif right_left == "right" and len(self.guessed_Combo) == 4:
            current_Num = self.guessed_Combo[3] + current_Num            
            
        while current_Num > 0:   #i hope they cant enter negative turns ...
            current_Num -= 60
        
        while current_Num < 0:   #i hope they cant enter negative turns ...
            current_Num += 60        
            
        adjusted_Num = current_Num
        
        if adjusted_Num == 60:
            return 0
        else:
            return adjusted_Num    
    
    #-----------------------------------------------------------------
    #purpose:   turn the dial current_Num amount to the left
    #parameter: current_Num: a number thats the amount we will turn  to the left
    #return:    none
    def turn_left(self, current_Num):
        adjusted_Num = self.properNum(current_Num, "left")
        self.guessed_Combo.extend(["l", adjusted_Num])
        
    #-----------------------------------------------------------------
    #purpose: turn the dial current_Num amount to the right
    #parameters: current_Num: a number thats the amount we will turn  to the right
    #return : none
    def turn_right(self, current_Num):
        adjusted_Num = self.properNum(current_Num, "right")
        self.guessed_Combo.extend(["r", adjusted_Num])
    
    #-----------------------------------------------------------------
    #purpose: checks if the lock is open by comparing winning combo,
    #         list with guessed combo list
    #parameters: none
    #return:  True if the lock is open, False otherwise
    def isopen(self):
        print("guess", self.guessed_Combo)
        print("winning", self.winning_Combo)
        return (self.winning_Combo == self.guessed_Combo)
    
    
    
 
# Do not modify these test functions
# However, you may write additional test functions
def test_combo_lock1():
    lock = ComboLock(25, 10, 0)
    assert str(lock) == 'ComboLock(25, 10, 0)' # __repr__ 
    assert not lock.isopen()
    
    # lock should open - basic
    lock.reset()
    lock.turn_right(25)
    lock.turn_left(15)
    lock.turn_right(50)
    assert lock.isopen()
       
    # lock should open - basic with reset in the middle
    lock.reset()
    lock.turn_right(35)
    lock.turn_left(5)
    lock.reset()
    lock.turn_right(25)
    lock.turn_left(15)
    lock.turn_right(50)
    assert lock.isopen()

    # lock should open - advanced 
    # the user turns the dial more than one full rotation
    lock.reset()
    lock.turn_right(85)
    lock.turn_left(135)
    lock.turn_right(50)
    assert lock.isopen()   
    
    # lock should not open - wrong combination
    lock.reset()
    lock.turn_right(15)
    lock.turn_left(25)
    lock.turn_right(10)
    lock.turn_left(24)    
    assert not lock.isopen()
 
    
def test_combo_lock2():    
    lock = ComboLock(40, 30, 5)
    assert str(lock) == 'ComboLock(40, 30, 5)' 
    assert not lock.isopen()
    
    # lock should open 
    lock.reset()
    lock.turn_right(40)
    lock.turn_left(10)
    lock.turn_right(35)
    assert lock.isopen()
    
    # lock should not open - wrong combination
    lock.reset()
    lock.turn_left(20)
    lock.turn_left(10)
    lock.turn_left(25)    
    assert not lock.isopen()
    
 
def test():
    test_combo_lock1()
    test_combo_lock2()
    print('passed all test cases...')
        
        
     
test()   #test my ComboLock class
