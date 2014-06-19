.. EScorpus documentation master file, created by
   sphinx-quickstart on Tue Aug  6 10:53:02 2013.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to EScorpus's documentation!
====================================

.. toctree::
   :glob:

EScorpus es una aplicación de escritorio del tipo *Front-End* para el trabajo con corpus de textos elaborados para detección de similaridad o detección de plagio. Está desarrollada en **Qt** y **Python**.

  *Objetivo:* Crear una aplicación para la creación de corpus en español para tareas de Procesamiento de Lenguaje Natural, fáciles de usar por lingüistas con poco conocimiento de informática.

Guía de Usuario
****************

Aquí van los enlaces a la ayuda del usuario.

Guía de Desarrollo
*******************

Arquitectura
^^^^^^^^^^^^^^

EScorpus es una herramienta desarrollada en Qt y Python. Basa su arquitectura en un modelo de plugins (carpeta **modules**) que facilita su desarrollo desde funciones básicas del procesamiento de las lenguas naturales, así como las interfaces simples para los linguistas. Sin embargo la raíz del proyecto está conformada por algunas carpetas que consideramos parte de la arquitectura, así como parte de la configuración del proyecto.

* :ref:`config`: *Datos de configuración, idioma,...*
* :ref:`EScorpus_data` 
	*Ubicación de los datos, corpus de paráfrasis en español en formato XML, diccionarios utilizados para el Procesamiento del Lenguaje Natural.*
* :ref:`doc` 
	*Expediente de proyecto usando SXP, otros ficheros de datos importantes para generar la documentación.*
* :ref:`EScorpus_libraries`: *Bibliotecas externas necesarias para ejecutar el proyecto con éxito.*
* :ref:`EScorpus_modules`: *Módulos implementados por el equipo de Sunshine*
* :ref:`ui`: *GUIs en Qt*

Documentación
^^^^^^^^^^^^^^
En esta sección orientada a desarrolladores de EScorpus se coloca de forma fácil para su acceso el expediente del proyecto. El proyecto utiliza la metodología SXP.

`Expediente de proyecto <_static/EScorpus.html>`_

Artefactos fundamentales:

  * :download: `XML de casos detectados por **AlgoritmoXXX** <_static/01_Ingenieria/1.2_Arquitectura_y_Design/suspXXX-plag-report.html>`_
  * :download: `Acta de Aceptación de la Arquitectura de Información <_static/02_Gestion_de_Proyectos/2.4_Acuerdos_de_trabajo/19_Acta_de_Aceptacion_Arq_de_Informacion.odt>`_

Otros datos
*******************

Esta sección refiere algunos apuntes históricos del proyecto, así como datos generales de la gestión de cambio y los colaboradores a lo largo de su desarrollo.

* :ref:`EScorpus_history`
* `Release Notes <appendix/A/revition_history.html>`_
* `Colaboradores <appendix/B/colaboradores.html>`_

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

