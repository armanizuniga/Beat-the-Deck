##Program: Final Project
##Name: Armani Zuniga
##Date: May 19th, 2021
# -------------------------------------------------------------#

"""This program uses a graphics library to simulate a game called 'Higer or Lower'.
   User is given a 52 card shuffled deck and must guess if the next card drawn is
   higher or lower than the card presented on gameboard. A score is kept until all
   cards have been drawn."""

from graphics import *
import random

SCORE = 0
class Card(object):

    def __init__(self, color, suit, value, weight):
        self.color = color
        self.suit = suit
        self.value = value
        self.weight = weight
        self.cardDisplay = Rectangle(Point(200, 100), Point(400, 400))
        self.message1 = Text(Point(220,120),f"{self.value}" )
        self.message2 = Text(Point(380, 380), f"{self.value}")
        self.messageSuit = Text(Point(300, 250), f"{self.suit}")

    def displayNumSides(self,win):
        """Draws characteristics of card."""
        self.message1.setSize(25)
        self.message1.setTextColor(self.color)
        self.message1.draw(win)
        self.message2.setSize(25)
        self.message2.setTextColor(self.color)
        self.message2.draw(win)
        self.messageSuit.setSize(25)
        self.messageSuit.setTextColor(self.color)
        self.messageSuit.draw(win)

    def drawCard(self,win):
        """Draws card shape to window"""
        self.displayNumSides(win)
        self.cardDisplay.draw(win)

    def eraseCard(self):
        """unDraws entire card."""
        self.cardDisplay.undraw()
        self.message1.undraw()
        self.message2.undraw()
        self.messageSuit.undraw()

def createDeck():
    """Creates a list of 52 Card objects and shuffles them then returns list"""
    # creating list
    deck = []
    twoDiamond = Card("red", "Diamond", 2, 2)
    twoHeart = Card("red", "Heart", 2, 2)
    twoSpade = Card("black", "Spade", 2, 2)
    twoClub = Card("black", "Club", 2,2)

    threeDiamond = Card("red", "Diamond", 3, 3)
    threeHeart = Card("red", "Heart", 3, 3)
    threeSpade = Card("black", "Spade", 3, 3)
    threeClub = Card("black", "Club", 3, 3)

    fourDiamond = Card("red", "Diamond", 4, 4)
    fourHeart = Card("red", "Heart", 4, 4)
    fourSpade = Card("black", "Spade", 4, 4)
    fourClub = Card("black", "Club", 4, 4)

    fiveDiamond = Card("red", "Diamond", 5, 5)
    fiveHeart = Card("red", "Heart", 5, 5)
    fiveSpade = Card("black", "Spade", 5, 5)
    fiveClub = Card("black", "Club", 5, 5)

    sixDiamond = Card("red", "Diamond", 6, 6)
    sixHeart = Card("red", "Heart", 6, 6)
    sixSpade = Card("black", "Spade", 6, 6)
    sixClub = Card("black", "Club", 6, 6)

    sevenDiamond = Card("red", "Diamond", 7, 7)
    sevenHeart = Card("red", "Heart", 7, 7)
    sevenSpade = Card("black", "Spade", 7, 7)
    sevenClub = Card("black", "Club", 7, 7)

    eightDiamond = Card("red", "Diamond", 8, 8)
    eightHeart = Card("red", "Heart", 8, 8)
    eightSpade = Card("black", "Spade", 8, 8)
    eightClub = Card("black", "Club", 8, 8)

    nineDiamond = Card("red", "Diamond", 9, 9)
    nineHeart = Card("red", "Heart", 9, 9)
    nineSpade = Card("black", "Spade", 9, 9)
    nineClub = Card("black", "Club", 9, 9)

    tenDiamond = Card("red", "Diamond", 10, 10)
    tenHeart = Card("red", "Heart", 10, 10)
    tenSpade = Card("black", "Spade", 10, 10)
    tenClub = Card("black", "Club", 10, 10)

    jackDiamond = Card("red", "Diamond", "J", 11)
    jackHeart = Card("red", "Heart", "J", 11)
    jackSpade = Card("black", "Spade", "J", 11)
    jackClub = Card("black", "Club", "J", 11)

    queenDiamond = Card("red", "Diamond", "Q", 12)
    queenHeart = Card("red", "Heart", "Q", 12)
    queenSpade = Card("black", "Spade", "Q", 12)
    queenClub = Card("black", "Club", "Q", 12)

    kingDiamond = Card("red", "Diamond", "K", 13)
    kingHeart = Card("red", "Heart", "K", 13)
    kingSpade = Card("black", "Spade", "K", 13)
    kingClub = Card("black", "Club", "K", 13)

    aceDiamond = Card("red", "Diamond", "A", 14)
    aceHeart = Card("red", "Heart", "A", 14)
    aceSpade = Card("black", "Spade", "A", 14)
    aceClub = Card("black", "Club", "A", 14)

    # appending instances to list
    deck.append(twoDiamond)
    deck.append(twoHeart)
    deck.append(twoSpade)
    deck.append(twoClub)

    deck.append(threeDiamond)
    deck.append(threeHeart)
    deck.append(threeSpade)
    deck.append(threeClub)

    deck.append(fourDiamond)
    deck.append(fourHeart)
    deck.append(fourSpade)
    deck.append(fourClub)

    deck.append(fiveDiamond)
    deck.append(fiveHeart)
    deck.append(fiveSpade)
    deck.append(fiveClub)

    deck.append(sixDiamond)
    deck.append(sixHeart)
    deck.append(sixSpade)
    deck.append(sixClub)

    deck.append(sevenDiamond)
    deck.append(sevenHeart)
    deck.append(sevenSpade)
    deck.append(sevenClub)

    deck.append(eightDiamond)
    deck.append(eightHeart)
    deck.append(eightSpade)
    deck.append(eightClub)

    deck.append(nineDiamond)
    deck.append(nineHeart)
    deck.append(nineSpade)
    deck.append(nineClub)

    deck.append(tenDiamond)
    deck.append(tenHeart)
    deck.append(tenSpade)
    deck.append(tenClub)

    deck.append(jackDiamond)
    deck.append(jackHeart)
    deck.append(jackSpade)
    deck.append(jackClub)

    deck.append(queenDiamond)
    deck.append(queenHeart)
    deck.append(queenSpade)
    deck.append(queenClub)

    deck.append(kingDiamond)
    deck.append(kingHeart)
    deck.append(kingSpade)
    deck.append(kingClub)

    deck.append(aceDiamond)
    deck.append(aceHeart)
    deck.append(aceSpade)
    deck.append(aceClub)

    random.shuffle(deck)
    return deck

