from bs4 import BeautifulSoup
import pandas as pd
import requests

text_list = []

for n in range(0, 158):
    pg = requests.get(f"https://dfrac.org/en/topic/fake/page/{n+1}/")
    cnt = pg.content

    soup = BeautifulSoup(cnt, 'html.parser')

    headline = soup.find_all('div', class_= 'td-module-meta-info')
    for i in headline:
        title = i.find('h3').get_text()
        title = title.strip()
        title = title.replace("- Read Fact Check", "").replace(" Read- Fact Check", "").replace("Read, Fact-Check", "").replace("Fact Check: ", "").replace(" Read Fact Check", "").replace("Fact Check-", "").replace('FactCheck:', '').replace('Fact-Check: ', '')
        title = title.strip()
        text_list.append(title)

data = {
    'Headline' : text_list,
    'Target' : ["false"] * len(text_list),
}

df = pd.DataFrame(data)
df = df.drop_duplicates()


#df.to_csv("[FILE LOCATION")
