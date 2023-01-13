from bs4 import BeautifulSoup
import pandas as pd
import requests

text_list = [] # List to store the news titles

# Going through the page
for n in range(0, 158): # Loop is for going through the pages 159 pages of data were available
    pg = requests.get(f"https://dfrac.org/en/topic/fake/page/{n+1}/")
    cnt = pg.content

    soup = BeautifulSoup(cnt, 'html.parser')

    headline = soup.find_all('div', class_= 'td-module-meta-info')
    for i in headline:
        title = i.find('h3').get_text()
        title = title.strip()
        # Cleaning the data (Removing Unnecessary Parts)
        title = title.replace("- Read Fact Check", "").replace(" Read- Fact Check", "").replace("Read, Fact-Check", "").replace("Fact Check: ", "").replace(" Read Fact Check", "").replace("Fact Check-", "").replace('FactCheck:', '').replace('Fact-Check: ', '')
        title = title.strip()
        text_list.append(title)


data = {
    'Headline' : text_list,
    'Target' : ["false"] * len(text_list),
}

# Making a datafram of the data
df = pd.DataFrame(data)
df = df.drop_duplicates()


#df.to_csv("[FILE LOCATION]")
# [FILE LOCATION] --> "data/scrapping.csv"
