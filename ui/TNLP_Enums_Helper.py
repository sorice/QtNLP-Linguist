#!/usr/bin/python
# -*- coding: utf-8 -*-

# Define plag types and associated resource
# structure
#    plag_type: (url of the associated resource alias, associated RGB color)

plag_types = {
   "none": (":/plag_type/pt_white", "#ffffff"),
   "literal": (":/plag_type/pt_red", "#ff0000"),
   "paraphrastic": (":/plag_type/pt_blue", "#0000ff"),
   "interlingual": (":/plag_type/pt_yellow", "#ffff00"),
   "bad_quotation": (":/plag_type/pt_orange", "#ff8000"),
   "copyleft": (":/plag_type/pt_green", "#00ff00"),
   "good_quotation": (":/plag_type/pt_green", "#00ff00"),
}

# Define paraphrase types used in annotations
paraphrase_types = [
   "inflectional changes",
   "modal-verb changes",
   "derivational changes",
   "lexicon format changes",
   "spelling changes",
   "same-polarity substitutions",
   "synthetic/analytic substitutions",
   "opposite-polarity substitutions",
   "converse substitutions",
   "diathesis alternations",
   "negation switching",
   "ellipsis",
   "coordination changes",
   "subordination-and-nesting",
   "discourse format changes",
   "punctuation changes",
   "direct/indirect-style alternations",
   "sentence-modality changes",
   "syntax/discourse-structure",
   "semantics-based changes",
   "change-of-order",
   "addition/deletion",
   "identical",
   "entailment",
   "non-paraphrase"
]

# Define phenomenom types used in annotations
phenomenom_types = [
   "similarity",
   "translation"
]

# Define text extension used in corpus
text_extension = [
   "paragraph",
   "sentence"
]

# Define text domain used in corpus
text_domain = [
   "computing",
   "informatic"
]

# Define text domain used in corpus
document_type = [
   "scientific paper",
   "book",
   "web page"
]

# Define src and susp doc topics. This list must be designed before compile QtNLP
document_topic = [
   "Data Base",
   "Software Engineering",
   "Software Test",
   "Artificial Intelligence"
]

