"""
a class for the tik tak map storing all the game functions 
"""
class tik_tak_map:
    def __init__(self, w, h): 
        self.w = int(w)
        self.h = int(h)
        self.map = []
        self.rounds = 1
        self.player_turn = 1    
    
    def creation(self): 
        # makes an array of hight = h and with = w filled with |_| 
        self.map = [["|_|" for x in range(self.w)] for y in range(self.h)]
   
    def display(self):
        # print(f"the with is {range(self.w)} and the hight {range(self.h)}")
        #---- 
        # player_turn = (self.rounds + 1) - self.rounds # bug in this line of code 
        #---- changes the player turn 
        match self.player_turn:
            case 1:
                self.player_turn = 2
            case 2:
                self.player_turn = 1

        print(f"round {self.rounds} player {self.player_turn}") # displays the round and player turn 
        for x in range(self.h):
            print(x)
            print(self.map[x][:]) # print whole array using a slice

    def insert(self,input_hight,input_with):
        self.rounds = self.rounds + 1
        # print(f"---- hight {input_hight} and with {input_with}")
        # print(self.map) 
        match self.player_turn: # draws the players moves
            case 1:
                self.map[input_hight][input_with] = "|O|"
            case 2:
                self.map[input_hight][input_with] = "|X|"

    def test(self): # a test function you can test it. :)
        for x in range(self.h):
            self.map[x][0] = str(x) # self.map[h][w]
    
    def __str__(self):
        return
        # return f"a matrix map of a hight of {self.h} and a with {self.w}\nand the dog shit map look like this {self.map}"

def intro():
    print("-------------------------")
    print("  a simple tik tow game  ")
    print("-------------------------")    

"""
the Game match system
"""
class Match(): 
    def __init__(self):
        self.game = tik_tak_map(3, 3)
    
    def create_match(self):
        self.game.creation() 
        self.game.display()
    
    def match_round(self, match_user_input):
        Input = match_user_input.split()
        # print(f'height{int(Input[0])}, with {int(Input[1])}') 
        self.game.insert(int(Input[0]), int(Input[1])) # 0 = y , 1 = x on the playing field
        self.game.display()

"""
the Game loop in the main function
"""
def main():
    intro()
    game_match = Match() # creates an class instance of Match containing the match system
    game_match.create_match() # creates a singel match 
    while(True): # this will make the match last for iternity
        print("Put in the x cordinate and then the y, with a space inbetween or not.") 
        user_input = input()
        if user_input == "quit":    exit() # exits the game of player types exit 
        game_match.match_round(user_input) # a singel game match

if __name__ == "__main__":
    main()
