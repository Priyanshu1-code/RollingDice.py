import random

def dice():
  while True:
    choice = input("Roll the dice.").lower()
    if choice == "y":
      print({random.randint(1, 6)}, {random.randint(1, 6)}) 
    else:
      print("THANK yoU FOR PLAyiNg.")
      break

dice()
