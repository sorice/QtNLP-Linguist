.. _EScorpus_features:

Funcionalidades
*******************

En esta sección se descripen los procesos que ocurren en EScorpus así como el 100% de las funcionalidades de la aplicación. También contenidas en el documento LRP de la documentación de desarrollo.

Procesos
==========

1. Preprocesamiento: 
	Convierte los textos en formato PDF o TXT al formato ZZZdoc.xml.
2. Estandarización de salidas de algoritmos: 
	Convierte la carpeta out de la salida de los algoritmos en un único XML, estandarizado para comparar con 
3. Comparación del algorithmXXX-plag-report.xml vs EScorpusYYY-plag-cases-corpus.xml
	Extracción de datos de las métricas: Precision, Recall, Granularity, F-Measure, PlagDet, Run-Time, etc.
4. Actualizar XMLs:
	Escribir datos de coincidencia en el *algorithmXXX-plag-report.xml*. Ej: etiqueta <case> = # del caso con el que coincide en el *EScorpusYYY-plag-cases-corpus*
	Escribir datos de las métricas en *algorithmXXX-data-report.xml*. Ej: Etiqueta <precision> = precisión.

Funcionalidades
=================


