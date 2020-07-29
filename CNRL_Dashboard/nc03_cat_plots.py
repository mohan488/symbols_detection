import plotly.graph_objs as go
import pandas as pd


#setting customise colors for the application
colors = {
    'background': ' #050505',
    'light blue': '#7FDBFF',
    'red': '#FF0000',
    'aqua': '#00FFFF',
    'green': '#008000',
    'blue': '#0000FF',
    'white':'#edf4f4',
    'deep blue':'#4333ff'
}




#importing the data frame
df = pd.read_csv('nc03_cat_values.csv')
df_pred = pd.read_csv('nc03_cat_pred.csv')
def historical_cat_anomaly_update():
        layout_stack=go.Layout(
        title= {
                  'text':'Historical CAT values,Anomaly and trend forcast',
                  'xanchor':'center',
                  'yanchor':'bottom',
                  'x':0.5,
                  'y':0.92

                },
        yaxis=dict(
            title='CAT Value'
        ),
        xaxis=dict(
            title='Year'))

        fig = go.Figure(layout=layout_stack)
        #stacked Figure
        #x=['2015', '2018', '2019', '2021','2022','2023']

        #plotting the trend
        fig.add_trace(go.Scatter(
            x=df_pred['ds'],
            y=df_pred['trend'],
            mode='markers+lines',
            #hover_data=["x", "y"],
            line=dict(shape='spline'),
            name="CAT Value trend",
             marker=dict(

                    color='green',
                    size=5,
                    line=dict(
                        color='MediumPurple',
                        width=1
                    )))),
#-----------------------------------------------------------------

        #CAT Value Trace
        #values = list(range(4))
        fig.add_trace(go.Scatter(
            x=df['Date'],
            y=df['CAT'],
            mode='markers',
            #hover_data=["x", "y"],
            #line=dict(shape='spline'),
            name="Historical CAT Values and Anomaly",
             marker=dict(
                     line=dict(
                        color='MediumPurple',
                        width=2
                     ),
                    size=20,
                   #size=10*abs(anomaly['importance']),
                   color=((df.CAT==0) & (df.CAT<=1)).astype('int'),
                        colorscale=[[0, 'red'], [1, 'green']]),
                    #color=values ,
                    )),
#----------------------------------------------------------------------------
            #Upper limit trace
            #taking the values of upper and lower hat
            #y_upper = df_pred['yhat_upper']
            #y_lower = df_ pred['yhat_lower']
        fig.add_trace(go.Scatter(
                    x = df_pred['ds'],
                    y = df_pred['yhat_upper'],
                    hoverinfo = 'x+y',
                    mode = 'lines',
                    line=dict(width=0.5,
                              #color='rgb(243, 161, 203)'),
                              #color='rgb(58, 203, 215)'),
                              color='rgb(184, 178, 247)'),
                              #color='rgb(178, 241, 247)'),
                    stackgroup = 'two',
                    showlegend=False
                    #color=values ,
                    )),

  ##setting the lines on the CAT values
        fig.add_trace(go.Scatter(x=[2006,2025],
                   y=[1,1 ,1,1],
                   #opacity=1.0,
                   mode="lines+text",
                   #text ='CAT-A',
                   name="CAT-A",
                   text=["CAT-A", "CAT-A", "CAT-A","CAT-A"],
                   textposition="bottom center",
                   showlegend=False,
                   hoverinfo = 'text',
                   line=dict(width=2.5,
                   color='yellow'),
                  #color='rgb(184, 178, 247)'),
                  #color='rgb(178, 241, 247)'),

                  )),


        fig.add_trace(go.Scatter(x=[2006,2025],
                   y=[2,2 ,2,2],
                   #opacity=1.0,
                   mode="lines+text",
                   text=["CAT-B", "CAT-B", "CAT-B","CAT-B"],
                   textposition="bottom center",
                   hoverinfo = 'text',
                   showlegend=False,
                   name="CAT-B",
                   line=dict(width=2.5,
                   color='orange'),
                  #color='rgb(184, 178, 247)'),
                  #color='rgb(178, 241, 247)'),

                  )),

        fig.add_trace(go.Scatter(x=[2006,2025],
                   y=[3,3,3,3],
                   mode="lines+text",
                   #opacity=1.0,
                   text=["CAT-C", "CAT-C", "CAT-C","CAT-C"],
                   textposition="bottom center",
                   hoverinfo = 'text',
                   showlegend=False,
                   name="CAT-C",
                   line=dict(width=2.5,
                   color='red'),
                  #color='rgb(184, 178, 247)'),
                  #color='rgb(178, 241, 247)'),

                  )),
        fig.add_trace(go.Scatter(x=[2006,2025],
                   y=[0,0,0,0],
                   mode="lines+text",
                   #opacity=1.0,
                   text=["No Anomaly", "No Anomaly", "No Anomaly","No Anomaly"],
                   textposition="bottom center",
                   hoverinfo = 'text',
                   showlegend=False,
                   name="No Anomaly",
                   line=dict(width=2.5,
                   color='green'),
                  #color='rgb(184, 178, 247)'),
                  #color='rgb(178, 241, 247)'),

                  )),




        #fig_stack.update_layout(yaxis_range=(0, 100))
        fig.update_layout(
            paper_bgcolor="LightSteelBlue",
            plot_bgcolor= 'light blue',
            height=300,
            width=450,
            margin=dict(
            t=30, # top margin: 30px, you want to leave around 30 pixels to
            b=30, # bottom margin: 10px
            l=10, # left margin: 10px
            r=30, # right margin: 10px
                ),

            legend=dict(
            orientation="h",
            yanchor="top",
            y=-0.10,
            xanchor="left",
            x=-.15
        ),),

        fig.update_yaxes(visible=False, showticklabels=False)
        #putting all traces in the figure
        return fig






