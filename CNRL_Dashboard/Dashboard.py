
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import dash
import dash_core_components as dcc
import dash_html_components as html
import base64
import pandas as pd
#importing other modules
import nc03_cat_plots
import nc03_ri_plots
import nc03_pipework
import nc03_anomaly_table_update



#seeting title of the app


#adding the external css
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

#app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app = dash.Dash(__name__, external_stylesheets= [dbc.themes.BOOTSTRAP])
#setting up app name
app.title = 'Ninian Central Platform'

#experiment figure
#fig = go.Figure(data=[go.Scatter(x=[1, 2, 3], y=[4, 1, 2])])

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

app.config.suppress_callback_exceptions = True

#importing Nin central image
image_filename = 'nin_central.png' # replace with your own image
encoded_image = base64.b64encode(open(image_filename, 'rb').read())

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Ninian-central-01", href="/NC-1"), id="NC-1-link"),
        dbc.NavItem(dbc.NavLink("Ninian-central-02", href="/NC-2"), id="NC-2-link"),
        dbc.NavItem(dbc.NavLink("Ninian-central-03", href="/NC-3"), id="NC-3-link")
    ],
    brand="Ninian Central Platform Dashboard",
    brand_href="/",
    color="primary",
    dark=True,
)

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')

])

# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    #"position": "fixed",
    "top": 10,
    "left": 0,
    "bottom": 0,
    "width": "12rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}
index_page = html.Div([

#creating a div for navigation bar
html.Div([navbar]),
html.Div([
html.Div(children='Important information about  Ninian central Platform',
style={
    'textAlign': 'center',
    'color': colors['green'],
    'fontSize':28
}),

html.Div([
    html.Div([
        html.Div([
html.Div([
    html.Div(children='Systems', style={'color': colors['green'],'fontSize':22}),
    dcc.Link('Ninian-central-01', href='/NC-1'),
    html.Br(),
    dcc.Link('Ninian-central-02', href='/NC-2'),
    html.Br(),
    dcc.Link('Ninian-central-03', href='/NC-3'),
    html.Br(),
    dcc.Link('Ninian-central-04', href='/index_page'),
    html.Br(),
    dcc.Link('Ninian-central-05', href='/index_page'),
    html.Br(),
    dcc.Link('Ninian-central-06', href='/index_page'),
    html.Br(),
    dcc.Link('Ninian-central-07', href='/index_page'),
    html.Br(),
    dcc.Link('Ninian-central-08', href='/index_page'),
    html.Br(),
    dcc.Link('Ninian-central-09', href='/index_page'),
    html.Br(),
    dcc.Link('Ninian-central-10', href='/index_page'),
    ],
    style=SIDEBAR_STYLE,

    ),
        ], className="six columns",style={'width':'60%','display': 'inline-block','padding': 15}),

        html.Div([
                html.Div([html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode()),style={'position':'right','height':'60%', 'width':'60%'})],
                ),
        ], className="six columns",style={'width':'40%','display': 'right','padding': 15,'position':'right'}),
    ], className="row")
]),
#html.Div([html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode()))]),
]),
#tghis div will hold the menu
# html.Div([
#     html.Div(children='Systems', style={'color': colors['green'],'fontSize':22}),
#     dcc.Link('Ninian-central-01', href='/NC-1'),
#     html.Br(),
#     dcc.Link('Ninian-central-02', href='/NC-2'),
#     html.Br(),
#     dcc.Link('Ninian-central-03', href='/NC-3'),
#     html.Br(),
#     dcc.Link('Ninian-central-04', href='/index_page'),
#     html.Br(),
#     dcc.Link('Ninian-central-05', href='/index_page'),
#     html.Br(),
#     dcc.Link('Ninian-central-06', href='/index_page'),
#     html.Br(),
#     dcc.Link('Ninian-central-07', href='/index_page'),
#     html.Br(),
#     dcc.Link('Ninian-central-08', href='/index_page'),
#     html.Br(),
#     dcc.Link('Ninian-central-09', href='/index_page'),
#     html.Br(),
#     dcc.Link('Ninian-central-10', href='/index_page'),
#     ],
#     #style=SIDEBAR_STYLE,
#     style={'width': '29%', 'display': 'inline-block'}
#     ),
]
)

NC_1_layout = html.Div([navbar, html.H1('under construction.......'),

#----------------------------------------------
html.H1('under construction.......')])



