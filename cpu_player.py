'''arg: cards_deck, player_cards, floor return card_deck, floor'''
import sys
from random import choice

played = None

def cpu_player(cards_deck, cpu_player_cards, floor):
    '''Function to simulate cpu as player, return values = floor, cards_deck'''
    global played
    special_cards = ['2','10','JOKER'] #list of all special cards
    to_play = ''
    token = None
    for item in special_cards: #check whether any special value is present in the floor card played by the CPU 
        if item in floor and floor != played:
            token = item
            break

    if token != None:
        print("PLAYER PLACED A SPECIAL CARD")
        for element in cpu_player_cards:
            if token in element or 'ACE' in element:
                to_play = element
                break
        if to_play != '': #check if a valid counter was found in the players cards
            print("YOU HAVE A COUNTER")
            cards_deck.append(floor)
            played = to_play
            floor = to_play
            cpu_player_cards.remove(to_play)
            print("new card on the floor: ",floor)
            return cards_deck, cpu_player_cards, floor
        else:
            print("YOU DO NOT HAVE A COUNTER")
            if token == '10': 
                print("YOU HAVE BEEN ISSUED 4 NEW CARDS")
                for i in range(4): #no valid counter so player will be issued with the penalty
                    new = choice(cards_deck)
                    cpu_player_cards.append(new)
                    cards_deck.remove(new)
            elif token == '2':
                print("YOU HAVE BEEN ISSUED 2 NEW CARDS")
                for i in range(2):
                    new = choice(cards_deck)
                    cpu_player_cards.append(new)
                    cards_deck.remove(new)
            elif token == 'JOKER':
                print("YOU HAVE BEEN ISSUED 5 NEW CARDS")
                for i in range(5):
                    new = choice(cards_deck)
                    cpu_player_cards.append(new)
                    cards_deck.remove(new)
            return cards_deck, cpu_player_cards, floor

    else:
        floor_to_list = floor.split(" ") #split into list in order to iterate through
        # valid = 0 #track whether player has a valid card
        index_of_valid_cards = []
        for item in floor_to_list: #first loop to isolate an element from floor to list to check whether it is present in the cpu available cards
            for element in cpu_player_cards:
                if item in element or 'JOKER' in element: #check if cpu has a valid card to play
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
        elif floor == "JOKER":
            cards_deck.append(floor)
            played = choice(cpu_player_cards)
            floor = played
            cpu_player_cards.remove(played)
            print("new card on the floor: ",floor)
        else:     
            print("------Picking up a card from the deck. CPU has no valid card to play ")
            new_card = choice(cards_deck)
            print("here is your card: ", new_card)
            cpu_player_cards.append(new_card)
            print(cpu_player_cards)
            cards_deck.remove(new_card)

        return cards_deck, cpu_player_cards, floor