.. EScorpus documentation master file, created by
   sphinx-quickstart on Tue Aug  6 10:53:02 2013.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

¡Bienvenidos a |EScorpus|!
============================================

|EScorpus| es una aplicación de escritorio del tipo *Front-End* para el trabajo con corpus de textos elaborados para detección de similaridad o detección de plagio. Está desarrollada en **Qt** y **Python**.

  *Objetivo:* Crear una aplicación para la creación de corpus en español para tareas de Procesamiento de Lenguaje Natural, fáciles de usar por lingüistas con poco conocimiento de informática.

Guía de Usuario
*******************

Si usted solo desea aprender a utilizar |EScorpus| como entusiasta, lingüista o investigador del procesamiento de los lenguajes naturales, entonces lea esta sección:

.. toctree::
   :maxdepth: 2

   /doc/help/help

Guía de Desarrollo
*******************

Esta sección está orientada a desarrolladores activos o entusiastas futuros desarrolladores de |EScorpus|. Ha sido dividida en dos partes **Arquitectura** y **Dev DOC** para ayudar a los desarrolladores con las dos cuestiones más importantes:

 * Básicamente, ¿cómo está constituida la estructura de |EScorpus|?
 * ¿Dónde puedo leer la documentación del proceso de desarrollo de |EScorpus|?  

Arquitectura
--------------

|EScorpus| es una herramienta desarrollada en Qt y Python. Basa su arquitectura en un modelo de plugins (carpeta **modules**) que facilita su desarrollo desde funciones básicas del procesamiento de las lenguas naturales, así como las interfaces simples para los linguistas. La raíz del proyecto está conformada por algunas carpetas que consideramos parte de la arquitectura, y algo importante a leer para iniciarse en el desarrollo de este proyecto:

.. _root-file-ToNgueLP:
.. figure:: /doc/raiz_ToNgueLP.png
	:align: center

	Sistema de ficheros raíz de |EScorpus|

* :ref:`config`: *Datos de configuración, idioma,...*
* :ref:`EScorpus_data` 
	*Ubicación de los datos, corpus de paráfrasis en español en formato XML, diccionarios utilizados para el Procesamiento del Lenguaje Natural.*
* :ref:`EScorpus_doc` 
	*Expediente de proyecto usando SXP, otros ficheros de datos importantes para generar la documentación.*
* :ref:`EScorpus_libraries`: *Bibliotecas externas necesarias para ejecutar el proyecto con éxito.*
* :ref:`modules <EScorpus_modules>`: *Módulos o plugins que componen |EScorpus|.*
* :ref:`ui`: *GUIs en Qt*

:leer más: :ref:`Arquitectura de Software <EScorpus_modules>` 

Dev DOC
----------
|EScorpus| posee un expediente de proyecto (basado en la metodología SXP), donde se encuentra documentado todo el proceso de desarrollo. Así mismo cada función de código es documentada con **docstrings** y se incluyen las ayudas a estas funciones autogeneradas dentro de la documentación con *Sphinx*. 

* Un nuevo desarrollador podrá leer cada función programada en |EScorpus|.
* Cada clase o método programado podrá ser leído en esta documentación, en el momento necesario.
* No se expone al desarrollador a leer la titánica lista de funciones de una en una para adivinar sus relaciones.

:ver más: `Expediente del proyecto <_static/EScorpus.html>`_

:dependencias: Para abrir/editar los documentos deberá tener instalados:

   * Libre Office, u ODT compatible.
   * Lyx or Latex compatible.
   * Pencil (Prototipos de Interfaz).
   * Navegador Web o HTML compatible.
   * Visor y Editor de Imágenes.

DOCs fundamentales
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Con el objetivo de ahorrar tiempo y estimular a futuros desarrolladores algunos artefactos significativos pueden ser leídos desde misma página de la documentación:

* `Estudio de Software Homólogos <_static/01_Ingenieria/1.2_Arquitectura_y_Design/Estudio_de_homologos/Estudio_de_homologos_Linguistic_Corpus_Tools.pdf>`_
* `XML de casos detectados por el Algoritmo-XXX <_static/01_Ingenieria/1.2_Arquitectura_y_Design/algorithmXXX-plag-report.html>`_

:ver más: `Expediente del proyecto <_static/EScorpus.html>`_

Acerca de:
*******************

Esta sección refiere algunos apuntes históricos del proyecto, así como datos generales de la gestión de cambio y los colaboradores a lo largo de su desarrollo.

* :ref:`Breve Historia del Proyecto <History>`
* :ref:`Release Notes <Release_notes>`
* :ref:`Colaboradores <Colaborators>`

:Copyright: Creative Commons Share Alike Non Commercial Use, 2014
.. sectionauthor:: Abel Meneses Abad <abelma1980@gmail.com> 

.. |EScorpus| replace:: ToNgueLP
