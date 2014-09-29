#!/usr/bin/env python
# -*- coding: utf-8-sig -*-

from ToNgueLP_Parser import *
from fuzzywuzzy import fuzz 
import time

corpus_dir = '/media/swlDOC/Doctorado/00_EScorpus/data/'

xml_corpus = corpus_dir+'ToNgueLP-plag-cases-corpus.xml'

kase = input('Entre el número del caso que desea revisar: ')

# This enters the XML parsing loop
handler = CorpusHandler()
parser = make_parser()
parser.setContentHandler(handler)
parser.parse(open(xml_corpus))

#~ print "El nombre del corpus es: ", handler.corpus_name
#~ print "Total Elements: %d" % handler.elements 

#~ print 'Elementos del Par de fragmentos[', handler.snippet_pair_id,'] = ',handler.snippet_pair[handler.snippet_pair_id]

element = handler.getCase(kase)
print 'element: ', element
 
if element != None:
	textoa = open(corpus_dir+'/susp/'+element[1]+'.txt','r').read()
	susp_snippet = textoa[int(element[7]):int(element[7])+int(element[5])]
	textob = open(corpus_dir+'/src/'+element[3]+'.txt','r').read()
	src_snippet = textob[int(element[11]):int(element[11])+int(element[9])]

	fuzzr = fuzz.ratio(susp_snippet,src_snippet)

	fuzz_partial = fuzz.partial_ratio(susp_snippet,src_snippet)
	init = time.time()

	fuzz_sort = fuzz.token_sort_ratio(susp_snippet,src_snippet)

	timea = time.time() - init

print 'El fragmento sospechoso es: ', susp_snippet

print '/n ****************************** /n'

print 'El fragmento fuente es: ', src_snippet

print 'fuzz ratio = ', fuzzr

print 'fuzz partial ratio = ', fuzz_partial

print 'fuzz sort ratio = ', fuzz_sort

print 'La comparación de los fragmentos demora: ', timea
