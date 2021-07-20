# This is a sandbox file to test the guts of the Negex class
from negex import *

sample_txt = 'He does not have chest pain. He does have a cough. He denies lightheadedness.'
clinical_terms = ['chest pain', 'cough', 'lightheadedness']

# Set up Negex class
rfile = open(r'negex_triggers.txt')
irules = sortRules(rfile.readlines())

tagger = negTagger(sentence = sample_txt, phrases = clinical_terms, rules = irules, negP=False)

# See the full tagged sentence
tagger.getNegTaggedSentence()

# See whether or not something was NEGATED
tagger.getNegationFlag()

# See the negations scopes
tagger.getScopes()