NC_2_layout = html.Div([navbar, html.H1('under construction.......')])


#Navbar for system 3
NC3_navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Ninian-central-03-01", href="/NC-03-01"), id="NC03-01-link"),
        dbc.NavItem(dbc.NavLink("Ninian-central-03-02", href="/NC-03-02"), id="NC03-02-link"),
        dbc.NavItem(dbc.NavLink("Ninian-central-03-03", href="/NC-03-03"), id="NC03-03-link")
    ],
    brand="Ninian Central Platform Dashboard",
    brand_href="/",
    color="primary",
    dark=True,
)

#Navbar for system 3 subsystems
NC3_sub_navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Ninian-central-03-01", href="/NC-03-01"), id="NC03-01-link"),
        dbc.NavItem(dbc.NavLink("Ninian-central-03-02", href="/NC-03-02"), id="NC03-02-link"),
        dbc.NavItem(dbc.NavLink("Ninian-central-03-03", href="/NC-03-03"), id="NC03-03-link")
    ],
    brand="Ninian Central Platform Dashboard System-03",
    brand_href="/NC-3",
    color="primary",
    dark=True,
)

#system three home page
NC_3_layout = html.Div([
#creating a div for navigation bar
html.Div([NC3_navbar]),

html.Div(children='Important information about  Ninian central - System 3', style={
    'textAlign': 'center',
    'color': colors['green'],
    'fontSize':28
}),
#tghis div will hold the menu
html.Div([
    html.Div(children='Sub-Systems', style={'color': colors['green'],'fontSize':22}),
    dcc.Link('Ninian-central-03-01', href='/NC-03-01'),
    html.Br(),
    dcc.Link('Ninian-central-03-02', href='/NC-03-02'),
    html.Br(),
    dcc.Link('Ninian-central-03-03', href='/NC-03-03'),
    ],
    style=SIDEBAR_STYLE,
    )
])


#hidden div for call backs


NC_03_02_layout = html.Div([NC3_sub_navbar, html.H1('Under progress .....')])
NC_03_03_layout = html.Div([NC3_sub_navbar, html.H1('Under progress.....')])

#-----------------------------------------------
#ninian central system three page
NC_03_01_layout = html.Div([NC3_sub_navbar,

    html.Div(children='Welcome to the Dashboard for Ninian central -System 3-Subsystem 1', style={
        'textAlign': 'center',
        'color': colors['green'],
        'fontSize':24
    }),

#=========================================================================

#=====================================================================
#html.H1('Welcome to the Dashboard for Ninian central -System 3-Subsystem 1'),
            html.Div([


              #html.H1('Welcome to the Dashboard for Ninian central -System 3-Subsystem 1'),
                html.Div([

                html.Div(children='Overview of External Corrosion (Coating Breakdown)', style={
                    'textAlign': 'center',
                    'color': colors['red'],
                    'fontSize':20
                }),


#------------------------------------------------------------------------------------------------------
                #this block to show the historical Ri values and anomaly
                html.Div([
                dcc.Graph(id='ri_anomaly_history', figure=nc03_ri_plots.historical_ri_anomaly_update())
                ],className="six columns",style={'display':'inline-block',
                        'width':'33%','padding': 5}),


#--------------------------------------------------------------------------------------------------------

                #this block to show the stacked RI Values
                html.Div([
                dcc.Graph(id='ri_anomaly', figure=nc03_ri_plots.stacked_ri_update())
                ],className="six columns",style={'display':'inline-block',
                        'width':'33%','padding': 5}),

#--------------------------------------------------------------------

                #this block to show the historical Ri values and anomaly in a table
                html.Div([
                dcc.Graph(id='ri_table', figure=nc03_ri_plots.ri_table_update())
                ],className="six columns",style={'display':'inline-block',
                        'width':'33%','padding': 5}),

]),
#------------------------------------------------------------------------------------------------------

#######start of row 2#################################

            html.Div([
                    html.Div(children='Overview of External Corrosion (Metal Loss)', style={
                        'textAlign': 'center',
                        'color': colors['red'],
                        'fontSize':20
                    }),

                #this block to show the historical CAT values and anomaly
                html.Div([
                dcc.Graph(id='cat_anomaly', figure=nc03_cat_plots.historical_cat_anomaly_update())
                ],className="six columns",style={'display':'inline-block',
                        'width':'33%','padding': 5}),


#--------------------------------------------------------------------------------------------------------
                #this block to show stacked CAT values
                html.Div([
                dcc.Graph(id='stacked_cat', figure=nc03_cat_plots.stacked_cat_update())
                ],className="six columns",style={'display':'inline-block',
                        'width':'33%','padding': 5}),



                #this block to show the historical CAT values and anomaly in a table
                html.Div([
                dcc.Graph(id='cat_table', figure=nc03_cat_plots.cat_table_update())
                ],className="six columns",style={'display':'inline-block',
                        'width':'33%','padding': 5}),
#end of cat rows
]),


#========================end of row 2 values===========================================================
            html.Div([
                html.Div(children='Pipework condition by line number', style={
                    'textAlign': 'center',
                    'color': colors['red'],
                    'fontSize':20
                }),


            html.Div([
            dcc.Dropdown(id='select_pipe',
                         options=[
                            {'label': '4_71112_B1A-S', 'value': '4_71112_B1A-S'},
                            {'label': '8_71711_A1A', 'value': '8_71711_A1A'},
                            {'label': '12_131679_A1A', 'value': '12_131679_A1A'},
                            {'label': '10_31240_B3A', 'value': '10_31240_B3A'}         ],
                             value='8_71711_A1A',
                          #multi=True
            ),],style={'verticalAlign':'top','width':'100%','color':'blue'}),
            html.Div([
                html.Div([
                    dcc.Graph(id='pipework_plot',figure={'data':[{'x':[1,5,7],'y':[3,5,7]}]}),

                ], className="six columns",style={'display':'inline-block',
                        'width':'50%','padding': 5}),

                html.Div([

                    dcc.Graph(id='future_anomaly_table',figure={'data':[{'x':[1,5,7],'y':[3,5,7]}]}),
                ], className="six columns",style={'display':'inline-block',
                        'width':'50%','padding': 5}),
            ], className="row")



]),
#===========================end of row 3==========================
#=========================================================================================================
                    ], className="row"),
                ],style={'backgroundColor': colors['background'],'padding': 15}

#end of the page layout of nc03-01
)




