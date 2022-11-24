import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import ShowingData as gd



def plottingdata():
    #Putting the right data in a varibel
    data = gd.fetchingData(gd.ldata)
    #setting the right data
    data1 = data['first_name']
    data2 = data['ged']

    y_value = data1
    x_value = data2

    plt.figure()
    plt.xlabel("God to english")
    plt.ylabel("First Name")
    plt.scatter(x_value,y_value)
    plt.show()

if __name__ == '__main__':
    plottingdata()