import numpy as np
import pandas as pd
from sklearn.neighbors import NearestNeighbors

# rating -> tconst	averageRating	numVotes
# pricipal -> tconst	ordering	nconst	category	job	characters
# title.akas -> titleId	ordering	title	region	language	types	attributes	isOriginalTitle
# basic -> tconst	titleType	primaryTitle	originalTitle	isAdult	startYear	endYear	runtimeMinutes	genres
# title.crew -> tconst	directors	writers
# title.episode -> tconst	parentTconst	seasonNumber	episodeNumber

print("hello")