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
