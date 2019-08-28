import pandas as pd
import os


BASEDIR = os.path.abspath(os.path.dirname(__file__))

def showData(d=','):
    URL = BASEDIR + '/static/data/redsox_2018_hitting.txt'

    bos18 = pd.read_csv(URL, sep=d)

    return bos18.to_html()
