import matplotlib.cbook
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from itertools import cycle, islice

import pylab as pl

import handlingdata.GettingData as getd

from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from matplotlib.cbook import get_sample_data
import os
from config.definitions import ROOT_DIR



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

    plt.bar(x - 0.25, first_place, 0.2, color="#FFD700", edgecolor="#FFD700", label="1st Place", linewidth=5)
    plt.bar(x, second_place, 0.2, color="#C0C0C0", edgecolor="#C0C0C0", label="2nd Place", linewidth=5)
    plt.bar(x + 0.25, third_place, 0.2, color="#CD7F32", edgecolor="#CD7F32", label="3rd Place", linewidth=5)

    plt.ylabel("Amount", fontsize=45)
    plt.xlabel("Character Name", fontsize=45)
    plt.title("Tournament Data", fontsize=45)
    plt.legend(loc="upper right", fontsize=30)
    plt.yticks(fontsize=34)
    plt.xticks(x, names, rotation=45)

    current_fig = plt.gcf()
    current_fig.set_size_inches(100, 20)
    plt.tight_layout()
    plt.show()


def top8_plotting():
    data = getd.fetching_data()

    x = np.arange(len(data['character'].tolist()))
    names = data['character'].tolist()

    my_colors = list(islice(cycle(['#FFD700', '#C0C0C0', '#CD7F32', '#80c904',
                                   '#73b504', '#66a103', '#5a8d03', '#4d7902']), None, 8))

    data.plot(kind="bar", color=my_colors, edgecolor="#000000")

    plt.ylabel("Amount", fontsize=45)
    plt.xlabel("Character Name", fontsize=45)
    plt.title("Tournament Data", fontsize=45)
    plt.xticks(x, names, rotation=45)
    plt.yticks(fontsize=34)
    plt.legend(['First Place', 'Second Place', 'Third Place', 'Fourth Place',
                'Fifth Place', 'Sixth Place', 'Seventh Place', 'Eighth Place'],
               loc="best", fontsize=30)

    plt.tick_params(axis='x')

    current_fig = plt.gcf()
    current_fig.set_size_inches(100, 20)
    plt.tight_layout()

    plt.show()


def masked_plot(characters):
    data = getd.fetching_data()
    mask = data['character'].isin(characters)

    data = data[mask]

    x = np.arange(len(data['character'].tolist()))
    names = data['character'].tolist()

    my_colors = list(islice(cycle(['#FFD700', '#C0C0C0', '#CD7F32', '#80c904',
                                   '#73b504', '#66a103', '#5a8d03', '#4d7902']), None, 8))

    data.plot(kind="bar", color=my_colors, edgecolor="#000000")

    plt.ylabel("Amount")
    plt.xlabel("Character Name")
    plt.title("Tournament Data")
    plt.xticks(x, names, rotation=45)
    plt.legend(['First Place', 'Second Place', 'Third Place', 'Fourth Place',
                'Fifth Place', 'Sixth Place', 'Seventh Place', 'Eighth Place'],
               loc="best")

    plt.tick_params(axis='x')

    plt.tight_layout()

    plt.show()


def getImage(path, zoom=1):
    return OffsetImage(plt.imread(path), zoom=zoom)


def win_scatter():
    data = getd.fetching_data()
    images = getd.fetching_images()

    x = np.arange(len(data['character'].tolist()))
    names = data['character'].tolist()
    y = data['firstPlaces']

    fig, ax = plt.subplots()
    ax.scatter(x, y)
    ax.set_title("1st Place Data", fontsize=65)
    ax.set_xlabel("Character Name", fontsize=65)
    ax.set_ylabel("Amount", fontsize=65)
    ax.set_xticks(x)
    ax.set_xticklabels(names, rotation=75)

    #
    ax.spines['left'].set_linewidth(4)
    ax.spines['right'].set_linewidth(4)
    ax.spines['top'].set_linewidth(4)
    ax.spines['bottom'].set_linewidth(4)

    ax.tick_params(axis="x")

    for x0, y0, icon in zip(x, y, images):
        ab = AnnotationBbox(getImage(icon, 0.2), (x0, y0), frameon=False)
        ax.add_artist(ab)

    current_fig = plt.gcf()
    current_fig.set_size_inches(50, 20)
    current_fig.tight_layout()

    plt.subplot()
    plt.show()


if __name__ == '__main__':
    #top3_plotting()

    #top8_plotting()

    demo_list = ["Mario", "Luigi", "Roy", "Bowser", "Mewtwo", "Olimar", "Fox", "Joker"]
    versus_list = ["Captain Falcon", "Piranha Plant", "Joker"]
    #masked_plot(versus_list)

    win_scatter()