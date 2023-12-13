#!/usr/bin/python3
"""organize the blind auction game"""

import os


logo = __import__("gavel_art").logo

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def highestBidder(bids):
    """find highest bidder from dictionary"""
    highestBid = 0
    bidder = ""
    bidItems = bids.items()
    for key, value in bidItems:
        if value > highestBid:
            highestBid = value
            bidder = key
    return [bidder, highestBid]


def blindAuction():
    """run the blind auction"""
    bids = {}
    stop = False

    while not stop:
        clear_screen()
        print(logo)
        name = input("Please input your name: ")
        bid = input("Please input your bid: #")
        try:
            bid = int(bid)
        except ValueError:
            print("That is an Invalid input")
        else:
            bids[name] = bid
            response = input("Would there be any more bids, (yes/no)\n").lower()
            if response == 'no':
                return highestBidder(bids)


if __name__ == "__main__":
    startBid = blindAuction()
    print(f"The Winner is {startBid[0]} with a bid of {startBid[1]}")