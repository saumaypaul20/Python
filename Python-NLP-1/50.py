'''
Done By:-
            SAUMAY PAUL         CSE 50-14
             DUIET, Dibrugarh University
'''

from nltk.stem import PorterStemmer,LancasterStemmer,RegexpStemmer, WordNetLemmatizer
from nltk import pos_tag
from nltk.tokenize import word_tokenize
 
ps = PorterStemmer()
ls = LancasterStemmer()


lemmatiser = WordNetLemmatizer()

f=open("text.txt", "r")
if f.mode == 'r':
    contents =f.read()

tokens = word_tokenize(contents) # Generate list of tokens

for i in tokens:
    print('GIVEN WORD:           %s' %i.upper())
    print('Porter Stemmer:       %s' %ps.stem(i))
    print('Lancaster Stemmer:    %s' %ls.stem(i))
    print('WordNetLemmatizer:    %s '% lemmatiser.lemmatize(i))
    print('')
    
