# FunWithWords
a place to practice with text analytics

 Masked Word Cloud of the US Constitution

This is just the starting point of a few text analytics projects involving the US Constitution and other public text documents.  

Program: USConst_MaskedWordCloud.py

Inputs:
Text document of the US Constitution: a text version adapted from the U.S. Government Publishing Office at https://www.gpo.gov/fdsys/pkg/GPO-CONAN-1992/content-detail.html
Mask file: a .jpg of the stencil of the continental United States

Output: USConst_wordCloud.png


UPDATE: 13-Sep-2017
Added more stop words.

Created a new word cloud for the Amendments:

Input: 
Text: Amendments.txt from http://hrlibrary.umn.edu/education/all_amendments_usconst.htm
Mask: eagle.jpg


 UPDATE: 21-Sep-2017
added:
USConst_bagOfWords.py: python program using CountVectorizer, etc., to create a bag of words from the US Constitution.  A dictionary of words and their frequencies are printed to an output file along in alphabetical order along with the total number of significant tokens (words) and the top 50 most frequently used words.  
USConst_wordFreq.txt: a text document containing the bag of words from the constitution order alphabetically with their counts, a total count of significant tokens (words) in the US Constitution and the top 50 most frequently used words.

NEXT: 
* Trim down the occurrence of similar words by performing some stemming, etc., to only get root words instead of counting multiple versions of the same word, such as state, states, etc.  
* N-grams in order to catch important phrases, titles, etc., such as Vice President as distinguished from President.  And also to analyze common phrases and to start on topic identification.  
* Topic modeling
* BUT WAIT, THERE'S MORE: Similar tasks++ with gensim, ntlk, etc., etc.
