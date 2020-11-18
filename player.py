import random
import sys

played = None #used to keep track if special the card on the floor was played by the player, so that we do not get stuck in a loop or penalty issued more than once 

def player(cards_deck, player_cards, floor):
    '''Function for the main player'''
    global played
    special_cards = ['2','10','JOKER'] #list of all special cards
    to_play = '' #checking if the player has a valid counter card
    token = None
    invalid = 0 #for checking if the card played is in fact valid
    for item in special_cards: #check whether any special value is present in the floor card played by the CPU 
        if item in floor and played != floor:
            token = item
            break

    if token != None: #player has a valid counter
        print("CPU PLAYED A SPECIAL CARD")
        for element in player_cards:
            if token in element or 'ACE' in element:
                to_play = element #assigning the counter card to be played
                break
        if to_play != '': #check if a valid counter was found in the players cards
            print("YOU HAVE A COUNTER")
            cards_deck.append(floor)
            played = to_play
            floor = to_play 
            player_cards.remove(to_play)
            print("new card on the floor: ",floor)
            return cards_deck, player_cards, floor
        else:
            print("YOU DO NOT HAVE A COUNTER")
            if token == '10': 
                print("YOU HAVE BEEN ISSUED 4 NEW CARDS")
                for i in range(4): #no valid counter so player will be issued with the penalty
                    new = random.choice(cards_deck)
                    player_cards.append(new)
                    cards_deck.remove(new)
            elif token == '2':
                print("YOU HAVE BEEN ISSUED 2 NEW CARDS")
                for i in range(2):
                    new = random.choice(cards_deck)
                    player_cards.append(new)
                    cards_deck.remove(new)
            elif token == 'JOKER':
                print("YOU HAVE BEEN ISSUED 5 NEW CARDS")
                for i in range(5):
                    new = random.choice(cards_deck)
                    player_cards.append(new)
                    cards_deck.remove(new)
            return cards_deck, player_cards, floor
    else:
        floor_to_list = floor.split(" ") #split into list in order to iterate through
        valid = 0 #track whether player has a valid card
        for item in floor_to_list: #first loop to isolate an element from floor to list to check whether it is present in the players available cards
            for element in player_cards:
                if item in element:
                    valid += 1
        if valid > 0: # player has a valid card
            print("------You have a valid card to play")
            print("On the floor: {}".format(floor))           
            while True:
                print('Cards: ', player_cards)
                try:
                    played = input("Choose the card (1 being the left most card)") #getting the index of the card chosen. Index will be -1
                    if played == 'exit':
                        sys.exit()
                    else:
                        played = int(played)
                        played = player_cards[played-1] #assigning the item @ index value to played
                except IndexError as index_err:
                    print("Invalid input, try again")
                    continue
                except ValueError as val_err:
                    print("Invalid input, try again")
                    continue
                
                for element in floor_to_list: # check if the selected card is in fact correct, check if any element is present in the floor card 
                    if not element in played and played != "JOKER": # check invalid element, if it is invalid, counter should increase
                        invalid += 1
                if invalid > 1:
                    print(invalid, floor_to_list, played)
                    print("That was not a valid input")
                    continue
                else:
                    cards_deck.append(floor) #appending the old floor back to the deck of cards that can be used
                    floor = played #new floor is now the card that was successfully played
                    player_cards.remove(played) #remove the card from the players available cards
                    print("new card on the floor: ",floor)
                    break
        elif len(player_cards) == 0: #if player has no card, they win
            print("Player has won") 
            sys.exit()
        elif floor == "JOKER":
            cards_deck.append(floor)
            while True:
                try:
                    played = input("JOKER ON THE FLOOR>>Choose any card (1 being the left most card)") #getting the index of the card chosen. Index will be -1
                    if played == 'exit':
                        sys.exit()
                    else:
                        played = int(played)
                        played = player_cards[played-1] #assigning the item @ index value to played
                except IndexError as index_err:
                    print("Invalid input, try again")
                    continue
                except ValueError as val_err:
                    print("Invalid input, try again")
                    continue
                floor = played
                player_cards.remove(played)
                print("new card on the floor: ",floor)
                break
        else:     
            print("------Picking up a card from the deck. You have no valid card to play ")
            new_card = random.choice(cards_deck)
            print("here is your card: ", new_card)
            player_cards.append(new_card)
            print(player_cards)
            cards_deck.remove(new_card)

        return cards_deck, player_cards, floor


        