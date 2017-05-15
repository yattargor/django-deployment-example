#####################################
### WELCOME TO YOUR OOP PROJECT #####
#####################################

# For this project you will be using OOP to create a card game. This card game will
# be the card game "War" for two players, you an the computer. If you don't know
# how to play "War" here are the basic rules:
#
# The deck is divided evenly, with each player receiving 26 cards, dealt one at a time,
# face down. Anyone may deal first. Each player places his stack of cards face down,
# in front of him.
#
# The Play:
#
# Each player turns up a card at the same time and the player with the higher card
# takes both cards and puts them, face down, on the bottom of his stack.
#
# If the cards are the same rank, it is War. Each player turns up three cards face
# down and one card face up. The player with the higher cards takes both piles
# (six cards). If the turned-up cards are again the same rank, each player places
# another card face down and turns another card face up. The player with the
# higher card takes all 10 cards, and so on.
#
# There are some more variations on this but we will keep it simple for now.
# Ignore "double" wars
#
# https://en.wikipedia.org/wiki/War_(card_game)

from random import shuffle

# Two useful variables for creating Cards.
SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

#two methods for creating this global variable
mycards = [(s,r) for s in SUITE for r in RANKS]
#the second method with nested FOR loops
# mycards = []
# for r in RANKS:
#     for s in SUITE:
#         mycards.append((s,r))

class Deck():
    """
    This is the Deck Class. This object will create a deck of cards to initiate
    play. You can then use this Deck list of cards to split in half and give to
    the players. It will use SUITE and RANKS to create the deck. It should also
    have a method for splitting/cutting the deck in half and Shuffling the deck.
    """
    #CREATE SINGLE DECK OF CARDS MIXING
    def __init__(self):
        print("Create deck of cards")
        self.allcards = [(s,r) for s in SUITE for r in RANKS]

    def shuffle_deck(self):
        print("Shuffling deck of cards")
        shuffle(self.allcards)

    def split_in_half(self):
        #return a tuple of this split cards
        return (self.allcards[:26],self.allcards[26:])

class Hand:
    '''
    This is the Hand class. Each player has a Hand, and can add or remove
    cards from that hand. There should be an add and remove card method here.
    '''
    def __init__(self, cards):
        self.cards = cards

    def __str__(self):
        #print how many cards is in the player hand
        return "Contains {} cards".format(len(self.cards))

    def add(self,added_cards):
        #cards is like a list so with this extend the list
        self.cards.extend(added_cards)

    def remove_card(self):
        return (self.cards.pop())

class Player:
    """
    This is the Player class, which takes in a name and an instance of a Hand
    class object. The Payer can then play cards and check if they still have cards.
    """
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

    def play_card(self):
        drawn_card = self.hand.remove_card()
        print ("{} has placed: {}".format(self.name,drawn_card))
        print ("\n")
        return (drawn_card)

    def remove_war_cards(self):
        war_cards = []
        if len(self.hand.cards) < 3:
            return self.hand.cards
        else:
            return self.hand.cards
        for x in range(3):
            war_cards.append(self.hand.remove_card())
        return (war_cards)

    def still_has_cards(self):
        """
        Return true if player still has cards left
        """
        return len(self.hand.cards) != 0



######################
#### GAME PLAY #######
######################
print("Welcome to War, let's begin...")

#Create a new deck and split in half
d = Deck()
d.shuffle()
half1,half2 = d.split_in_half()

#Create both players
comp = Player("computer", Hand(half1))

name = input("What's your name?")
user = Player(name, Hand(half2)

#setup counter for round and war
total_rounds = 0
war_count = 0

#Until player and pc has cards the game continuosly
while user.still_has_cards() and comp.still_has_cards():
    total_rounds += 1
    print("Time for a new round!")
    print("here are the current standings")
    print(user.name + "has the count: " + str(len(user.hand.cards)))
    print(comp.name + "has the count: " + str(len(comp.hand.cards)))
    print("play a card")
    print('\n')

    #represent cards in the midlle of the table
    table_cards = []

    c_card = comp.play_card()
    p_card = user.play_card()

    table_cards.append(c_card)
    table_cards.append(p_card)

    #for camparing the card one each other is important the ranking(second position in tuple, value 1)
    if c_card[1] == p_card[1]:
        war_count += 1
        print("war!")

        table_cards.extend(user.remove_war_cards)
        table_cards.extend(comp.remove_war_cards)

        if RANKS.index(c_card[1]) < RANKS.index(p_card[1]):
            user.hand.add(table_cards)
        else
            comp.hand.add(table_cards)

    else:
        if RANKS.index(c_card[1]) < RANKS.index(p_card[1]):
            user.hand.add(table_cards)
        else
            comp.hand.add(table_cards)

print("game over, number of rounds: "+ str(total_rounds))
print("a war happened "+ str(war_count) + " times")
print("Does the computer still has cards?: ")
print(str(comp.still_has_cards()))
print("Does the human player still has cards?: ")
print(str(user.still_has_cards()))
















# Use the 3 classes along with some logic to play a game of war!
