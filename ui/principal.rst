.. _EScorpus_module_principal:

Vista Principal
*****************

La vista principal está dirigida a los lingüistas.
	* Objetivo: Permitir la creación de casos de plagio con paráfrasis. Clasificar estos. Y además categorizar los casos generados automáticamente para |EScorpus| de forma manual, lo que permitirá evaluar con las métricas definidas los algoritmos de detección.

.. _vista-principal:
.. figure:: /doc/01_Ingenieria/1.2_Arquitectura_y_Design/Mockups/Vista_Principal_for_sphinx-doc.png
	:align: center

	Vista principal de |EScorpus|.

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
| Colores 	  | Tipos de Plagio	       |
+=================+============================+
| |Red Plag|	  | Plagio Literal	       |
+-----------------+----------------------------+
| |Blue Plag|	  | Plagio Parafrástico	       |
+-----------------+----------------------------+
| |Yellow Plag|	  | Plagio Traslingue	       |
+-----------------+----------------------------+
| |Orange Plag|	  | Citas Erróneas	       |
+-----------------+----------------------------+
| |Green Plag|	  | Copyleft y Citas correctas |
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

Copyright
==========

:Licencia: Creative Commons Share Alike Non Commercial Use, 2014

.. sectionauthor:: Abel Meneses Abad <abelma1980@gmail.com>

.. |EScorpus| replace:: ToNgueLP