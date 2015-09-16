.. _ToNgueLP_ui_file: 

**Interfaces**

.. toctree::
   :maxdepth: 2

   /ui/ui

.. _QtToNgueLP_module_principal:

Vista Principal
*****************

La vista principal está dirigida a los lingüistas.
   * Objetivo: Permitir la creación de casos de plagio con paráfrasis. Clasificar estos. Y además categorizar los casos generados automáticamente para |EScorpus| de forma manual, lo que permitirá evaluar con las métricas definidas los algoritmos de detección.

.. _qt-vista-principal:
.. figure:: /doc/01_Ingenieria/1.2_Arquitectura_y_Design/Mockups/QtToNgueLP_Vista_Principal.png
   :align: center
   :height: 350pt
   :width:  550pt

   Vista Principal de |EScorpus| elaborada en Qt4.

Descripción de los elementos
===================================

   1. “Barra de Menús”: Barras de Menú
   2. “Loguin”: Opción de Loguin, para expertos autorizados a confirmar manualmente los casos generados automáticamante.
   3. “Tabs Corpus”: Acceder simultáneamente a diferentes corpus cargados.
   4. “Barras de Herramientas”: Barra de Plugins o .
   5. “Search”: Componente de búsqueda.
   6. “Case List”: Lista de casos
   7. “Tabs Case”: Tabs de casos y/o vistas de la aplicación.
   8. “src Case Text”: Fragmento del texto del documento fuente u original.
   9. “src Case Bar Data”: Barra de datos del fragmento fuente.
   10. “susp Case Text”: Fragmento del texto del documento sospechoso.
   11. “susp Case Bar Data”: Barra de datos del fragmento sospechoso.
   12. “Barra de Edición de Casos”: Elementos para editar fragmentos.

Código de colores
===================

.. tabularcolumns:: m{150pt} m{150pt} |c|c|

+-----------------+----------------------------+
| Colores         | Tipos de Plagio            |
+=================+============================+
| |White Plag|    | No Plagio                  |
+-----------------+----------------------------+
| |Red Plag|      | Plagio Literal             |
+-----------------+----------------------------+
| |Blue Plag|     | Plagio Parafrástico        |
+-----------------+----------------------------+
| |Yellow Plag|   | Plagio Traslingue          |
+-----------------+----------------------------+
| |Orange Plag|   | Citas Erróneas             |
+-----------------+----------------------------+
| |Green Plag|    | Copyleft y Citas correctas |
+-----------------+----------------------------+
  
.. |Red Plag| image:: /resources/plag_colors/red.png
                 :height: 15pt
                 :width:  15pt

.. |Blue Plag| image:: /resources/plag_colors/blue.png
                 :height: 15pt
                 :width:  15pt

.. |Yellow Plag| image:: /resources/plag_colors/yellow.png
                 :height: 15pt
                 :width:  15pt

.. |Orange Plag| image:: /resources/plag_colors/orange.png
                 :height: 15pt
                 :width:  15pt

.. |Green Plag| image:: /resources/plag_colors/green.png
                 :height: 15pt
                 :width:  15pt

.. |White Plag| image:: /resources/plag_colors/white.png
                 :height: 15pt
                 :width:  15pt

.. _QtToNgueLP_module_matching:

Vista de Comparación
***********************

La vista de comparación está dirigida a los usuarios del tipo **Investigador NLP**.
   * Objetivo: Comparar los casos disponibles en |EScorpus| con los detectados, introducidos en la carpeta *Out* configurada por el investigador.

Este módulo genera información que es escrita de forma automática en los XMLs del algoritmo que está siendo probado.

.. _qt-vista-comparacion:
.. figure:: /doc/01_Ingenieria/1.2_Arquitectura_y_Design/Mockups/Vista_de_Comparacion.png
   :align: center

   Vista de Comparacion de |EScorpus|.

.. _QtToNgueLP_module_dicts:

Vista de Diccionarios
***********************

La vista de diccionarios está dirigida a los usuarios de todo tipo.
   * Objetivo: Revisar las palabras disponibles en el diccionario de |EScorpus|. Además permitirá agregar nuevas palabras existentes en los textos que se estén procesando.

:nota: Los diccionarios serán guardados en el formato de wordnet.

.. _qt-vista-diccionario:

.. figure:: /doc/01_Ingenieria/1.2_Arquitectura_y_Design/Mockups/Vista_de_Diccionario.png
   :align: center

   Vista de Diccionarios de |EScorpus|.

Copyright
***********

:Licencia: Creative Commons Share Alike Non Commercial Use, 2014

.. sectionauthor:: Abel Meneses Abad <abelma1980@gmail.com>

.. |EScorpus| replace:: ToNgueLP
