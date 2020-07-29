import plotly.graph_objs as go
import pandas as pd

#historical data for 8-inch-71711
df_8_inch_71711_A1A = pd.read_csv('nc03_pipework_values_8_71711.csv')
df_12_131679_A1A = pd.read_csv('nc03_pipework_values_12_131679_A1A.csv')

df_04_71112_B1A_S = pd.read_csv('nc03_pipework_values_04_71112_B1A-S.csv')
df_10_31240_B3A = pd.read_csv('nc03_pipework_values_10_31240_B3A.csv')


def update_pipework(select_pipe):
#----------------------------------------------------------------------
    if select_pipe == '8_71711_A1A':
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

        #adding historical Values
        fig.add_trace(go.Scatter(
        x = df_8_inch_71711_A1A['Date'],
        y = df_8_inch_71711_A1A['MWT'],
        name="Historical Thickness",
        mode='markers+lines',
        hoverinfo = 'x+y',
        #hover_data=["x", "y"],
        #line=dict(shape='spline'),
        marker=dict(
         line=dict(
            color='MediumPurple',
            width=2
         ),),)),


        #adding prediction
        fig.add_trace(go.Scatter(
        x = [2019,2021,2024,2029,2032],
        y = [7.1,6.9,6.7,6.3,6.1],
        name="Predicted Thickness",
        mode='markers+lines',
        line = dict(color='royalblue', width=4, dash='dash'),
        hoverinfo = 'x+y',
        #hover_data=["x", "y"],
        #line=dict(shape='spline'),
        marker=dict(
         line=dict(
            color='red',
            width=2
         ),),)),
       #adding  worse condition traces
        fig.add_trace(go.Scatter(
                x = [2006,2012,2019,2022,2028,2032],
                y = [8.6,6.9,7.0,6.3,5.6,5.1],
                name="Worse predicted thickness",
                mode='markers+lines',
                line=dict(width=0.5, color='red'),
                hoverinfo = 'x+y',
                #hover_data=["x", "y"],
                #line=dict(shape='spline'),
                marker=dict(
                 line=dict(
                    color='red',
                    width=2
                 ),
                size=10,),)),


        #adding the conc trace
        fig.add_trace(go.Scatter(
                x = [2006,2032],
                y = [4.4,4.4],
                name="CONC",
                text='CONC',
                textposition="bottom left",
                mode='markers+lines+text',
                line=dict(width=0.5, color='red'),
                fill='tozeroy',
                hoverinfo = 'x+y',
                showlegend=False,
                #hover_data=["x", "y"],
                #line=dict(shape='spline'),
                marker=dict(
                 line=dict(
                    color='red',
                    width=2
                 ),),)),

        #fig_stack.update_layout(yaxis_range=(0, 100))
        fig.update_layout(
            paper_bgcolor="LightSteelBlue",
            plot_bgcolor= 'light blue',
            height=350,
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
            x=-.25
        ),),

        #fig.update_yaxes(visible=False, showticklabels=False)
        #putting all traces in the figure
        return fig


