#!/usr/bin/env python
# -*- coding: utf-8-sig -*-

"""
.. module:: ToNgueLP_corpus_XML_read
   :platform: Linux
   :synopsis: Leer datos del XML del corpus base de ToNgueLP.

.. moduleauthor:: Abel Meneses Abad <abelma1980@gmail.com>
.. moduleauthor:: Leonel Salazar Videaux <lordford@openmailbox.org>

"""

from lib.python_contrib.pxdom import pxdom
import os, urllib, re
from modules.TNLP_textNormalization.textMode_Functions import convertWin_Into_UnixText

class TNLP_XML_Manager:
   """Helper to manage the TNLP.xml information file."""

   def __init__(self):
      """Init global attributes."""

      self.__parsed = False
      self.__xml_path = None
      self.__xml_document = None
      self.__root_node = None
      self.__cases_node = None
      self.__groups = None
      self.__cases = []
      self.__case_info = None


   # public methods
   def parse_xml(self, xml_file): #OK
      """Parse the indicated xml_file"""

      result = False
      self.__xml_path = xml_file
      self.__xml_document = pxdom.parse(xml_file)
      # TODO: Validate parse(...) result
      # if no errors
      self.__root_node = self.__xml_document._get_documentElement()
      self.__groups = self.__root_node.getElementsByTagName('group')
      # there is only ONE cases node
      self.__cases_node = self.__root_node.getElementsByTagName('cases')[0]

      result = True
      self.__parsed = True

      return result


   def get_corpus_info(self): #OK
      """Return the root element info in a dictionary."""

      # update corpus info
      self.__update_corpus_info()

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
         case['domain'] = item.getAttribute('domain')
         case['document_type'] = item.getAttribute('document_type')

         # susp snippet node
         case['susp_snippet_doc'] = item.getElementsByTagName('susp_snippet')[0].getAttribute('doc')
         case['susp_snippet_offset'] = item.getElementsByTagName('susp_snippet')[0].getAttribute('offset')
         case['susp_snippet_length'] = item.getElementsByTagName('susp_snippet')[0].getAttribute('length')
         case['susp_snippet_sentences_count'] = item.getElementsByTagName('susp_snippet')[0].getAttribute('sentences_count')
         case['susp_snippet_words_count'] = item.getElementsByTagName('susp_snippet')[0].getAttribute('words_count')
         case['susp_snippet_topic'] = item.getElementsByTagName('susp_snippet')[0].getAttribute('topic')

         case['susp_text'] = self.__get_snippet_text(case['susp_snippet_doc'], case['susp_snippet_offset'], case['susp_snippet_length'])

         # susp snippet node
         case['src_snippet_doc'] = item.getElementsByTagName('src_snippet')[0].getAttribute('doc')
         case['src_snippet_offset'] = item.getElementsByTagName('src_snippet')[0].getAttribute('offset')
         case['src_snippet_length'] = item.getElementsByTagName('src_snippet')[0].getAttribute('length')
         case['src_snippet_sentences_count'] = item.getElementsByTagName('src_snippet')[0].getAttribute('sentences_count')
         case['src_snippet_words_count'] = item.getElementsByTagName('src_snippet')[0].getAttribute('words_count')
         case['src_snippet_topic'] = item.getElementsByTagName('src_snippet')[0].getAttribute('topic')

         case['src_text'] = self.__get_snippet_text(case['src_snippet_doc'], case['src_snippet_offset'], case['src_snippet_length'])

         self.__cases.append(case)

      return self.__cases


   def get_case_by_id(self, case_id): #OK
      """Return the case by it's id."""

      if not self.__parsed:
         return None

      case = {}

      tmp_cases = self.__root_node.getElementsByTagName('case')
      for item in tmp_cases:
         case['id'] = item.getAttribute('id')
         if case['id'] == str(case_id):
            case['problem_type'] = item.parentNode.getAttribute('NLP_problem_type')
            case['text_extension'] = item.parentNode.getAttribute('text_extension')

            case['description'] = item.getAttribute('description')
            case['plag_type'] = item.getAttribute('plag_type')
            case['annotator_summary'] = item.getAttribute('annotator_summary')
            case['automatic_summary'] = item.getAttribute('automatic_summary')
            case['original_corpus'] = item.getAttribute('original_corpus')
            case['original_corpus_id'] = item.getAttribute('original_corpus_id')
            case['generated_by'] = item.getAttribute('generated_by')
            case['generator_name'] = item.getAttribute('generator_name')
            case['domain'] = item.getAttribute('domain')
            case['document_type'] = item.getAttribute('document_type')
            case['paraphrase_composition'] = item.getAttribute('paraphrase_composition')
            case['lenght'] = item.getAttribute('lenght')

            # susp snippet node
            case['susp_snippet_doc'] = item.getElementsByTagName('susp_snippet')[0].getAttribute('doc')
            case['susp_snippet_offset'] = item.getElementsByTagName('susp_snippet')[0].getAttribute('offset')
            case['susp_snippet_length'] = item.getElementsByTagName('susp_snippet')[0].getAttribute('length')
            case['susp_snippet_sentences_count'] = item.getElementsByTagName('susp_snippet')[0].getAttribute('sentences_count')
            case['susp_snippet_words_count'] = item.getElementsByTagName('susp_snippet')[0].getAttribute('words_count')
            case['susp_snippet_topic'] = item.getElementsByTagName('susp_snippet')[0].getAttribute('topic')

            case['susp_text'] = self.__get_snippet_text(case['susp_snippet_doc'],case['susp_snippet_offset'], case['susp_snippet_length'])

            # src snippet node
            case['src_snippet_doc'] = item.getElementsByTagName('src_snippet')[0].getAttribute('doc')
            case['src_snippet_offset'] = item.getElementsByTagName('src_snippet')[0].getAttribute('offset')
            case['src_snippet_length'] = item.getElementsByTagName('src_snippet')[0].getAttribute('length')
            case['src_snippet_sentences_count'] = item.getElementsByTagName('src_snippet')[0].getAttribute('sentences_count')
            case['src_snippet_words_count'] = item.getElementsByTagName('src_snippet')[0].getAttribute('words_count')
            case['src_snippet_topic'] = item.getElementsByTagName('src_snippet')[0].getAttribute('topic')

            case['src_text'] = self.__get_snippet_text(case['src_snippet_doc'], case['src_snippet_offset'], case['src_snippet_length'])

            #~ # locate parent data
            #~ parent_group = None
            #~ tmp_groups = self.__root_node.getElementsByTagName('group')
            #~ for group in groups:
               #~ tmp_cases = group.getElementsByTagName('case')
               #~ for item in tmp_cases:
                  #~ if item.getAttribute('id') == str(case_id):
                     #~ parent_group = group

            break

      return case

   def __get_snippet_text(self, _snippet_doc, _snippet_offset, _snippet_length):
      """Return from a specific text the snippet with the given offset and length."""

      _corpus_dir = os.path.dirname(self.__xml_path) + '/'

      convertWin_Into_UnixText(self, _corpus_dir + _snippet_doc + '.txt')

      _doc = open(_corpus_dir + _snippet_doc + '.txt')
      _tmp_doc = unicode(_doc.read(),'utf8')
      _text = _tmp_doc[int(_snippet_offset):int(_snippet_offset) + int(_snippet_length)]
      _doc.close()

      return _text


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

         annotation['susp_sentence'] = self.__get_sentence_from_snippet(_case['susp_text'], annotation['susp_chunk_offset'])
         annotation['src_sentence'] = self.__get_sentence_from_snippet(_case['src_text'], annotation['src_chunk_offset'])

         annotations.append(annotation)

      return annotations


   def __get_sentence_from_snippet(self, _snippet, _chunk_offset):

      _chunk_offset = int(_chunk_offset)

      _tmp_text1 = _snippet[:_chunk_offset]
      _tmp_text2 = _snippet[_chunk_offset:]

      _sentence = _tmp_text1[_tmp_text1.rfind('.') + 1:] + _tmp_text2[:_tmp_text2.find('.')]

      return _sentence


   def add_case(self, _problem_type, _extension, _description, _plag_type, _summary, _auto_summary,
      _original_corpus, _original_corpus_id, _generated_by, _generator_name, _domain, _document_type, _topic_match, _paraphrase_composition, _lenght, _susp_doc, _susp_offset,
      _susp_length, _susp_sentences_count, _susp_words_count, _susp_doc_topic, _src_doc, _src_offset, _src_length, _src_sentences_count, _src_words_count, _src_doc_topic, _case_id = None): #OK
      """Add a new case to the corpus"""

      #TODO validate all input data

      result = False
      target = -1

      for i in range(len(self.__groups)):
         if self.__groups[i].getAttribute('NLP_problem_type') == _problem_type:
            if self.__groups[i].getAttribute('text_extension') == _extension:
               target = i

      # if group already exists
      if target <> -1:
         actual_group = self.__groups[target]
      else: # create group
         actual_group = self.__xml_document.createElement('group')
         actual_group.setAttribute('NLP_problem_type', str(_problem_type))
         actual_group.setAttribute('text_extension', str(_extension))
         self.__cases_node.appendChild(actual_group)

      # calculate new case id
      if _case_id == None:
         ids = []
         for c in self.get_cases():
            ids.append(int(c['id']))

         if len(ids) > 0:
            case_id = max(ids) + 1
         else:
            case_id = 1
      else:
         case_id = _case_id

      # create new node and append it to current group
      # case node
      case = self.__xml_document.createElement('case')
      case.setAttribute('id', str(case_id))
      case.setAttribute('description', _description)
      case.setAttribute('plag_type', _plag_type)
      case.setAttribute('annotator_summary', _summary)
      case.setAttribute('automatic_summary', _auto_summary)
      case.setAttribute('original_corpus', _original_corpus)
      case.setAttribute('original_corpus_id', _original_corpus_id)
      case.setAttribute('generated_by',_generated_by)
      case.setAttribute('generator_name', _generator_name)
      case.setAttribute('domain',_domain)
      case.setAttribute('document_type', _document_type)
      case.setAttribute('topic_match', _topic_match)
      case.setAttribute('paraphrase_composition', _paraphrase_composition)
      case.setAttribute('lenght', _lenght)

      # susp snippet node
      susp_snippet = self.__xml_document.createElement('susp_snippet')
      susp_snippet.setAttribute('doc', _susp_doc)
      susp_snippet.setAttribute('offset', str(_susp_offset))
      susp_snippet.setAttribute('length', str(_susp_length))
      susp_snippet.setAttribute('sentences_count', str(_susp_sentences_count))
      susp_snippet.setAttribute('words_count', str(_susp_words_count))
      susp_snippet.setAttribute('topic', str(_susp_doc_topic))
      case.appendChild(susp_snippet)

      # src snippet node
      src_snippet = self.__xml_document.createElement('src_snippet')
      src_snippet.setAttribute('doc', _src_doc)
      src_snippet.setAttribute('offset', str(_src_offset))
      src_snippet.setAttribute('length', str(_src_length))
      src_snippet.setAttribute('sentences_count', str(_src_sentences_count))
      src_snippet.setAttribute('words_count', str(_src_words_count))
      src_snippet.setAttribute('topic', str(_src_doc_topic))
      case.appendChild(src_snippet)

      # add case to group
      actual_group.appendChild(case)

      # update result
      result = True

      # update corpus info
      self.__update_corpus_info()

      return case_id


   def add_annotation(self, _case_id, _author, _is_paraphrase, _validated_by_human_beings, _recognized_by_algorithms, _algorithms_names,
      _date, _type, _projection, _chunk_offset, _chunk_length, _chunk_src_offset, _chunk_src_length):
      """Add an annotation to a case"""

      #TODO validate all input data
      #TODO calculate next id using max(existing_ids)

      result = False
      case = {}

      tmp_cases = self.__root_node.getElementsByTagName('case')
      for item in tmp_cases:
         if item.getAttribute('id') == str(_case_id):
            actual_case = item

      # calculate new case id
      ids = []
      for a in self.get_annotations_of_case(_case_id):
         ids.append(int(a['id']))

      if len(ids) > 0:
         annotation_id = max(ids) + 1
      else:
         annotation_id = 1

      #Calculate if annotation in not paraphrase or = to "false positive"
      if _type == "non-paraphrase":
         _is_paraphrase="False"

      # create new node and append it to current case
      # annotation node
      annotation = self.__xml_document.createElement('annotation')
      annotation.setAttribute('id', str(annotation_id))
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
      susp_chunk.setAttribute('offset', _chunk_offset)
      susp_chunk.setAttribute('length', _chunk_length)
      annotation.appendChild(susp_chunk)

      # susp chunk node
      src_chunk = self.__xml_document.createElement('src_chunk')
      src_chunk.setAttribute('offset', _chunk_src_offset)
      src_chunk.setAttribute('length', _chunk_src_length)
      annotation.appendChild(src_chunk)

      # add annotation to case
      actual_case.appendChild(annotation)

      # calc paraphrase_composition
      annotations = self.get_annotations_of_case(_case_id)
      types = set()
      for item in annotations:
         types.add(item['phenomenon_type'])

      paraphrase_composition = "pure"
      if len(types) > 2:
         paraphrase_composition = "multiple"
      else:
         if len(types) > 1:
            paraphrase_composition = "mixed"

      actual_case.setAttribute('paraphrase_composition',paraphrase_composition)

      # update result
      result = True

      # update corpus info
      self.__update_corpus_info()

      return self.get_annotations_of_case(_case_id)[-1]

   def write_xml(self):
      """Write data to _xml_file"""

      serialiser = self.__xml_document.implementation.createLSSerializer()
      serialiser.writeToURI(self.__xml_document, 'file:' + urllib.pathname2url(self.__xml_path))
      self.__human_readable_parse()


   def get_corpus_name(self):
      """Returns the corpus name"""

      if self.__parsed:
         return self.__root_node.getAttribute('name')


   def get_case_summary(self, _index):
      """Return basic information about a especific case."""

      case = {}

      tmp_cases = self.__root_node.getElementsByTagName('case')

      if 0 < _index and _index <= self.get_corpus_total_cases():
         case['id'] = tmp_cases[_index - 1].getAttribute('id')
         case['annotator_summary'] = tmp_cases[_index - 1].getAttribute('annotator_summary')
         case['plag_type'] = tmp_cases[_index - 1].getAttribute('plag_type')

      return (case['plag_type'], case['id'], case['annotator_summary'])


   def create_corpus(self, _xml_file, _name, _version, _lang, _total_cases, _total_true_cases, _total_annotations,
      _total_true_annotations, _license, _copyright, _owners, _authors, _country, _creation_date, _last_modification_date, _xmlns):
      """Creata a new corpus XML file."""

      dom = pxdom.getDOMImplementation('')
      doc = dom.createDocument('', None, None)

      # root node
      corpus = doc.createElement('corpus')
      corpus.setAttribute('name', _name)
      corpus.setAttribute('version', _version)
      corpus.setAttribute('lang', _lang)
      corpus.setAttribute('total_cases', _total_cases)
      corpus.setAttribute('total_true_cases', _total_true_cases)
      corpus.setAttribute('total_annotations', _total_annotations)
      corpus.setAttribute('total_true_annotations', _total_true_annotations)
      corpus.setAttribute('license', _license)
      corpus.setAttribute('copyright', _copyright)
      corpus.setAttribute('owners', _owners)
      corpus.setAttribute('authors', _authors)
      corpus.setAttribute('country', _country)
      corpus.setAttribute('creation_date', _creation_date)
      corpus.setAttribute('last_modification_date', _last_modification_date)
      corpus.setAttribute('xmlns', _xmlns)

      cases = doc.createElement('cases')
      corpus.appendChild(cases)

      doc.appendChild(corpus)

      # write corpus
      serialiser = doc.implementation.createLSSerializer()
      serialiser.writeToURI(doc, 'file:' + urllib.pathname2url(_xml_file))

      return True


   def get_xml_url(self):
      """Return corpus url'"""

      return self.__xml_path


   def edit_case(self, _case_id, _problem_type, _extension, _description, _plag_type, _summary, _auto_summary,
      _original_corpus, _original_corpus_id, _generated_by, _generator_name, _domain, _document_type, _topic_match, _paraphrase_composition, _lenght, _susp_doc, _susp_offset,
      _susp_length, _susp_sentences_count, _susp_words_count, _susp_doc_topic, _src_doc, _src_offset, _src_length, _src_sentences_count, _src_words_count, _src_doc_topic): #OK
      """Add a new case to the corpus"""

      #TODO validate all input data

      result = False

      self.remove_case(_case_id)
      self.add_case(_problem_type, _extension, _description, _plag_type, _summary, _auto_summary,
         _original_corpus, _original_corpus_id, _generated_by, _generator_name, _domain, _document_type, _topic_match, _paraphrase_composition, _lenght, _susp_doc, _susp_offset,
         _susp_length, _susp_sentences_count, _susp_words_count, _susp_doc_topic, _src_doc, _src_offset, _src_length, _src_sentences_count, _src_words_count, _src_doc_topic, _case_id)

      # update result
      result = True

      # update corpus info
      self.__update_corpus_info()

      return _case_id


   # auxiliar & private methods
   def __update_corpus_info(self):
      """Update corpus information such as modification date and so on..."""

      #Count total cases.
      tmp_cases = self.__root_node.getElementsByTagName('case')
      total_cases = len(tmp_cases)
      self.__root_node.setAttribute('total_cases', str(total_cases))

      #Count total true cases.
      case = {}
      total_true_cases = 0
      for item in tmp_cases:
         case['plag_type'] = item.getAttribute('plag_type')
         if case['plag_type'] != "none":
            total_true_cases += 1
      self.__root_node.setAttribute('total_true_cases', str(total_true_cases))

      #Count total annotations.
      tmp_annotations = self.__root_node.getElementsByTagName('annotation')
      total_annotations = len(tmp_annotations)
      self.__root_node.setAttribute('total_annotations', str(total_annotations))

      #Count total true cases.
      annotation = {}
      total_true_annotations = 0
      for item in tmp_annotations:
         annotation['is_paraphrase'] = item.getAttribute('is_paraphrase')
         if annotation['is_paraphrase'] == "True":
            total_true_annotations += 1
      self.__root_node.setAttribute('total_true_annotations', str(total_true_annotations))

      #Write calculated data to XML.
      self.write_xml()

      return
      
   def __human_readable_parse(self):
      """Parse the writed xml and rewrite it in a human readable form."""
      
      xml_file = open(self.__xml_path).read() #open de xml
      
      #Adding four whitespace by level of deepness
      xml_file = re.sub('>\s*<cases>', '>\n    <cases>',xml_file)
      xml_file = re.sub(r'>\s*</cases>', '>\n    </cases>',xml_file)
      xml_file = re.sub(r'>\s*<group', '>\n        <group',xml_file)
      xml_file = re.sub(r'>\s*</group>', '>\n        </group>',xml_file)
      xml_file = re.sub(r'>\s*<case ', '>\n            <case ',xml_file)
      xml_file = re.sub(r'>\s*</case>', '>\n            </case>',xml_file)
      xml_file = re.sub(r'>\s*<susp_snippet', '>\n                <susp_snippet',xml_file)
      xml_file = re.sub(r'>\s*<src_snippet', '>\n                <src_snippet',xml_file)
      xml_file = re.sub(r'>\s*<annotation', '>\n                <annotation',xml_file)
      xml_file = re.sub(r'>\s*</annotation>', '>\n                </annotation>',xml_file)
      xml_file = re.sub(r'>\s*<phenomenon', '>\n                    <phenomenon',xml_file)
      xml_file = re.sub(r'>\s*<susp_chunk', '>\n                    <susp_chunk',xml_file)
      xml_file = re.sub(r'>\s*<src_chunk', '>\n                    <src_chunk',xml_file)
      
      new_xml_file = open(self.__xml_path,'w')
      new_xml_file.write(xml_file)
      new_xml_file.close()

   def remove_case(self, _case_id):
      """Remove a case from XML"""

      # locate target case
      tmp_cases = self.__root_node.getElementsByTagName('case')
      for item in tmp_cases:
         if item.getAttribute('id') == str(_case_id):
            item.parentNode.removeChild(item)

            #~ if len(item.parentNode.childNodes) == 1:
               #~ item.parentNode.parentNode.removeChild(item.parentNode)
            #~ else:

            return

