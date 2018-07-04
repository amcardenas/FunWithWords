# -*- coding: utf-8 -*-
"""
NAME: nltkPractice.py
PURPOSE: Perform text analytics techniques with various documents.
AUTHOR: Aimee Cardenas
"""

import argparse
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from collections import Counter
from matplotlib import pyplot as plt

# parse the command line arguments so that you can use this code for other 
# text documents.  
parser = argparse.ArgumentParser()
parser.add_argument('--infile', action = 'store', 
    default = "../TextInput/Amendments.txt", 
    help='path to text file')
parser.add_argument('--outfile', action = 'store',
    default = "../TextOutput/Amendments_wordSet.txt", 
    help='path to output file')
parser.add_argument('--outpng', action = 'store', 
    default = '../Plots/Amendments_WordLengthHistogram.png',
    help = 'path to output png file for histogram')
parser.add_argument('--title', action = 'store', 
    default = "The Amendments to the US Contitution",
    help = 'Title for Histogram of Word Lengths')
args = parser.parse_args()

# read the text document into a single string
with open(args.infile, 'r') as myfile:
    data=myfile.read().replace('\n', ' ')

# tokenize the document on sentences
sentences = sent_tokenize(data)

# tokenize the documment on lower case alphabetic characters only
tokens = [w for w in word_tokenize(data.lower()) if w.isalpha()]

# add other stopwords to the pre-made stopword list
moreStopWords = ["amendment", "section", "without", "article", "hereby",
                 "within", "otherwise", "upon", "whenever", "begin", "thereof",
                 "unless", "become", "among", "may", "made", "day", "make", 
                 "place", "either", "every", "wherein", "hereof", "therein", 
                 "shall", "iv", "b", "ex", "hu", "also", "robt", "vi", "mr",
                 "thereby", "richd", "vii", "st", "iii", "jun", "gouv", "ii",
                 "abr", "danl", "ix", "u", "v", "xiv", "xi", "x", "viii", "xiii",
                 "xv", "xvi", "xvii", "xviii", "xix", "xx", "xxi", "xxii", 
                 "xxiii", "xxiv", "xxv", "xxvi"]
allStopWords = set(stopwords.words('english')).union(moreStopWords)

# remove stop words
noStopWords = [t for t in tokens if t not in allStopWords]

# Instantiate the WordNetLemmatizer
wordLemmatizer = WordNetLemmatizer()

# Lemmatize all words into a new list
lemmatized = [wordLemmatizer.lemmatize(t) for t in noStopWords]

# open output text file
outfile = open(args.outfile, 'w')

# print the number of sentences and words in the document
print("\nNumber of sentences: ", len(sentences), file = outfile)
print("Number of words excluding stop words, words lemmatized: ", 
      len(lemmatized), file = outfile)

# Create a value-sorted bag-of-words
bow = dict(Counter(lemmatized).most_common(len(lemmatized)))

# print the words and their respective counts
print("Lemmatized Bag of Words sorted by the word frequency: \n", file = outfile)
for k, v in bow.items():
    print(k, " : ", v, file = outfile)

# close text output files
outfile.close()

# create a list of word lengths
wordLengths = [len(w) for w in lemmatized]

# plot a histogram of the word lengths
plt.hist(wordLengths)
plt.xlabel("Word Lengths (Lemmatized)")
plt.ylabel("Frequency of Word Lengths")
plt.suptitle(args.title)
plt.title("No Stop Words Included; Words Lemmatized", fontsize = 8)
plt.savefig(args.outpng)





'''


'''