def buttons(win):
    """Draws buttons that user will interact with"""
    buttonHiger = Rectangle(Point(450, 400), Point(550, 450))
    buttonHiger.setFill("red")
    buttonLower = Rectangle(Point(450, 480), Point(550, 530))
    buttonLower.setFill("blue")
    messageHigher = Text(Point(500, 425), "Higher")
    messageHigher.setTextColor("white")
    messageHigher.setStyle("bold")
    messageHigher.setSize(20)
    messageLower = Text(Point(500, 505), "Lower")
    messageLower.setTextColor("white")
    messageLower.setStyle("bold")
    messageLower.setSize(20)
    buttonHiger.draw(win)
    buttonLower.draw(win)
    messageLower.draw(win)
    messageHigher.draw(win)

def checkClick(clickPoint):
    """Checks if buttons were clicked"""
    clickX = clickPoint.getX()
    clickY = clickPoint.getY()

    if clickX >= 450 and clickX <= 550:
        if clickY <= 450 and clickY >= 400:
            return 2

        elif clickY <= 530 and clickY >= 480:
            return 1
        else:
            return 0
    else:
        return 0

def printScore(win,scoreMessage):
    """Prints score"""
    scoreMessage.setSize(20)
    scoreMessage.undraw()
    scoreMessage.draw(win)


def playGame(win,deck):
    """Function that drives majority of game"""
    global SCORE
    current = deck.pop(0)
    print(current.color, current.value, sep=' ')
    current.drawCard(win)
    buttons(win)
    scoreMessage = Text(Point(300, 550), f"{SCORE}")
    printScore(win, scoreMessage)
    clickPoint = win.getMouse()
    clickCheck = checkClick(clickPoint)

    while clickCheck == 0:
        clickPoint = win.getMouse()
        clickCheck = checkClick(clickPoint)

    if clickCheck == 2:
        if len(deck) != 0:
            if deck[0].weight > current.weight:
                SCORE = SCORE + 1
                print("correct")
            else:
                print("wrong")
            print("Higher")
            scoreMessage.undraw()

    elif clickCheck == 1:
        if len(deck) != 0:
            if deck[0].weight < current.weight:
                SCORE = SCORE + 1
                print("correct")
            else:
                print("wrong")
            print("Lower")
            scoreMessage.undraw()

    current.eraseCard()
    pass

def main():
    """Main function"""
    win = GraphWin("Beat the Deck", 600, 600)
    deck = createDeck()
    scoreMessage1 = Text(Point(260, 550), f"Score:")
    scoreMessage1.setSize(20)
    scoreMessage1.draw(win)

    while len(deck) != 0:
        playGame(win,deck)

    win.getMouse()
    win.close()


if __name__ == '__main__':
    main()