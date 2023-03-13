import requests
from bs4 import BeautifulSoup
from Horse import Horse

global count
count = 0
START_HORSE = Horse("AT THE STATIION2", "/at+the+station2", 1)


def process_horse(horses, start_horse, generation):
    url = "https://www.pedigreequery.com" + start_horse
    page = requests.get(url)

    soup = BeautifulSoup(page.content, "html.parser")

    results = soup.find_all("td", class_=["f", "m"])

    for line in results:
        process_line(line, horses, generation)


def process_line(data, horses, generation):
    horseName = data.find("a", class_="horseName")
    if horseName:
        relative_generation = int(data.attrs.get("data-g"))
        name = horseName.text
        link = horseName.attrs.get('href')
        new_gen = generation + relative_generation
        horse = Horse(name, link, new_gen)
        if horse not in horses:
            horses.append(horse)
            if relative_generation == 5:
                global count
                count += 1
                process_horse(horses, link, new_gen)
                print(count, link)
        else:
            horses[horses.index(horse)].add_generation(new_gen)


def save_file(horse_data):
    with open(f"{START_HORSE[0]}.txt", 'w+') as f:
        for horse in horse_data:
            f.write(horse.print_info())


def main():
    horses = [START_HORSE]
    generation = 1

    process_horse(horses, START_HORSE.link, generation)
    save_file(horses)


if __name__ == "__main__":
    main()
