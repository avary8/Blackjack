import random

class blackJack:
    userHand = 0
    dealerHand = 0
    gamesPlayed = 0
    userWins = 0
    dealerWins = 0
    ties = 0
    running = bool(True)
    inner = bool(True)

    def reset(self):
        self.gamesPlayed += 1
        self.userHand = 0
        self.dealerHand = 0
        
    def deal(self):
        randomNum = random.randint(1,13)
        cards = ["ACE", "2", "3", "4","5","6","7","8", "9", "10","JACK", "QUEEN", "KING"]
        cardChosen = cards[randomNum-1]
        print("Your card is a " + cardChosen + "!")
        self.userHand += randomNum 
        print("Your hand total is " + str(self.userHand))
        
        if self.userHand == 21:
            self.userWins += 1
            self.inner = bool(False)
            print ("BLACKJACK! You win!")
        if self.userHand > 21:
            self.dealerWins += 1
            self.inner = bool(False)
            print ("You exceeded 21! You lose.")
        
    def dealer(self):
        dealerNum = random.randint(16,26)
        self.inner = bool(False)
        if dealerNum > 21 or self.userHand > dealerNum:
            self.userWins += 1
            print("You win!")
        elif dealerNum == self.userHand:
            self.ties += 1
            print("It's a tie! No one wins!")
        else:
            dealerNum > self.userHand
            self.dealerWins += 1
            print ("Dealer wins!")

    def printStats(self):
        print("""********Game Stats********
        Games played: """ + str(self.gamesPlayed) + """
        Wins: """ + str(self.userWins) + """
        Losses: """ + str(self.dealerWins) + """
        Ties: """ + str(self.ties))

    def switch(self, userInput):
        if userInput == "1":
            self.deal()
        elif userInput == "2":
            self.dealer()
        elif userInput == "3":
            self.printStats()
        elif userInput == "4":
            self.inner = bool(False)
            self.running = bool(False)
            
    def menu(self):
        print("""
                1. Get another card
                2. Hold hand
                3. Print statistics
                4. Exit""")
        userInput = input()
        self.switch(userInput)


game = blackJack()
while game.running:
    game.reset()
    game.inner = bool(True)
    print ("Start Game #" + str(game.gamesPlayed))
    game.deal()

    while game.inner:
        game.menu()
    
    