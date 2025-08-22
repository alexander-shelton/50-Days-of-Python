#!/usr/bin/env python3
#
# Day 46: Create a DataFrame  
import pandas as pd

table = {'year': [2009, 2002, 2009, 2010, 2009],
            'title': ['Brothers', 'Spider-Man', 'WatchMen', 'Inception', 'Avatar'],
            'genre': ['Drama', 'Sci-fi', 'Drama', 'Sci-fi', 'Fantasy']}
movies = pd.DataFrame(table)
print(movies)

## Extra Challenge: Website Data with Pandas
print(pd.read_html("https://en.wikipedia.org/wiki/Python_(programming_language)")[1][['Type', 'Mutability']])