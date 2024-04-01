import requests
from bs4 import BeautifulSoup
import numpy as np
#<------------Imports--------------->


#<-------------Getting All the data from the Web(Scanner.in)----------------->
def get_webdata(symbol):
    symbol=symbol.upper()
    sales_growth_list=[]
    profit_growth_list=[]
    roce_list=[]
    getting_url=f"https://www.screener.in/company/{symbol}/consolidated"
    get_data=requests.get(getting_url)
    soup=BeautifulSoup(get_data.content, "html.parser")
    PE=soup.find_all('span', class_="number")[4].get_text() #--------------------------------Current Stock Price
    sales_growth=soup.find_all('table',class_="ranges-table")[0]
    tr=sales_growth.find_all("tr")
    for td in tr:
        tdd=td.find_all("td")
        tdd=tdd[1::2]
        for data in tdd:
            data1=data.get_text().replace("%", "")
            sales_growth_list.append(data1) #-------------------------------------------------Sales Growth 
    profit_growth=soup.find_all('table',class_="ranges-table")[1]
    tr=profit_growth.find_all("tr")
    for td in tr:
        tdd=td.find_all("td")
        tdd=tdd[1::2]
        for data in tdd:
            data1=data.get_text().replace("%", "")
            profit_growth_list.append(data1) #-------------------------------------------------Profit Growth
    roce=soup.find_all( 'table',class_="data-table")[4]
    roc=roce.find_all("tr")[6]
    rr=roc.find_all('td')
    rr=rr[7:12]
    for i in rr:
        a=i.get_text()
        clear=a.replace("%", "")
        intclear=int(clear)
        roce_list.append(intclear)
    ROCE=np.median(roce_list) #------------------------------------------------------------------ROCE   
    netprofit=soup.find_all("tr", class_="strong")[5]
    netprofit=netprofit.find_all('td')[12]
    dd=netprofit.get_text().replace(",",'') #-----------------------------------------------------Net-Profit
    MarketCapital=soup.find_all('span', class_="number")[0].get_text().replace(",", "") #---------Market-Capital
    FY23PE=round(int(MarketCapital)/int(dd), 1) #-------------------------------------------------FY23PE
    print(FY23PE)
get_webdata("tcs")