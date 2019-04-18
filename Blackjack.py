#This program simulates the card-based game Blackjack. When playing Blackjack, the hand that’s value is as close to 21 as possible
without going over wins. 
To ‘hit’ is to ask for another card for your hand and to ‘stand’ is to end your turn.
#By: Diana Hakim
#12.10.2018

print("Welcome this is my BlackJack Game")
def shuffleDeck(): #tested
    'create a random deck of 52 cards'
    import random
    # suits is a set of 4 Unicode symbols for suits
    
    suits = {'\u2660', '\u2661', '\u2662', '\u2663'}
    ranks = {'2','3','4','5','6','7','8','9','10','J','Q','K','A'}
    deck = []
    
    # create deck of 52 cards
    
    for suit in suits:
        for rank in ranks: # create deck of 52 cards that contain ranks and suits
            deck.append(rank + suit) # put rank & suit togther
            
    # shuffle the deck and return
    
    random.shuffle(deck)
    return deck




def dealCard(deck, player): #tested
    'deal card to play and remove card from deck'
    
    card = deck.pop()
    player.append(card)
    return card




def total(hand): #tested
    'compute the total of a blackjack hand'
    
    values = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '1':10, 'J':10, 'Q':10, 'K':10, 'A':11}
    
    result = 0
    numAces = 0

    
    for card in hand: # find number of Aces in hand
        result += values[card[0]]
        
        if card[0] == 'A':
            numAces += 1
            
        #hand now has a value where every ace is 11
        #if value > 21 then reduce first ace by 10
        #to have value of 1. Repeat until value < 21
            
    while result > 21 and numAces > 0:
        result -= 10
        numAces -= 1
    return result
#ex. hand = ['3x','5x','Jx','Ax','Ax']





def compareHands(house, player): #tested
    'compute the winner, input house, player total for the house and player'
    
    houseTotal, playerTotal = total(house), total(player)
    
    if houseTotal > playerTotal:
        print('You lose. ')
    elif houseTotal < playerTotal:
        print('You win!')
    elif houseTotal == 21 and 2 == len(house) < len(player):
        print('You lose') # house wins with blackjack and player does not have blackjack
    elif playerTotal == 21 and 2 == len(player) < len(house):
        print('You win')
    else:
        print(' a TIE!')




def blackjack():
    'simulates the house playing blackjack'
    
    deck = shuffleDeck()
    house = [] # house hand
    player = [] # player hand
    
    for i in range(2): # deal 2 cards to house & hand
        dealCard(deck, player)
        dealCard(deck, house)
        dealCard(deck, player)
        dealCard(deck, house)
        #print hands

        print('House: {:>7}{:>7}'.format(house[0], house[1]))
        print('Y o u: {:>7}{:>7}'.format(player[0], player[1]))
        # give cards to user as requested
        
        answer = input('hit or stand? (ENTER means hit) :')
        while answer in ('', 'h', 'hit'):
            card = dealCard(deck, player)
            print('You got {:<7}'.format(card))
            if total(player) > 21: # you bust
                  print('You bust .. sorry')
                  return
            answer = input('hit or stand? (ENTER means hit) :')
            
        #house must play
        while total(house) < 17: # house must hit until >16
            card = dealCard(deck, house)
            print ('House got {:>7}'.format(card))
            if total(house) > 21: #house bust
                print('House bust .. you win')
                return
        #both hands done, see who wins
            compareHands(house,player)
            return 

blackjack()
