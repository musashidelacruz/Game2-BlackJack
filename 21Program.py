import random
from MainPackage import blackjackscript

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

class Card:
#suit and rank not yet defined
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        
    def __str__(self):
        return self.rank + ' of ' + self.suit

class Deck:

    def __init__(self):
        self.deck = [] 
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))

    def __str__(self):
        deck_comp = ''#start with empty string to add cards
        for card in self.deck:
            deck_comp += '\n ' +card.__str__()  # add each Card object's print string
        return 'Remaining Cards:' + deck_comp

    def shuffle(self): 
        random.shuffle(self.deck)

    def deal(self):
        single_card= self.deck.pop()
        return single_card #This does not print; print returns position

class Hand:
    
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces
    
    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank] #refrences step 1 rank string and step 2 deffinition of each card's calue then ueses it as key to access step 1 value dictionary
        if card.rank == 'Ace':
            self.aces += 1  # add to self.aces
 
    def adjust_for_aces(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1
         
class Chips:
    
    def __init__(self,total):
        self.total = total  # This can be set to a default value or supplied by a user input
        self.bet = 0
        
    def win_bet(self):
        self.total += self.bet
    
    def lose_bet(self):
        self.total -= self.bet

def take_bet(chips):

    while True:
        try:
            chips.bet=int(input("How much would you like to bet?   "))
      
        except ValueError:
            print('Sorry, how many chips?')
            
        else:
            if chips.bet > chips.total:
                print(f"Please bet your total, {chips.total}, or fewer.  How may chips will you bet?") 
            else:
                break

def hit(deck,hand):
    hand.add_card(deck.deal())
    hand.adjust_for_aces()

def hit_or_stand(deck,hand):
    global playing
    
    while True:
        x = input("Hit or Stand?  h/s: ")
        
        if x[0].lower() == 'h':
            hit(deck,hand)
        elif x[0].lower() == 's':
            print ("\n \n \n Player stands.\n \n Dealer's Turn.")
            playing = False
        else: 
            print ('If you would like another card, hit: type "h". If you would like to end your turn, stand: type "s".')
            continue
        break
            
def show_player(player,dealer):    
    print ("\n Your Cards:", *player.cards, sep='| |') 
           

def show_some(player,dealer):
    print ("\n Dealer's Hand:")
    print ("|<Hidden Card>|", dealer.cards[1])

def show_all(player,dealer):
    print ("\n Your Final Hand:", *player.cards, sep='| |') 
    print ("                    = ", player.value)
    print ("\n Dealer's Final Hand:")
    print (*dealer.cards, sep='| |')
    print ("                    = ", dealer.value)



###################### G A M E ########################
import random
playing = True
# Set up the Player's chips
playerchips = Chips(100)

## while True:
# Print an opening statement
print ("\n \n \n \n Let's play Black Jack! \n Get as close to 21 as you can without busting.")
print("You have 100 chips.\n" )


while True:

    # Create & shuffle the deck, deal two cards to each player
    deck = Deck()
    deck.shuffle()
    
    player = Hand() 
    player.add_card(deck.deal())
    player.add_card(deck.deal())
    
    dealer = Hand()
    dealer.add_card(deck.deal())
    dealer.add_card(deck.deal()) 
    
    
    # Prompt the Player for their bet
    take_bet(playerchips) 
    
    print ("\n Ok, I'll deal. \n")
    # Show cards (but keep one dealer card hidden)
    show_player(player, dealer)
    
    while playing:  # recall this variable from our hit_or_stand function
        
        # Prompt for Player to Hit or Stand
        hit_or_stand(deck, player)
        
        # Show cards (but keep one dealer card hidden)
        show_some(player, dealer)
        show_player(player,dealer) 
        
        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player.value > 21:
            blackjackscript.player_busts(player,dealer,playerchips)
            break
        


    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    while dealer.value <= 17:
        dealer.add_card(deck.deal())
        # Show all cards
    
    show_all(player,dealer)     
 
    
        # Run different winning scenarios
    if player.value == dealer.value:
        blackjackscript.push(player,dealer)
        print ("Your chips stand at: " + str(playerchips.total))

    elif dealer.value < player.value <= 21:
            blackjackscript.player_wins(player,dealer,playerchips) 

    elif dealer.value > 21:
            blackjackscript.dealer_busts(player,dealer,playerchips) 

        
    elif player.value < dealer.value <= 21:
            blackjackscript.dealer_wins(player,dealer,playerchips) 

             
     # Inform Player of their chips total 
    print ("Your chips stand at: " + str(playerchips.total))

    
    
    # Ask to play again
    play_again = input ("Would you like to play again? y/n: ")
    if play_again[0].lower() == 'y':
        print("\n \n \n ")
        playing = True  
        continue
    else:
        print ("\n Thank you for playing.")
        break