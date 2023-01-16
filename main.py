print('Rock-Paper-Scissors')
print('You [player 1] will play rock, paper, scissors against the computer [player 2]')
import random
ScoreAi = 0
ScorePlayer = 0
while True:
  print('choose between:')
  print('1) Rock')
  print('2) Paper')
  print('3) Scissors')
  PlayerOne = int(input('Press 1, 2, or 3. '))
  Computer = random.randint(1,3)
  print('The Computer chose ' + str(Computer))
  if PlayerOne == Computer:
    print('It is a tie!')
    ScoreAi = ScoreAi + 1
    ScorePlayer = ScorePlayer + 1
  elif PlayerOne == 1 and Computer == 2:
    print(' Computers Paper beats your rock! You lose! ')
    ScoreAi = ScoreAi + 1
  elif PlayerOne == 1 and Computer == 3:
    print('Your Rock beats Computers scissors! You win!')
    ScorePlayer = ScorePlayer + 1
  elif PlayerOne == 2 and Computer == 3:
    print('Computers Scissors beats your paper! You Lose!')
    ScoreAi = ScoreAi + 1
  elif PlayerOne == 2 and Computer == 1:
    print('Your Paper beats Computers rock! You Win!')
    ScorePlayer = ScorePlayer + 1
  elif PlayerOne == 3 and Computer == 2:
    print('Your Scissors beats Computers paper! You Win!')
    ScorePlayer = ScorePlayer + 1
  elif PlayerOne == 3 and Computer == 1:
    print('Computers Rock beats your paper! You Lose!')
    ScoreAi = ScoreAi + 1
  print('Do you want to keep playing?')
  print('1) Yes')
  print('2) No')
  Choice = input('Choose 1 or 2.')

  
  print('Thank you for playing!')
  break

  
  urllib.request.urlretrieve(
  'https://media.istockphoto.com/id/1056840214/vector/rock-paper-scissors-vector-illustration.jpg?s=1024x1024&w=is&k=20&c=EbGQn0HknRzWKhfbWwl2rDyZeRh5OERbVGr-PZgh-qM=')
  
img=Image.open("https://media.istockphoto.com/id/1056840214/vector/rock-paper-scissors-vector-illustration.jpg?s=1024x1024&w=is&k=20&c=EbGQn0HknRzWKhfbWwl2rDyZeRh5OERbVGr-PZgh-qM=")
img.show()