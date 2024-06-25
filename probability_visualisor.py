import matplotlib.pyplot as plt
import random

data = []
def main():
    print("Welcome to the Longterm relative frequency of probability Visualisa")
    #Show menu
    option = 99
    
    while option != 5:
        
        menu()
        option = int(input("Choose an option: "))
        



def menu():
    print("********************************")
    print("MENU:",
          "\n1. Roll die",
          "\n2.Visual represantation.",
          "\n3. show data",
          "\n4. Show Stats",
          "\n5. Calculate probability. ",
          )
    print("********************************")


def die_roll():
    n = int(input("Enter the number of desired rolls"))


    for i in range(n):
        outcome = randint(1,7)
        data.append(outcome)
    
main()
