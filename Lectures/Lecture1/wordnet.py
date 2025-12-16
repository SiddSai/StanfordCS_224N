# Old NLP solution --> WordNet
# Thesaurus with synonyms and hypernyms

import nltk
nltk.download('wordnet')
nltk.download('omw-1.4')
from nltk.corpus import wordnet as wn


# Print all synonyms for the word "afraid"
poses = { 'n': 'noun', 'v': 'verb', 's': 'satellite adjective', 'a': 'adjective', 'r': 'adverb' }

print("Synonyms for the word 'good':")
for synonymset in wn.synsets("good"):
    print({"{}: {}".format(poses[synonymset.pos()],
                           ", ".join([l.name() for l in synonymset.lemmas()]))})

# Print all hypernyms for the word "afraid"
print("\nHypernyms for the word 'bad':")
bad = wn.synset("bad.a.01")

# Define anynonyms function to return s's hypernyms
hypernyms = lambda s: s.hypernyms()

list(bad.closure(hypernyms))
