.. _Sunshine_history:

Historia de Sunshine
======================

Resumen
**********

Sunshine nació en la idea del Ing. Eddy Ernesto del Valle Pino en el año 2011. Entonces estudiante de la UCI, visualizó el problema de como cientos de documentos (libros fundamentalmente) bajados de internet, se perdían de la red universitaria, al egresar sus ingenieros, o marcharse de la universidad sus profesores más antiguos con colecciones excepcionales acumuladas durante años. Propuso entonces la creación de un repositorio colaborativo de documentos, con una estética o usabilidad similar a la del Google Book del 2011. En este sistema cada usuario tendría una contraseña y compartiría sus bibliotecas personales, creando colecciones temáticas y propiciando la descarga de libros más populares, entre otras opciones. En septiembre de 2011 se instaló la primera y única versión, la v0.1. Acumuló hasta agosto de 2013 unos 3600 libros y documentos. El sistema quedó sin mantenimiento debido al egreso de Eddy de la UCI, y no menos importante, debido a numerosos errores arquitectónicos que impidieron su actualización posterior, sin documentación de esta versión y con las mismas necesidades, surgió la v1.x.

:Nota: Esta sección es para documentar los momentos más importantes de Sunshine, así como referenciar un grupo de documentos que sin esta guía escrita no tendrían ningún valor.

Ppales momentos
**********************************

* Septiembre de 2011 instalación se servidor público de la UCI, v0.1.
* Octubre de 2011 planificación v0.2
* Noviembre de 2011 planificación v0.3. No se entregaba ni desplegaba la versión 0.2, y hubo que hacer un tag intermedio v0.2.1. Este finalmente tampoco se entregó. Se elaboran los perfiles de Eddy y Carlos Giralt.
* Diciembre de 2011 planificación de la v0.4
* De Enero a Mayo de 2012 se desarrollaron las dos tesis pactadas, pero el sistema nunca fue actualizado. Solo lo podía hacer Eddy, y no estaba documentado en ningún caso como hacerlo.
* Abril 2012, Julio Madera accede a ser el tutor de doctorado de Abel y abrir una nueva idea que contemple la *detección semántica de plagio*.
* Junio 2012 - Abril 2013 se estudian las tecnologías existentes en esos momentos más indicadas para la versión 1.x, objetivo fundamental: cambiar la arquitectura de Django, Spine, CofeScript, BD desconocida, HTML a algo más estandar y conocido, se piensa en: Django, JQuery, JavaScript, HTML5, PostgreSQL.
	- Todavía se mantiene activo el servicio de la v0.1
* Enero 2013 aprobado el tema de tesis sobre Plagio Parafrástico en la UCLV a Abel Meneses.
* Febrero 2013 presentación del proyecto I+D en la Sesión Científica de la FRG de la Universidad de Granma. Aprobado.
* Junio 2013 primeras pruebas pilotos con Lemur y pymur, se resuelve probar otras tecnologías de python pues pymur está abandonado desde el 2009.
* Julio 2013 tras 30 días, no continuos, de trabajo se obtiene una versión con NLTK para el NLP, python-whoosh para la Recuperación de Información y los HTMLs del proyecto Ombú modificado.
* Agosto 2013 tras múltiples pruebas se encuentra en estado estable la configuración del proyecto con sus 7 carpetas principales: data, doc, libraries, modules, static, tags, templates.

Historia
************

2011
------

En octubre de 2011, en el apto de Manuel, `debatimos <documents/2011-10_Debate1_de_tesis_Eddy.txt>`_ con Eddy y Manuel donde se plantea darle a Eddy como tesis un problema sencillo: `la detección de duplicados <documents/2012-07_Thesis-Del_Valle-Deteccion_de_duplicados_en_Sunshine.pdf>`_. En esta discusión se deja por escrito el *objetivo principal de Sunshine*: **gestión del conocimiento de colecciones privadas**.

De regreso en Manzanillo por primera vez se planifica el proyecto por Abel Meneses. En ese momento ya estaba en el *redmine de comunidades* - así se le llamaba al servidor de *proyectos de software* para la comunidad de desarrolladores dentro de la UCI. El proyecto se planificaba en tiempo real en `el sitio web de desarrollo del proyecto Sunshine <http://comunidades.uci.cu/projects/sunshine>`_ con visibilidad nacional. Sin embargo esta planificación no fue respetada a pesar que Eddy hablaba de getting real comenzaron a aparecer problemas de arquitectura por las tecnologías utilizadas, y esto se hizo constante a partir de los cambios frecuentes de tecnología que hizo Eddy durante ese año.

