#three_chartsp.py

import plotly
import plotly.graph_objs as go

from plotly.plotly import plot, iplot
from chart_studio.plotly import plot, iplot
#
# CHART 1 (PIE)
#

pie_data = [
    {"company": "Company X", "market_share": 0.55},
    {"company": "Company Y", "market_share": 0.30},
    {"company": "Company Z", "market_share": 0.15}
]

labels = [d["company"] for d in pie_data]
values = [d["market_share"] for d in pie_data]

trace = go.Pie(labels=labels, values=values)
plotly.offline.plot([trace], filename="basic_pie_chart.html", auto_open=False)

#print("----------------")
#print("GENERATING PIE CHART...")
#print(pie_data) # TODO: create a pie chart based on the pie_data

#
# CHART 2 (LINE)
#https://plot.ly/python/line-charts/

line_data = [
    {"date": "2019-01-01", "stock_price_usd": 100.00},
    {"date": "2019-01-02", "stock_price_usd": 101.01},
    {"date": "2019-01-03", "stock_price_usd": 120.20},
    {"date": "2019-01-04", "stock_price_usd": 107.07},
    {"date": "2019-01-05", "stock_price_usd": 142.42},
    {"date": "2019-01-06", "stock_price_usd": 135.35},
    {"date": "2019-01-07", "stock_price_usd": 160.60},
    {"date": "2019-01-08", "stock_price_usd": 162.62},
]

import plotly.express as px

labels = [d["date"] for d in line_data]
values = [d["stock_price_usd"] for d in line_data]

df = px.data.gapminder().query("country=='Canada'")
fig = px.line(df, x=labels, y=values, title='Stock Price Flactuation')
fig.show()
breakpoint()
#print("----------------")
#print("GENERATING LINE GRAPH...")
#print(line_data) # TODO: create a line graph based on the line_data

#
# CHART 3 (HORIZONTAL BAR)
#
import plotly.plotly as py

bar_data = [
    {"genre": "Thriller", "viewers": 123456},
    {"genre": "Mystery", "viewers": 234567},
    {"genre": "Sci-Fi", "viewers": 987654},
    {"genre": "Fantasy", "viewers": 876543},
    {"genre": "Documentary", "viewers": 283105},
    {"genre": "Action", "viewers": 544099},
    {"genre": "Romantic Comedy", "viewers": 121212}
]

labels = [d["genre"] for d in bar_data]
values = [d["viewers"] for d in bar_data]

trace = [go.Bar(x=labels, y=values)]
py.iplot([trace], filename="basic_Bar_chart.html", auto_open=True)
#print("----------------")
#print("GENERATING BAR CHART...")
#print(bar_data) # TODO: create a horizontal bar chart based on the bar_data


