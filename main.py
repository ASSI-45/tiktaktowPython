from math import remainder

# a class for the tik tak map 
class tik_tak_map:
    def __init__(self, w, h): 
        self.w = w
        self.h = h
        self.map = []
        self.rounds = 0
    
    def creation(self): 
        # makes an array of hight = h and with = w filled with |_| 
        self.map = [["|_|" for x in range(self.w)] for y in range(self.h)]
   
    def display(self):
        # print(f"the with is {range(self.w)} and the hight {range(self.h)}")
        player_turn = remainder(self.rounds, (self.rounds + 1)) # bug in this line of code 
        print(f"round {self.rounds} player {player_turn}") 
        for x in range(self.h): 
            print(self.map[x][:]) # print whole array using a slice

    def insert(self,input_hight,input_with,player):
        self.rounds = self.rounds + 1
        match player:
            case 1:
                self.map[input_hight][input_with] = '|O|'
            case 2:
                self.map[input_hight][input_with] = '|X|'

    def test(self):
        for x in range(self.h):
            self.map[x][0] = str(x) # self.map[h][w]
    
    def __str__(self):
        return
        # return f"a matrix map of a hight of {self.h} and a with {self.w}\nand the dog shit map look like this {self.map}"

def intro():
    print("-------------------------")
    print("  a simple tik tow game  ")
    

def main():
    print("hello world")
    user_input = input()
    if user_input == "quit":    exit() 

if __name__ == "__main__":
    main()

m1 = tik_tak_map(3,3)
m1.creation()
m1.display()
m1.insert(1,1,2)
m1.display()
m1.insert(1,0,1)  
m1.display()  
