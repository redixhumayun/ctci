# #! /usr/bin/env python3

from random import shuffle

class Card():
    def __init__(self, suit, number):
        self.suit = suit
        self.number = number
        self.available = True

    def isAvailable(self):
        return self.available

    def makeUnavailable(self):
        self.available = False

class Deck(Card):
    def __init__(self, cards):
        self.cards = cards

    def shuffle(self):
        #shuffle the deck of cards
        shuffle(self.cards)
        return

    def dealHand(self):
        #return two random cards in a list from the deck of cards
        if self.cards[0].isAvailable() and self.cards[1].isAvailable():
            self.cards[0].makeUnavailable()
            self.cards[1].makeUnavailable()
            self.removeCardsFromDeck()
            return [self.cards[0], self.cards[1]]

    def dealCard(self):
        #deal the top card from the list of cards
        if self.cards[0].isAvailable():
            return self.cards[0]
        else:
            del self.cards[0]
            return self.dealCard()

    def removeCardsFromDeck(self):
        #remove the card from the deck
        for card in self.cards:
            if is not card.isAvailable():
                self.cards.remove(card)
        return

    def remainingCards(self):
        return len(self.cards)


class Hand(Card):
    def __init__(self, cards):
        self.cards = cards #List of cards with their suit and face value

    def addCard(self, card):
        self.cards.append(card) #Add a new card to the users hand
        self.changeScore(card.number) #calling the method to add the new score
        return

    def __str__(self):
        return ("card1= " + self.cards[0].suit + ", " + self.cards[0].number + "\n"
        + "card2= " + self.cards[1].suit + ", " + self.cards[1].number)

class BlackJackHand(Hand):
    def __init__(self, cards):
        super().__init__(cards)
        self.score = 0

    def getScore(self):
        return self.score

    def checkScore(self):
        self.score = self.calculateScore()
        if self.score == 21:
            return "GAME WON"
        else:
            return self.score

    def calculateScore(self):
        score = 0 #calculating score with A as 1 here
        for card in cards:
            if card.number > 10:
                score += 10
            else:
                score += card.number

        max_score = self.getMaxScore() #calculating score with A as 11 here
        if max_score <= 21:
            return max_score
        else:
            return self.score


    def getMaxScore(self): #calculates value of hand with A as 11
        score = 0
        for card in cards:
            if card.isAce():
                score += 11
            elif card.number > 10:
                score += 10
            else:
                score += card.number

        return score

class BlackJackCard(Card):
    def __init__(self, suit, number):
        super().__init__(suit, number)

    def isAce(self):
        if self.number == 1:
            return True
        else:
            return False



if __name__ == "__main__":
    deck_list = [("Heart", "13"), ("Spade", "1"), ("Diamond", "12"),
                ("Club", "11"), ("Heart", "2"), ("Diamond", "5"), ("Spade", "4")]
    card_list = []

    for card in deck_list:
        card_list.append(BlackJackCard(card[0], card[1]))

    deck = Deck(card_list)
    deck.shuffle()
    hand = BlackJackHand(deck.dealHand())
    print(hand)
