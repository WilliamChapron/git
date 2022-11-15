
import random
import time
import pyfiglet

listpc = ["rock", "paper", "cisors"]



def emotional():

   emotions = ["Friendly","Killer","No logic","Computer win"]

   rockpercent = 1 / len(listpc)
   paperpercent = 1 / len(listpc)
   cisorspercent = 1 / len(listpc)

   emotional = emotions[random.randint(0, 3)]
   emotionalIndex = emotions.index(emotional)

   print("THE COMPUTER CONDUCT IS ", emotional,", Your game can differ, You must have a strategy !")

   if emotionalIndex == 0:
       rockpercent = 0.1
       paperpercent = 0.6
       cisorspercent = 0.3
   # Elseif
   elif emotionalIndex == 1:
       rockpercent = 0.5
       paperpercent = 0.1
       cisorspercent = 0.4

   coeffs = [rockpercent, paperpercent, cisorspercent]


   
   if emotionalIndex == 3:
     computerchoice = "Win Anyway !"
   else:
     computerchoice = "".join(random.choices(listpc,coeffs))
       
   if emotionalIndex == 3:
     Computer = 3
   else:
     Computer = listpc.index(computerchoice)

   return computerchoice,Computer


def round():


   pointPlayer = 0
   pointComputer = 0
   roundIs = 0

   while True:
       print("YOU ARE IN : " + str(roundIs) + " ROUND")

       playerchoice = -1

       computerchoice, Computer = emotional() 
     
       while playerchoice == -1:

           inputplayerchoice = input("What is your choice ? (rock, paper or cisors)")
           if inputplayerchoice in ["ROCK","PAPER","CISORS", "WELL", "rock", "paper", "cisors", "well", "1", "2", "3", "4"]:

               if inputplayerchoice == "ROCK":
                   inputplayerchoice = 1
               elif inputplayerchoice == "PAPER":
                   inputplayerchoice = 2
               elif inputplayerchoice == "CISORS":
                   inputplayerchoice = 3

               try:   
                   if inputplayerchoice in ["WELL", "well", "4"]:
                     Player = 4
                     playerchoice = "well"
                   else:
                     Player = int(inputplayerchoice)
                     Player -= 1
                     playerchoice = listpc[Player]
               except:
                   Player = listpc.index(inputplayerchoice)
                   playerchoice = listpc[Player]
           if playerchoice == -1:
               print("You must type you choice number")


       if Player == 0 and Computer == 1:
           print(pyfiglet.figlet_format("Player Win"))
           pointPlayer += 1
       elif Player == 0 and Computer == 2:
           print(pyfiglet.figlet_format("Player Win"))
           pointPlayer += 1
       elif Player == 1 and Computer == 0:
           print(pyfiglet.figlet_format("Computer Win"))
           pointComputer += 1
       elif Player == 1 and Computer == 2:
           print(pyfiglet.figlet_format("Computer Win"))
           pointComputer += 1
       elif Player == 2 and Computer == 0:
           print(pyfiglet.figlet_format("Computer Win"))
           pointComputer += 1
       elif Player == 2 and Computer == 1:
           print(pyfiglet.figlet_format("Player Win"))
           pointPlayer += 1
       elif Computer == 3:
          print(pyfiglet.figlet_format("Computer Win thanks to Emotions"))
          pointComputer += 1
       elif Player == 4 and Computer == 0 or Computer == 2:
         print(pyfiglet.figlet_format("Player win with Well"))
         pointPlayer += 1
       elif Player == 4 and Computer == 1:
         print(pyfiglet.figlet_format("Computer win because paper fuck well"))
         pointComputer += 1
       else:
           print(pyfiglet.figlet_format("Equality"))


       print(pyfiglet.figlet_format("PLAYER") + pyfiglet.figlet_format(playerchoice))
       print(pyfiglet.figlet_format("COMPUTER") + pyfiglet.figlet_format(computerchoice))

       print("The player points are : " + str(pointPlayer))
       print("The computer points are : " + str(pointComputer))

       roundIs += 1


       if pointPlayer >= 5  or pointComputer >= 5:
           question2 = input("Do you want to play again ?")
           if question2 == "play":
               round()
           break

print("Hi bro, welcome on chi fu mi game !")

time.sleep(1)


def play():
   question = input("Do you want to play ? (type play to begin !)")
   if question in ["play","PLAY"]:
       return True


def doubleplay():
   if play():
       round()
   else:
       doubleplay()




  
if play():
   round()
else:
   print("do you don't want play ?")
   doubleplay()






 
     



 
         
 

 




















































































