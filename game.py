import random
import cpu_player, player


"""BASIC TEXT BASED CRAZY EIGHT CARD GAME"""
"""cards are held in cards.txt"""

def get_player_name():
    '''Function to get the players name'''

    name = input("Hi player, please enter your name: ")
    print(f"Welcome {name}. Let's get started!")

def card_deck():
    '''Function to pull the cards from list'''

    card_file = open('cards.txt', 'r') #open the card file
    card_list = card_file.readlines() #turning each line in the file to an element in a list
    card_file.close() #close the file
    return card_list 

def first_card_issue_and_floor(card_deck):
    '''Function to issue the first set of cards to player and comp'''

    player_cards = []
    while len(player_cards) != 5: 
        card = random.choice(card_deck) #generate a random card from the card list
        if card in player_cards:    #check for a duplicate card, since only one deck is being used
            continue
        else: 
            player_cards.append(card) #append the card to the players cards
            card_deck.remove(card)  #remove the card from the deck.
    print("Your cards have been issued. {} \n\n".format(player_cards))
    
    while True:
        floor = random.choice(card_deck) #generate a random card to start the game. 
        if ('8' in floor) or ('10' in floor) or ('JACK' in floor) or ('JOKER' in floor): #if any special card was chosen then process should be repeated
            continue
        else:
            print("\n\nOn the floor: ", floor)
            break 

    return card_deck, player_cards, floor 

def player(cards_deck, player_cards, floor):
    '''Function for the main player'''
    floor_to_list = list(floor)
    i = 0
    while i < 2:
        if floor_to_list[i] in  

def cpu_player(cards_deck, player_cards, floor):
    '''Function to simulate cpu as player, return values = floor, cards_deck'''

def


def run_game():
    '''Main Function to run the game.'''

    cards_deck = card_deck()
    cards_deck, player_cards, floor = first_card_issue_and_floor(cards_deck)


run_game()
