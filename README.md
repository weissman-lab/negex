# Negex

An updated version of NegEx for Python with a working example.

This is adapted from Brian Chapman's Negex repo: https://github.com/chapmanbe/negex

# File guide

- `readme.txt` the original readme file from the original Python code
- `negex.py` the file that implements the negex class to do the negations
- `README.md` this file. an overview of this updated version and repo
- `wrapper.py` a python script that demonstrates how to use the negex class, modified from the original
- `negex_triggers.txt` a list of negation terms
- `Annotations-1-120.txt` a list of sample clinical text annotations to negate
- `sandbox.py` a short working example

# Brief working example

```{python}
from negex import *

sample_txt = 'He does not have chest pain. He does have a cough. He denies lightheadedness.'
clinical_terms = ['chest pain', 'cough', 'lightheadedness']

# Set up Negex class
rfile = open(r'negex_triggers.txt')
irules = sortRules(rfile.readlines())

tagger = negTagger(sentence = sample_txt, phrases = clinical_terms, rules = irules, negP=False)

# See the full tagged sentence
tagger.getNegTaggedSentence()
## 'He does [PREN]not have[PREN] [NEGATED]chest pain[NEGATED]. He does have a [NEGATED]cough[NEGATED]. He [PREN]denies[PREN] [NEGATED]lightheadedness[NEGATED].'


# See whether or not something was NEGATED
tagger.getNegationFlag()

### 'negated'


# See the negations scopes
tagger.getScopes()

### ['[NEGATED]chest_pain[NEGATED]. He does have a [NEGATED]cough[NEGATED].',
 '[NEGATED]lightheadedness[NEGATED].']

```
