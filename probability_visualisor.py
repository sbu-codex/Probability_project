import matplotlib.pyplot as plt
import pandas as pd
import random

data = []
def main():
    print("Welcome to the Longterm relative frequency of probability Visualisa")
    #Show menu
    option = 99
    
    while option != 5:
        
        menu()
        option = int(input("Choose an option: "))

        if option == 1:
            die_roll()
        elif option == 2:
            visual_rep()
        elif option == 3:
            show_data()
        elif option ==4:
            show_stats()
        else:
            print ("Invalid option")
            
        



def menu():
    print("********************************")
    print("MENU:",
          "\n1. Roll die",
          "\n2. Visual represantation.",
          "\n3. show data",
          "\n4. Show Stats",
          "\n5. EXIT. ",
          )
    print("********************************")


def die_roll():
    n = int(input("Enter the number of desired rolls: "))


    for i in range(n):
        outcome = random.randint(1,6)
        data.append(outcome)

def visual_rep():
    

    if not data:
        print("No data to visualize. Roll the die first.")
        return

    total_rolls = len(data)
    frequencies = [data.count(i) for i in range(1, 7)]
    relative_frequencies = [f / total_rolls for f in frequencies]

    plt.bar(range(1, 7), relative_frequencies, align='center', edgecolor='black')
    plt.xlabel('Die face')
    plt.ylabel('Relative Frequency')
    plt.title('Relative Frequency of Die Rolls')
    plt.xticks(range(1, 7))
    plt.ylim(0, 1)
    plt.show()
    


def show_data():
    

    if not data:
        print("No data available. Roll the die first.")
        return
    
    print("Data: ", data)

def show_stats():

    if not data:
        print("No data available. Roll the die first.")
        return    

    df = pd.Series(data)
    print(df.describe())
    
    
    
main()
