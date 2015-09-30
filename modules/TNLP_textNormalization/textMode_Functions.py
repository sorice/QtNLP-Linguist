import re
from replacers1 import RegexpReplacer1
import string
from text_normalization_methods import *

LETTERS = ''.join([string.letters, string.digits])

def preProcessFlow(self, doc_name):#if __name__ == "__main__":
    """Flow of text pre-processing"""
    #~ print doc_name
    #~ if path != '':
        #~ path = path+'/'
    #~ if pathb != '':
        #~ pathb = pathb+'/'
    
    #-------------------Special tokens recognition and normalization
    text = open(doc_name).read().decode('utf8')
    #processing urls
    text = url_string_recognition_support(text)
    #processing some special punctuation signs
    text = punctuation_filter(text)
    #multi-words representation
    text = contiguos_string_recognition_support(text) 
    # Add a final dot to the document.
    text = text+' .'
   
    texto = open(doc_name, 'w')
    texto.write(text.encode('utf8'))
    texto.close()

    #-------------------Clean all punctuation sign
    text = unicode(open(doc_name).read(),'utf8')
    replacer = RegexpReplacer1()
    chunk = replacer.replace(text)
    
    texto = open(doc_name,'w')
    texto.write(chunk.encode('utf8'))
    texto.close()
