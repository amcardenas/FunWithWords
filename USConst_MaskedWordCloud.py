# -*- coding: utf-8 -*-
"""
NAME: USConst_MaskedWordCloud.py
PURPOSE: Create a word cloud from a text document of the US Constitution and
        shape it like the continental US.
SOURCE: Adapted from Andreas Mueller's examples at 
        https://amueller.github.io/word_cloud/auto_examples/index.html
"""

import argparse
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS

# parse the command line arguments so that you can use this code for other 
# text documents and masks.  
parser = argparse.ArgumentParser()
parser.add_argument('--infile', action = 'store', 
    default = "../Documents/NatLangProc/USConstitution/USConstitution.txt", 
    help='path to text file')
parser.add_argument('--mask', action = 'store', 
    default = "us.jpg", help='path to mask file as a .jpg')
parser.add_argument('--out', action = 'store',
    default = "USConst_wordCloud.png", help='path to output file')
args = parser.parse_args()

# read US Constintution text into a single string
with open(args.infile, 'r') as myfile:
    text = myfile.read().replace('\n', ' ')

# read the mask image
# from http://www.stencilry.org/stencils/
us_mask = np.array(Image.open(args.mask))

# create a set ouf of stopwords
stopwords = set(STOPWORDS)

# instantiate the word cloud generator
wc = WordCloud(background_color = 'aliceblue', mask = us_mask, stopwords = stopwords, 
               margin=5, colormap = 'seismic', random_state = 9)

# generate word cloud
wc.generate(text)

# store to file
wc.to_file(args.out)

# show
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.show()