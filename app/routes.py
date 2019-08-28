from app import app
from flask import render_template
from app.graph import plotPoints
from app.tables import showData
from app.parse import getData


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/graphs')
def graphs():
    x = [1,2,3,4]
    y = [2.3,4.2,5.6,8.8]
    xlabel = 'Years'
    ylabel = 'Population (billions)'
    title = 'Population Over Time'

    FILENAME = plotPoints(x,y,xlabel,ylabel,title)

    return render_template('graph.html', FILENAME=FILENAME)


@app.route('/tables')
def tables():
    table_html = showData()
    return render_template('tables.html', table_html=table_html)


@app.route('/parse')
def parse():
    URL = 'http://www.arthurleej.com/e-love.html'
    data = getData(URL)
    return render_template('parse.html', data=data)
