# name    : Metehan Dagsuyu
# program : lab1 see part # for programs below

#part 1 start-------------------------------------------------------------------

#function below is called: print_right_aligned(TheList)
#parameter(TheList) is a list filled with strings of varying length
#it returns those same strings aligned to the right in a print statement
def print_right_aligned(TheList):
    
    length = max_length(TheList) #uses my max_length function to find the lengthiest string in 'TheList' and sets it to the variable 'length'
    for i in TheList: #for every data(string in this case) in 'TheList', it will do appropriate task below
        print((length-len(i))*" "+i) #this line uses the 'length' variable to assist in right aligning text and prints in on the screen
        
        
        
#function below is called: max_length(TheList)
#parameter(TheList) is a list filled with strings of varying length
#it returns 'length' which is the lengthiest string in 'TheList'       
def max_length(TheList):
    
    length = 0 #the variable 'length' is set to 0, it will be used to keep track of the lengthiest string
    for i in TheList: #for every data(string in this case) in 'TheList',  it will do appropriate task below
        if len(i) > length: #compare the length of current string to the length of the lengthiest string. 
            length = len(i) #if bigger; replace the current largest with this one
    return length #length is returned to the place it was called from to be used for other stuff

#part 1 end-------------------------------------------------------------------




#part 2 start-----------------------------------------------------------------

#function below is called: percent_odd(TheList)
#parameter(TheList) is a list filled with integers
#it returns the percentage of odd numbers from 'TheList' as a print statement
def percent_odd(TheList):
    total_ints= len(TheList) #checks the total number of integers in 'TheList'
    total_odd = count_odd(TheList) #uses the count_odd(TheList) function below to get the number of odd integers
    try: #trys to operations that are below in line 39 and 40
        percent = total_odd/total_ints*100 #this formula uses the number odd integers and the number total integers to give a percentage
        print(percent) #prints the percentage of odd numbers in 'TheList'
    except ZeroDivisionError: #this line checks if line 39 and 40 give the ZeroDivisionError,
        print("0.0") #if line 39 and 40 gives the ZeroDivisionError, this line prints off a statement
        
#function below is called: count_odd(TheList)
#parameter(TheList) is a list filled with integers
#it returns 'total_odd' which is the count of odd numbers in'TheList'
def count_odd(TheList):
    total_odd = 0 #sets the total number of odd ints to 0 as it might add some onto it in the future, after checking 'TheList'
    for i in TheList: #for every data in 'TheList' it will do the following once
        if i % 2 == 1 : #checks to see if the integer is even or odd by using the modulus function
            total_odd += 1 #if the integer is odd this line adds one to the total count of odd numbers
    return total_odd #returns 'total_odd' which is the total number of odd integers in 'TheList'

#part 2 end-------------------------------------------------------------------




#part 3 start-----------------------------------------------------------------

#function below is called: alternate(list1,list2)
#parameters :(list1,list2). 'list1' and 'list2' contain alternating elements, such as strings or integers, etc.
#it returns one list as a print statement. which basically merges 'list1'  and 'list2', ex:if  ' alternate([1, 2], ['a', 'b']) ' was inputed. it would print out ' [1, 'a', 2, 'b'] ' 
def alternate(list1,list2):
    short = short_list_finder(list1,list2) #uses the short_list_finder(list1,list2) below to get the length of the shortest list
    final_part = [] #create a list where the merged list will go
    for i in range(short): #for the range of shortest list, it will do the operations listed below 
        final_part.extend([list1[i]]) #adds the data from 'list1' thats in a certain location to the new list 'final_part'
        final_part.extend([list2[i]]) #adds the data from 'list2' thats in a certain location to the new list 'final_part'
    if len(list1) > short: #checks if length of'list1' is bigger than length of the shortest list
        for i in range(len(list1)-short): #for the range of the difference between the lengthiest string and the least lengthiest string do the following operations
            final_part.extend([list1[short+i]]) #adds the data from 'list1' thats in a certain location to the new list 'final_part'
    else:
        for i in range(len(list2)-short): #for the range of the difference between the lengthiest string and the least lengthiest string do the following operations
            final_part.extend([list2[short+i]]) #adds the data from 'list2' thats in a certain location to the new list 'final_part'        
    print(final_part) #returns 'final_part' which is the final merged list    

#function below is called: short_list_finder(list1,list2)
#parameters: (list1,list2). 'list1' and 'list2' contain alternating elements, such as strings or integers, etc.
#it returns the shortest length between 'list1'  and 'list2'.
def short_list_finder(list1,list2):
    if len(list1) > len(list2) : #compares the lengths of 'list1'  and 'list2'
        return len(list2) #if 'list1' is bigger, it returns the length of 'list2' 
    else:
        return len(list1) #otherwise if 'list2' is bigger, it returns the length of 'list1'
    
#part 3 end-----------------------------------------------------------------