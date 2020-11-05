import random

def login():
  print("Welcome to Guess the Number")
  username=input("Please enter your username :")
  password=input("PLease enter your password :")

  if username =="Prathyusha" and password =="1234":
    print("You have entered the correct credentials!Login Succes!")
    return True
  else:
    print("You have entered the wrong credentials!Login Failed")
    return False


def start_game():
  if login():
    number=random.randint(1,10)
    chances=0

    while chances  < 10:
      print("The random number has been generated")
      guess= int(input("Guess the Number!:"))
      chances=chances+1

      if guess ==number:
        print("Hurray!You guessed the number!Please run the program again to play again.")
        break

      elif guess<number:
        print("You are closer to the number")
      elif guess<number:
        print("You are far from the number")
    if chances >10:
      print("Oops!You have have run out of chances!Please run the program again to play again.")
      print("GAME OVER!!")
start_game()
