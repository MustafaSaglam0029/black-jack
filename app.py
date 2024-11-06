
from cards import create_deck, initial_cards
from turns import player_turn, dealer_turn
from get import get_integer_input, get_valid_answer



def  play_game():
     player_money = get_integer_input("How much money would you like to play: ")
     dealer_money = 10000
     round_number = 1
     print(f"Player Money: {player_money} \n Dealer Money : {dealer_money} \n Round Number: {round_number}")

     while player_money > 0:
        print("Would you like to continue:")
        answer = get_valid_answer()
        if answer == "y":
            print(f"Starting round {round_number}")
        else:
            print(f"You have {player_money} Euros")
            break


        
        while True:

            bet_amount = get_integer_input("How much money would you like to bet:")

            if  bet_amount < player_money :
                print(f"You bet with {bet_amount}")
                break 
            else:
                print("Invalid input, please enter an amount that you have.")
    

        deck = create_deck()
        player_hand, dealer_hand = initial_cards(deck)

        print(f"Dealer visible card is {dealer_hand[0]}")
        player_hand, player_total, player_status = player_turn(deck, player_hand)

        if player_status == "bust":
            dealer_money += bet_amount
            player_money -= bet_amount
            print(f"Your current money {player_money} Euros and dealer money is {dealer_money}")
            round_number += 1
            continue
        print(f"Dealer's hidden card was : {dealer_hand[1]} ")
        dealer_hand, dealer_total = dealer_turn(deck, dealer_hand)
        print(f"Dealer total is {dealer_total} and player total is {player_total}")
        if player_total>dealer_total or dealer_total>21 or player_total == 21:
            print("You win!")
            dealer_money -= bet_amount*2
            player_money += bet_amount*2
        elif player_total < dealer_total:
            print("You lost!")
            dealer_money += bet_amount
            player_money -= bet_amount
        else:
            print("It is a tie")
        print(f"Your current money {player_money} Euros and dealer money is {dealer_money} Euros")
        round_number += 1
     if player_money == 0:
        print(f"Game over. You ran out of money")
     print(f"Thank you for playing ")


play_game()