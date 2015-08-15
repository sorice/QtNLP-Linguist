.. _ToNgueLP_config_file:  

Archivos de Configuración
***************************

La carpeta config es una carpeta del sistema.

	* Objetivo: crear una capa de configuración accesible por todos los elementos de la aplicación en cualquier momento. Permitiendo cambios en determinados valores del sistema incluso en tiempo real.

Ejemplo de uso
===============

|EScorpus| permite la adición de nuevos documentos a un corpus cargado, cuando se intenta construir un nuevo caso. Una vez escogido el documento por el lingüista, |EScorpus| lee la ruta configurada de SRC/SUSP, permitiendo incluir estos en el orginal o en una dirección dentro de una carpeta experimental.

	:Nota: Hacer un caso de plagio, pudiera no ser tan trivial como parece, cuando es necesario colocar informaciones como "Tipo", "Clase", etc. Todos estos son elementos innovadores dentro del corpus de |EScorpus|.

:Nota para desarrolladores: Esta carpeta es necesaria para el desarrollador cuando se incluyan nuevos parámetros en nuevas versiones de |EScorpus|. Ejemplo: direcciones a nuevos diccionarios, listados de stopwords, etc. Estos recursos generalmente son cambiantes.


Parámetros configurables
=========================

* **SRC:** dirección de los documentos fuentes.
* **SUSP:** dirección de los documentos sospechosos.
* **Out:** dirección de la salida del algoritmo que esté en análisis.
* **Parser:** parser activo para la lectura del corpus.
* **stop-words:** listas de stop words activas para el procesamiento NLP.
* **lang:** idioma escogido para mostrar en la UI.
* **Resources:** dirección donde se encuentran los recursos para el procesamiento NLP o la normalización.

:Nota: (aquí me faltan por definir el resto)

Copyright
==========

:Licencia: Creative Commons Share Alike Non Commercial Use, 2014

.. sectionauthor:: Abel Meneses Abad <abelma1980@gmail.com>

.. |EScorpus| replace:: ToNgueLP
