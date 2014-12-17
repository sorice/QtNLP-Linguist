.. _EScorpus_modules:

Plugins
*****************

|EScorpus| es un sistema basado en módulos o plugins. En esta sección mostramos a través del modelo de las 3 capas cómo está desarrollada esta aplicación informática. En la sección final usted también podrá encontrar la documentación dividida por módulos.

	* :ref:`ToNgueLP Corpus Parser <ToNgueLP_corpus_parser_module>`

View Level
================

* Prototipo y código fuente  en Qt de la :ref:`Vista Principal <QtToNgueLP_module_principal>`.
* Prototipo y código fuente en Qt de la :ref:`Vista de Comparación <QtToNgueLP_module_matching>`.
* Prototipo y código fuente en Qt de la :ref:`Vista de Diccionarios <QtToNgueLP_module_dicts>`.

Control Level
================

Breve lista de los procesos que ocurren en |EScorpus|:

1. **Preprocesamiento:** Convertir todos los docs al formato ZZZdoc.xml.
2. **Estandarización** de salidas de algoritmos: Convertir carpeta out en un único XML.
3. **Comparación de XMLs:** *algorithmXXX-plag-report.xml* vs *EScorpusYYY-plag-cases-corpus.xml*.
4. **Actualizar XMLs:** Escribir datos de la comparación en el *algorithmXXX-plag-report.xml*.

:Ver más: `Lista completa de Funcionalidades <../doc/features/features.html>`_

Data Model
==============

|EScorpus| no usa gestor de BD relacional o no relacional. La persistencia de sus datos se garantizan a través de XMLs diseñados para cada función de la aplicación.

* `XML del Corpus de casos de Plagio  <../_static/01_Ingenieria/1.2_Arquitectura_y_Design/EScorpusYYY-plag-cases-corpus.html>`_
	XML propio de |EScorpus| con el corpus etiquetado de los casos de plagio parafrástico manualmente anotados. Está basada en un artículo [1]_ dedicado a la creación del primer corpus de paráfrasis para la detección de plagio.
* `XML base de todos los documentos <../_static/01_Ingenieria/1.2_Arquitectura_y_Design/ZZZdoc.html>`_
	Formato XML de todos los textos contenidos en |EScorpus|. Contienen información de los textos originales extraídas con diferentes técnicas NLP.
* `Reporte XML de casos detectados  <../_static/01_Ingenieria/1.2_Arquitectura_y_Design/algorithmXXX-plag-report.html>`_
	XML de casos detectados por el **Algoritmo-XXX**
* `Reporte XML de los datos del Algoritmo-XXX  <../_static/01_Ingenieria/1.2_Arquitectura_y_Design/algorithmXXX-data-report.html>`_
	XML con datos del **Algoritmo-XXX** antes y después del proceso de comparación.

Módulos de |EScorpus|
=======================

* :ref:`Módulo principal <EScorpus_module_principal>` o **Linguist View**.
* :ref:`Modulo de comparación <EScorpus_module_matching>` o **Matching View**.
* :ref:`Módulo de diccionarios <EScorpus_module_dicts>` o **Dict View**.

:leer más: :ref:`Arquitectura de Software <ToNgueLP_architecture>` 

Referencias
=============

.. [1] Barrón-Cedeño Alberto, Vila Marta, Martí M. Antonia, Rosso Paolo. 2013. Title *"`Plagiarism meets Paraphrasing: Insights for the Next Generation in Automatic Plagiarism Detection <http://www.mitpressjournals.org/doi/pdf/10.1162/COLI_a_00153>`_"*. In *Computational Linguistics*.

:Licencia: Creative Commons Share Alike Non Commercial Use, 2014

.. sectionauthor:: Abel Meneses Abad <abelma1980@gmail.com>

.. |EScorpus| replace:: ToNgueLP
