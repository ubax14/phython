import random

def main():
     value=99
     print=(f'the value is{value}')
     change_me(value)
def change_me(arg):
     print("i'm changing  the value")
     arg=0
     print(f'now the value is {arg}')
main()

def main():
    dist_kilm=int(input("enter a number of distance kilometer"))
    change_d(dist_kilm)
def change_d(a):
     miles=a*0.62
     print("now the convertion is ",miles,"miles")
main()