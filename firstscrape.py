import requests
from requests_html import HTML

req=requests.get("https://www.boxofficemojo.com/daily/2021/")
if req.status_code == 200:
    parsed_html=HTML(html=req.text)
    container=parsed_html.find('.imdb-scroll-table')
    tablecontainer=container[0].find('.imdb-scroll-table-inner')
    innertable = tablecontainer[0].find('tr')
    mainlist=[]
    mainheader = innertable[0].find('th')
    
    for i,k in enumerate(innertable[1:]):
        data=k.find('td')
        print(i,k)
        
        # for k in data:
        #     sublist.append(k.text)

        # print(sublist)




