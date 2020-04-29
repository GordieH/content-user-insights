# this is the start of importing imdb code
import pandas as pd
import numpy as np
import pickle 

def store_data(filePath,storedFilePath):
    loadedFile = pd.read_csv(filePath, sep='\t', header=0)
    loadedFile.to_pickle(storedFilePath)


def name_lookup(searchString):
    refTitles = names[names['primaryName'].str.lower() == searchString]['knownForTitles'].values[0].split(',')
    return titles[titles['tconst'].isin(refTitles)]

def load_data():
    names = pd.read_pickle('/Users/gordon.hammond/Documents/practice/content-user-insights/data/imdb_names.obj')
    titles = pd.read_pickle('/Users/gordon.hammond/Documents/practice/content-user-insights/data/imdb_title_basics.obj')

    return names, titles

#store_data('/Users/gordon.hammond/Documents/practice/content-user-insights/data/name.basics.tsv', '/Users/gordon.hammond/Documents/practice/content-user-insights/data/imdb_names.obj')
# store_data('/Users/gordon.hammond/Documents/practice/content-user-insights/data/title.basics.tsv', '/Users/gordon.hammond/Documents/practice/content-user-insights/data/imdb_title_basics.obj')
names, title = load_data()
name_lookup("julia garner")


#titles = pd.read_pickle('/Users/gordon.hammond/Documents/practice/content-user-insights/data/imdb_title_basics.obj')

#titles[titles['tconst'].isin(['tt0420472', 'tt12075930', 'tt9010994', 'tt3230032'])]