# Update the index
@app.callback(Output('page-content', 'children'), [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/NC-1':
        return NC_1_layout
    elif pathname == '/NC-2':
        return NC_2_layout
    elif pathname == '/NC-3':
        return NC_3_layout
    #for subsystem in system 03
    elif pathname == '/NC-03-01':
        return NC_03_01_layout
    elif pathname == '/NC-03-02':
        return NC_03_02_layout
    elif pathname == '/NC-03-03':
        return NC_03_03_layout
    else:
        return index_page
        # You could also return a 404 "URL not found" page here

##call back for update the pipe once a value is selected
@app.callback(Output('pipework_plot','figure'),
             [Input(component_id='select_pipe', component_property='value')])
def update_pipework(select_pipe):
    return nc03_pipework.update_pipework(select_pipe)

#updating anomaly table_data

@app.callback(Output('future_anomaly_table','figure'),
             [Input(component_id='select_pipe', component_property='value')])
def anomaly_table(select_pipe):
    return nc03_anomaly_table_update.update_anomaly_table(select_pipe)


# Update which link is active in the navbar
# If there's lots of pages, we can probably be cleverer about generating
# these functions dynamically.
@app.callback(Output('NC-1-link', 'active'), [Input('url', 'pathname')])
def set_page_1_active(pathname):
    return pathname == '/NC-1'

@app.callback(Output('NC-2-link', 'active'), [Input('url', 'pathname')])
def set_page_2_active(pathname):
    return pathname == '/NC-2'

@app.callback(Output('NC-3-link', 'active'), [Input('url', 'pathname')])
def set_page_3_active(pathname):
    return pathname == '/NC-3'

#for system 3
# Update which link is active in the navbar
# If there's lots of pages, we can probably be cleverer about generating
# these functions dynamically.
@app.callback(Output('NC03-01-link', 'active'), [Input('url', 'pathname')])
def set_page_1_active(pathname):
    return pathname == '/NC-03-01'

@app.callback(Output('NC03-2-link', 'active'), [Input('url', 'pathname')])
def set_page_2_active(pathname):
    return pathname == '/NC-03-02'

@app.callback(Output('NC03-3-link', 'active'), [Input('url', 'pathname')])
def set_page_3_active(pathname):
    return pathname == '/NC-03-03'


if __name__ == '__main__':
    app.run_server(debug=True, port=8000)
