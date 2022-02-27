import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
choices = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
# if choice == 0:
#   print(rock)
# elif choice == 1:
#   print(paper)
# else :
#   print(scissors)
if choices >= 3 or choices < 0:
  print("Entered wrong number!!!")
all_details = [rock, paper, scissors]
x = all_details[choices]
print(x)


comp = random.randint(0,2)
y = all_details[comp]
print("Computer chose: " + y)
if choices == 0 and comp == 2:
  print("You win!!!")
elif choices == 2 and comp ==0:
  print("You lose")
elif choices > comp:
  print("You win!")
elif choices < comp:
  print("You lost")
elif choices == comp:
  print("Draw")
