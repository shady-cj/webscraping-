import requests
from requests_html import HTML
import pandas as pd
req=requests.get("https://www.boxofficemojo.com/daily/2021/")
if req.status_code == 200:
    parsed_html=HTML(html=req.text)
    container=parsed_html.find('.imdb-scroll-table')
    tablecontainer=container[0].find('.imdb-scroll-table-inner')
    rows= tablecontainer[0].find('tr')
    mainlist=[]
    mainheader = rows[0].find('th')
    header_names = []
    for headername in mainheader:
        header_names.append(headername.text)

    mainlist.append(header_names)
    for row in rows[1:]:
        cols=row.find('td')
        
        sublist=[]
        for col in cols:
            sublist.append(col.text)

        mainlist.append(sublist)

    print(mainlist)

df = pd.DataFrame(mainlist, columns = header_names) 
df.to_csv('movies.csv',index=False)


