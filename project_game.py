import random
import math
import time

player1=raw_input("Enter name for player one")
player2=raw_input("Enter name for player two")
player3=raw_input("Enter name for player three")

print ("DICE GAME")
time.sleep(1)
i=0
dt1=0
dt2=0
while(i<5):
    print("ROUND :",i+1)
    print("\n")
    print("rolling dice for player 1")
    dice1=random.randint(1,8)
    print("You rolled",dice1)
    time.sleep(1)
    print("rolling dice for player 2")
    dice2=random.randint(1,8)
    print("You rolled",dice2)
    if(dice1>dice2):
        print("Player 1 won this time")
        i=i+1
        dt1=dt1+1
    elif(dice2>dice1):
        print("Player 2 won this time")
        i=i+1
        dt2=dt2+1
    else:
        print("There is a tie")
        print("ROUND",i+1,"will be taken again")
time.sleep(1)
if(dt1>dt2):
    print("Winner of Dice round is",player1)
    player=player1
else:
    print("Winner of Dice round is",player2)
    player=player2

print "NOW TIC-TAC-TOE ROUND WILL BE BETWEEN",player,"AND",player3

time.sleep(1)
print'\t\t\t___|__|___'
print'\t\t\t___|__|___'
print'\t\t\t   |  |   '
print("please choose your symbol:\n1.",player,"->X\n2.",player3,"->O\n>>")
print'\t\t\t_1|_2_|_3__'
print'\t\t\t_4|_5_|_6_'
print'\t\t\t 7| 8 | 9 '
list_Pl = []
list_Pl3 = []
list = ['', '', '', '', '', '', '', '', '', '']

def displayBoard(player, input):

    print('the input is', input)
    ''''''
    print"\t\t\t_", list[1], "_|_", list[2], "_|_", list[3], "_"
    print"\t\t\t_", list[4], "_|_", list[5], "_|_", list[6], "_"
    print"\t\t\t_", list[7], "_|_", list[8], "_|_", list[9], "_"

def check_input(input_pl):
    if list[input_pl] == '':
        return True
    else:
        return False


def winner(chk):
    return (list[1] == list[2] == list[3] == chk or
            list[4] == list[5] == list[6] == chk or
            list[7] == list[8] == list[9] == chk or
            list[1] == list[4] == list[7] == chk or
            list[2] == list[5] == list[8] == chk or
            list[3] == list[6] == list[9] == chk or
            list[1] == list[5] == list[9] == chk or
            list[7] == list[5] == list[3] == chk)




def play():

    list_input = 1

    error_pl3 = 'off'
    while(list_input <= 9):  # ie loop runs for 9 values from players
        if(list_input % 2 != 0):  
            print('Player:X Enter your desired position')
            input_Pl = int(input(''))  
            if (check_input(input_Pl)) and (error_pl3 == 'off'):
                            list[input_Pl] = "X"
                displayBoard('X', input_Pl)
                
                if(winner('X')):
                    print(player,"X is winner")
                    break
                    
                list_input += 1

            else:  
                print('the position is already taken.Please choose wisely player X\n`')
                continue
        else:
            
            if(list_input != 9):
                print('Player:O Enter your desired position')

                input_Pl3 = int(input(''))
                if check_input(input_Pl3):

                    list[input_Pl3] = "O"
                    list_Pl3.append(input_Pl3)
                    if(winner("O")):
                        print(player3," O is winner")
                        break
                    list_input += 1

                    displayBoard("O", input_Pl3)
                    error_pl3 = 'off'

                else:
                    print(
                        'the position is already taken .Please choose wisely player O \n')
                
                    error_pl3 = 'on'


play()



    
        
        
    
