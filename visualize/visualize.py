# Reference for plotly https://plot.ly/python/offline/
import plotly
# from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import plotly.offline as offline
import plotly.graph_objs as go


def genereateBarGraph(X, Y, fileName):
    offline.iplot([go.Bar(x=X, y=Y)], filename=fileName)
