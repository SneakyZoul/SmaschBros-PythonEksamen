import numpy as np
import matplotlib.pyplot as plt
from itertools import cycle, islice
import handlingdata.GettingData as getd
from matplotlib.offsetbox import OffsetImage, AnnotationBbox


def top3_plotting():
    # Gets the absolute dataframe
    data = getd.fetching_data()

    # Sets x-numerical range.
    x = np.arange(len(data['character'].tolist()))  # outputs array of indexes of 'character' column
    names = data['character'].tolist()
    first_place = data['firstPlaces'].tolist()
    second_place = data['secondPlaces'].tolist()
    third_place = data['thirdPlaces'].tolist()

    # Makes 3 bars with each individual value and colors. Representing each of their data
    plt.bar(x - 0.25, first_place, 0.2, color="#FFD700", edgecolor="#FFD700", label="1st Place", linewidth=5)
    plt.bar(x, second_place, 0.2, color="#C0C0C0", edgecolor="#C0C0C0", label="2nd Place", linewidth=5)
    plt.bar(x + 0.25, third_place, 0.2, color="#CD7F32", edgecolor="#CD7F32", label="3rd Place", linewidth=5)

    # Sets x & y labels, title and legend
    plt.ylabel("Amount", fontsize=45)
    plt.xlabel("Character Name", fontsize=45)
    plt.title("Tournament Data", fontsize=45)
    plt.legend(loc="upper right", fontsize=30)

    # Increases size of x & y ticks size
    plt.yticks(fontsize=34)
    plt.xticks(x, names, rotation=45)  # x = index, names = labels for xticks

    # Configures size of plot
    current_fig = plt.gcf()  # Get current figure
    current_fig.set_size_inches(100, 20)
    # Makes it neat
    plt.tight_layout()
    plt.show()


def top8_plotting():
    # Gets the absolute dataframe
    data = getd.fetching_data()

    # Sets x-numerical range.
    x = np.arange(len(data['character'].tolist()))  # outputs array of indexes of 'character' column
    names = data['character'].tolist()

    # Configures custom colors for bars
    # islice is an iteration tool
    # cycle returns iterator object for islice
    my_colors = list(islice(cycle(['#FFD700', '#C0C0C0', '#CD7F32', '#80c904',
                                   '#73b504', '#66a103', '#5a8d03', '#4d7902']), None, 8))

    # Makes plot with DataFrame.plot
    data.plot(kind="bar", color=my_colors, edgecolor="#000000")

    # Sets x & y labels, title and legend
    plt.ylabel("Amount", fontsize=45)
    plt.xlabel("Character Name", fontsize=45)
    plt.title("Tournament Data", fontsize=45)
    plt.xticks(x, names, rotation=45)
    plt.yticks(fontsize=34)
    plt.legend(['First Place', 'Second Place', 'Third Place', 'Fourth Place',
                'Fifth Place', 'Sixth Place', 'Seventh Place', 'Eighth Place'],
               loc="best", fontsize=30)

    # Configures size of plot
    current_fig = plt.gcf()  # Get current figure
    current_fig.set_size_inches(100, 20)
    # Makes the plot neat
    plt.tight_layout()

    plt.show()


def masked_plot(characters):
    # Gets the absolute dataframe
    data = getd.fetching_data()
    # Makes mask
    mask = data['character'].isin(characters)

    data = data[mask]

    # Sets x-numerical range.
    x = np.arange(len(data['character'].tolist()))  # outputs array of indexes of 'character' column
    names = data['character'].tolist()

    # Configures custom colors for bars
    # islice is an iteration tool
    # cycle returns iterator object for islice
    my_colors = list(islice(cycle(['#FFD700', '#C0C0C0', '#CD7F32', '#80c904',
                                   '#73b504', '#66a103', '#5a8d03', '#4d7902']), None, 8))

    # Makes bar plot from DataFrame.plot
    data.plot(kind="bar", color=my_colors, edgecolor="#000000")

    # Sets x & y labels
    plt.ylabel("Amount")
    plt.xlabel("Character Name")
    plt.title("Tournament Data")
    plt.xticks(x, names, rotation=45)
    plt.legend(['First Place', 'Second Place', 'Third Place', 'Fourth Place',
                'Fifth Place', 'Sixth Place', 'Seventh Place', 'Eighth Place'],
               loc="best")

    # Makes plot neat
    plt.tight_layout()

    plt.show()


def get_image(path, zoom=1):
    # Returns modified image
    return OffsetImage(plt.imread(path), zoom=zoom)


def win_scatter():
    # Gets the absolute dataframe
    data = getd.fetching_data()
    images = getd.fetching_images()

    # Sets x-numerical range.
    x = np.arange(len(data['character'].tolist()))  # outputs array of indexes of 'character' column
    names = data['character'].tolist()
    y = data['firstPlaces']

    # Configures figure and plot as ax
    fig, ax = plt.subplots()
    # Makes scatter points
    ax.scatter(x, y)

    # Sets x & y labels, title and xticks
    ax.set_title("1st Place Data", fontsize=65)
    ax.set_xlabel("Character Name", fontsize=65)
    ax.set_ylabel("Amount", fontsize=65)
    ax.set_xticks(x)
    plt.yticks(fontsize=45)
    ax.set_xticklabels(names, rotation=75)

    # Configures line width of spine. So it fits the size of the plot
    ax.spines['left'].set_linewidth(4)
    ax.spines['right'].set_linewidth(4)
    ax.spines['top'].set_linewidth(4)
    ax.spines['bottom'].set_linewidth(4)

    ax.tick_params(axis="x")

    # For loop that iterates every dot, and places an image on given spot
    for x0, y0, icon in zip(x, y, images):
        ab = AnnotationBbox(get_image(icon, 0.2), (x0, y0), frameon=False)
        ax.add_artist(ab)

    # Configures size of plot
    current_fig = plt.gcf()  # Get Current Figure
    current_fig.set_size_inches(50, 20)

    # Makes plot neat
    current_fig.tight_layout()

    plt.subplot()
    plt.show()


if __name__ == '__main__':
    # top3_plotting()

    #top8_plotting()

    demo_list = ["Mario", "Luigi", "Roy", "Bowser", "Mewtwo", "Olimar", "Fox", "Joker"]
    versus_list = ["Captain Falcon", "Piranha Plant", "Joker"]
    masked_plot(versus_list)

    #win_scatter()
