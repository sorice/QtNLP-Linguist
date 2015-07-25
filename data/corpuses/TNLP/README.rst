.. _TNLP_corpus:

Sobre TNLP corpus
==================

El **TNLP.xml** es un documento XML elaborado de forma genérica para la construcción de corpus lingüísticos re-utilizables para entrenar y probar algoritmos o soluciones computacionales de problemas del área del Procesamiento de los Lenguajes Naturales (NLP). Su característica fundamental es ser usado en problemas que requieran una lista de casos conformados por dos partes u objetos, y anotaciones para cada caso que permitan verificar una propiedad entre estas dos partes.

Esta guía muestra un ejemplo en particular, TNLP, un corpus para detectar similaridad semántica en textos compuestos por más de una oración, o sea fragmentos de textos siempre mayores a una oración.

TNLP contiene 300 casos elaborados a partir de Wikipedia en español, con términos exclusivamente sobre computación.

El corpus está disponible totalmente para investigaciones en:
	http://TNLP.reduc.edu.cu/corpus/es/computational-paraphrase-corpus-download

Un análisis sobre el proceso de diseño y construcción del corpus bien detallado puede ser leído en el artículo **Spanish Corpus for Paraphrase Similarity and Text Re-Use Detection**. :cite:`Meneses-Abad2015`

Folder Contents
================

- **README.rst** 	→ The readme file
- **TNLP.xml**	 	→ The TNLP corpus
- **src** 		→ Plagiarism suspicious folder colection
- **susp**	 	→ Plagiarism source folder colection

El formato del corpus es un XML. Y es acompañado por dos carpetas **susp** y **src** con los textos completos a los cuales se hacen referencia, similar a los corpus PAN-PC-09, PAN-PC-10 y PAN-PC-11. :cite:`Barron-Cedeno2010a`, :cite:`Barron-Cedeno2010c`, :cite:`Potthast2011a`

De los textos completos se extraen los fragmentos u objetos de análisis - párrafos, oraciones o segmentos - utilizando su posición en el texto y longitud. Este particular, a diferencia de algunos corpus que no incluyen los textos completos, se realiza en función de comparar la capacidad real que tienen los algoritmos de similaridad de extraer los fragmentos del caso correctamente. O sea que extraen el segmento anotado, y los umbrales de diferencia al inicio o al final. Dando al sistema TNLP y a los investigadores la capacidad de verificar la sensibilidad de algunas técnicas ante los bordes de los fragmentos. Así por ejemplo un fragmento podría comenzar de la siguiente forma *"habiendo comenzado el ..."*, y luego el fragmento detectado ser *"quiso decir Leonel habiendo..."*. Evidentemente el algoritmo ha agregado de la oración anterior un fragmento que puede conformar, en su totalidad, una construcción gramatical correcta o no. El manejo de estos umbrales de detección puede dar mayor información sobre el comportamiento de las técnicas NLP.

El **README.rst** se utiliza para generar el *README.html*.

Formato del Corpus
===================

Código Fuente XML
-------------------

.. highlight:: xml
   :linenothreshold: 2

.. literalinclude:: TNLP.xml
   :language: xml
   :lines: 1-17

Descripción del XML
----------------------

El formato del corpus es un XML.

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

De la línea **[4]** a la **[8]** se describen los **casos** **[4]** *<cases*. Las etiquetas usadas son: **[5]** *<group*, grupo de casos; **[6]** *<case*, caso; **[7]** *<sus_snippet* y **[8]** *<src_snippet*, se corresponden con la descripción de los fragmentos de texto considerados como pares. 

Atributos de la **lista de casos** o *<group*:
	* **NLP_problem_type**	→ tipo de problema NLP (puede ser similaridad, traducción, etc)
	* **text_extension**	→ tamaño del texto (puede ser párrafo, oración, fragmento, etc)
Atributos de **un caso** o *<case*:
	* **id**			→ identificador único del caso
	* **description**		→ descripción
	* **plag_type**			→ en el caso de TNLP describe tipo de plagio
	* **annotator_summary**		→ resumen del caso hecho por el anotador
	* **automatic_summary**		→ resumen del caso hecho por un PC, Ej.: Bag of Words, etc.
	* **original_corpus**		→ nombre del corpus original de donde vinieron los textos del caso
	* **original_corpus_id**	→ id del caso en su corpus original
	* **generated_by**		→ identifica el mecanismo de generación: humano o automático.
	* **generator_name**		→ nombre del algoritmo o persona que generó el caso

Atributos de los **fragmentos** o *<xxx_snippet*:
	* **doc**			→ documento sospechoso o fuente de(l) plagio
	* **offset**			→ posición en el texto en la que comienza el fragmento
	* **length**			→ tamaño del fragmento (se utiliza para calcular la posición final)
	* **sentences_count**		→ número de oraciones del fragmento

Anotaciones
^^^^^^^^^^^^^^^^^^^^^^^
 
De la línea **[9]** a la **[12]** se describen las **[9]** **anotaciones**, o *<annotations*, hechas por lingüistas o anotadores del corpus. Las etiquetas usadas son: **[10]** *<phenomenon*, **[11]** *<susp_chunk* y **[12]** *<src_chunk*. *<phenomenon* particularmente es de P4P para describir el fenómeno de la paráfrasis, **ver** :cite:`Barron-Cedeno2012a` , :cite:`Vila2013a` ; *<susp_chunk* se refiere al trozo recortado del **fragmento** o *<susp_snippet* que se está analizando, *<src_chunk* ibidem a *<susp_chunck* pero para el *<src_snippet*.

Atributos de una **anotación** o *<annotation*:
	* **id**			→ identificador único para la anotación
	* **author**			→ autor de la anotación
	* **is_paraphrase**		→ atributo específico de TNLP para confirmar los casos positivos de paráfrasis
	* **validated_by_human_beings**	→ si el caso ha sido confirmado por otro revisor humano
	* **recognized_by_algorithms**	→ si el caso ha sido verificado por el algoritmo baseline
	* **algorithms_names**		→ nombres de algoritmos que han reconocido el caso correctamnte(este campo enlaza con el XML de cada algoritmo).
	* **annotation_date**			→ fecha de la anotación

Atributos de la etiqueta *<phenomenon*:
	* **type**			→ tipo de paráfrasis, ver `Tipos de paráfrasis <#id5>`_
	* **projection**		→ impacto de la paráfrasis en el contexto :cite:`Vila2013`

Atributos de los **trozos** o *<xxx_chunks*:
	* **offset**			→ posición dentro del fragmento donde comienza el trozo analizado en la anotación 
		(*+<xxx_snippet.offset* daría su posición en el texto completo)
	* **length**			→ tamaño del pedazo anotado


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
  :cited: