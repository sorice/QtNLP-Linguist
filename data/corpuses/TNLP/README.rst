.. _TNLP_corpus:

Sobre TNLP corpus
==================

El TNLP.xml es un formato de XML elaborado de forma genérica para la construcción de corpus lingüísticos re-utilizables para entrenar y probar algoritmos o soluciones computacionales de problemas del área del Procesamiento de los Lenguajes Naturales. Su característica fundamental es ser usado en problemas que requieran una lista de casos conformados por dos partes, y anotaciones para cada caso que permitan verificar una propiedad entre estas dos partes.

El ejemplo que verán a continuación se corresponde con el corpus para detectar similaridad semántica en textos compuestos por más de una oración, o sea fragmentos de textos siempre mayores a una oración.

TNLP contiene 300 casos elaborados a partir de Wikipedia en español, con términos exclusivamente sobre computación.

El corpus está disponible totalmente para investigaciones en:
	http://TNLP.reduc.edu.cu/corpus/es/computational-paraphrase-corpus-download

Un análisis sobre el proceso de diseño y construcción del corpus bien detallado puede ser leído en el artículo **Spanish Corpus for Paraphrase Similarity and Text Re-Use Detection**.:cite:`Meneses-Abad2015`

Folder Contents
================

- **README.rst** 	→ The readme file
- **TNLP.xml**	 	→ The TNLP corpus
- **src** 		→ Plagiarism suspicious folder colection
- **susp**	 	→ Plagiarism source folder colection

Formato del Corpus
===================

Código Fuente XML
-------------------

.. highlight:: xml
   :linenothreshold: 2

.. literalinclude:: TNLP.xml
   :language: xml
   :lines: 1-24

Descripción del XML
----------------------

El formato del corpus es un XML, más los textos a los cuales se hacen referencia.

Encabezado
^^^^^^^^^^^^^^^^^^^^

Las líneas **[1]** y **[2]** se corresponden con el inicio del formato XML y el fichero DTD que verifica o valida las especificaciones para cada etiqueta.

En la línea **[3]** se encuentra la etiqueta *corpus* y dentro de ella todos los atributos genéricos del corpus. En el caso del TNLP para similaridad de fragmentos parafraseados encontramos:
	* **name** 		→ nombre del corpus
	* **version** 		→ versión 
	* **lang**		→ idioma o lenguaje natural de los casos del corpus
	* **total_cases**	→ total de casos
	* **total_true_cases** 	→ casos veradaderos
	* **total_annotations**	→ total de anotaciones hechas a los casos
	* **total_true_annotations** → anotaciones verdaderas con respecto al fenómeno subyacente entre pares
	* **license**		→ licencia bajo la cual se libera el corpus
	* **copyright**		→ tipo de copyright
	* **owners**		→ poseedores de los derechos patrimoniales
	* **authors**		→ autores
	* **country**		→ en qué país se elaboró
	* **creation_date**	→ fecha de creación del corpus
	* **last_modification_date** → fecha de la última anotación registrada
	* **xmlns** 		→ identificador utilizado en XML para asegurar uniformidad

Casos
^^^^^^^^^^^^^^^^^^^^^^^

de la línea **[4]** a la **[9]** se describen los **casos** **[4]** *<cases*. Las etiquetas usadas son: **[5]** *<case_pair*, caso; **[6]** *<snippet_1* y **[7]** *<snippet_2*, se corresponden con la descripción de los fragmentos de texto considerados como pares. 

Atributos de la **lista de casos** o *<cases*:
	* **NLP_problem_type**	→ tipo de problema NLP (puede ser similaridad, traducción, etc)
	* **text_extension**	→ tamaño del texto (puede ser párrafo, oración, fragmento, etc)
Atributos de los **pares de casos** o *<case_pair*:
	* **id**			→ identificador único del caso
	* **case_pair_description**	→ descripción
	* **plag_type**			→ en el caso de TNLP describe tipo de plagio
	* **annotator_summary**		→ resumen del caso hecho por el anotador
	* **automatic_summary**		→ resumen del caso hecho por un PC, Ej.: Bag of Words, etc.
	* **original_corpus**		→ nombre del corpus original de donde vinieron los textos del caso
	* **original_corpus_id**	→ id del caso en su corpus original
Atributos de los **fragmentos** o *<snippet_#*:
	* **susp_doc**			→ documento sospechoso de plagio
	* **snippet_offset**		→ posición en el texto en la que comienza el fragmento
	* **snippet_length**		→ tamaño del fragmento (se utiliza para calcular la posición final)
	* **src_doc**			→ documento fuente de plagio
	* **snippet_src_offset**		→ posición en el texto fuente en la que comienza el fragmento
	* **snippet_src_length**		→ tamaño del fragmento fuente (se utiliza para calcular la posición final)

