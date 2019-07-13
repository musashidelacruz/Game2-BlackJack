
def player_busts(player,dealer,chips):
    print ("\n Player Busts")
    chips.lose_bet()
    

def player_wins(player,dealer,chips):
    print ("\n You Win!")
    chips.win_bet()
    
def dealer_busts(player,dealer,chips):
    print ("\n House Busts")
    chips.win_bet()
    
def dealer_wins(player, dealer, chips):
    print ("\n House Wins")
    chips.lose_bet()
    
def push(player, dealer):
     print("\n Push.  You tie with the House.")

