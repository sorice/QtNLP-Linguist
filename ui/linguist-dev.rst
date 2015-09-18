.. _ToNgueLP_linguist_module:

El módulo para lingüistas, necesario para crear el corpus TNLP, tiene XXX GUI.

Main Window
=============

Ventana principal desde la que se ejecutan todos los procesos. Contiene menús.

.. autoclass:: ui.TNLP_MW.TNLP_MW
   :members:
   :private-members:
   :special-members: 

Case Tab
==========

Clase para hacer tabs de cada caso.

.. autoclass:: ui.TNLP_Cases_Tab.TNLP_CaseTab
   :members:
   :private-members:
   :special-members:
   
New Corpus
===========

Clase para manejar la creación de un nuevo corpus.

.. autoclass:: ui.TNLP_New_Corpus.TNLP_NewCorpus
   :members:
   :private-members:
   :special-members:

Add Case
===========

Clase para adicionar un caso u objeto de pares. Un caso contiene más nodos o tags, y sus respectivos atributos.

.. autoclass:: ui.TNLP_Add_Case.TNLP_AddCase
   :members:
   :private-members:
   :special-members:
   
Add Annotation
===================

Clase para adicionar una anotación, que es un sub-tag del caso. Un caso contiene más nodos o tags, y sus respectivos atributos.

.. autoclass:: ui.TNLP_Add_Annotation.TNLP_AddAnnotation
   :members:
   :private-members:
   :special-members:
   
