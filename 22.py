#playing Round 1

Player1=input("+Round1: \nplayer1 turn (Scissors/Paper/Rock) ")
Player2=input("+Round1: \nplayer2 turn (Scissors/Paper/Rock) ")
if (Player1=="Paper" and Player2=="Paper") or (Player1=="Rock" and Player2=="Rock") or (Player1=="Scissors" and Player2=="Scissors"):
    print('tie!')
elif Player1=="Scissors":
    if Player2=="Rock":
        print("+Round1= \n+Player2 has won!")
    elif Player2=="Paper":
        print("+Round1= \n+Player1 has won!")
elif Player1=='Rock':
    if Player2=='Scissors':
        print("+Round1= \n+Player1 has won!")
    elif Player2=="Paper":
        print("+Round1= \n+Player2 has won!")
elif Player1=="Paper":
    if Player2=='Scissors':
        print("+Round1= \n+Player2 has won!")
    elif Player2=='Rock':
        print("+Round1= \n+Player1 has won!")
else:
    print("you did not enter the rules correctly, Round 1 has been lost")

#playing Round 2

Player1R2=input("+Round2: \nplayer1 turn (Scissors/Paper/Rock) ")
Player2R2=input("+Round2: \nplayer2 turn (Scissors/Paper/Rock) ")
if (Player1R2=="Paper" and Player2R2=="Paper") or (Player1R2=="Rock" and Player2R2=="Rock") or (Player1R2=="Scissors" and Player2R2=="Scissors"):
    print('tie!')
elif Player1R2=="Scissors":
    if Player2R2=="Rock":
        print("+Round2= \n+Player2 has won!")
    elif Player2R2=="Paper":
        print("+Round2= \n+Player1 has won!")
elif Player1R2=='Rock':
    if Player2R2=='Scissors':
        print("+Round2= \n+Player1 has won!")
    elif Player2R2=="Paper":
        print("+Round2= \n+Player2 has won!")
elif Player1R2=="Paper":
    if Player2R2=='Scissors':
        print("+Round2= \n+Player2 has won!")
    elif Player2R2=='Rock':
        print("+Round2= \n+Player1 has won!")
else:
    print("you did not enter the rules correctly, Round 2 has been lost")
        
#playing Round 3

Player1R3=input("+Round3: \nplayer1 turn (Scissors/Paper/Rock) ")
Player2R3=input("+Round3: \nplayer2 turn (Scissors/Paper/Rock) ")
if (Player1R3=="Paper" and Player2R3=="Paper") or (Player1R3=="Rock" and Player2R3=="Rock") or (Player1R3=="Scissors" and Player2R3=="Scissors"):
    print('tie!')
elif Player1R3=="Scissors":
    if Player2R3=="Rock":
        print("+Round3= \n+Player2 has won!")
    elif Player2R3=="Paper":
        print("+Round3= \n+Player1 has won!")
elif Player1R3=='Rock':
    if Player2R3=='Scissors':
        print("+Round3= \n+Player1 has won!")
    elif Player2R3=="Paper":
        print("+Round3= \n+Player2 has won!")
elif Player1R3=="Paper":
    if Player2R3=='Scissors':
        print("+Round3= \n+Player2 has won!")
    elif Player2R3=='Rock':
        print("+Round3= \n+Player1 has won!")
else:
    print("you did not enter the rules correctly, Round 3 has been lost")


        
