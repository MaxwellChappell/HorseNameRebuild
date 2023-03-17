# HorseNameRebuild
Collection of projects that will theoretically lead to a race horse name generator. 

Horse.py: Horse class used in Pedigree.py

Pedigree.py: Looks at a horse and scrapes all of it's ancesors

name_collector.py: Scrapes pedigree query to collect horse names by looking at a horse in the todo list's children and adding them to the todo list.

name_collector_recurse.py: Scrapes pedigree query to collect horse names by looking at a horses children and recursively checking that horses children. Has an issue that causes it to end early that I need to find.

preprocess.py: Takes the links and makes them into plaintext names with trailing numbers removed and puts them in a text file. Also removes names with modern illegal racehorse name words

generator.ipynb: Just a basic Keras project that one hot encodes names and throws them into a simple model. Only ran once and not even close to having good results, need to actually reasearch what will be good and look into using my GPU so it doesn't take forever
