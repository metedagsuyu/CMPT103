# name: Metehan Dagsuyu
# program: Lab2MD.py


#part 1 start ------------------------------------
def loop_a():
    for i in range(20,33,3):
        print(i)

def loop_b():
    for i in range(7,-2,-2):
        print(i)
        
#part 1 end  -------------------------------------
        
#part 2 start -------------------------------------

#Purpose: Print a hollow diamond centered within a square of the specified width
#Syntax: hollow_diamond(width)
#Parameter: width: an even integer indicating the width of the square surrounding the diamond
#Return value: None

def hollow_diamond(width):
    middle = width//2 #assigns the middle number of the width to "middle"
    first_half(middle) #calls function
    second_half(middle) #calls function
    
#Purpose: Print the top half of the hollow diamond centered within a square of the specified width
#Syntax: first_half(middle)
#Parameter: middle: an even integer indicating the middle of the width
#Return value: none
def first_half(middle):
    for i in range(middle): #first half of the diamond
        print("*" * (middle-i), end="") #prints the left "*"s
        print(" " * i * 2, end="") #prints the spaces in the middle
        print("*" * (middle-i)) #prints the right set of "*"s
        
#Purpose: Print the bottom half of the hollow diamond centered within a square of the specified width
#Syntax: second_half(middle)
#Parameter: middle: an even integer indicating the middle of the width
#Return value: none       
def second_half(middle):
    for i in range(middle-1,-1,-1): #second half of the diamond
        print("*" * (middle-i), end="") #prints the left "*"s
        print(" " * i * 2, end="") #prints the spaces in the middle
        print("*" * (middle-i)) #prints the right set of "*"s
        
#part 2 end -------------------------------------

#part 3 start -----------------------------------
#Purpose: Print a full diamond with numbers
#Syntax: full_diamond(width)
#Parameter: width: an odd integer representing the widest part of the diamond
#Return value: None

def full_diamond(width):
    middle = width//2 #find the middle of width to print the top half then bottom half
    nums = "1" # make a string of one variable to start with
    for i in range(2,middle+2): #for the length of the 'middle+2' do operations below
        nums = str(i) + nums #at the start of the list add the new int
        mid_nums = nums.index("1") #find index of '1' so we know where the middle of the list 'nums' is
        nums =  nums[0: mid_nums+i:]+  str(i) + nums[mid_nums+i:] #add the new int to the right and left side of 1 
    first_part(middle,nums) #calls function below
    second_part(middle,nums) #calls function below
    
#Purpose: Print the top half of the full diamond
#Syntax: first_part(middle)
#Parameter: middle: an even integer indicating the middle of the width
#           nums : list of integers like in the description picture
#Return value: none
def first_part(middle,nums):
    mid_nums = nums.index("1") #find index of '1' so we know where the middle of the list 'nums' is
    for i in range(middle+1): #for the length of middle + 1 do the operations below
        print(" "*(middle-i),end="") #print the proper number of spaces before the ints start showing
        print(nums[mid_nums-i : mid_nums+i+1]) #using the str 'nums', print according ints
        
        
#Purpose: Print the bottom half of the full diamond
#Syntax: second_part(middle)
#Parameter: middle: an even integer indicating the middle of the width
#           nums : list of integers like in the description picture
#Return value: none  
def second_part(middle,nums):
    mid_nums = nums.index("1") #find index of '1' so we know where the middle of the list 'nums' is
    for i in range(middle-1,-2,-1): #for the length of middle + 1 do the operations below
        print(" "*(middle-i),end="") #print the proper number of spaces before the ints start showing
        print(nums[mid_nums-i : mid_nums+i+1]) #using the str 'nums', print according ints


#part 3 end -------------------------------------