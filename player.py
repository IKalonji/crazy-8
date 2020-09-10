import random

def player(cards_deck, player_cards, floor):
    '''Function for the main player'''
    floor_to_list = floor.split(" ") #split into list in order to iterate through
    valid = 0 #track whether player has a valid card
    for item in floor_to_list: #first loop to isolate an element from floor to list to check whether it is present in the players available cards
        for element in player_cards:
            if item in element:
                valid += 1
    if valid > 0: # player has a valid card
        print("You have a valid card to play\n")           
        while True:
            print('Cards: ', player_cards, '\n')
            played = int(input("\nChoose the card (1 being the left most card)")) #getting the index of the card chosen. Index will be -1
            played = player_cards[played-1] #assigning the item @ index value to played
            for element in floor_to_list: # check if the selected card is in fact correct, check if any element is present in the floor card
                invalid = 0  
                if not element in played: # check invalid element, if it is invalid, counter should increase
                    invalid += 1
            if invalid > 0:
                print("That was not a valid input")
                continue
            else:
                floor = played
                print("new card on the floor: ",floor)
                break
    else: 
        print("Pick up a card from the deck. You have no valid card to play ")
        new_card = random.choice(cards_deck)
        print("here is your card: ", new_card)
        player_cards.append(new_card)
        cards_deck.remove(new_card)

    return cards_deck, player_cards, floor


        