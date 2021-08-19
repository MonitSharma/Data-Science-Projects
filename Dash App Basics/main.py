import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc 

from dash.dependencies import Input, Output, State

import plotly.graph_objs as go
import plotly.express as px
import numpy as np
import pandas as pd



# adding an CSS stylesheet

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# initilaise dash_html_components

app = dash.Dash(__name__, external_stylesheets = external_stylesheets)
server = app.server




# now read the data to it

df = pd.read_csv('restaurants_zomato.csv', encoding='ISO-8859-1')



# We will visualize a map, a bar chart, and a Pie chart with

#map
col_label = 'country_code'
col_values = "count"



v = df[col_label].value_counts()
new = pd.DataFrame({
    col_label: v.index,
    col_values: v.values
})





hexcode = 0

borders = [hexcode for x in range(len(new))],
map = dcc.Graph(

            id='8',
            figure = {
            'data': [{
            'locations':new['country_code'],
            'z':new['count'],
            'colorscale': 'Earth',
            'reversescale':True,
            'hover-name':new['country_code'],
            'type': 'choropleth'
            
            }],
            
            'layout':{'title':dict(
            
                text = 'Restaurant Frequency by Location',
                font = dict(size=20,
                color = 'white')),
                "paper_bgcolor":"#111111",
                "plot_bgcolor":"#111111",
                "height": 800,
                "geo":dict(bgcolor= 'rgba(0,0,0,0)') } 
                
                })




# The above lines of code will create the map, 
# and colour each region according to the 
# number of restaurants listed.



# bar chart



df2 = pd.DataFrame(df.groupby(by='Restaurant Name')['Votes'].mean())
df2 = df2.reset_index()
df2 = df2.sort_values(['Votes'],ascending=False)
df3 = df2.head(10)

bar1 =  dcc.Graph(id='bar1',
              figure={
        'data': [go.Bar(x=df3['Restaurant Name'],
                        y=df3['Votes'])],
        'layout': {'title':dict(
            text = 'Top Restaurants in India',
            font = dict(size=20,
            color = 'white')),
        "paper_bgcolor":"#111111",
        "plot_bgcolor":"#111111",
        'height':600,
        "line":dict(
                color="white",
                width=4,
                dash="dash",
            ),
        'xaxis' : dict(tickfont=dict(
            color='white'),showgrid=False,title='',color='white'),
        'yaxis' : dict(tickfont=dict(
            color='white'),showgrid=False,title='Number of Votes',color='white')
    }})






# pie chart
col_label = "Rating text"
col_values = "Count"

v = df[col_label].value_counts()
new2 = pd.DataFrame({
    col_label: v.index,
    col_values: v.values
})

pie3 = dcc.Graph(
        id = "pie3",
        figure = {
          "data": [
            {
            "labels":new2['Rating text'],
            "values":new2['Count'],
              "hoverinfo":"label+percent",
              "hole": .7,
              "type": "pie",
                 'marker': {'colors': [
                                                   '#0052cc',  
                                                   '#3385ff',
                                                   '#99c2ff'
                                                  ]
                                       },
             "showlegend": True
}],
          "layout": {
                "title" : dict(text ="Rating Distribution",
                               font =dict(
                               size=20,
                               color = 'white')),
                "paper_bgcolor":"#111111",
                "showlegend":True,
                'height':600,
                'marker': {'colors': [
                                                 '#0052cc',  
                                                 '#3385ff',
                                                 '#99c2ff'
                                                ]
                                     },
                "annotations": [
                    {
                        "font": {
                            "size": 20
                        },
                        "showarrow": False,
                        "text": "",
                        "x": 0.2,
                        "y": 0.2
                    }
                ],
                "showlegend": True,
                "legend":dict(fontColor="white",tickfont={'color':'white' }),
                "legenditem": {
    "textfont": {
       'color':'white'
     }
              }
        } }
)






# now the CSS Part

graphRow1 = dbc.Row([dbc.Col(map,md=12)])
graphRow2 = dbc.Row([dbc.Col(bar1, md=6), dbc.Col(pie3, md=6)])



# run the server and
navbar = dbc.Nav()

app.layout = html.Div([navbar,html.Br(),graphRow1,html.Br(),graphRow2], style={'backgroundColor':'black'})

if __name__ == '__main__':
    app.run_server(debug=True,port=8056)