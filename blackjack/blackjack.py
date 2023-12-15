#!/usr/bin/python3


import random


logo = __import__("art").logo

card = [
    'A', 2, 3, 4, 5,
    6, 7, 8, 9, 10,
    'J', 'K', 'Q']


def add_cards(cards):
    """adds users cards together"""
    total = 0
    for i in cards:
        if str(i) in "JKQ":
            total += 10
        elif i == 'A':
            total += 11
        else:
            total += i
    return total


def change_ace(deals):
    """change aces to users choice"""
    aces = deals.count('A')
    for i in range(aces):
        ace = input(f"You have {'an' if i == 1 else 'another'}"
                    " Ace, pick '1'or '11': ")
        deals[deals.index('A')] = 1 if ace == '1' else 11
    return deals


def change_dealers_ace(deals):
    """follows specific processes to pick
    a number for the computr ace card"""
    aces = deals.count('A')
    for i in range(aces):
        deals.remove('A')
    total = add_cards(deals)
    for i in range(aces):
        if (total + 11) > 21:
            deals.append(1)
            total += 1
        elif (total < 17):
            deals.append(11)
            total += 11
        else:
            deals.append(1)
            total += 1
    return deals


def get_winner(user, dealer):
    """get the game winner"""
    user = change_ace(user)
    users_deal = add_cards(user)
    dealer = change_dealers_ace(dealer)
    dealers_deal = add_cards(dealer)
    if dealers_deal < 17:
        print(dealer)
        print("Dealer is less than 17, an extra card will be given")
        dealer.append(random.choice(card))
        dealers_deal = add_cards(change_dealers_ace(dealer))
    if users_deal < 17:
        print(user)
        print("Your card is less than 17, an extra card will be given")
        user.append(random.choice(card))
        users_deal = add_cards(change_ace(user))
    print(f"Dealers cards are {dealer} with a total of {dealers_deal}")
    print(f"Your cards are {user} with a total of {users_deal}")
    if users_deal == dealers_deal:
        print("Its a DRAW")
    elif dealers_deal > users_deal:
        print("You LOSE")
    else:
        print("You WIN")


def blackjack():
    """run the blackjack game"""
    stop, started = (False, False)
    user, dealer = ([], [])
    print(logo)

    while not stop:
        if not started:
            deal = input("Start a new blackjack game: (y/n) ")
        else:
            deal = input("Type 'y' to get another card or 'n' to pass: ")
        if (deal == 'y') and (not started):
            started = True
            user = [random.choice(card) for i in range(2)]
            dealer = [random.choice(card) for i in range(2)]
            print(f"Your cards are {user}")
            print(f"Dealers open card is {dealer[0]}")
        elif (deal == 'y') and (started):
            user.append(random.choice(card))
            user = change_ace(user)
            users_deal = add_cards(user)
            dealers_deal = add_cards(change_dealers_ace(dealer))
            print(f"Your cards are {user}")
            if (users_deal > 21) and ('A' not in user):
                print(f"The Dealers card are {dealer}")
                print("You LOSE")
                started = False
            elif (users_deal > 21):
                user = change_ace(user)
                users_deal = add_cards(user)
                if (users_deal > 21):
                    print(f"The Dealers card are {dealer}")
                    print("You LOSE")
                    started = False
            elif dealers_deal < 17:
                dealer.append(random.choice(card))
        elif (deal == 'n') and (started):
            get_winner(user, dealer)
            started = False
        else:
            stop = True


if __name__ == "__main__":
    blackjack()
