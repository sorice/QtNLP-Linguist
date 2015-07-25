
# Test Environment
if __name__ == "__main__":
   '''
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
   "PAN_PC-15","12345", 'human', 'abelm','susp/susp-doc00560', '15', '30', 'src/src-doc01360', '60', '101', '5', '6')

   print "\nCORPUS TOTAL CASES: "
   print a.get_corpus_total_cases()

   print "\nADD ANNOTATION"
   print a.add_annotation(id, 'leonelsv', 'True', 'None', 'True', 'ngram-1',
   '2015-02-26', 'coordination', 'local', '10', '55', '2', '120')

   print "\nANNOTATIONS LENGTH, case = " + str(id) + ": "
   print len(a.get_annotations_of_case(id))
   print "\nANNOTATIONS, case = " + str(id) + ": "
   print a.get_annotations_of_case(id)

   a.write_xml()
   '''
   pass
