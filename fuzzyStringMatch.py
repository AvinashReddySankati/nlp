#https://towardsdatascience.com/fuzzy-string-matching-in-python-68f240d910fe

#pip install fuzzywuzzy
#pip install python-Levenshtein

from fuzzywuzzy import fuzz
from fuzzywuzzy import process

#Get Similarity scores

print(fuzz.ratio("Catherine M Gitau","Catherine Gitau")) #Uses difflib.ratio
print(fuzz.partial_ratio("Catherine M. Gitau","Catherine Gitau"))
print(fuzz.token_sort_ratio("Catherine Gitau M.", "Gitau Catherine"))

