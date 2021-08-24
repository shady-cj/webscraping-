import requests
from requests_html import HTML
import pandas as pd
import os 


BASE_DIR = os.path.dirname(__file__)
def scrape(startyear=2020,span=1):
    assert isinstance(startyear, int)
    assert isinstance(span, int)
    for s in range(0,span+1):
        generate(startyear)
        startyear+=1

def generate(year = 2021):
    req=requests.get(f"https://www.boxofficemojo.com/daily/{year}/")
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

        for row in rows[1:]:
            cols=row.find('td')
            
            sublist=[]
            for col in cols:
                sublist.append(col.text)

            mainlist.append(sublist)

    movie = os.path.join(BASE_DIR,"movies")
    os.makedirs("movies",exist_ok=True)
    dirfile=os.path.join(movie,f"{year}.csv")
    df = pd.DataFrame(mainlist, columns = header_names) 
    df.to_csv(dirfile,index=False)


if __name__ == "__main__":
    scrape(startyear=2012,span=6)