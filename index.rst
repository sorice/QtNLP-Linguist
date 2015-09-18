.. EScorpus documentation master file, created by
   sphinx-quickstart on Tue Aug  6 10:53:02 2013.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

¡Bienvenidos a |EScorpus|!
============================================

|EScorpus| es una aplicación de escritorio del tipo *Front-End* para el trabajo con corpus lingüísticos. Está desarrollada en **Qt** y **Python**.

  **Objetivo:** Crear una aplicación para la creación, edición y análisis de corpus en español para tareas de Procesamiento de Lenguaje Natural, fáciles de usar por lingüistas con poco conocimiento de informática; y también por especialistas informáticos que investigan en el área de NLP.

  **v1.0**: En su primera versión estará dedicada al desarrollo de la arquitectura de la aplicación y el trabajo con corpus de textos elaborados para detección de similaridad o detección de plagio.

Instalación
*************
¿Cómo instalar ToNgueLP?

.. toctree::
   :maxdepth: 2

   /doc/01_Ingenieria/1.3_Implementacion_y_Prueba/install

Guía de Usuario
*******************

|EScorpus| puede ser usado como **lingüista**, como **investigador** del procesamiento de los lenguajes naturales, o como **entusiasta de los idiomas**. Si usted desea conocer como usar esta herramienta lea esta sección:

.. list-table::
   :class: contentstable

   * - :ref:`Vista p/ Lingüistas <EScorpus_module_principal>`

       |Vista Principal|

     - :ref:`Vista p/ Investigadores <EScorpus_module_matching>`   

       |Vista de Comparación|

     - :ref:`Entusiasta de Idiomas <EScorpus_module_dicts>`

       |Vista de Diccionarios|   

.. toctree::
   :maxdepth: 2

   /doc/01_Ingenieria/1.3_Implementacion_y_Prueba/Manual_de_usuario/help

Guía de Desarrollo
*******************

Esta sección está orientada a desarrolladores activos, o entusiastas (futuros desarrolladores) de |EScorpus|. Ha sido dividida en dos partes **Arquitectura** y **Dev DOC** para ayudar a los desarrolladores con las dos cuestiones más importantes:

 * Básicamente, ¿cuál es el diseño de |EScorpus|?
 * ¿Cómo puedo desarrollar |EScorpus|? ¿Documentación?

.. toctree::
   :maxdepth: 2

   /modules/modules

Arq Software
---------------

  :Avanzado: 
    * :ref:`Arquitectura de Software de ToNgueLP <ToNgueLP_architecture>`
    * :ref:`Estilo de Código de ToNgueLP<TNLP_code_style>` 
    * :ref:`Complete example to add a new tag/attribute in XML, UI, and code <ToNgueLP_dev_full_example>`

Documentación
----------------

  Conozca |EScorpus| por su aspecto documental: ¿cómo se hizo? ¿que etapas fue recorriendo?, etc. El proyecto está documentado usando la metodología SXP (híbrido cubano de XP -SCRUM). Usted podrá encontrar aquí los artefactos finales entregados a los clientes de |EScorpus|, y los editables para su uso atendiendo al copyright especificado.

  .. toctree::
     :maxdepth: 2

     /doc/doc

Matlab Example
***************

.. code-block:: matlab

   nf = fix((nx-len+inc)/inc);
   f=zeros(nf,len);
   indf= inc*(0:(nf-1)).';
   inds = (1:len);
   f(:) = x(indf(:,ones(1,len))+inds(ones(nf,1),:));
   if (nwin > 1)
       w = win(:)';
       f = f .* w(ones(nf,1),:);
   end

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
