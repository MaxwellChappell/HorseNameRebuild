import requests
from bs4 import BeautifulSoup
import pandas as pd
from traceback import print_exc
from datetime import datetime


def scrape_kids(horse, todo, done):
    url = "https://www.pedigreequery.com/progeny" + horse
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find_all("td", class_=["f", "m"])
    for line in results:
        link = line.find("a").attrs.get('href')
        if link not in done:
            if link not in todo:
                todo.append(link)


def save(l, fn):
    df = pd.DataFrame(l, columns=["Horses"])
    df.to_csv(fn, index=False)


def load(fn):
    l = pd.read_csv(fn, usecols=['Horses'])
    return l["Horses"].values.tolist()


def first_run():
    td = ['/darley+arabian', '/godolphin+arabian', '/byerley+turk']
    d = []
    return td, d


def normal_run():
    td = load("to_do.csv")
    d = load("done.csv")
    return td, d


def update(td, d):
    global start_time, count
    print()
    print("Update")
    print("To Do: ", len(td))
    print("Done: ", len(d))
    print(datetime.now() - start_time, count)
    print()
    save(d, "done.csv")
    save(td, "to_do.csv")


to_do, done = normal_run()

count = 0
start_time = datetime.now()
update(to_do, done)
try:
    while len(to_do) > 0:
        scrape_kids(to_do[0], to_do, done)
        done.append(to_do.pop(0))
        count += 1
        if count % 1000 == 0:
            update(to_do, done)
except Exception as e:
    print("type is:", e.__class__.__name__)
    print_exc()
finally:
    update(to_do, done)
