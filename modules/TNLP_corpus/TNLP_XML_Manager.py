#!/usr/bin/env python
# -*- coding: utf-8-sig -*-

from xml.dom import minidom

class TNLP_XML_Manager:
   """Helper to manage the TNLP.xml information file"""

   def __init__(self):
      """Init global attributes"""

      self.__parsed = False
      self.__xml_document = None
      self.__root_node = None
      self.__cases_node = None


   # public methods
   def parse_xml(self, xml_file):
      """Parse the indicated xml_file"""

      result = False
      self.__xml_document = minidom.parse(xml_file)
      # TODO: Validate parse(...) result
      # if no errors
      self.__root_node = self.__xml_document.documentElement
      # refer to this as self.__cases_node[0] because there is only one 'cases' node
      self.__cases_node = self.__root_node.getElementsByTagName('cases')
      # refer to this as self.__annotations_node[0] because there is only one 'annotations' node
      self.__annotations_node = self.__root_node.getElementsByTagName('annotations')
      result = True
      self.__parsed = True

      return result


   def get_corpus_info(self):
      """Return the root element info in a dictionary"""

      corpus = {}
      corpus['name'] = self.__root_node.attributes['name'].value
      corpus['version'] = self.__root_node.attributes['version'].value
      corpus['lang'] = self.__root_node.attributes['lang'].value
      corpus['total_cases'] = self.__root_node.attributes['total_cases'].value
      corpus['total_true_cases'] = self.__root_node.attributes['total_true_cases'].value
      corpus['total_annotations'] = self.__root_node.attributes['total_annotations'].value
      corpus['total_true_annotations'] = self.__root_node.attributes['total_true_annotations'].value
      corpus['license'] = self.__root_node.attributes['license'].value
      corpus['copyright'] = self.__root_node.attributes['copyright'].value
      corpus['owners'] = self.__root_node.attributes['owners'].value
      corpus['authors'] = self.__root_node.attributes['authors'].value
      corpus['country'] = self.__root_node.attributes['country'].value
      corpus['creation_date'] = self.__root_node.attributes['creation_date'].value
      corpus['last_modification_date'] = self.__root_node.attributes['last_modification_date'].value
      corpus['xmlns'] = self.__root_node.attributes['xmlns'].value

      return corpus


   def get_total_cases(self):
      """Return how many cases exists in corpus"""

      if not self.__parsed:
         return None

      cases = self.__get_cases()
      return len(cases)


   def get_cases(self):
      """Retrun all cases"""

      cases = []

      tmp_cases = self.__get_cases()
      for item in tmp_cases:
         case = {}
         case['id'] = item.getAttribute('id')
         case['case_pair_description'] = item.getAttribute('case_pair_description')
         case['plag_type'] = item.getAttribute('plag_type')
         case['annotator_summary'] = item.getAttribute('annotator_summary')
         case['automatic_summary'] = item.getAttribute('automatic_summary')
         case['original_corpus'] = item.getAttribute('original_corpus')
         case['original_corpus_id'] = item.getAttribute('original_corpus_id')

         cases.append(case)

      return cases


   def get_case(self, case_id):
      """Return the case case_id"""

      if not self.__parsed:
         return None

      case = None

      tmp_cases = self.__get_cases()
      for item in tmp_cases:
         if item.hasAttribute('id') and item.getAttribute('id') == str(case_id):
            case = {}
            case['id'] = item.getAttribute('id')
            case['case_pair_description'] = item.getAttribute('case_pair_description')
            case['plag_type'] = item.getAttribute('plag_type')
            case['annotator_summary'] = item.getAttribute('annotator_summary')
            case['automatic_summary'] = item.getAttribute('automatic_summary')
            case['original_corpus'] = item.getAttribute('original_corpus')
            case['original_corpus_id'] = item.getAttribute('original_corpus_id')

      return case


   def get_annotations_of_case(self, case_id):
      """Return annotations corresponding to a case_pair"""

      annotations = []

      tmp_annotations = self.__get_annotations(case_id)

      # if there are no annotations
      if tmp_annotations == None:
         return annotations

      tmp_annotations = tmp_annotations.getElementsByTagName('annotation')
      for item in tmp_annotations:
         tmp = {}
         tmp['id'] = item.getAttribute('id')
         tmp['author'] = item.getAttribute('author')
         tmp['is_paraphrase'] = item.getAttribute('is_paraphrase')
         tmp['human_validation'] = item.getAttribute('human_validation')
         tmp['artificial_validation'] = item.getAttribute('artificial_validation')
         tmp['annotation_date'] = item.getAttribute('annotation_date')
         for i in item.childNodes:
            if i.nodeType == i.ELEMENT_NODE:
               if i.nodeName == 'phenomenon':
                  tmp['type'] = i.getAttribute('type')
                  tmp['projection'] = i.getAttribute('projection')
               elif i.nodeName == 'chunk_1':
                  tmp['chunk_offset'] = i.getAttribute('chunk_offset')
                  tmp['chunk_length'] = i.getAttribute('chunk_length')
               elif i.nodeName == 'chunk_2':
                  tmp['chunk_src_offset'] = i.getAttribute('chunk_src_offset')
                  tmp['chunk_src_length'] = i.getAttribute('chunk_src_length')

         annotations.append(tmp)

      return annotations


   def add_case(self, _problem_type, _extension, _pair_description, _plag_type,
      _summary, _auto_summary, _original_corpus, _original_corpus_id, _susp_doc,
      _susp_offset, _susp_length, _src_doc, _src_offset, _src_length):
      """Add a new case to the corpus"""

      #TODO validate all input data

      result = False

      # select the correct group for the case
      groups = self.__cases_node[0].getElementsByTagName('group')
      for group in groups:
        if group.hasAttribute('NLP_problem_type') and group.getAttribute('NLP_problem_type') == str(_problem_type):
           if group.hasAttribute('text_extension') and group.getAttribute('text_extension') == str(_extension):
               # create new node and append it to current group
               # case_pair node
               case = self.__xml_document.createElement('case_pair')
               case.setAttribute('id', str(len(self.__cases_node[0].getElementsByTagName('case_pair')) + 1))
               case.setAttribute('case_pair_description', _pair_description)
               case.setAttribute('plag_type', _plag_type)
               case.setAttribute('annotator_summary', _summary)
               case.setAttribute('automatic_summary', _auto_summary)
               case.setAttribute('original_corpus', _original_corpus)
               case.setAttribute('original_corpus_id', _original_corpus_id)
               # snippet_1 node
               snippet_1 = self.__xml_document.createElement('snippet_1')
               snippet_1.setAttribute('susp_doc', _susp_doc)
               snippet_1.setAttribute('snippet_offset', str(_susp_offset))
               snippet_1.setAttribute('snippet_length', str(_susp_length))
               case.appendChild(snippet_1)
               # snippet_2 node
               snippet_2 = self.__xml_document.createElement('snippet_2')
               snippet_2.setAttribute('src_doc', _src_doc)
               snippet_2.setAttribute('snippet_src_offset', str(_src_offset))
               snippet_2.setAttribute('snippet_src_length', str(_src_length))
               case.appendChild(snippet_2)
               # add case to group
               group.appendChild(case)

               # update result
               result = True
               break

      return result


   def add_annotation(self, _pair_id, _author, _is_paraphrase, _human_val, _artificial_val,
      _date, _type, _projection, _chunk_offset, _chunk_length, _chunk_src_offset, _chunk_src_length):
      """Add an annotation to a case"""

      #TODO validate all input data

      result = False

      # create new node and append it to current case
      # annotation node
      annotation = self.__xml_document.createElement('annotation')
      annotation.setAttribute('id', str(len(self.__annotations_node[0].getElementsByTagName('annotation')) + 1))
      annotation.setAttribute('author', _author)
      annotation.setAttribute('is_paraphrase', _is_paraphrase)
      annotation.setAttribute('human_validation', _human_val)
      annotation.setAttribute('artificial_validation', _artificial_val)
      annotation.setAttribute('annotation_date', _date)
      # phenomenon node
      phenomenon = self.__xml_document.createElement('phenomenon')
      phenomenon.setAttribute('type', _type)
      phenomenon.setAttribute('projection', _projection)
      annotation.appendChild(phenomenon)
      # chunk_1 node
      chunk_1 = self.__xml_document.createElement('chunk_1')
      chunk_1.setAttribute('chunk_offset', _chunk_offset)
      chunk_1.setAttribute('chunk_length', _chunk_length)
      annotation.appendChild(chunk_1)
      # chunk_2 node
      chunk_2 = self.__xml_document.createElement('chunk_2')
      chunk_2.setAttribute('chunk_src_offset', _chunk_src_offset)
      chunk_2.setAttribute('chunk_src_length', _chunk_src_length)
      annotation.appendChild(chunk_2)

      # select the correct case for the annotation
      cases = self.__annotations_node[0].getElementsByTagName('case_pair')
      for case in cases:
         if case.hasAttribute('id') and case.getAttribute('id') == str(_pair_id):
            # add annotation to case
            case.appendChild(annotation)

            # update result
            result = True
            break

      # if case_pair not found create it an add it to annotations
      if not result:
         case_pair = self.__xml_document.createElement('case_pair')
         case_pair.setAttribute('id', str(_pair_id))
         # add annotation to case_pair
         case_pair.appendChild(annotation)
         # add case_pair to annotations node
         self.__annotations_node[0].appendChild(case_pair)

         # update result
         result = True

      return result


   def write_xml(self, _xml_file):
      """Write data to _xml_file"""

      from PyQt4.QtCore import QFile, QTextStream
      from PyQt4.QtXml import QDomDocument
      f = QFile(_xml_file)
      f.open(QFile.WriteOnly | QFile.Text)
      out = QTextStream(f)
      domDocument = QDomDocument()
      domDocument.setContent(self.__xml_document.toxml())
      domDocument.save(out, 3)


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
   a.parse_xml('/home/lordford/TNLP/TNLP.xml')

   print "CORPUS INFO: "
   print a.get_corpus_info()

   print "\nTOTAL CASES: "
   print a.get_total_cases()

   print "\nALL CASES: "
   print a.get_cases()

   id = a.get_cases()[0]['id']
   print "\nCASE, id = " + str(id) + ": "
   print a.get_case(id)

   print "\nANNOTATIONS LENGTH, case = " + str(id) + ": "
   print len(a.get_annotations_of_case(id))
   print "\nANNOTATIONS, case = " + str(id) + ": "
   print a.get_annotations_of_case(id)

   print "\nADD CASE"
   print a.add_case("similarity","paragraph","desc","paraphrase","manual summary","auto summary","PAN_PC-15","unknown",
      'susp/susp-doc00547', '8', '20', 'src/src-doc01356', '0', '101')

   print "\nTOTAL CASES: "
   print a.get_total_cases()

   id = 3 #a.get_cases()[1]['id']
   print "\nADD ANNOTATION"
   print a.add_annotation(id, 'leonel', 'True', 'None', 'True', '2015-02-26', 'lex_same_polarity', 'local', '10', '55', '2', '100')

   print "\nANNOTATIONS LENGTH, case = " + str(id) + ": "
   print len(a.get_annotations_of_case(id))
   print "\nANNOTATIONS, case = " + str(id) + ": "
   print a.get_annotations_of_case(id)

   a.write_xml('/home/lordford/TNLP/out.xml')
