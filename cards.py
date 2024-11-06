import random


def  create_deck() : 
     suits = ["Spades", "Clubs", "Diamonds", "Hearts"]
     ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
     cards = {"A":(1,11),"K":10,"Q":10,"J":10,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10}
     deck = [(f"{rank} of {suit}", cards[rank]) for suit in suits for rank in ranks]

     random.shuffle(deck)
     return deck


def  initial_cards(shuffled_deck) :
     player_hand=[shuffled_deck.pop(), shuffled_deck.pop()]
     dealer_hand=[shuffled_deck.pop(), shuffled_deck.pop()]
     return player_hand,dealer_hand