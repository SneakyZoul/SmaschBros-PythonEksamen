import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import HadlingData.GettingData as gd



def plot_won():
    #Putting the right data in a varibel
    data = gd.fetchingData()
    #setting the right data

    y_value = data['Won'].tolist()
    x_value = data['Name'].tolist()

    plt.figure()
    plt.title("Won")
    plt.xlabel("Names")
    plt.ylabel("Tournaments Won")
    plt.scatter(x_value,y_value)
    plt.show()

def plot_played():
    #Putting the right data in a varibel
    data = gd.fetchingData()
    #setting the right data

    y_value = data['Played'].tolist()
    x_value = data['Name'].tolist()

    plt.figure()
    plt.title("Played")
    plt.xlabel("Names")
    plt.ylabel("Tournaments Played")
    plt.scatter(x_value,y_value)
    plt.show()

def plot_lost():
    #Putting the right data in a varibel
    data = gd.fetchingData()
    #setting the right data

    y_value = data['tournamentsLost'].tolist()
    x_value = data['character'].tolist()

    plt.figure()
    plt.title("Lost")
    plt.xlabel("Names")
    plt.ylabel("Tournaments Lost")
    plt.scatter(x_value,y_value)
    plt.show()

def overall_plotting():
    data = gd.fetchingData()

    x = np.arange(len(data['character'].tolist()))
    names = data['character'].tolist()
    winLine = data['tournamentsWon'].tolist()
    playLine = data['tournamentsPlayed'].tolist()
    lostLine = data['tournamentsLost'].tolist()

    plt.bar(x - 0.2, winLine, 0.2, color="#b2e061", edgecolor="#000000", label="Won")
    plt.bar(x, playLine, 0.2, color="#7eb0d5", edgecolor="#000000", label="Played")
    plt.bar(x + 0.2, lostLine, 0.2, color="#fd7f6f",edgecolor="#000000", label="Lost")

    plt.ylabel("Amount")
    plt.xlabel("Character Name")
    plt.title("Tournament Data")
    plt.legend(loc="upper right")
    plt.xticks(x, names, rotation=45)
    fig = plt.gcf()
    fig.set_size_inches(100, 20)
    plt.show()


if __name__ == '__main__':
   overall_plotting()