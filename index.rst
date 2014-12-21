.. EScorpus documentation master file, created by
   sphinx-quickstart on Tue Aug  6 10:53:02 2013.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

¡Bienvenidos a |EScorpus|!
============================================

|EScorpus| es una aplicación de escritorio del tipo *Front-End* para el trabajo con corpus de textos elaborados para detección de similaridad o detección de plagio. Está desarrollada en **Qt** y **Python**.

  **Objetivo:** Crear una aplicación para la creación de corpus en español para tareas de Procesamiento de Lenguaje Natural, fáciles de usar por lingüistas con poco conocimiento de informática; y también por especialistas informáticos que investigan en el área de NLP.

Instalación
*************
¿Cómo instalar ToNgueLP?

.. toctree::
   :maxdepth: 2

   /doc/install/install

Guía de Usuario
*******************

|EScorpus| puede ser usado como *lingüista*, *investigador* del procesamiento de los lenguajes naturales, o *entusiasta de los idiomas*. Si usted desea conocer como usar esta herramienta lea esta sección:

.. tabularcolumns:: m{150pt} m{150pt} m{150pt} |c|c|c|

======================================================== =========================================================== =======================================================
 |Vista Principal|								 |Vista de Comparación|								|Vista de Diccionarios|
======================================================== =========================================================== =======================================================
 :ref:`Vista p/ Lingüistas <EScorpus_module_principal>`   :ref:`Vista p/ Investigadores <EScorpus_module_matching>`   :ref:`Entusiasta de Idiomas <EScorpus_module_dicts>`
======================================================== =========================================================== =======================================================

.. |Vista Principal| image:: /doc/01_Ingenieria/1.2_Arquitectura_y_Design/Mockups/Vista_Principal_for_sphinx-doc.png
                 :height: 105pt
                 :width:  120pt
                 :alt: Vista principal de ToNgueLP.

.. |Vista de Comparación| image:: /doc/01_Ingenieria/1.2_Arquitectura_y_Design/Mockups/Vista_de_Comparacion.png
                 :height: 90pt
                 :width:  120pt
                 :alt: Vista principal de ToNgueLP.

.. |Vista de Diccionarios| image:: /doc/01_Ingenieria/1.2_Arquitectura_y_Design/Mockups/Vista_de_Diccionario.png
                 :height: 120pt
                 :width:  90pt
                 :alt: Vista principal de ToNgueLP.

.. toctree::
   :maxdepth: 2

   /doc/help/help

Guía de Desarrollo
*******************

Esta sección está orientada a desarrolladores activos, o entusiastas futuros desarrolladores de |EScorpus|. Ha sido dividida en dos partes **Arquitectura** y **Dev DOC** para ayudar a los desarrolladores con las dos cuestiones más importantes:

 * Básicamente, ¿cómo está constituida la estructura de |EScorpus|?
 * ¿Dónde puedo leer la documentación del proceso de desarrollo de |EScorpus|?  

.. toctree::
   :maxdepth: 2

   /modules/modules

Arq Software
---------------

:Avanzado: :ref:`Arquitectura de Software de ToNgueLP <ToNgueLP_architecture>`

Documentación
****************

Esta sección está dirigida a aquellos que deseen conocer |EScorpus| por su aspecto documental: ¿cómo se hizo? ¿que etapas fue recorriendo?, etc. Todo el proyecto está documentado usando la metodología SXP, un híbrido cubano de XP y SCRUM. Usted podrá encontrar aquí los artefactos finales archivados en papel y entregados a los clientes de |EScorpus| y además los editables para su reproducción atendiendo a los derechos de copyright especificados.

.. toctree::
   :maxdepth: 2

   /doc/doc

Acerca de:
*******************

Esta sección refiere algunos apuntes históricos del proyecto, así como datos generales de la gestión de cambio y los colaboradores a lo largo de su desarrollo.

* :ref:`Breve Historia del Proyecto <History>`
* :ref:`Release Notes <Release_notes>`
* :ref:`Colaboradores <Colaborators>`

Copyright
***********

:Licencia: Creative Commons Share Alike Non Commercial Use, 2014

.. sectionauthor:: Abel Meneses Abad <abelma1980@gmail.com> 

.. |EScorpus| replace:: ToNgueLP
