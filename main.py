print('Rock-Paper-Scissors')
print('You [player 1] will play rock, paper, scissors against the computer [player 2]')
import random
ScoreAi = 0
ScorePlayer = 0
while True:
  print('-----------------------------------------------------')
  print('choose between:')
  print('1) Rock')
  print('2) Paper')
  print('3) Scissors')
  PlayerOne = int(input('Press 1, 2, or 3. '))
  Computer = random.randint(1,3)
  print('The Computer chose ' + str(Computer))
  if PlayerOne == Computer:
    print('It is a tie!')
    print('-----------------------------------------------------')
    ScoreAi = ScoreAi + 1
    ScorePlayer = ScorePlayer + 1
  elif PlayerOne == 1 and Computer == 2:
    print(' Computers Paper beats your rock! You lose! ')
    print('-----------------------------------------------------')
    ScoreAi = ScoreAi + 1
  elif PlayerOne == 1 and Computer == 3:
    print('Your Rock beats Computers scissors! You win!')
    print('-----------------------------------------------------')
    ScorePlayer = ScorePlayer + 1
  elif PlayerOne == 2 and Computer == 3:
    print('Computers Scissors beats your paper! You Lose!')
    print('-----------------------------------------------------')
    ScoreAi = ScoreAi + 1
  elif PlayerOne == 2 and Computer == 1:
    print('Your Paper beats Computers rock! You Win!')
    print('-----------------------------------------------------')
    ScorePlayer = ScorePlayer + 1
  elif PlayerOne == 3 and Computer == 2:
    print('Your Scissors beats Computers paper! You Win!')
    print('-----------------------------------------------------')
    ScorePlayer = ScorePlayer + 1
  elif PlayerOne == 3 and Computer == 1:
    print('Computers Rock beats your paper! You Lose!')
    print('-----------------------------------------------------')
    ScoreAi = ScoreAi + 1
  print('Do you want to keep playing?')
  print('1) Yes')
  print('2) No')
  Choice = input('Choose 1 or 2.')

  if Choice == '2':
    print('-----------------------------------------------------')
    print('You won ' + str(ScorePlayer) + ' game/s and the computer won ' + str(ScoreAi) + ' game/s.')
    if ScorePlayer > ScoreAi:
      print('Congratulations! You win!')
    elif ScorePlayer < ScoreAi:
      print('The computer won most of the games. You lose!')
    else:
      print('Tie!')
    print('-----------------------------------------------------')  
    print('Thank you for playing!')
    print("(rock-paper-scissors)")
   
    print(' __     ____') 
    print("/  \    |  |    ]< ")
    print("----    ----") 
    
    break