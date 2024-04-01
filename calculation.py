import requests
from bs4 import BeautifulSoup


def get_webdata(symbol):
    symbol=symbol.upper()
    sales_growth_list=[]
    profit_growth_list=[]
    roce_list=[]
    getting_url=f"https://www.screener.in/company/{symbol}/consolidated"
    get_data=requests.get(getting_url)
    soup=BeautifulSoup(get_data.content, "html.parser")
    PE=soup.find_all('span', class_="number")[4].get_text() #------Current Stock Price
    