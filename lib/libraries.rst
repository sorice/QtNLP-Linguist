.. _Libraries:

Libraries Section
====================

Resumen
*********

Esta sección del proyecto, contiene todas las librerías externas y no desarrolladas por el proyecto Sunshine. En su totalidad son bibliotecas de python y códigos C++ que optimizan ciertos procesos.

Bibliotecas
************

nltk
^^^^^^

Biblioteca estándar de python para procesamiento del lenguaje natural.

whoosh
^^^^^^^^

Biblioteca de python para **recuperación de información**.

django
^^^^^^^

Marco de trabajo web de alto nivel en python que impulsa el desarrollo limpio y rápido de aplicaciones con un diseño práctico.

langid
^^^^^^^^

Biblioteca de pytho para la identificación del idioma, implementa un modelo probabilístico que está autocontenido en el código fuente.

celery
^^^^^^^^

Este complemento de Sunshine es la biblioteca estandar de python para **ejecutar tareas en segundo plano**. Es la biblioteca que aporta mayor complejidad a la sección *libraries* pues contiene un gran número de dependencias.

Son dependencias de celery:

* amqp
* anyjson
* billiard
* kombu
* pytz

python-pdfminer
^^^^^^^^^^^^^^^^

Utilizada para la extracción de datos de los metadatos de los PDF.

Otras aplicaciones
********************

pdftotxt
^^^^^^^^^^^^

Binario compilado para GNU/Linux Ubuntu 12.04, que convierte los PDF en txt. No es la utilidad que viene con la aplicación xpdf, sino un código externo independiente compilado por el equipo.

pdftotxt
^^^^^^^^^^^^
Binario compilado para GNU/Linux Ubuntu 12.04 que convierte hojas de un PDF en formato de imagen .ppm. En Sunshine es utilizado para generar los thumbnails de la primera hoja.