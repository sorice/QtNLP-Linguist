.. _en_TNLP_corpus:

About TNLP
==================

**TNLP** is an annotated corpus of texts based on the XML format. It was developed in a generic way for the construction of multiple linguistic corpus, designed to be used as a resource to solve several problems of the ​​Natural Language Processing (NLP) area of knowleage. Mostly re-usable in the training and testing of algorithms. One of its key features is to contain the original text for the extraction of objects of study, similar to the PAN corpus texts. :cite:`Potthast2010a` This design can be used for problems requiring a list of cases made up of two parts or elements, and notes for each case in order to verify a property between these two parties.

.. Raw :: html

    <p><b> Example short: </b><I> description of a case. </I><br/></p>
    <blockquote><b> Problem NLP </b>: <I>semantic similarity between two sentences. </I><br/>
    <b><tb/>Sentence 1 </b>: <I> ... compile the code in a non-standard PC, and get the executable.</I><br/>
    <b>Sentence 2 </b>: <I>... build a binary functions running on a processor assembly. </I> <br/>
    <b>Property </b>: <I> Paraphrase type </I> = <I> semantic. </I></blockquote>

This guide shows the design of the first linguistic corpus made based on TNLP structure: a corpus to detect semantic similarity in texts composed by more than one sentence.

TNLP contains 300 cases made of computing terms extracted from Spanish Wikipedia.

The corpus is available entirely for research:
    http://gpln.reduc.edu.cu/corpuses/es/computational-paraphrase-corpus-download

An analysis of the process of design and construction of very detailed corpus can be read in the article **Spanish Corpus for Paraphrase Similarity and Text Re-Use Detection**. :cite:`Meneses-Abad2015` if you use this corpus must reference `this <./README_EN.html#meneses-abad2015>`_ article.

Parts of Corpus
===================

- **README.rst**  → The readme file to construct this HTML.
- **TNLP.xml**    → The information and TNLP corpus cases.
- **Src**         → Plagiarism suspicious src folder colection.
- **Susp**        → Plagiarism source folder colection.
- **Pair.txt**    → List of documents Pairs With positive and false cases.

The format is an XML corpus. It is accompanied by two folders **susp** and **src** with the full texts to which reference is made, similar to the PAN-PC-09, PC-PAN-PAN-10 and PC-11 corpus. :cite:`Barron-Cedeno2010a`, :cite:`Barron-Cedeno2010c`, :cite:`Potthast2011a`

Using its position in the text and full text length fragments or objects of analysis (paragraphs, sentences or segments) are extracted. This particular corpus unlike some that do not include the full texts, are made based on comparing the actual ability of similarity algorithms to extract fragments of the case correctly. So that extract annotated segment and difference thresholds at the beginning or end. TNLP system and giving researchers the ability to verify the sensitivity of some techniques to the edges of the fragments. For example a fragment could begin as follows *"having begun ..."*, then the fragment to be detected *"meant Leonel having ..."*. Clearly the algorithm has been added in the preceding sentence fragment that can be well formed, in whole, or not correct grammatical construction. Managing these detection thresholds can provide more information about the behavior of NLP techniques.

The **README.rst** is used to generate *README.html*.

Corpus format
===================

XML Source Code 
-------------------

.. highlight :: xml
   :linenothreshold: 2

.. literalinclude:: TNLP-base.xml
   :language: xml
   :lines: 1-17

XML Description 
----------------------

The format is an XML corpus.

Header
^^^^^^^^^^^^^^^^^^^^

Lines **[1]** and **[2]** correspond with the beginning of the DTD XML file format and verifying or validating the specifications for each label.

In line **[3]** is the label *corpus* and within all generic attributes of the corpus. In the case of TNLP for similarity paraphrased fragments are:
    * **name**  → name of the corpus
    * **version**  → version
    * **lang**  → language or natural language corpus cases
    * **total_cases** → total cases
    * **total_true_cases** → total true cases
    * **total_annotations** →  total of annotations to cases
    * **total_true_annotations** → true annotations with respect to the underlying phenomenon peer
    * **license** → license under which the body is released
    * **copyright** → copyright type
    * **owners** → owners of the economic rights
    * **authors** →  authors
    * **country** → in which country was elaborated
    * **creation_date**  → creation date of the corpus
    * **last_modification_date** → date of the last entry recorded
    * **xmlns** →  identifier used in XML to ensure uniformity

Cases
^^^^^^^^^^^^^^^^^^^^^^^

From Line **[4]** to **[8]** described **cases** , **[4]** *<cases*. The labels used are: **[5]** *<group* group of cases; **[6]** *<case* case; **[7]** *<sus_snippet* and **[8]** *<src_snippet*, they correspond to the description of the text fragments considered peers.

Attributes of the **case list** or *<group*:
    * **NLP_problem_type**    → type of NLP problem (can be similarity, translation, etc.)
    * **text_extension**      →  text size (may be paragraph, sentence, passage, etc)
