from xml.dom.minidom import Element


class Bank :
    def __init__(self) :
        self.accounts = []
        
class Account :
    def __init__(self, amount, customer) :
        self.amount = amount
        self.customer = customer

class Customer :
    def __init__(self, *args) :
        if len(args) == 1 :
            self.name = args[0]

        elif len(args) == 2 : 
            self.name = args[0]
            self.age = args[1]

        else:
            self.name = args[0]
            self.age = args[1]
            self.gender = args[2]



class Bird :
    def __init__(self, positionX, positionY, direction, moveList) :
        self.positionX = positionX
        self.positionY = positionY
        self.direction = direction
        self.moveList = []

    def readMoveList(self, Pig) :
        [(coordinate, move) for tuple in self.moveList if "y" in tuple  ]

    def move(self, input, Pig) :
        if input == "a" and self.direction == "North" or input == "d" and self.direction == "South" :
            self.direction = "West"
        elif input == "a" and self.direction == "East" or input == "d" and self.direction == "West" :
            self.direction = "South" 
        elif input == "a" and self.direction == "South" or input == "d" and self.direction == "North" :
            self.direction = "East"
        elif input == "a" and self.direction == "West" or input == "d" and self.direction == "East" :
            self.direction = "North"
        elif input == "w" and self.direction == "North" :
            self.moveList.append("y",1)
        elif input == "w" and self.direction == "South" :
            self.moveList.append("y",-1)   
        elif input == "w" and self.direction == "East" :
            self.moveList.append("x",1)
        elif input == "w" and self.direction == "West" :
            self.moveList.append("x",-1)
        elif input == "q" :
            self.readMoveList(Pig)   

    def victoryOrLoss(self, Pig) :
        if self.positionX == Pig.positionX and self.positionY == Pig.positionY :
            print("Squark! Victory!")      
        elif self.positionX != Pig.positionX or self.positionY != Pig.positionY :
            print("Oh no, the pigs won! Oink oink!")        

        

class Pig :
    def __init__(self, positionX, positionY) :
        self.positionX = positionX
        self.positionY = positionY       


class Board :
    boardPiece = ["*"]
    def __init__(self, boardPiece, board) -> None:
        #for element in boardPiece
        return