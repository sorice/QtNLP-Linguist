.. _ToNgueLP_scripts:

Scripts del Negocio
=====================

Resumen
*********

Esta sección del proyecto, contiene todos los scripts diseñados para el correcto funcionamiento del negocio de |EScorpus|.

Update corpus XML info
^^^^^^^^^^^^^^^^^^^^^^^

Este script debe velar por la integridad de los datos en el XML del corpus. O sea los parámetros que son susceptibles de modificar a mano y que pueden generar errores en las interfaces deben ser rectificados automáticamente tras cada modificación manual. Ej. **total_corpus_cases** debe estar en correspondencia con el **<snippet_pair**

.. automodule:: update_corpus_xml_info
   :members:

Copyright
***********

:Licencia: Creative Commons Share Alike Non Commercial Use, 2014

.. sectionauthor:: Abel Meneses Abad <abelma1980@gmail.com> 

.. |EScorpus| replace:: ToNgueLP