Anotaciones
^^^^^^^^^^^^^^^^^^^^^^^
 
De la línea **[9]** a la **[23]** se describen las **[9]** **anotaciones**, o *<annotations*, hechas por lingüistas o anotadores del corpus. Las etiquetas usadas son: **[10]** *<case_pair*, **[11]** *<phenomenon*, **[12]** *<chunk_1* y **[13]** *<chunk_2*. El **[11]** *<case_pair* se corresponde con **[5]**; *<phenomenon* particularmente es de TNLP para describir el fenómeno de la paráfrasis, **ver** :cite:`Barron-Cedeno2012a` , :cite:`Vila2013a` ; *<chunk_1* se refiere al trozo recortado del **fragmento** o *<snippet_1* que se está analizando, *<chunk_2* ibidem a *<chunck_1* pero para el *<snippet_2*.

Aunque no existen atributos para la etiqueta **anotaciones** o *<annotations*, esto permite, a los especialistas, agregar de NLP los atributos generales necesarios en función del para qué se utilizará el corpus creado.

Atributos de una **anotación** o *<annotation*:
	* **id**			→ identificador único para la anotación
	* **author**			→ autor de la anotación
	* **is_paraphrase**		→ atributo específico de TNLP para confirmar los casos positivos de paráfrasis
	* **human_validation**		→ si el caso ha sido confirmado por otro revisor humano
	* **artificial_validation**	→ si el caso ha sido verificado por el algoritmo baseline
	* **annotation_date**			→ fecha de la anotación
Atributos de la etiqueta *<phenomenon*:
	* **type**			→ tipo de paráfrasis, ver `Tipos de paráfrasis <#id4>`_
	* **projection**		→ impacto de la paráfrasis en el contexto :cite:`Vila2013`
Atributos de los **trozos** o *<chunks_#*:
	* **chunk_offset**		→ posición dentro del fragmento donde comienza el trozo analizado en la anotación 
		(*+<snippet_offset* daría su posición en el texto completo)
	* **chunk_length**		→ tamaño del pedazo anotado


Tipos de paráfrasis 
=======================

Tomado de :cite:`Vila2013a`

+---------------------------+-----------------------------------+-----------------------------------+
|          Class            |           Tag             	|             Meaning               |
+===========================+===================================+===================================+
|                           | mor_inflectional          	| inflectional changes              |
| Morphology-based changes  | mor_modal_verb            	| modal-verb changes                |
|                           | mor_derivational          	| derivational changes              |
+---------------------------+-----------------------------------+-----------------------------------+
|			    | lex_spelling_and_format (P4P)  	| spelling-and-format changes       |
|                           | lex_spelling (MSRP-A, WRPA-A)	| spelling changes		    |
|                           | lex_same_polarity         	| same-polarity substitutions       |
| Lexicon-based changes     | lex_synt_ana              	| synthetic/analytic substitutions  |	
|                           | lex_opposite_polarity     	| opposite-polarity substitutions   |
|                           | lex_inverse	              	| converse substitutions            |
+---------------------------+-----------------------------------+-----------------------------------+	
|                           | syn_diathesis             	| diathesis alternations            |
|                           | syn_negation              	| negation switching                |
| Syntax-based changes      | syn_ellipsis              	| ellipsis                          |
|                           | syn_coordination          	| coordination changes              |
|                           | syn_subord_nesting        	| subordination-and-nesting changes |
+---------------------------+-----------------------------------+-----------------------------------+
|                           | dis_punct_format (P4P)        	| punctuation-and-format changes    |  
|  			    | dis_punctuation (MSRP-A, WRPA-A)	| punctuation changes	            |
| Discourse-based changes   | dis_direct_indirect      	 	| direct/indirect-style alternations|
|                           | dis_sent_modality         	| sentence-modality changes         |
|                           | syn_dis_structure         	| syntax/discourse-structure changes|
+---------------------------+-----------------------------------+-----------------------------------+
| Semantics-based changes   | semantic                  	| semantics-based changes           |
+---------------------------+-----------------------------------+-----------------------------------+  
|                           | format (MSRP-A, WRPA-A)           | change of format                  |
| Miscellaneous changes     | order         			| change of order                   |
|			    | addition_deletion 		| addition/deletion		    |
+---------------------------+-----------------------------------+-----------------------------------+
| 	                    | identical                 	| identical                         |
| Paraphrase extremes       | entailment (MSRP-A, WRPA-A)       | entailment                        |
|			    | non_paraphrases			| non-paraphrase		    |
+---------------------------+-----------------------------------+-----------------------------------+  

Referencias
============

.. bibliography:: ../../../doc/references.bib
  :style: plain
  :list: enumerated
  :enumtype: arabic