#!/usr/bin/python
# -*- coding: utf-8 -*-

# Define plag types and associated resource
# structure
#    plag_type: (url of the associated resource alias, associated RGB color)

plag_types = {
   "literal": (":/plag_type/pt_red", "#ff0000"),
   "paraphrastic": (":/plag_type/pt_blue", "#0000ff"),
   "interlingual": (":/plag_type/pt_yellow", "#ffff00"),
   "bad_quotation": (":/plag_type/pt_orange", "#ff8000"),
   "copyleft": (":/plag_type/pt_green", "#00ff00"),
   "good_quotation": (":/plag_type/pt_green", "#00ff00"),
}

# Define paraphrase types used in annotations
paraphrase_types = [
   "inflectional modal-verb",
   "derivational changes",
   "spelling-and-format",
   "same-polarity",
   "synthetic/analytic",
   "opposite-polarity",
   "converse",
   "diathesis alternations negation",
   "switching ellipsis coordination",
   "subordination-and-nesting",
   "punctuation-and-format",
   "punctuation",
   "direct/indirect-style",
   "sentence-modality",
   "syntax/discourse-structure",
   "semantics",
   "format/order",
   "addition/deletion",
   "identical entailment non-paraphrase"
]

# Define phenomenom types used in annotations
phenomenom_types = [
   "similarity",
   "translation"
]

# Define text extension used in corpus
text_extension = [
   "paragraph"
]
