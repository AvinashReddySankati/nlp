#spacy model load 
import spacy
#loading english model
nlp = spacy.load('en_core_web_sm')
doc = nlp("Simplilearn is one of the world's leading certification providers.")
#printing POS tag for tokens
for token in doc:
print(token.text, " --- ", token.pos_)