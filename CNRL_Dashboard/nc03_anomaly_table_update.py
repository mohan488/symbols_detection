import plotly.graph_objs as go
import pandas as pd

def update_anomaly_table(select_pipe):
    if select_pipe == '8_71711_A1A':
        layout_stack=go.Layout()
        fig_table = go.Figure(layout=layout_stack)

        #fig_table = ff.create_table(table_data, height_constant=60)

        fig_table = go.Figure(data=[go.Table(
                    header=dict(values=['Year','Thickness','Coating Breakdown(Ri)','Metal loss(CAT)','MCDR'],
                                line_color='darkslategray',
                                fill_color='lightskyblue',
                                align='left'),
                    cells=dict(values=[

                                       ['2021','2024','2029','2032'],
                                       ['6.9','6.7','6.3','6.1'],
                                       ['Ri-1','Ri-1', 'Ri-2','Ri-2'],
                                       ['CAT-A','CAT-A', 'CAT-B','CAT-B'],
                                       ['No','No','Yes','Yes'],


                                       ], # 2021
                               line_color='darkslategray',
                               fill_color='lightcyan',
                               align='left'))
                ])

        #fig_stack.update_layout(yaxis_range=(0, 100))
        fig_table.update_layout(
            paper_bgcolor="LightSteelBlue",
            plot_bgcolor= 'light blue',
            height=350,
            width=450,
            #textAlign= center,
            title= {
                      'text':'Significant Anomaly Prediction',
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

    elif select_pipe == '12_131679_A1A':
        layout_stack=go.Layout()
        fig_table = go.Figure(layout=layout_stack)

        #fig_table = ff.create_table(table_data, height_constant=60)

        fig_table = go.Figure(data=[go.Table(
                    header=dict(values=['Year','Thickness','Coating Breakdown(Ri)','Metal loss(CAT)','MCDR'],
                                line_color='darkslategray',
                                fill_color='lightskyblue',
                                align='left'),
                    cells=dict(values=[

                                       ['2021','2024','2029','2032'],
                                       ['9.74','9.72','9.70','9.69'],
                                       ['Ri-2','Ri-2', 'Ri-3','Ri-4'],
                                       ['CAT-A','CAT-A', 'CAT-A','CAT-B'],
                                       ['No','No','No','Yes'],


                                       ], # 2021
                               line_color='darkslategray',
                               fill_color='lightcyan',
                               align='left'))
                ])

        #fig_stack.update_layout(yaxis_range=(0, 100))
        fig_table.update_layout(
            paper_bgcolor="LightSteelBlue",
            plot_bgcolor= 'light blue',
            height=350,
            width=450,
            #textAlign= center,
            title= {
                      'text':'Significant Anomaly Prediction',
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
        ),)

        return fig_table


    elif select_pipe == '4_71112_B1A-S':
        layout_stack=go.Layout()
        fig_table = go.Figure(layout=layout_stack)

        #fig_table = ff.create_table(table_data, height_constant=60)

        fig_table = go.Figure(data=[go.Table(
                    header=dict(values=['Year','Thickness','Coating Breakdown(Ri)','Metal loss(CAT)','MCDR'],
                                line_color='darkslategray',
                                fill_color='lightskyblue',
                                align='left'),
                    cells=dict(values=[

                                       ['2021','2024','2029','2032'],
                                       ['6.3','6.3','6.3','6.3'],
                                       ['Ri-5','Ri-5+', 'Ri-5+','Ri-5+'],
                                       ['CAT-A','CAT-A', 'CAT-A','CAT-A'],
                                       ['Yes','Yes','Yes','Yes'],


                                       ], # 2021
                               line_color='darkslategray',
                               fill_color='lightcyan',
                               align='left'))
                ])

        #fig_stack.update_layout(yaxis_range=(0, 100))
        fig_table.update_layout(
            paper_bgcolor="LightSteelBlue",
            plot_bgcolor= 'light blue',
            height=350,
            width=450,
            #textAlign= center,
            title= {
                      'text':'Significant Anomaly Prediction',
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
        ),)

        return fig_table


    elif select_pipe == '10_31240_B3A':
        layout_stack=go.Layout()
        fig_table = go.Figure(layout=layout_stack)

        #fig_table = ff.create_table(table_data, height_constant=60)

        fig_table = go.Figure(data=[go.Table(
                    header=dict(values=['Year','Thickness','Coating Breakdown(Ri)','Metal loss(CAT)','MCDR'],
                                line_color='darkslategray',
                                fill_color='lightskyblue',
                                align='left'),
                    cells=dict(values=[
                                       ['2021','2024','2029','2032'],
                                       ['8.64','8.55','8.40','8.30'],
                                       ['Ri-4','Ri-5', 'Ri-5+','Ri-5+'],
                                       ['CAT-A','CAT-A', 'CAT-A','CAT-A'],
                                       ['No','Yes','Yes','Yes'],
                                       ], # 2021
                               line_color='darkslategray',
                               fill_color='lightcyan',
                               align='left'))
                ])

        #fig_stack.update_layout(yaxis_range=(0, 100))
        fig_table.update_layout(
            paper_bgcolor="LightSteelBlue",
            plot_bgcolor= 'light blue',
            height=350,
            width=450,
            #textAlign= center,
            title= {
                      'text':'Significant Anomaly Prediction',
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
        ),)

    return fig_table
