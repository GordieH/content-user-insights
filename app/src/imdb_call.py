# this is the start of importing imdb code
import pandas as pd
import numpy as np
import pickle 

def store_data(filePath,storedFilePath):
    loadedFile = pd.read_csv(filePath, sep='\t', header=0)
    loadedFile.to_pickle(storedFilePath)


def name_lookup(searchString):
    print("NAME RESULTS...")
    try:
        refTitles = names[names['primaryName'].str.lower() == searchString]['knownForTitles'].values[0].split(',')
        title_results = titles[titles['tconst'].isin(refTitles)].set_index('tconst')
        results = pd.concat([title_results,title_ratings.set_index('tconst')], axis=1, join='inner')
        results['ratings_score'] = results['averageRating'] * results['numVotes'] / (2021-results['startYear'].astype(int))
        return results.sort_values('ratings_score', ascending=False).head(5)
    except:
        print("No Person Results")

def title_lookup(searchString):
    print("TITLE RESULTS...")
    try:
        title_search = titles[titles['primaryTitle'].str.contains(searchString, na=False, regex=False, case=False)].set_index('tconst')
        results = pd.concat([title_search,title_ratings.set_index('tconst')], axis=1, join='inner')
        results['ratings_score'] = results['averageRating'] * results['numVotes'] / (2021-results['startYear'].astype(int))
        return results.sort_values('ratings_score', ascending=False).head(5)
    except:
        print("No Title Results")

def acronym_lookup(searchString):
    print("ACRONYM RESULTS...")
    try:
        titles['acronym'] = titles['primaryTitle'].apply(lambda x: "".join(word[0] for word in str(x).split()))
        title_search = titles[titles['acronym'].str.contains(searchString, na=False, regex=False, case=False)].set_index('tconst')
        results = pd.concat([title_search,title_ratings.set_index('tconst')], axis=1, join='inner')
        results['ratings_score'] = results['averageRating'] * results['numVotes'] / (2021-results['startYear'].astype(int))
        return results.sort_values('ratings_score', ascending=False).head(5)
    except:
        print("No Acronym Results")

def load_data():
    names = pd.read_pickle('/Users/gordon.hammond/Documents/practice/content-user-insights/data/imdb_names.obj')
    titles = pd.read_pickle('/Users/gordon.hammond/Documents/practice/content-user-insights/data/imdb_title_basics.obj')
    title_akas = pd.read_pickle('/Users/gordon.hammond/Documents/practice/content-user-insights/data/imdb_title_akas.obj')
    title_ratings = pd.read_pickle('/Users/gordon.hammond/Documents/practice/content-user-insights/data/imdb_title_ratings.obj')
    return names, titles, title_akas, title_ratings

# store_data('/Users/gordon.hammond/Documents/practice/content-user-insights/data/name.basics.tsv', '/Users/gordon.hammond/Documents/practice/content-user-insights/data/imdb_names.obj')
# store_data('/Users/gordon.hammond/Documents/practice/content-user-insights/data/title.basics.tsv', '/Users/gordon.hammond/Documents/practice/content-user-insights/data/imdb_title_basics.obj')
# store_data('/Users/gordon.hammond/Documents/practice/content-user-insights/data/title.akas.tsv', '/Users/gordon.hammond/Documents/practice/content-user-insights/data/imdb_title_akas.obj')
# store_data('/Users/gordon.hammond/Documents/practice/content-user-insights/data/title.ratings.tsv', '/Users/gordon.hammond/Documents/practice/content-user-insights/data/imdb_title_ratings.obj')

names, titles, title_akas, title_ratings = load_data()

searchTerm = 'svu'
acronym = acronym_lookup(searchTerm)
person = name_lookup(searchTerm)
title = title_lookup(searchTerm)

overall_results = pd.concat([acronym,person,title],axis=0).sort_values('ratings_score', ascending=False).head(5)
overall_results