def stacked_cat_update():
        layout_stack=go.Layout(
        title= {
                  'text':'Distribution of CAT Values',
                  'xanchor':'center',
                  'yanchor':'bottom',
                  'x':0.5,
                  'y':0.92

                },
        yaxis=dict(
            title='CAT Value distribution'
        ),
        xaxis=dict(
            title='Year'))

        fig_stack = go.Figure(layout=layout_stack)
        #stacked Figure
        #x=['2015', '2018', '2019', '2021','2022','2023']

        #plotting cat d
        fig_stack.add_trace(go.Scatter(
            x=['2015', '2018', '2019', '2021','2022','2023','2028','2032'], y=[0, 0, 0, 0,0,0,0,0],
            text="CAT-D",
            hoverinfo='text+x+y',
            mode='lines',
            name="CAT-D",
            line=dict(width=0.5, color='darkred'),
            stackgroup='one'
        )),

        #plotting cat c
        fig_stack.add_trace(go.Scatter(
            x=['2015', '2018', '2019', '2021','2022','2023','2028','2032'], y=[0, 0, 2.79, 2.89,3.43,3.97,6.65,8.79],
            text="CAT-C",
            hoverinfo='text+x+y',
            mode='lines',
            name="CAT-C",
            line=dict(width=0.5, color='red'),
            stackgroup='one'
        )),


        #plotting CAT B
        fig_stack.add_trace(go.Scatter(
            x=['2015', '2018', '2019', '2021','2022','2023','2028','2032'], y=[1.28, 1.47, 15.17, 15.82,18.50,21.19,34.62,45.36],
            text="CAT-B",
            hoverinfo='text+x+y',
            mode='lines',
            name="CAT-B",
            line=dict(width=0.5, color='orange'),
            stackgroup='one'
        )),

        #plotting CAT A
        fig_stack.add_trace(go.Scatter(
            x=['2015', '2018', '2019', '2021','2022','2023','2028','2032'], y=[44.96, 66.54, 69.65, 83.87,90.28,96.69,130,140],
            text="CAT-A",
            hoverinfo='text+x+y',
            mode='lines',
            name="CAT-A",
            line=dict(width=0.5, color='yellow'),
            stackgroup='one'
        )),

        #plotting no anomaly
        fig_stack.add_trace(go.Scatter(
            x=['2015', '2018', '2019', '2021','2022','2023'], y=[53, 31, 12, 0],
            text="No Anomaly",
            hoverinfo='text+x+y',
            mode='lines',
            name="No Anomaly",
            line=dict(width=0.5, color='green'),
            stackgroup='one' # define stack group
        )),
        #fig_stack.update_layout(yaxis_range=(0, 100))
        fig_stack.update_layout(
            paper_bgcolor="LightSteelBlue",
            plot_bgcolor= 'light blue',
            height=300,
            width=450,
            margin=dict(
            t=30, # top margin: 30px, you want to leave around 30 pixels to
            b=30, # bottom margin: 10px
            l=30, # left margin: 10px
            r=30, # right margin: 10px
                ),

            legend=dict(
            orientation="h",
            yanchor="top",
            y=-0.10,
            xanchor="left",
            x=-.15
        ),
            #showlegend=True,
            xaxis_type='category',
            yaxis=dict(
                type='linear',
                range=[1, 100],
                ticksuffix='%'))

        return fig_stack


import plotly.figure_factory as ff
def cat_table_update():
        layout_stack=go.Layout()
        fig_table = go.Figure(layout=layout_stack)

        #fig_table = ff.create_table(table_data, height_constant=60)

        fig_table = go.Figure(data=[go.Table(
                    header=dict(values=['CAT Labels','2015','2018', '2019', '2021-predictions'],
                                line_color='darkslategray',
                                fill_color='lightskyblue',
                                align='left'),
                    cells=dict(values=[
                                       ['No Anomaly', 'CAT-A', 'CAT-B', 'CAT-C','CAT-D'],
                                       ['57.76%','44.96%', '1.28%', '0%','0%'], # no anomaly#2015
                                       ['31.96%','66.54%', '1.47%', '0%','0%'], # CAt A
                                       ['12.38%','69.65%', '15.17%', '2.79%','0%'], # CAT B
                                       ['0%','83.87%', '15.82%', '2.89%','0%'],#CAT C


                                       ], # 2021
                               line_color='darkslategray',
                               fill_color='lightcyan',
                               align='left'))
                ])

        #fig_stack.update_layout(yaxis_range=(0, 100))
        fig_table.update_layout(
            paper_bgcolor="LightSteelBlue",
            plot_bgcolor= 'light blue',
            height=300,
            width=450,
            #textAlign= center,
            title= {
                      'text':'CAT value percentages',
                      'xanchor':'center',
                      'yanchor':'bottom',
                      'x':0.5,
                      'y':0.90

                    },
            margin=dict(
            t=50, # top margin: 30px, you want to leave around 30 pixels to
            b=30, # bottom margin: 10px
            l=30, # left margin: 10px
            r=30, # right margin: 10px
                ),

            legend=dict(
            orientation="h",
            yanchor="top",
            y=-0.10,
            xanchor="left",
            x=-.15
        ),
            #showlegend=True,
            xaxis_type='category',
            yaxis=dict(
                type='linear',
                range=[1, 100],
                ticksuffix='%'))

        return fig_table