#-----------------------------------------------------------------------
    elif select_pipe == '4_71112_B1A-S':
        layout_stack=go.Layout(
        title= {
                  'text':'Historical pipework thickness values and forcast',
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

        #adding historical Values
        fig.add_trace(go.Scatter(
        x = df_04_71112_B1A_S['Date'],
        y = df_04_71112_B1A_S['MWT'],
        name="Historical Thickness",
        mode='markers+lines',
        hoverinfo = 'x+y',
        #hover_data=["x", "y"],
        #line=dict(shape='spline'),
        marker=dict(
         line=dict(
            color='MediumPurple',
            width=2
         ),),)),


        #adding prediction
        fig.add_trace(go.Scatter(
        x = [2019,2021,2024,2029,2032],
        y = [6.3,6.3,6.3,6.3,6.3],
        name="Predicted Thickness",
        mode='markers+lines',
        line = dict(color='royalblue', width=4, dash='dash'),
        hoverinfo = 'x+y',
        #hover_data=["x", "y"],
        #line=dict(shape='spline'),
        marker=dict(
         line=dict(
            color='royalblue',
            width=2
         ),),)),
       #adding  worse condition traces
        fig.add_trace(go.Scatter(
                x = [2006,2012,2019,2022,2028,2032],
                y = [5.8,5.8,5.5,5.45,5.3,5.2],
                name="Worse predicted thickness",
                mode='markers+lines',
                line=dict(width=0.5, color='red'),
                hoverinfo = 'x+y',
                #hover_data=["x", "y"],
                #line=dict(shape='spline'),
                marker=dict(
                 line=dict(
                    color='red',
                    width=2
                 ),
                size=10,),)),


        #adding the conc trace
        fig.add_trace(go.Scatter(
                x = [2006,2032],
                y = [3.1,3.1],
                name="CONC",
                text='CONC',
                textposition="bottom left",
                mode='markers+lines+text',
                line=dict(width=0.5, color='red'),
                fill='tozeroy',
                hoverinfo = 'x+y',
                showlegend=False,
                #hover_data=["x", "y"],
                #line=dict(shape='spline'),
                marker=dict(
                 line=dict(
                    color='red',
                    width=2
                 ),),)),

        #fig_stack.update_layout(yaxis_range=(0, 100))
        fig.update_layout(
            paper_bgcolor="LightSteelBlue",
            plot_bgcolor= 'light blue',
            height=350,
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
            x=-.25
        ),),

        #fig.update_yaxes(visible=False, showticklabels=False)
        #putting all traces in the figure
        return fig

    elif select_pipe == '12_131679_A1A':
            layout_stack=go.Layout(
            title= {
                      'text':'Historical pipework thickness values and forcast',
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

            #adding historical Values
            fig.add_trace(go.Scatter(
            x = df_12_131679_A1A['Date'],
            y = df_12_131679_A1A['MWT'],
            name="Historical Thickness",
            mode='markers+lines',
            hoverinfo = 'x+y',
            #hover_data=["x", "y"],
            #line=dict(shape='spline'),
            marker=dict(
             line=dict(
                color='MediumPurple',
                width=2
             ),),)),


            #adding prediction
            fig.add_trace(go.Scatter(
            x = [2019,2021,2024,2029,2032],
            y = [9.75,9.74,9.72,9.70,9.69],
            name="Predicted Thickness",
            mode='markers+lines',
            line = dict(color='royalblue', width=4, dash='dash'),
            hoverinfo = 'x+y',
            #hover_data=["x", "y"],
            #line=dict(shape='spline'),
            marker=dict(
             line=dict(
                color='royalblue',
                width=2
             ),),)),
           #adding  worse condition traces
            fig.add_trace(go.Scatter(
                    x = [2006,2012,2019,2022,2028,2032],
                    y = [9.1,9.00,8.88,8.8,8.73,8.60],
                    name="Worse predicted thickness",
                    mode='markers+lines',
                    line=dict(width=0.5, color='red'),
                    hoverinfo = 'x+y',
                    #hover_data=["x", "y"],
                    #line=dict(shape='spline'),
                    marker=dict(
                     line=dict(
                        color='red',
                        width=2
                     ),
                    size=10,),)),


            #adding the conc trace
            fig.add_trace(go.Scatter(
                    x = [2006,2032],
                    y = [5.34,5.34],
                    name="CONC",
                    text='CONC',
                    textposition="bottom left",
                    mode='markers+lines+text',
                    line=dict(width=0.5, color='red'),
                    fill='tozeroy',
                    hoverinfo = 'x+y',
                    showlegend=False,
                    #hover_data=["x", "y"],
                    #line=dict(shape='spline'),
                    marker=dict(
                     line=dict(
                        color='red',
                        width=2
                     ),),)),

            #fig_stack.update_layout(yaxis_range=(0, 100))
            fig.update_layout(
                paper_bgcolor="LightSteelBlue",
                plot_bgcolor= 'light blue',
                height=350,
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
                x=-.25
            ),),

            #fig.update_yaxes(visible=False, showticklabels=False)
            #putting all traces in the figure
            return fig

    elif select_pipe == '10_31240_B3A':
            layout_stack=go.Layout(
            title= {
                      'text':'Historical pipework thickness values and forcast',
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

            #adding historical Values
            fig.add_trace(go.Scatter(
            x = df_10_31240_B3A['Date'],
            y = df_10_31240_B3A['MWT'],
            name="Historical Thickness",
            mode='markers+lines',
            hoverinfo = 'x+y',
            #hover_data=["x", "y"],
            #line=dict(shape='spline'),
            marker=dict(
             line=dict(
                color='MediumPurple',
                width=2
             ),),)),


            #adding prediction
            fig.add_trace(go.Scatter(
            x = [2019,2021,2024,2029,2032],
            y = [8.71,8.64,8.55,8.40,8.30],
            name="Predicted Thickness",
            mode='markers+lines',
            line = dict(color='royalblue', width=4, dash='dash'),
            hoverinfo = 'x+y',
            #hover_data=["x", "y"],
            #line=dict(shape='spline'),
            marker=dict(
             line=dict(
                color='royalblue',
                width=2
             ),),)),
           #adding  worse condition traces
            fig.add_trace(go.Scatter(
                    x = [2006,2012,2018,2019,2022,2028,2032],
                    y = [8.5,8.3,8.7,7.1,7.12,7.40,7.19],
                    name="Worse predicted thickness",
                    mode='markers+lines',
                    line=dict(width=0.5, color='red'),
                    hoverinfo = 'x+y',
                    #hover_data=["x", "y"],
                    #line=dict(shape='spline'),
                    marker=dict(
                     line=dict(
                        color='red',
                        width=2
                     ),
                    size=10,),)),


            #adding the conc trace
            fig.add_trace(go.Scatter(
                    x = [2006,2032],
                    y = [5.34,5.34],
                    name="CONC",
                    text='CONC',
                    textposition="bottom left",
                    mode='markers+lines+text',
                    line=dict(width=0.5, color='red'),
                    fill='tozeroy',
                    hoverinfo = 'x+y',
                    showlegend=False,
                    #hover_data=["x", "y"],
                    #line=dict(shape='spline'),
                    marker=dict(
                     line=dict(
                        color='red',
                        width=2
                     ),),)),

            #fig_stack.update_layout(yaxis_range=(0, 100))
            fig.update_layout(
                paper_bgcolor="LightSteelBlue",
                plot_bgcolor= 'light blue',
                height=350,
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
                x=-.25
            ),),

            #fig.update_yaxes(visible=False, showticklabels=False)
            #putting all traces in the figure
            return fig
