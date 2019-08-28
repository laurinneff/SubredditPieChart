from collections import Counter
import plotly.graph_objects as go
from plotly.offline import plot
from datetime import datetime
subcount = 100 # How many subreddits should be included in the chart?
labels = []
counts = []
with open('subreddits.txt', 'r') as subreddits:
    subs = subreddits.read().split('\n')
    postcount = len(subs)
    labels = list(Counter(subs).keys())
    counts = list(Counter(subs).values())
layout = go.Layout(
    annotations=[
        go.layout.Annotation(
            showarrow=False,
            text='Rendered on: ' + datetime.utcnow().isoformat() + '+00:00.<br>Dataset size: ' + str(postcount) + ' posts',
            xanchor='right',
            x=1,
            yanchor='top',
            y=0.1
        )])
fig = go.Figure(data=[go.Pie(labels=labels[:subcount], values=counts[:subcount], textposition='inside')], layout=layout)
plot(fig, filename='piechart.html', auto_open=False)
