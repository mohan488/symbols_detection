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
df = pd.read_csv('nc03_ri_values.csv')
df_pred = pd.read_csv('nc03_ri_pred.csv')
def historical_ri_anomaly_update():
        layout_stack=go.Layout(
        title= {
                  'text':'Historical Ri values,Anomaly and trend forcast',
                  'xanchor':'center',
                  'yanchor':'bottom',
                  'x':0.5,
                  'y':0.92

                },
        yaxis=dict(
            title='Ri Value'
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
            name="Ri Value trend",
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
            y=df['Ri_scale'],
            mode='markers',
            #hover_data=["x", "y"],
            #line=dict(shape='spline'),
            name="Historical Ri Values and Anomaly",
             marker=dict(
                     line=dict(
                        color='MediumPurple',
                        width=2
                     ),
                    size=20,
                   #size=10*abs(anomaly['importance']),
                   color=((df.Ri_scale==0) & (df.Ri_scale<=1)).astype('int'),
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
        ),)


        #putting all traces in the figure
        return fig



#creating
def stacked_ri_update():
        layout_stack=go.Layout(
        title= {
                  'text':'Distribution of Ri Values',
                  'xanchor':'center',
                  'yanchor':'bottom',
                  'x':0.5,
                  'y':0.92

                },
        yaxis=dict(
            title='Ri Value distribution'
        ),
        xaxis=dict(
            title='Year'))

        fig_stack = go.Figure(layout=layout_stack)
        #stacked Figure
        #x=['2015', '2018', '2019', '2021','2022','2023']

        #plotting ri5
        fig_stack.add_trace(go.Scatter(
            x=['2018', '2019', '2020'], y=[20, 8, 5, 0],
            text="Ri-5",
            hoverinfo='text+x+y',
            mode='lines',
            name="Ri-5",
            line=dict(width=0.5, color='darkred'),
            stackgroup='one'
        )),

        #plotting ri 4
        fig_stack.add_trace(go.Scatter(
            x=['2018', '2019', '2020'], y=[51, 40, 29],
            text="Ri-4",
            hoverinfo='text+x+y',
            mode='lines',
            name="Ri-4",
            line=dict(width=0.5, color='red'),
            stackgroup='one'
        )),


        #plotting ri 3
        fig_stack.add_trace(go.Scatter(
            x=['2018', '2019', '2020'], y=[0, 3, 6],
            text="Ri-3",
            hoverinfo='text+x+y',
            mode='lines',
            name="Ri-3",
            line=dict(width=0.5, color='orange'),
            stackgroup='one'
        )),

        #plotting ri2
        fig_stack.add_trace(go.Scatter(
            x=['2018', '2019', '2020'], y=[0, 14, 30],
            text="Ri-2",
            hoverinfo='text+x+y',
            mode='lines',
            name="Ri-2",
            line=dict(width=0.5, color='yellow'),
            stackgroup='one'
        )),

        #plotting ri 1
        fig_stack.add_trace(go.Scatter(
            x=['2018', '2019', '2020'], y=[27, 20, 13],
            text="Ri-1",
            hoverinfo='text+x+y',
            mode='lines',
            name="RI-1",
            line=dict(width=0.5, color='blue'),
            stackgroup='one'
        )),

        #Plotting no anomaly
        fig_stack.add_trace(go.Scatter(
            x=['2018', '2019', '2020'], y=[0, 14, 27],
            hoverinfo='x+y',
            mode='lines',
            name="No Anomaly(Ri-0)",
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
def ri_table_update():
        layout_stack=go.Layout()
        fig_table = go.Figure(layout=layout_stack)

        # Add table data
        table_data = [['CAT Labels','2015','2018', '2019', '2021-predictions'],
                      ['No Anomaly', '53.76%', '31.96%', '12.38%','0%'],
                      ['CAT-A', '44.96%', '66.54%', '69.65%','83.87%'],
                      ['CAT-B ', '1.28%', '1.47%', '15.17%','15.82%'],
                      ['CAT-C', '0%', '0%', '2.79%','2.89%']]
        # Initialize a fig with ff.create_table(table_data)
        #fig_table = ff.create_table(table_data, height_constant=60)

        fig_table = go.Figure(data=[go.Table(
                    header=dict(values=['Ri Scale','2018','2019','2020-predictions'],
                                line_color='darkslategray',
                                fill_color='lightskyblue',
                                align='left'),
                    cells=dict(values=[
                                       ['No Anomaly', 'Ri-1', 'Ri-2', 'Ri-3','Ri-4','Ri-5'],
                                       ['0%','27.35%', '0%', '0%','51.70%','20.93%'], #
                                       ['13.43%','20.54%', '14.54%', '2.58%','40.88%','8.0%'], #
                                       ['26.86%','13.73%', '29.08%', '5.16%','29.18%','5%'], #

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
