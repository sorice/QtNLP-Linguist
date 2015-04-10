#!/usr/bin/env python
# -*- coding: utf-8-sig -*-

"""
.. module:: ToNgueLP_corpus_XML_read
   :platform: Linux
   :synopsis: Leer datos del XML del corpus base de ToNgueLP.

.. moduleauthor:: Abel Meneses Abad <abelma1980@gmail.com>
.. moduleauthor:: Leonel Salazar Videaux <lordford@openmailbox.org>

"""

#~ from lib.python_contrib.pxdom import *
import pxdom
import os

class TNLP_XML_Manager:
   """Helper to manage the TNLP.xml information file"""

   def __init__(self):
      """Init global attributes"""

      self.__parsed = False
      self.__xml_file = None
      self.__xml_document = None
      self.__root_node = None
      self.__cases_node = None
      self.__groups = None
      self.__NLP_problem_type = 'similarity'
      self.__text_extension = 'paragraph'
      self.__cases = []
      self.__case_info = None


   # public methods
   def parse_xml(self, xml_file): #OK
      """Parse the indicated xml_file"""

      result = False
      self.__ruta = xml_file
      self.__xml_document = pxdom.parse(xml_file)
      # TODO: Validate parse(...) result
      # if no errors
      self.__root_node = self.__xml_document._get_documentElement()
      # refer to this as self.__cases_node[0] because there is only one 'cases' node
      self.__groups = self.__root_node.getElementsByTagName('group')
      # refer to this as self.__annotations_node[0] because there is only one 'annotations' node
      self.__annotations_node = self.__root_node.getElementsByTagName('annotations')
      result = True
      self.__parsed = True

      return result


   def get_corpus_info(self): #OK
      """Return the root element info in a dictionary."""

      corpus = {}
      corpus['name'] = self.__root_node.getAttribute('name')
      corpus['version'] = self.__root_node.getAttribute('version')
      corpus['lang'] = self.__root_node.getAttribute('lang')
      corpus['total_cases'] = self.__root_node.getAttribute('total_cases')
      corpus['total_true_cases'] = self.__root_node.getAttribute('total_true_cases')
      corpus['total_annotations'] = self.__root_node.getAttribute('total_annotations')
      corpus['total_true_annotations'] = self.__root_node.getAttribute('total_true_annotations')
      corpus['license'] = self.__root_node.getAttribute('license')
      corpus['copyright'] = self.__root_node.getAttribute('copyright')
      corpus['owners'] = self.__root_node.getAttribute('owners')
      corpus['authors'] = self.__root_node.getAttribute('authors')
      corpus['country'] = self.__root_node.getAttribute('country')
      corpus['creation_date'] = self.__root_node.getAttribute('creation_date')
      corpus['last_modification_date'] = self.__root_node.getAttribute('last_modification_date')
      corpus['xmlns'] = self.__root_node.getAttribute('xmlns')

      return corpus


   def get_corpus_total_cases(self): #OK
      """Return how many cases exists in corpus"""

      total_cases = 0

      if not self.__parsed:
         return None

      for i in range(len(self.__groups)):
         case = self.__groups[i].getElementsByTagName('case')
         total_cases += len(case)

      return total_cases


   def get_specific_total_cases(self,NLP_problem_type): #OK
      """Return how many cases exists in corpus about a specific NLP problem type."""

      if not self.__parsed:
         return None

      for i in range(len(self.__groups)):
         if self.__groups[i].getAttribute('NLP_problem_type') == NLP_problem_type:
            target = i
      cases = self.__groups[target].getElementsByTagName('case')

      return len(cases)


   def get_cases(self): #OK
      """Return all cases in a list."""

      tmp_cases = self.__root_node.getElementsByTagName('case')
      for item in tmp_cases:
         case = {}
         case['id'] = item.getAttribute('id')
         case['description'] = item.getAttribute('description')
         case['plag_type'] = item.getAttribute('plag_type')
         case['annotator_summary'] = item.getAttribute('annotator_summary')
         case['automatic_summary'] = item.getAttribute('automatic_summary')
         case['original_corpus'] = item.getAttribute('original_corpus')
         case['original_corpus_id'] = item.getAttribute('original_corpus_id')
         case['generated_by'] = item.getAttribute('generate_by')
         case['generator_name'] = item.getAttribute('generator_name')
         case['susp_snippet_doc'] = item.getElementsByTagName('susp_snippet')[0].getAttribute('doc')
         case['susp_snippet_offset'] = item.getElementsByTagName('susp_snippet')[0].getAttribute('offset')
         case['susp_snippet_length'] = item.getElementsByTagName('susp_snippet')[0].getAttribute('length')
         case['susp_snippet_sentences_count'] = item.getElementsByTagName('susp_snippet')[0].getAttribute('sentences_count')
         case['src_snippet_doc'] = item.getElementsByTagName('src_snippet')[0].getAttribute('doc')
         case['src_snippet_offset'] = item.getElementsByTagName('src_snippet')[0].getAttribute('offset')
         case['src_snippet_length'] = item.getElementsByTagName('src_snippet')[0].getAttribute('length')
         case['src_snippet_sentences_count'] = item.getElementsByTagName('src_snippet')[0].getAttribute('sentences_count')
         case['text_susp'] = self.__get_snippet_text(case['susp_snippet_doc'], case['susp_snippet_offset'], case['susp_snippet_length'])
         case['text_src'] = self.__get_snippet_text(case['src_snippet_doc'], case['src_snippet_offset'], case['src_snippet_length'])
         
         self.__cases.append(case)

      return self.__cases

   def __get_snippet_text(self, _snippet_doc, _snippet_offset, _snippet_length):
      """Return from a specific text the snippet with the given offset and length."""
      
      _tmp_ruta = self.__ruta[:self.__ruta.rfind('/')]
      _corpus_file = _tmp_ruta[_tmp_ruta.rfind('/')+1:]
      _doc = open('./data/corpuses/'+_corpus_file+'/'+_snippet_doc+'.txt')
      _tmp_doc = _doc.read()
      _text = _tmp_doc[int(_snippet_offset):int(_snippet_offset)+int(_snippet_length)]
      _doc.close()
      
      return _text

   def get_case_by_id(self, case_id): #OK
      """Return the case by it's id."""

      if not self.__parsed:
         return None

      case = {}

      tmp_cases = self.__root_node.getElementsByTagName('case')
      for item in tmp_cases:
         case['id'] = item.getAttribute('id')
         if case['id'] == str(case_id):
            case['description'] = item.getAttribute('description')
            case['plag_type'] = item.getAttribute('plag_type')
            case['annotator_summary'] = item.getAttribute('annotator_summary')
            case['automatic_summary'] = item.getAttribute('automatic_summary')
            case['original_corpus'] = item.getAttribute('original_corpus')
            case['original_corpus_id'] = item.getAttribute('original_corpus_id')
            case['generated_by'] = item.getAttribute('generated_by')
            case['generator_name'] = item.getAttribute('generator_name')
            case['susp_snippet_doc'] = item.getElementsByTagName('susp_snippet')[0].getAttribute('doc')
            case['susp_snippet_offset'] = item.getElementsByTagName('susp_snippet')[0].getAttribute('offset')
            case['susp_snippet_length'] = item.getElementsByTagName('susp_snippet')[0].getAttribute('length')
            case['susp_snippet_sentences_count'] = item.getElementsByTagName('susp_snippet')[0].getAttribute('sentences_count')
            case['src_snippet_doc'] = item.getElementsByTagName('src_snippet')[0].getAttribute('doc')
            case['src_snippet_offset'] = item.getElementsByTagName('src_snippet')[0].getAttribute('offset')
            case['src_snippet_length'] = item.getElementsByTagName('src_snippet')[0].getAttribute('length')
            case['src_snippet_sentences_count'] = item.getElementsByTagName('src_snippet')[0].getAttribute('sentences_count')
            case['text_susp'] = self.__get_snippet_text(case['susp_snippet_doc'], case['susp_snippet_offset'], case['susp_snippet_length'])
            case['text_src'] = self.__get_snippet_text(case['src_snippet_doc'], case['src_snippet_offset'], case['src_snippet_length'])

            break

      return case


   def get_annotations_of_case(self, case_id):
      """Return annotations corresponding to a case."""

      #TODO: refactorize
      annotations = []

      _cases = self.__root_node.getElementsByTagName('case')

      for item in _cases:
         if item.getAttribute('id') == str(case_id):
            _annotations = item.getElementsByTagName('annotation')
      _case = self.get_case_by_id(case_id)

      # if there are no annotation
      if _annotations == None:
         return _annotations

      for item in _annotations:
         annotation = {}

         annotation['id']= item.getAttribute('id')
         annotation['author']= item.getAttribute('author')
         annotation['is_paraphrase']= item.getAttribute('is_paraphrase')
         annotation['validated_by_human_beings']= item.getAttribute('validated_by_human_beings')
         annotation['recognized_by_algorithms']= item.getAttribute('recognized_by_algorithms')
         annotation['algorithms_names']= item.getAttribute('algorithms_names')
         annotation['annotation_date']= item.getAttribute('annotation_date')
         annotation['phenomenon_type'] = item.getElementsByTagName('phenomenon')[0].getAttribute('type')
         annotation['projection'] = item.getElementsByTagName('phenomenon')[0].getAttribute('projection')
         annotation['susp_chunk_offset'] = item.getElementsByTagName('susp_chunk')[0].getAttribute('offset')
         annotation['susp_chunk_length'] = item.getElementsByTagName('susp_chunk')[0].getAttribute('length')
         annotation['src_chunk_offset'] = item.getElementsByTagName('src_chunk')[0].getAttribute('offset')
         annotation['src_chunk_length'] = item.getElementsByTagName('src_chunk')[0].getAttribute('length')
         # TODO: extract sentences from TNLP.xml (sentences etc...)
         annotation['lb_note_susp_sentence'] = self.__get_sentence_from_snippet(_case['text_susp'], annotation['susp_chunk_offset'])
         annotation['lb_note_src_sentence'] = self.__get_sentence_from_snippet(_case['text_src'], annotation['src_chunk_offset'])

         annotations.append(annotation)

      return annotations

   def __get_sentence_from_snippet(self, _snippet, _chunk_offset):
      
      _chunk_offset = int(_chunk_offset)
      
      _tmp_text1 = _snippet[:_chunk_offset]
      _tmp_text2 = _snippet[_chunk_offset:]
      
      _sentence = _tmp_text1[_tmp_text1.rfind('.')+1:]+_tmp_text2[:_tmp_text2.find('.')]
      
      return _sentence

   def add_case(self, _problem_type, _extension, _description, _plag_type,
      _summary, _auto_summary, _original_corpus, _original_corpus_id, _generated_by, _generator_name, _susp_doc, _susp_offset,
      _susp_length, _src_doc, _src_offset, _src_length): #OK
      """Add a new case to the corpus"""

      #TODO validate all input data

      result = False

      # select the correct group for the case
      for i in range(len(self.__groups)):
         if self.__groups[i].getAttribute('NLP_problem_type') == NLP_problem_type:
            target = i

      actual_group = self.__groups[target]
      total_cases = len(self.__root_node.getElementsByTagName('case'))

      # create new node and append it to current group
      # case node
      case = self.__xml_document.createElement('case')
      case.setAttribute('id', str(total_cases + 1))
      case.setAttribute('description', _description)
      case.setAttribute('plag_type', _plag_type)
      case.setAttribute('annotator_summary', _summary)
      case.setAttribute('automatic_summary', _auto_summary)
      case.setAttribute('original_corpus', _original_corpus)
      case.setAttribute('original_corpus_id', _original_corpus_id)
      case.setAttribute('generated_by',_generated_by)
      case.setAttribute('generator_name', _generator_name)

      # susp snippet node
      susp_snippet = self.__xml_document.createElement('susp_snippet')
      susp_snippet.setAttribute('doc', _susp_doc)
      susp_snippet.setAttribute('offset', str(_susp_offset))
      susp_snippet.setAttribute('length', str(_susp_length))
      case.appendChild(susp_snippet)

      # src snippet node
      src_snippet = self.__xml_document.createElement('src_snippet')
      src_snippet.setAttribute('doc', _src_doc)
      src_snippet.setAttribute('offset', str(_src_offset))
      src_snippet.setAttribute('length', str(_src_length))
      case.appendChild(src_snippet)

      # add case to group
      actual_group.appendChild(case)

      # update result
      result = True

      return result


   def add_annotation(self, _case_id, _author, _is_paraphrase, _validated_by_human_beings, _recognized_by_algorithms, _algorithms_names,
      _date, _type, _projection, _chunk_offset, _chunk_length, _chunk_src_offset, _chunk_src_length):
      """Add an annotation to a case"""

      #TODO validate all input data

      result = False
      case = {}

      tmp_cases = self.__root_node.getElementsByTagName('case')
      for item in tmp_cases:
         case['id'] = item.getAttribute('id')
         if case['id'] == str(_case_id):
            actual_case = item

      if actual_case.getElementsByTagName('annotation'):
         total_annotation = len(actual_case.getElementsByTagName('annotation'))
      else:
         total_annotation = 0

      # create new node and append it to current case
      # annotation node
      annotation = self.__xml_document.createElement('annotation')
      annotation.setAttribute('id', str(total_annotation + 1))
      annotation.setAttribute('author', _author)
      annotation.setAttribute('is_paraphrase', _is_paraphrase)
      annotation.setAttribute('validated_by_human_beings', _validated_by_human_beings)
      annotation.setAttribute('recognized_by_algorithms', _recognized_by_algorithms)
      annotation.setAttribute('algorithms_names', _algorithms_names)
      annotation.setAttribute('annotation_date', _date)

      # phenomenon node
      phenomenon = self.__xml_document.createElement('phenomenon')
      phenomenon.setAttribute('type', _type)
      phenomenon.setAttribute('projection', _projection)
      annotation.appendChild(phenomenon)

      # susp chunk node
      susp_chunk = self.__xml_document.createElement('susp_chunk')
      susp_chunk.setAttribute('chunk_offset', _chunk_offset)
      susp_chunk.setAttribute('chunk_length', _chunk_length)
      annotation.appendChild(susp_chunk)

      # susp chunk node
      src_chunk = self.__xml_document.createElement('src_chunk')
      src_chunk.setAttribute('chunk_offset', _chunk_src_offset)
      src_chunk.setAttribute('chunk_length', _chunk_src_length)
      annotation.appendChild(src_chunk)

      # add annotation to case
      actual_case.appendChild(annotation)

      # update result
      result = True

      return result

   def write_xml(self, _xml_file):
      """Write data to _xml_file"""

      serialiser = self.__xml_document.implementation.createLSSerializer()
      serialiser.writeToURI(self.__xml_document, _xml_file)


   def get_corpus_name(self):
      """Returns the corpus name."""
      
      _corpus_name = self.__root_node.getAttribute('name')

      return _corpus_name


   def get_case_summary(self, _index):
      """Return basic information about a especific case."""

      case = {}

      tmp_cases = self.__root_node.getElementsByTagName('case')

      if 0 < _index and _index <= self.get_corpus_total_cases():
         case['id'] = tmp_cases[_index - 1].getAttribute('id')
         case['annotator_summary'] = tmp_cases[_index - 1].getAttribute('annotator_summary')
         case['plag_type'] = tmp_cases[_index - 1].getAttribute('plag_type')

      return (case['plag_type'], case['id'], case['annotator_summary'])


   # auxiliar & private methods
   def __get_cases(self):
      """Helper: return cases from all groups"""

      cases = self.__cases_node[0].getElementsByTagName('case_pair')
      return cases


   def __get_annotations(self, case_pair_id):
      """Helper: return annotations for a specific case_id"""

      annotations = None

      tmp_cases = self.__annotations_node[0].getElementsByTagName('case_pair')
      for item in tmp_cases:
         if item.hasAttribute('id') and item.getAttribute('id') == str(case_pair_id):
            annotations = item
            break

      return annotations


   def __update_corpus_info(self):
      """Update corpus information such as modification date and so on..."""

      pass


