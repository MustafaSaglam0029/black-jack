
from get import calculate_score


def player_turn(shuffled_deck,player_hand):
    while True:
        player_total=calculate_score(player_hand)
        print(f"Your current hand is {player_hand} and total is  {player_total}")

        if player_total > 21:
            print(f"You lost!,Your total score {player_total} is over 21")
            return player_hand,player_total,"bust"

        decision = input("Would you like to hit or stand?(h/s)").lower()

        if decision == "s":
            return player_hand, player_total, "s"
        elif decision == "h":
            new_card=shuffled_deck.pop()
            player_hand.append(new_card)
            print(f"You drew {new_card}")
            player_total=calculate_score(player_hand)
        else:
            print("Invalid input, please type 's' or 'h'?")


def  dealer_turn(shuffled_deck, dealer_hand) :
     while calculate_score(dealer_hand) < 17:
         new_card=shuffled_deck.pop()
         dealer_hand.append(new_card)
         print(f"Dealer drew {new_card}")

     dealer_total=calculate_score(dealer_hand)
     print(f"Dealer hand is {dealer_hand} and total is  {dealer_total}")
     return dealer_hand,dealer_total