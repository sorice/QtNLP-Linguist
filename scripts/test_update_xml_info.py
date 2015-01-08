#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. module:: Test_Update_Corpus_XML_Infomation
   :platform: Linux
   :synopsis: Batería de pruebas en unittest para comprobar el funcionamiento del 
   script Update_Corpus_XML_Info [UCXI].

.. moduleauthor:: Abel Meneses Abad <abelma1980@gmail.com>

""" 

from unittest import TestCase, main
from mocker import Mocker

import update_corpus_xml_info

class test_UCXI_constructor(TestCase):
   def test_init(self):
      """Probando el constructor de la clase :class: update_corpus_xml_inf.
      """
      mocker = Mocker()
      number = mocker.mock()
      corpus_file = mocker.mock()
      corpus_dir = mocker.mock()
      text = mocker.mock()
      mocker.replay()
      script = update_corpus_xml_info.Update_Corpus_XML_Info(number, corpus_file, corpus_dir, text)
      mocker.restore()
      mocker.verify()
      self.assertTrue(script.number == number)
      
class test_UCXI_snippet_pair_count(TestCase):
   def test_snippet_pair_count_without_xml(self):
      """Probando el método snippet_pair_count cuando no está el fichero. 
      Para ello se utiliza un nombre de fichero no existente en esta ruta 'script.rst'. 
      .. Nota:: se acerca bastante al nombre del fichero que aparece allí que es scripts.rst, es intencional la selección de este nombre para que parezca que sí lo encontrará pero al final no lo hace.
      """
      mocker = Mocker()
      number = mocker.mock()
      corpus_file = mocker.mock()
      corpus_dir = mocker.mock()
      text = mocker.mock()
      corpus_file = 'script.rst'
      mocker.replay()
      script = update_corpus_xml_info.Update_Corpus_XML_Info(number, corpus_file, corpus_dir, text)
      mocker.restore()
      mocker.verify()
      self.assertEqual(script.snippet_pair_count(), None)

      
   def test_UCXI_snippet_pair_count_with_xml(self):
      """Probando cuando el fichero si está que devuelva el valor correcto. 
      Para ello se utiliza el XML de pruebas contenido en la carpeta test.
      """
      mocker = Mocker()
      number = mocker.mock()
      corpus_file = mocker.mock()
      corpus_dir = mocker.mock()
      text = mocker.mock()
      corpus_file = '../test/ToNgueLP-test-plag-cases-corpus.xml'
      mocker.replay()
      script = update_corpus_xml_info.Update_Corpus_XML_Info(number, corpus_file, corpus_dir, text)
      self.assertEqual(script.snippet_pair_count(), 6)
      mocker.restore()
      mocker.verify()
      
if __name__ == '__main__':
   main()
