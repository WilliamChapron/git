# import module random, time, pyfiglet

# Create list named list pc with 3 element, rock, paper and cisors



# Init emotional function with no args

   # Create list named emotions with 4 elements, Friendly, Killer, No logic, Computer Win

   # Assign to rockpercent variable, 1 divide by the number of lenght of listpc
   # Assign to paperpercent variable, 1 divide by the number of lenght of listpc
   # Assign to cisorspercent variable, 1 divide by the number of lenght of listpc

   # Init emotional variable with a generate random value between 0 and 3
   # Init emotionalIndex with the index of emotional variable found in emotions list

   # Display the Computer Conduct with a display of emotional variable

   # if emotionalIndex is equal to 0
       # So
       # Assign rockpercent to 0.1
       # Assign paperpercent to 0.6
       # Assign cisorspercent to 0.3
   # Elseif
       # So
       # Assign rockpercent to 0.5
       # Assign paperpercent to 0.1
       # Assign cisorspercent to 0.4

   # Init coeffs list with the rockpercent, paperpercent and cisorspercent variable


   
   # if emotionalIndex equal to 3
     # So
     # Assign computerchoice to Win Anyway string
   # Else 
     # Assign to computerchoice, Generate random value with random choice function with listpc and coeffs args, and transform list type to string type
       
   # if emotionalIndex equal to 3 
     # So
     # Assign Computer to 3
   # Else
     # So
     # Assign Computer to index of computerchoice variable from listpc list

   # Now we have INT Computer and string ComputerChoice, we return it to use it in next condition to know the choice of computer
   # Return computerchoice and Computer


# ROUND SYSTEM

   # Init player, computer point and roundIs to 0
   # While Loop is True
       # So 
       # display round

       # Assign playerchoice to -1 

       # Assign computer choice and Computer to emotional function with no args to get the return of emotional function in this two variables
     
       # ASK CHOICE TO PLAYER, UNTIL NOT MAKE, ASK AGAIN

           # Assign inputplayerchoice with the return of the execution of input function as What is your choice
  
           # Get INPUT in condition, if INPUT in table -> execute instruction
           # if inputplayerchoice is in table with string elements ROCK,PAPER,CISORS,WELL,rock,paper,cisors,well,1,2,3,4

               # Transform INPUT in capital letters string to INT to use it in try except to assign Player playerchoice value because they aren't in listpc
               # if inputplayerchoice equal to string ROCK
                   # So
                   # Assign inputplayerchoice to 1
               # Elseif inputplayerchoice equal to string PAPER
                   # So
                   # Assign inputplayerchoice to 2
               # Elseif inputplayerchoice equal to string CISORS
                   # So
                   # Assign inputplayerchoice to 3

               # TRY/EXCEPT IF IS STRING OR IF STRING NUMBER
               # Try
                   
                   #Condition if else in try except to change player in case of player use well
                   # If inputplayerchoice is in table with string elements WELL,well,4
                     # So
                     # Assign Player to 4
                     # Assign playerchoice to string well
                   # Else
                     # So
                     # Assign Player to the integer of the inputplayerchoice string
                     # Assign Player to Player - 1
                     # We make sub to get Player from the table
                     # Assign playerchoice to value from listpc list found with index of Player variable
               # except it's not a number try to find index of the right string
               # Except
           # condition if to ask again if player don't make right input choice
           # if playerchoice equal to -1
               # So 
               # display you must type a number





       # GAME SYSTEM AND POINT ADD

       # create condition if elif else to make winner according to variables Player/Computer 
       # if Player equal to 0 and Computer equal to 1
           # So
           # Display Player Win
           # Assign to pointPlayer, pointPlayer + 1
       # else if Player equal to 0 and Computer equal to 2
           # So
           # Display Player Win
           # Assign to pointPlayer, pointPlayer + 1
       # else if Player equal to 1 and Computer equal to 0
           # So
           # Display Computer Win
       # else if Player equal to 0 and Computer equal to 2
           # So
           # Display Computer Win
           # Assign to pointComputer, pointComputer + 1
       # else if Player equal to 2 and Computer equal to 0
           # So
           # Display Computer Win
           # Assign to pointComputer, pointComputer + 1
       # else if Player equal to 2 and Computer equal to 1
           # So
           # Display Computer Win
           # Assign to pointPlayer, pointPlayer + 1
       # condition elseif when computer win anyway thanks to his emotions 
       # else if Computer equal to 3
          # So 
          # Display that Computer Win thanks to his Emotions
          # Assign to pointComputer, pointComputer + 1
       # when well win rock and cisors -> print win with well 
       # else if Player equal to 4 and Computer equal to 0 or 2
         # So
         # Display that player win with well
         # Assign to pointPlayer, pointPlayer + 1
       # when well don't win paper -> it's for print you loose in this case
       # else if Player equal to 4 and computer equal to 1
         # So 
         # Display that player loose because of paper win well
         # Assign to pointComputer, pointComputer + 1
       # in others case -> equality
       # Else 
           # So 
           # Display Equality

       # Display computer choice and player choice in string type with pyfiglet draw module in each round
       # Display PLAYER + playerchoice in the same line
       # Display COMPUTER + computerchoice in the same line

       # Display player point
       # Display computer point

       # Increment roundIs value to know in which round we are
       # Assign roundIs to roundIs + 1

       # END OR NOT ? condition if according to c and p point with instruction -> ask play again 
       # if pointPlayer is inferior or equal to 5 or pointComputer is inferior or equal to 5
           # So 
           # Init question2 with input as Do you want to play again ?
           # if question2 equal to play string 
               # So 
               # Execute round function 
           # Break


# start print of the game to say you'r welcome
# Display hi bro

# Timer before ask question with input
# Timer with argument 1 second, to stop code


# Play function, ask do you want play the first time 
# Init play function (the first time accept to play with right input)
   # input to ask if you want play
   # init question with the return of the execution of the imput function as Do you want to play 
   # if question is in table with play,PLAY
       # So 
       # Return true


# Replay function, if you don't want play, it ask again
# Init doubleplay function
   # condition if you want you play if you don't respect input it ask again with doubleplay function
   # if assertion play function is True
       # So 
       # Execute round function
   # Else
       # So 
       # Execute doubleplay function




     
# GAME START
# if assertion play function is True
   # So 
   # Execute round function
# Else, ask again with doubleplay function
# Else
   # So 
   # Display as do you don't want play ?
   # Ask again
   # execute doubleplay function




