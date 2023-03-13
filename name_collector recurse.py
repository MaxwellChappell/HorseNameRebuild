import requests
from bs4 import BeautifulSoup
import pandas as pd
from traceback import print_exc
from datetime import datetime

count = 0


def scrape_kids(horse, df):
    global count
    # path.append(horse)
    # print(path)
    url = "https://www.pedigreequery.com/progeny" + horse
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find_all("td", class_=["f", "m"])
    for line in results:
        link = line.find("a").attrs.get('href')
        if not df['Horses'].eq(link).any():
            #print("looking at", link, 'children')
            scrape_kids(link, df)
            df.loc[len(df)] = [link]
            #print(link, "done")

            #count += 1
            # if count % 1000 == 0:
            #    print(datetime.now(), count)
            #    save(df)
    # path.pop()


def save(df):
    df.to_csv("horses2.csv",  index=False)


def load():
    df = pd.read_csv('horses2.csv', usecols=['Horses'])
    return df


# start from scratch
#count = 0
#name_list = pd.DataFrame(columns=["Horses"])

# load
starttime = datetime.now()
print(starttime)
try:
    name_list = load()
    count = len(name_list)
    startcount = count
    print(count)
    path = []
    start = ['/darley+arabian', '/godolphin+arabian', '/byerley+turk']
    for horse in start:
        scrape_kids(horse, name_list)
        name_list.loc[len(name_list)] = [horse]
        print(horse, "done")
except Exception as e:
    print("type is:", e.__class__.__name__)
    # print_exc()
finally:
    passed = datetime.now() - starttime
    horses_processed = len(name_list) - count
    print(passed, horses_processed)
    save(name_list)
