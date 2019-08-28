import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
import os


def plotPoints(x,y,xlabel,ylabel,title):
    fig = plt.figure(figsize=(20,10))

    plt.plot(x,y,'bo-')
    plt.title(f'{title}', fontsize=36)
    plt.xlabel(f'{xlabel}', fontsize=24)
    plt.ylabel(f'{ylabel}', fontsize=24)

    # define the path where the file will be saved
    IMAGE_FOLDER = os.path.abspath(os.path.dirname(__file__)) + '/static/graph_images/'

    FILENAME = 'plot_graph.png'

    URL = IMAGE_FOLDER + FILENAME

    # save the file and return the filename
    fig.savefig(URL)
    return FILENAME
