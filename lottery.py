from random import randint as RN

# class based program to help us see who gets to work overtime.

class Lottery: #defined a class that contines all the functions we need for our program
    def __init__(self, participants = [], dates = [], winner = {}):
         self.participants = participants
         self.dates = dates
         self.winner = winner

    def randomizer(self):
        i = RN(0, len(self.participants)-1)
        w1 = self.participants[i]
        self.winner[w1] = ""
        self.participants.remove(w1)
        x = RN(0, len(self.dates)-1)
        d1 = self.dates[x]
        self.winner[w1] = d1
        self.dates.remove(d1)
        return input("The winner is" + str(self.winner))

    def randomize(self):
        for x in range(0, len(self.dates)):
            self.randomizer()     
    def names_inupt(self):
        for i in range(int(user_input1)):
            parts = input("enter the name of the participants one by one followed by enter: ")
            self.participants.append(parts)

    def date_input(self):
        for i in range(int(user_input2)):
             date = input("enter the dates one by one followed by enter: ")
             self.dates.append(date)
l1 = input(# to make the program look nicer.
"""   w           w    EEEEEEEE    L        CCCCCCC   OOOOOOOO        M      M      EEEEEEEE
    w    w w   w    E           L       C         O        O      M M    M  M     E
     w  w   w  w    EEEEEEEE    L       C          O      O      M   M  M    M    EEEEEEEE
      w       w     E           L       C           O    O      M     MM      M   E
       W      W     EEEEEEEE    LLLLLL   CCCCCCC     OOOO      M               M  EEEEEEEE
    Press any key to continue """)

    #Getting users  with safety procedure so the program doesn't crush
try:
    user_input1 = int(input("Please enter the number of participaints: "))
except ValueError:
    user_input1 = int(input("Invalid choice, Please enter the number of participants: "))

while user_input1 <= 1 :
    user_input1 = int(input("Invalid choice, Please enter the number of participants: "))

try:
    user_input2 = int(input("please enter the number of winning days: "))
except ValueError:
    user_input2 = int(input("Invalid choice, please enter the number of winning days: "))

#CALLING THE CLASS
lot = Lottery()
lot.names_inupt()
lot.date_input()

lot.randomize()


