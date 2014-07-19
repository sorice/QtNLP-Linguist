.. _EScorpus_data:

data
================

Esta es la segunda carpeta en importancia en |EScorpus|. Ella contiene, entre otros, el corpus de casos de plagio de |EScorpus|, y ofrece la posibilidad de colocar otros corpus y algoritmos de detección para calcular sus métricas.

XMLs
*****************

Todos los datos en |EScorpus| han sido estandarizados y convertidos a XML. Las razones fundamentales de esto son:
	* Existe una tendencia internacional a trabajar con ficheros XML en todos los corpus lingḯsticos experimentales.
	* Al trabajar con miles de documentos se hace necesario conservar datos obtenidos una vez como resultado de cierto procesamiento, sin necesidad de volver a calcularlos. Los XMLs actuan también como objetos de la programación.
	* Al utilizar XMLs bien anotados, es posible construir parsers en diferentes lenguajes de programación para abordar diferentes problemas, que luego visualmente son mostrados a través de las interfaces.

Los 4 XMLs más importantes de |EScorpus| son:

1. `XML corpus <../_static/01_Ingenieria/1.2_Arquitectura_y_Design/EScorpusYYY-plag-cases-corpus.html>`_
2. `XML algoritmoXXX <../_static/01_Ingenieria/1.2_Arquitectura_y_Design/algorithmXXX-data-report.html>`_
3. `XML de casos detectados por algoritmoXXX <../_static/01_Ingenieria/1.2_Arquitectura_y_Design/algorithmXXX-plag-report.html>`_
4. `XML de los documentos <../_static/01_Ingenieria/1.2_Arquitectura_y_Design/ZZZdoc.html>`_

Estructura de Ficheros
**************************

.. _files-ToNgueLP-data
.. figure:: /doc/files_ToNgueLP-data.png
	:align: center

	Ficheros de la carpeta *data* de |EScorpus|. 

* :ref:`Algorithms <Algorithms>`.
	Carpeta de algoritmos en proceso de comparación.
* :Corpuses: `Carpeta de corpus adicionados por el usuario <Corpuses>`.
* :src: Carpeta de documentos originales (o fuentes) del corpus de |EScorpus|.
* :susp: Carpeta de documentos sospechosos del corpus de |EScorpus|
* :data.srt: Fichero necesario para generar la documentación automáticamente.
* :metadata-corpus.xml: `Metadatos del corpus <data/metadata-corpus.xml>`_

:Copyright: Creative Commons Share Alike Non Commercial Use, 2014
.. sectionauthor:: Abel Meneses Abad <abelma1980@gmail.com> 

.. |EScorpus| replace:: ToNgueLP