# Test Environment
if __name__ == "__main__":
   a = TNLP_XML_Manager()
   a.parse_xml('../../data/corpuses/TNLP/TNLP.xml')

   print "CORPUS INFO: "
   print a.get_corpus_info()

   print "\nCORPUS TOTAL CASES: "
   print a.get_corpus_total_cases()

   NLP_problem_type = 'similarity'
   print "\nTOTAL CASES OF "+ NLP_problem_type
   print a.get_specific_total_cases(NLP_problem_type)

   print "\nCASES"
   list = a.get_cases()
   print "TNLP.__cases[0] = ",list[0]

   id = 6
   print "\nCASE, id = " + str(id) + ": "
   print a.get_case_by_id(id)

   print "\nANNOTATIONS #s, case = " + str(id) + ": "
   print len(a.get_annotations_of_case(id))
   print "\nANNOTATIONS, case = " + str(id) + ": "
   print a.get_annotations_of_case(id)

   print "\nADD CASE"
   print a.add_case("similarity","paragraph","desc","paraphrase","manual summary","auto summary",
   "PAN_PC-15","12345", 'human', 'abelm','susp/susp-doc00560', '15', '30', 'src/src-doc01360', '60', '101')

   print "\nCORPUS TOTAL CASES: "
   print a.get_corpus_total_cases()

   print "\nADD ANNOTATION"
   print a.add_annotation(id, 'leonelsv', 'True', 'None', 'True', 'ngram-1',
   '2015-02-26', 'coordination', 'local', '10', '55', '2', '120')

   print "\nANNOTATIONS LENGTH, case = " + str(id) + ": "
   print len(a.get_annotations_of_case(id))
   print "\nANNOTATIONS, case = " + str(id) + ": "
   print a.get_annotations_of_case(id)

   a.write_xml('salida.xml')
