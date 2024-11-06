
def  calculate_score(hand) :
     total = 0
     aces = 0

     for card,value in hand:
         if isinstance(value,tuple):
            aces += 1
            total += 11
         else:
            total += value

     while total > 21 and aces > 0 :
        total -= 10
        aces -= 1
     return total


def  get_integer_input(prompt):
     while True:
        value = input(prompt)
        if value.isnumeric():  
            return int(value)  
        else:
            print("Invalid input. Please enter a valid amount.")

def  get_valid_answer():
     valid_input = ["y","n"]
     while True:
        answer = input().lower()
        if answer in valid_input:
            return answer
        else:
            print("Invalid input.Please type 'y' or 'n'")