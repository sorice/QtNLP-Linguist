.. _TNLP_corpus:

Sobre TNLP corpus
==================

El TNLP.xml es un formato de XML construido de forma bastante genérica para el uso en corpus lingüísticos que se utilizan para elaborar soluciones computacionales a problemas del Procesamiento de Lenguajes Naturales. Su característica fundamental es ser usado en problemas que requieran casos que contengan dos partes, y anotaciones para verificar una propiedad entre estas dos partes.

El ejemplo que verán a continuación se corresponde con el corpus para detectar similaridad semántica en textos compuestos por más de una oración, o sea fragmentos de textos siempre mayores a una oración.

TNLP contiene 300 casos elaborados a partir de Wikipedia en español, con términos absolutamente sobre computación.

El corpus está disponible totalmente para investigaciones en:
	http://TNLP.reduc.edu.cu/corpus/es/computational-paraphrase-corpus-download

[1] paper por escribir.

Folder Contents
================

- The readme file		TNLP/README.rst
- The TNLP corpus		TNLP.xml
- Suspicious folder colection	/src
- Source folder colection	/susp

Formato
========

[1]<?xml version="1.0" encoding="utf-8"?>

[2]<!-- <!DOCTYPE report SYSTEM "TNLP.dtd"> -->

[3]<corpus name="TNLP" version="0.2" lang="es" total_cases="1" total_true_cases="1" total_annotations="2" total_true_annotations="1" license="Creative Commons 3.0 Author Attribution Share Alike Non-Commercial Use" copyright="copyleft" owners="uclv,uc" authors="abel,leonel" country="Cuba" creation_date="Fry Jul 25 22:34:54 2014" last_modification_date="Thu Jul 31 23:48:06 2014" xmlns = "http://tnlp.github.com">

[4]    <cases NLP_problem_type="similarity" text_extension="paragraph">
[5]        <case_pair id="006" case_pair_description="" plag_type="paraphrase" annotator_summary="magna aliquyam erat" automatic_summary="" original_corpus="PAN-PC-12" original_corpus_id="unknown"/>
[6]            <snippet_1 susp_doc="susp/susp-doc00539" snippet_offset="966" snippet_length="416"/>
[7]            <snippet_2 src_doc="src/src-doc01529" snippet_src_offset="827" snippet_src_length="443"/>
[8]    </cases>

[9]   <annotations>
[10]        <case_pair id="006">
[11]            <annotation id="1" author="abelm" is_paraphrase="True" human_validation="None" artificial_validation="True" date="2015/02/14">
[12]                <phenomenon type="lex_same_polarity" projection="local"/>
[13]                <chunk_1 chunk_offset="30" chunk_length="47"/>
[14]                <chunk_2 chunk_src_offset="14" chunk_src_length="30"/>
[15]            </annotation>
[16]            <annotation id="2" author="abelm" is_paraphrase="False" human_validation="True" artificial_validation="True" annotation_date="2015/02/15">
[17]                <phenomenon type="None" projection="None"/>
[18]                <chunk_1 chunk_offset="18" chunk_length="8"/>
[19]                <chunk_2 chunk_src_offset="18" chunk_src_length="6"/>
[20]            </annotation>
[21]        </case_pair>
[22]   </annotations>
[23]</corpus>

El formato del corpus es un XML.

Las líneas [1] y [2] se corresponden con el inicio del formato XML y el fichero DTD que verifica o valida las especificaciones para cada etiqueta.

En la línea [3] se encuentra la etiqueta 'corpus' y dentro de ella todos los atributos genéricos del corpus. En el caso del TNLP para similaridad de fragmentos parafraseados encontramos:
	* name		-> nombre del corpus
	* version 	-> versión 
	* lang		-> idioma o lenguaje natural de los casos del corpus
	* total_cases	-> total de casos
	* total_true_cases-> casos veradaderos
	* total_annotations-> total de anotaciones hechas a los casos
	* total_true_annotations-> anotaciones verdaderas con respecto al fenómeno subyacente entre pares
	* license	-> licencia bajo la cual se libera el corpus
	* copyright	-> tipo de copyright
	* owners	-> poseedores de los derechos patrimoniales
	* authors	-> autores
	* country	-> en qué país se elaboró
	* creation_date	-> fecha de creación del corpus
	* last_modification_date-> fecha de la última anotación registrada
	* xmlns 	-> identificador utilizado en XML para asegurar uniformidad

de la línea [4] a la [8] se describen los [4]casos. Las etiquetas usadas son: [5] case_pair, [6] snippet_1 y [7] snippet 2. Los dos últimos se corresponden con la descripción de los fragmentos de texto considerados como pares. 

Atributos de la lista de casos:
	* NLP_problem_type	-> tipo de problema NLP (puede ser similaridad, traducción, etc)
	* text_extension	-> tamaño del texto (puede ser párrafo, oración, fragmento, etc)
Atributos de los pares de casos:
	* id			-> identificador único del caso
	* case_pair_description	-> descripción
	* plag_type		-> en el caso de TNLP describe tipo de plagio
	* annotator_summary	-> resumen del caso hecho por el anotador
	* automatic_summary	-> resumen del caso hecho por un PC, Ej.: Bag of Words, etc.
	* original_corpus	-> corpus original de donde vinieron los textos del caso
	* original_corpus_id	-> id del caso en su corpus original
Atributos del fragmento:
	* susp_doc		-> documento sospechoso de plagio
	* snippet_offset	-> posición en el texto en la que comienza el fragmento
	* snippet_length	-> tamaño del fragmento (se utiliza para calcular la posición final)
 
De la línea [9] a la [23] se describen las [9]anotaciones hechas por lingüistas o anotadores del corpus. Las etiquetas usadas son: [10] case_pair, [11] phenomenon, [12] chunk_1 y [13] chunk_2. El case_pair se corresponde con [5]; phenomenon particularmente es de TNLP para describir el fenómeno de la paráfrasis (similar a la del corpus P4P); chunk_1 se refiere al trozo recortado del fragmento o snippet_1 que se está analizando, chunk_2 idem a chunck_1 pero para el snippet_2.

Aunque no existen atributos para la etiqueta anotaciones, esto permite agregar para los especialistas de NLP los necesarios en función de para que se utilizará su corpus.

Atributos de una anotación:
	* id			-> identificador único para la anotación
	* author		-> autor de la anotación
	* is_paraphrase		-> atributo específico de TNLP para confirmar los casos positivos de paráfrasis
	* human_validation	-> si el caso ha sido confirmado por otro revisor humano
	* artificial_validation	-> si el caso ha sido verificado por el algoritmo baseline
	* date			-> fecha de la anotación
Atributos de la etiqueta 'phenomenon':
	* type			-> tipo de paráfrasis ver descripción de P4P
	* projection		-> impacto de la paráfrasis en el contexto, ver tesis de doctorado de Marta Vila
Atributos de los **trozos** o *chunks*:
	* chunk_offset		-> caracter dentro del fragmento donde comienza el pedazo analizado en la anotación (+ snippet_offset daría su posición en el texto)
	* chunk_length		-> tamaño del pedazo anotado

Tipos de paráfrasis (tomado de README del P4P):

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

.. Note: Ponerla en formato bibtext.
