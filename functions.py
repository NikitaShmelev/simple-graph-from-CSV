import csv
from numpy import genfromtxt
import matplotlib.pyplot as plt


def get_data(file_name):
    return genfromtxt(file_name, delimiter=',')


def get_header(file_name):
    file = open(file_name)
    csvreader = csv.reader(file)
    header = next(csvreader)
    file.close()
    return header


def make_graph(data, header, dotted):
    plt.plot(
        [i[0] for i in data[1:]],  # X
        [i[1] for i in data[1:]],  # y
        ':' if dotted else '-'
    )
    plt.xlabel(header[0])
    plt.ylabel(header[1])
    plt.show()
