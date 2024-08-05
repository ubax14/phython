import random

import random
def main():
   x="y"
   while x=="y" or x=="Y":
       r_number=random.randint(1,20)
       luck=int(input("enter number of lucky"))
       if r_number==luck:
           print("conguraguation you'r lucky😊😊😊👏")
       else:
           print("sory enter again😒😒😒😢🤦‍♂️")
           print("the number of lucky is:",r_number)
           print("to contenues press y/Y"" or any keys you exist")
main()