Attributes of a **case** or *<case*:
    * **id** → unique identifier of a case
    * **description**         → Description
    * **plag_type**           → in case of plagiarism described TNLP
    * **annotator_summary**   → summary of the case by the scorer
    * **automatic_summary**   → summary of the case made by a PC, eg .: Bag of Words, etc.
    * **original_corpus**     → name of the original corpus of text case which came from
    * **original_corpus_id**  → id of the case in the original corpus
    * **generated_by**        → identifies generating mechanism: human or automatic.
    * **generator_name**      → name of the algorithm or person that generated the event
    * **domain**              → area of knowledge of the content of susp case doc.
    * **document_type**       → type of document: Scientific, book, story, conversation, ...

Attributes **fragments** o *<xxx_snippet*:
    * **doc** → suspect document or source (l) plagiarism
    * **offset** →  position in the text where the fragment starts
    * **length** →  fragment size (used to calculate the final position)
    * **centences_count**  → number of sentences of the fragment

Annotations
^^^^^^^^^^^^^^^^^^^^^^^
 
From line **[9]** to **[12]** describes the **[9]** **annotations** , or *<annotations*, made by linguists or scoring the corpus. The labels used are: **[10]** *<phenomenon*, **[11]** *<susp_chunk* and **[12]** *<src_chunk*. *<phenomenon* is particularly from P4P corpus, this describe the phenomenon of paraphrasing, **see**  :cite:`Barron-Cedeno2012a`, :cite:`Vila2013a`; *<susp_chunk* refers to the cut piece of **fragment** o *<susp_snippet* being analyzed, *<src_chunk* same as *<susp_chunck* but for the *<src_snippet*.

Attributes of an **annotation** or *<annotation*:
    * **id**              → unique identifier for the entry
    * **author**          →  author annotation
    * **is_paraphrase**   →  specific TNLP attribute to confirm positive cases of paraphrases
    * **validated_by_human_beings**  → if the case has been confirmed by another human reviewer
    * **recognized_by_algorithms**  → if the application has been verified by the baseline algorithm
    * **algorithms_names** →  names of algorithms that have correctly recognized the case (this field link to the XML of each algorithm).
    * **annotation_date** →  date of entry

Tag *<phenomenon* attributes:
    * **type**       → type of paraphrase, see `Types of paraphrases <#id8>`_
    * **projection** → impact of paraphrasing in context :cite:`Vila2013`

**Chunks** attributes or *<xxx_chunks*:
    * **offset** →  position of the first character of the chunk within the analyzed fragment in the annotation.
        (*+<xxx_snippet.offset* give its position on the full text)
    * **length**  → annotated chunk size


Types of paraphrases
=======================

Versioning from :cite:`Vila2013a`.

+---------------------------+-------------------------------------+-------------------------------------+
|          Class            |              Tag                    |             Meaning                 |
+===========================+=====================================+=====================================+
|                           | - mor_inflectional                  | - inflectional changes              |
| Morphology-based changes  | - mor_modal_verb                    | - modal-verb changes                |
|                           | - mor_derivational                  | - derivational changes              |
+---------------------------+-------------------------------------+-------------------------------------+
|                           | - lex_format (P4P)                  | - lexicon format changes            |
|                           | - lex_spelling (MSRP-A, WRPA-A)     | - spelling changes                  |
|                           | - lex_same_polarity                 | - same-polarity substitutions       |
| Lexicon-based changes     | - lex_synt_ana                      | - synthetic/analytic substitutions  |
|                           | - lex_opposite_polarity             | - opposite-polarity substitutions   |
|                           | - lex_inverse                       | - converse substitutions            |
+---------------------------+-------------------------------------+-------------------------------------+
|                           | - syn_diathesis                     | - diathesis alternations            |
|                           | - syn_negation                      | - negation switching                |
| Syntax-based changes      | - syn_ellipsis                      | - ellipsis                          |
|                           | - syn_coordination                  | - coordination changes              |
|                           | - syn_subord_nesting                | - subordination-and-nesting changes |
+---------------------------+-------------------------------------+-------------------------------------+
|                           | - dis_punct_format (P4P)            | - discourse format changes          |  
|                           | - dis_punctuation (MSRP-A, WRPA-A)  | - punctuation changes               |
| Discourse-based changes   | - dis_direct_indirect               | - direct/indirect-style alternations|
|                           | - dis_sent_modality                 | - sentence-modality changes         |
|                           | - syn_dis_structure                 | - syntax/discourse-structure changes|
+---------------------------+-------------------------------------+-------------------------------------+
| Semantics-based changes   | - semantic                          | - semantics-based changes           |
+---------------------------+-------------------------------------+-------------------------------------+
| Miscellaneous changes     | - order                             | - change of order                   |
|                           | - addition_deletion                 | - addition/deletion                 |
+---------------------------+-------------------------------------+-------------------------------------+
|                           | - identical                         | - identical                         |
| Paraphrase extremes       | - entailment (MSRP-A, WRPA-A)       | - entailment                        |
|                           | - non_paraphrases                   | - non-paraphrase                    |
+---------------------------+-------------------------------------+-------------------------------------+

References
============

.. bibliography:: ../../../doc/references.bib 
  :style: plain
  :cited:
