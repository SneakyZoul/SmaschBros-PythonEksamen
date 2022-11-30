import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import handlingdata.GettingData as getd


def plot_won():
    # Putting the right data in a variable
    data = getd.fetching_data()
    # setting the right data

    y_value = data['Won'].tolist()
    x_value = data['Name'].tolist()

    plt.figure()
    plt.title("Won")
    plt.xlabel("Names")
    plt.ylabel("Tournaments Won")
    plt.scatter(x_value, y_value)
    plt.show()


def plot_played():
    # Putting the right data in a variable
    data = getd.fetching_data()
    # setting the right data

    y_value = data['Played'].tolist()
    x_value = data['Name'].tolist()

    plt.figure()
    plt.title("Played")
    plt.xlabel("Names")
    plt.ylabel("Tournaments Played")
    plt.scatter(x_value, y_value)
    plt.show()


def plot_lost():
    # Putting the right data in a variable
    data = getd.fetching_data()
    # setting the right data

    y_value = data['tournamentsLost'].tolist()
    x_value = data['character'].tolist()

    plt.figure()
    plt.title("Lost")
    plt.xlabel("Names")
    plt.ylabel("Tournaments Lost")
    plt.scatter(x_value, y_value)
    plt.show()


def top3_plotting():
    data = getd.fetching_data()

    x = np.arange(len(data['character'].tolist()))
    names = data['character'].tolist()
    first_place = data['firstPlaces'].tolist()
    second_place = data['secondPlaces'].tolist()
    third_place = data['thirdPlaces'].tolist()

    plt.bar(x - 0.2, first_place, 0.2, color="#FFD700", edgecolor="#000000", label="Won")
    plt.bar(x, second_place, 0.2, color="#C0C0C0", edgecolor="#000000", label="Played")
    plt.bar(x + 0.2, third_place, 0.2, color="#CD7F32", edgecolor="#000000", label="Lost")

    plt.ylabel("Amount", fontsize=45)
    plt.xlabel("Character Name", fontsize=45)
    plt.title("Tournament Data", fontsize=45)
    plt.legend(loc="upper right", fontsize=30)
    plt.yticks(fontsize=34)
    plt.xticks(x, names, rotation=45)
    fig = plt.gcf()
    fig.set_size_inches(100, 20)
    plt.show()


if __name__ == '__main__':
    top3_plotting()
