import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import ShowingData as gd



def plottingdata(data):
    #Putting the right data in a varibel
    data = gd.fetchingData(data)
    #setting the right data
    data1 = data['Name']
    data2 = data['Play_style']

    y_value = data1
    x_value = data2

    plt.figure()
    plt.xlabel("God to english")
    plt.ylabel("First Name")
    plt.scatter(x_value,y_value)
    plt.show()

if __name__ == '__main__':
    plottingdata()