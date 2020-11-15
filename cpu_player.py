'''arg: cards_deck, player_cards, floor return card_deck, floor'''

from random import choice

def cpu_player(cards_deck, cpu_player_cards, floor):
    '''Function to simulate cpu as player, return values = floor, cards_deck'''
    floor_to_list = floor.split(" ") #split into list in order to iterate through
    # valid = 0 #track whether player has a valid card
    index_of_valid_cards = []
    for item in floor_to_list: #first loop to isolate an element from floor to list to check whether it is present in the cpu available cards
        for element in cpu_player_cards:
            if item in element: #check if cpu has a valid card to play
                index_of_valid_cards.append(cpu_player_cards.index(element))
    if len(index_of_valid_cards) > 0: # player has a valid card
        print("------CPU has a valid card to play")
        print("On the floor: {}".format(floor))           
        print('Cards: ', cpu_player_cards)
        played = cpu_player_cards[choice(index_of_valid_cards)]  #assigning the item @ random index value of valid cards to played
        cards_deck.append(floor) #appending the old floor back to the deck of cards that can be used
        floor = played #new floor is now the card that was successfully played
        cpu_player_cards.remove(played) #remove the card from the players available cards
        print("new card on the floor: ",floor)
    elif len(cpu_player_cards) == 0:
        print("CPU Player has won")
        sys.exit()
    else:     
        print("------Picking up a card from the deck. CPU has no valid card to play ")
        new_card = choice(cards_deck)
        print("here is your card: ", new_card)
        cpu_player_cards.append(new_card)
        print(cpu_player_cards)
        cards_deck.remove(new_card)

    return cards_deck, cpu_player_cards, floor