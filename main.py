import random
side= int(input("enter 1 for heads and 2 for tails:"))
comp_side=random.randint(1,2)
print(f"the side is {comp_side}")
if comp_side == side:
  print("you won")
else:
  print("you lost")