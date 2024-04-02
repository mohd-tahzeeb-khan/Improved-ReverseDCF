import dash
from dash import Dash, html, dcc, Output, Input
app=dash.Dash(__name__)


#----------------------------------------------------------Drop Down Option-------------------------------------------------------------------
dropdown=dcc.Dropdown(options=[{
    "label":dcc.Link(children="Home", href="/HOME", style={"color":"#fff", "textDecoration":"none"}),
    "value":"HOME"

}, {
    "label":dcc.Link(children="DCF Valuation", href="/DCF",style={"color":"#fff", "textDecoration":"none"},),
    "value":"DCF",

}, ],placeholder="PAGES",value="HOME",clearable=False,
id="dropdownoption", className="dropdownoption")
#--------------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------Navigation Bar---------------------------------------------------------------------------
navigationbar=html.Div([
    html.Div([
        html.H3("Reverse DCF")], className="Heading-text"), 
        html.Div([dropdown],id="attachdropdown")], id="Navbar",)
textline=html.Div([
    html.H4("This site provides interactive tools to valuate and analyze stocks through Reverse DCF model. Check the navigation bar for more.")
], id="textline")
#--------------------------------------------------------------------------------------------------------------------------------------------------------
main=html.Div(children=[], id="main")
#-----------------------------------------------------main App---------------------------------------------------------------------------------------------
app.layout=html.Div([navigationbar, main])



#--------------------------------------------callback Functions--------------------------------------------------------------------------
#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||




#-------------------------------------------------callback function for rendering page content-----------------------------------------
@app.callback(
    [Output('main', 'children')],
    Input('dropdownoption', 'value')
)
def renderpage(page):
    if page=="HOME":
        return [textline]
    else:
        return ["dr bro"]

if __name__=='__main__':
    app.run(debug=True)