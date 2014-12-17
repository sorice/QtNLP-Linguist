.. _ToNgueLP_scripts:

Scripts del Negocio
=====================

Resumen
*********

Esta sección del proyecto, contiene todos los scripts diseñados para el correcto funcionamiento del negocio de |EScorpus|.
En la `Arquitectura de Información <../_static/01_Ingenieria/1.2_Arquitectura_y_Design/11_Arq_de_informacion.pdf>`_ y partiendo del `Diagrama de estados <../_images/Diagrama_de_Estados_Vista_Principal_ToNgueLP-Corpus_Process.png>`_ se definen en la Vista Principal los siguientes scripts:

1. :(nombre x definir): Convertir documentos TXT o PDF a ZZZdoc.XML.
2. :(nombre x definir): Verificar compatibilidad del Corpus cargado con el Parser configurado.
3. :(nombre x definir): Generar XML estandar a partir de la carpeta OUT de la salida de un algoritmo de detección.
4. :(nombre x definir): Comparación del XML estandar con XML del corpus cargado.
5. :`Update corpus XML info`_: Actualizar ciertos tags del XML de datos del algoritmo y actualizar ciertos tags del XML reporte de casos detectados.
6. :(el el futuro): “Adicionar nuevo script”, tener los elementos posibles en pantalla y unirlos como en un simulador o sea moviendo cuadritos *(preguntar a Leonel como se llamaban los elementos visuales desplazables que había en el UI del SCADA)*.

Update corpus XML info
^^^^^^^^^^^^^^^^^^^^^^^

Este script debe velar por la integridad de los datos en el XML del corpus. O sea los parámetros que son susceptibles de modificar a mano y que pueden generar errores en las interfaces deben ser rectificados automáticamente tras cada modificación manual. 

.. code-block:: rest

	Ej. **total_corpus_cases** debe estar en correspondencia con el **<snippet_pair**.

.. automodule:: update_corpus_xml_info
   :members:

Copyright
***********

:Licencia: Creative Commons Share Alike Non Commercial Use, 2014

.. sectionauthor:: Abel Meneses Abad <abelma1980@gmail.com> 

.. |EScorpus| replace:: ToNgueLP

.. figure:: /doc/01_Ingenieria/1.2_Arquitectura_y_Design/Diagrams/Diagrama_de_Estados_Vista_Principal_ToNgueLP-Corpus_Process.png
                 :height: 0pt
                 :width:  0pt