#name - METEHAN DAGSUYU
#Lab4MD.py
#blackjack
#------------------------------------
import random

#Syntax: make_deck()
#Parameter: None
#Return value: deck – a list of 52 shuffled cards
def make_deck():
    suit = ["H","C","D","S"]
    cards = ["A","2","3","4","5","6","7","8","9","T","J","Q","K"]
    deck = []
    for number in range(len(suit)):    #create deck
        for face in range(len(cards)):
            deck.append(cards[face]+suit[number])
    deck = ' '.join([str(w) for w in random.sample(deck, len(deck))])    #shuffle deck 
    deck = deck.split(" ")    #split deck
    return deck

#Syntax: deal_blackjack(deck, num_of_players)
#Parameter: deck – a deck of 52 shuffled cards
#           num_of_players – the number of players
#Return value: hands - a list of lists of cards, one list for each player
def deal_blackjack(deck, num_of_players):
    hands = []
    for current in range(0,num_of_players*2,2):    #increment for 2 cards per player
        player = [" "," "]    
        player[0] = str(deck[current]) 
        player[1] = str((deck[current+1]))
        hands.append(player)
    return hands


#Syntax: print_blackjack(hands)
#Parameter: hands – a list containing a list for each hand
#Return value: None
def print_blackjack(hands):
    for first in range(len(hands)):
        print(hands[first][0]+"\t", end = "")
    print("")
    for second in range(len(hands)):
            print(hands[second][1]+"\t", end = "")    
    print("")
        

#Syntax: get_max(hands, win = 0):
#Parameter: hands – a list containing a list for each hand
#           win - used when show_winner(hands) function is called, used to get index of winning players
#Return value: the value of the hand with the maximum value
def get_max(hands, win = 0):
    total_of_hands = []
    non_number = "ATJQK"
    for player in hands:
        first_card = player[0][0]
        second_card = player[1][0]
        if first_card in non_number:     
            first_card = 10
        if second_card in non_number:    
            second_card = 10
        total_of_hands.append(int(first_card) + int(second_card))
    if win == 1:
        return max_helper(total_of_hands, 1)
    return max_helper(total_of_hands)


#Syntax: max_helper(total_of_hands)
#Parameter: total_of_hands – a list containing totals of each players' hands
#           win - used when show_winner(hands) function is called, used to get index of winning players
#Return value: the value of the hand with the biggest value
def max_helper(total_of_hands, win = 0):
    biggest = 0
    for each in range(len(total_of_hands)):
        if total_of_hands[each] > biggest :
            biggest = total_of_hands[each]
    if win == 1:
        winner = []
        for i in range(len(total_of_hands)):
            if biggest == total_of_hands[i]:
                winner.append(i)
        return winner
    return biggest


#Purpose:  that prints out the hands and marks the winning hand with an asterisk
#Syntax: show_winner(hands)
#Parameter: hands –  a list containing a list for each hand
#Return value: none
def show_winner(hands):
    print_blackjack(hands)
    positions = get_max(hands, win = 1)
    new = ""
    for i in range(len(hands)):
        if i not in positions:
            new += "\t "
        else:
            new += "\t*"
    print(new[1:])
    
        
#Syntax: lab_four()
#Parameters: None
#Return value: None
def lab_four():
    deck = make_deck()
    print("\nMaking a deck...")
    hands = deal_blackjack(deck, 5)
    print("Dealing 5 hands...")
    print("\nPrinting out the hands...")
    print_blackjack(hands)
    print("\nShowing the winners...")    
    show_winner(hands)