Hubo que hacer una versión intermedia 0.2.2 ante los problemas de arquitectura para alinear los requisitos con lo que se estaba haciendo en realidad, pero nunca se desplegaron estas versiones 0.2.x.

En noviembre de 2011 Abel, Eddy y Carlos deciden reforzar la parte visual, pues Eddy necesitaba un poco de ayuda. Se conforma entonces una tesis para Carlos que contemplara el diseño y la implementación de un `cliente web para Sunshine <documents/2012-06_Thesis-Giralt_Carlos-Cliente_Web_para_Sunshine.pdf>`_. Manuel abandonó la UCi por esta época y quedó solo consultando a Eddy. El equipo desarrollaba en Artemisa (entonces un municipio de provincia Habana) en muy malas condiciones. Afortunadamente encontramos el apoyo de Annies y otros funcionarios de la facultad para proseguir con el proyecto. Abel se encontraba ocupado en su maestría.

En este mismo mes se creó el primer documento del sistema de `Evento - Reputación - Permisos <documents/2011-11_Sistema_evento-reputacion-permisos.ods>`_, diseñado originalmente como concepto de *web collective intelligence*, una forma en la que el sistema aprendería de los usuarios autoadministrando sus roles con la intervención mínima del administrador del sistema.

2012
-----------

En enero de 2012 antes de Abel marchar a su doctorado propuso `la última planificación de la versión 0.x <documents/2012-01_Roadmap_v0.3.txt>`_. Solo las tesis llegaron a elaborarse y también el código pero este nunca fue desplegado.

En abril de 2012 simultáneamente en Ciudad de La Habana y Camagüey `se presenta el proyecto <documents/2012-04_Presentation_Sunshine_FLISOL.pdf>`_ en el Festival Latinoamericano de Instalación de SWL.

En mayo de 2012 se conciebe la `versión 1.0 <documents/2012-05_Cronograma_Sunshine_1.0.txt>`_ ante el inminente fracaso de la versión 0.x debido a: los cambios tecnológicos constantes de Eddy, el tamaño extraordinario del índice que pesaba más que la colección misma (luego se comprobó que usar Xapian podría traer estos problemas), el incumplimiento de la planificación, la futura desaparición de la facultad de Artemisa que sería convertida en la universidad de la recién formada provincia *Artemisa*.

Comienza así un período en el que Eiger Mora y Abel Meneses mantienen la versión instalada en la UCI, cuyo funcionamiento se hacía complicado pues la aplicación tenía problemas de optimización y cero documentación. Abel comenzó sus estudios tecnológicos sobre recuperación de información con swl y sobre el proceso de identificación de plagio, similaridad, etc. Este período está bastante desprovisto de artefactos documentales hasta la llegada del 2013.

2013
-----------

Tras la terminación de `la presentación de su tema de doctorado sobre plagio <documents/2013-01-07_Analisis_de_relaciones_semanticas_Deteccion_de_Plagio_rephrase.pdf>`_, y con el estudio tecnológico bastante adelantado en febrero de 2012 se presentó `el proyecto I+D Sunshine <documents/2013-02-21_Sunshine_Repositorio_Institucional_Avanzado_de_Acceso_Abierto.pdf>`_ en el consejo científico de la entonces facultad regional de Granma de la UCI (un mes después se convertiría en la Facultad de Ciencias Informáticas de la Universidad de Granma).

En Junio de 2013 una semana antes de la liberación de su cargo como director del CDFRG, Abel comienza a desarrollar junto a Leonardo Texidó la nueva versión con una nueva arquitectura. Un `resumen <documents/2013-06_sunshine_with_lemur.rst>`_ de los detalles encontrados el los primeros experimentos con Lemur dieron al traste con esta propuesta y se propuso la utilización de bibliotecas de python.

Un conjunto de anotaciones del primer mes de desarrollo en Manzanillo puede ser encontrado en :ref:`Wall_Gitlab_FRG_2013`