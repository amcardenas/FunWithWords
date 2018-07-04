# -*- coding: utf-8 -*-
"""
NAME: USConst_bagOfWords.py
PURPOSE: Create a bag of words from a text document of the US Constitution.
Author: Aimee Cardenas
"""

import argparse
from collections import Counter
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction import text

# parse the command line arguments so that you can use this code for other 
# text documents.  
parser = argparse.ArgumentParser()
parser.add_argument('--infile', action = 'store', 
    default = "../Documents/NatLangProc/USConstitution/USConstitution.txt", 
    help='path to text file')
parser.add_argument('--outfile', action = 'store',
    default = "../Documents/NatLangProc/USConstitution/USConst_wordFreq.txt", 
    help='path to output file')
args = parser.parse_args()

# create token pattern
alphaNum_tkns = '[A-Za-z0-9]+(?=\\s+)'

# add other stopwords to the pre-made stopword list
moreStopWords = ["amendment", "section", "without", "article", "hereby",
                 "within", "otherwise", "upon", "whenever", "begin", "thereof",
                 "unless", "become", "among", "may", "made", "day", "make", 
                 "place", "either", "every", "wherein", "hereof", "therein", 
                 "shall"]
allStopWords = text.ENGLISH_STOP_WORDS.union(moreStopWords)

# instantiate count vectorizer object
CtVec_alphaNum = CountVectorizer(token_pattern = alphaNum_tkns, 
                                 stop_words = allStopWords, lowercase = True)

# read US Constintution text into a single string
with open(args.infile, 'r') as myfile:
    data=myfile.read().replace('\n', ' ')
    
# Count the frequency of words based on the tokenization pattern
Mx_an = CtVec_alphaNum.fit_transform([data])

# print messages about the number of tokens found 
an_outfile = open(args.outfile, 'w')
print('There are', len(CtVec_alphaNum.get_feature_names()), \
            'tokens in the US Constitution if we split the text by ' \
            'non-alpha numberic characters.', file = an_outfile) 

# create a dictionary for later use and print the tokens and their count  
print('\nFrom Non-AlphaNumberic Tokenization, alphabetic order: \n', file = an_outfile)
an_dict = {}
for k in sorted(CtVec_alphaNum.vocabulary_.keys()):
    an_dict[k] = Mx_an[0, CtVec_alphaNum.vocabulary_[k]]
    print(k, " : ",  Mx_an[0, CtVec_alphaNum.vocabulary_[k]], file = an_outfile)

# print the top 50 words according to frequency of the word
top50 = dict(Counter(an_dict).most_common(50))
print("\n\nTop 50 most frequently used words in the document: \n", file = an_outfile)
for k, v in top50.items(): 
    print(k, ": ", v, file = an_outfile)
    
an_outfile.close()
