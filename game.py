import random
import time
from cpu_player import cpu_player
from player import player
from colorama import Fore, Style



"""BASIC TEXT BASED CRAZY EIGHT CARD GAME"""
"""cards are held in cards.txt"""

def get_player_name():
    '''Function to get the players name'''

    name = input("Hi player, please enter your name: ")
    print(f"Welcome {name}. Let's get started!")
    return name

def card_deck():
    '''Function to pull the cards from list'''
    
    card_file = open('cards.txt', 'r') #open the card file
    # card_list = card_file.readlines() #turning each line in the file to an element in a list
    card_list = [line.strip() for line in card_file]
    card_file.close() #close the file
    return card_list

def first_card_issue(cards_deck):
    '''Function to issue the first set of cards to player and comp'''
    random.shuffle(cards_deck) #shuffle the card deck
    print("The card deck has been shuffled") 
    player_cards = []
    while len(player_cards) != 5: 
        card = random.choice(cards_deck) #generate a random card from the card list
        if card in player_cards:    #check for a duplicate card, since only one deck is being used
            continue
        else: 
            player_cards.append(card) #append the card to the players cards
            cards_deck.remove(card)  #remove the card from the deck.
    print("Your cards have been issued: {}".format(player_cards))

    return cards_deck, player_cards

def floor_card_issue(cards_deck):   
    '''Function to issue the first card on the floor'''

    while True:
        floor = random.choice(cards_deck) #generate a random card to start the game. 
        if ('8' in floor) or ('10' in floor) or ('JACK' in floor) or ('JOKER' in floor): #if any special card was chosen then process should be repeated
            continue
        else:
            print("On the floor: ", floor)
            break 
    return floor 

def run_game():
    '''Main Function to run the game.'''
    print("Starting game")
    name = get_player_name()
    cards_deck = card_deck()
    cards_deck, player_cards = first_card_issue(cards_deck)
    cards_deck, cpu_player_cards = first_card_issue(cards_deck)
    floor = floor_card_issue(cards_deck)
    
    while True:
        print(f"{Fore.GREEN}{name}")
        cards_deck, player_cards, floor =  player(cards_deck, player_cards, floor)
        print("\n")
        print("*"*100)
        time.sleep(3)
        print(f"{Fore.BLUE}CPU PLAYER")
        cards_deck, cpu_player_cards, floor = cpu_player(cards_deck, cpu_player_cards, floor)
        time.sleep(3)
        print("*"*100)


if __name__ == "__main__":
    run_game()