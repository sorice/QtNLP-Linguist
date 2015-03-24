.. _ToNgueLP_architecture:

Arquitectura
--------------

|EScorpus| es una herramienta desarrollada en Qt y Python. Basa su arquitectura en un modelo de plugins (carpeta **modules**) que facilita su desarrollo desde funciones básicas del procesamiento de las lenguas naturales, así como las interfaces simples para los linguistas. La raíz del proyecto está conformada por algunas carpetas que consideramos parte de la arquitectura, y algo importante a leer para iniciarse en el desarrollo de este proyecto:

.. _root-file-ToNgueLP:
.. figure:: /doc/raiz_ToNgueLP.png
	:align: center

	Sistema de ficheros raíz de |EScorpus|

* :ref:`bin <ToNgueLP_bin_path>`: *Binarios de la aplicación.*
* :ref:`config <ToNgueLP_config_file>`: *Datos de configuración, idioma,...*
* :ref:`EScorpus_data`: *Ubicación de los datos, corpus de paráfrasis en español en formato XML, diccionarios utilizados para el Procesamiento del Lenguaje Natural.*
* :ref:`EScorpus_doc`: *Contiene el expediente de proyecto usando la metodología SXP, además de otros recursos importantes, como las imágenes, para generar esta documentación web.*
* :ref:`EScorpus_libraries`: *Bibliotecas externas al core de python necesarias para ejecutar el proyecto con éxito. Ej: python-nltk.*
* :ref:`modules <EScorpus_modules>`: *Módulos o plugins que componen la aplicación.*
* :ref:`scripts <ToNgueLP_scripts>`: *Scripts necesarios para el funcionamiento del negocio de ToNgueLP.*
* :ref:`ui <ToNgueLP_ui_file>`: *GUIs en Qt*

.. list-table::
   :class: contentstable

   * - `Lib <lib/lib.html>`_

       Bibliotecas adicionales que se utilizan.

     - `UI <ui/ui.html>`_

       Interfaz gráfica de TNLP.

Copyright
----------

:Licencia: Creative Commons Share Alike Non Commercial Use, 2014

.. sectionauthor:: Abel Meneses Abad <abelma1980@gmail.com>

.. |EScorpus| replace:: ToNgueLP
