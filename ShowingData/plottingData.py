import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
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

    y_value = data['Lost'].tolist()
    x_value = data['Name'].tolist()

    plt.figure()
    plt.title("Lost")
    plt.xlabel("Names")
    plt.ylabel("Tournaments Lost")
    plt.scatter(x_value,y_value)
    plt.show()

def overall_plotting():
    data = gd.fetchingData()

    x = np.arange(len(data['Name'].tolist()))
    names = data['Name'].tolist()
    winLine = data['Won'].tolist()
    playLine = data['Played'].tolist()
    lostLine = data['Lost'].tolist()

    fig = plt.figure()
    # ax.bar(x, winLine, color='g', width=0.25)
    # ax.bar(x, playLine, color='b', width=0.25)
    # ax.bar(x, lostLine, color='r', width=0.25)
    # plt.show()

    plt.bar(x - 0.2, winLine, 0.2, color="g", label="Won")
    plt.bar(x, playLine, 0.2, color="b", label="Played")
    plt.bar(x + 0.2, lostLine, 0.2, color="r", label="Lost")
    plt.legend(loc="upper right")
    plt.xticks(x, names)
    plt.show()


if __name__ == '__main__':
   overall_plotting()