Notas del autor.

Quiero agradecer mediante estas notas a todas las personas que hicieron posible la elaboración de este diagrama. Dejar plasmado además de forma breve un poco de la historia del mismo.

En el año 2011 mientras intentaba terminar mi maestría de Informática Aplicada viajé a La Habana, y dejé a 800km a mis equipos de desarrollo en Manzanillo. Me vi obligado pues en la distancia a elaborar una forma didáctica para explicar SXP, que requiriera poco de mí y me permitiera responder pocas preguntas y de forma sencilla en la distancia a la que me encontraba.

En el año 2007 Malay, primera autora de SXP, había creado algo que conocíamos como "El guión de la metodología", y fue este artefacto durante 4 años la forma más comoda de ver SXP en una o dos páginas.

En el 2009 recurrimos tras múltiples intentos a acomodar SXP para su uso por proyectos de la UCI, utilizando CMMI como estandar de calidad. Se hizo difícil saber donde estaba cada artefacto pues CMMI mira procesos, y nuestro cerebro funciona linealmente, revisando en cada momento que nuevo artefacto o actividad se debe ejecutar. ¿Cómo poner ambas cosas en un mismo lugar?

En el 2012 Yadira y Viana convirtieron cada plantilla de SXP a Lyx para poder gestionar los cambios en el control de versiones. Algo que los equipos necesitan, aún cuando muchas veces no lo saben. (sigo convencido de que RestructuredText es mejor que Latex para esto, más no tengo tiempo de probar mi teoría)

En marzo de 2013 fui invitado a dar una conferencia de SXP en Ciego de Ávila. Estuve varios días preparando una conferencia de problemas comunes y soluciones que daban las ágiles y que SXP contenía dentro. Gracias a Maday y su equipo del proyecto, en especial otro joven del que no recuerdo su nombre muy buen programador de Symfony, me ayudaron a comprender que a lo largo de estos 7 años que llevábamos desarrollando la metodología, muchas plantillas habían sido adicionadas, tenían errores, había exceso de materiales, mucha gente creía por viejas versiones del expediente que había cosas como "plantilla de código fuente", o "Estado del Arte", "Cronograma de Producción", etc.

v4.0 Release notes
===================

Así que estos son los principales cambios que tiene esta rama de la metodología que corre a mi cargo:
- El Plan de Release es el documento organizacional fundamental, no existe el Cronograma de Producción.
- La plantilla de Gestión de clientes sirve como artefacto manuscrito para dejar plasmadas visitas a los clientes y al mismo tiempo las minutas de reunión.
- La "Carta de Intención" se define como el acuerdo de trabajo inicial, pues con la experiencia de la FRG nos dimos cuenta de que escribir un Proyecto Técnico toma tiempo pues el cliente no envía su información a tiempo, y el proyecto debe empezar con un compromiso por escrito de que la empresa supervisará el proyecto, hará entrega y descripción de su negocio, irá a las reuniones, etc, etc... este artefacto fue una creación del año 2011 y lo más difícil ha sido lograr el despliegue final en clientes que no pagan el proyecto.
- Para la inscripción del proyecto en la infraestructura productiva de la institución en concreto, se ha desarrollado la "Ficha Técnica" que contiene gran parte de la información otrora muy importante de visión, misión, el equipo, las fechas iniciales, etc. Con esta plantilla hacemos oficial los proyectos en nuestro consejo de producción.
- La LRP contiene "Requisitos No Funcionales" un olvido lamentable desde el inicio de SXP.
- La plantilla de HU tiene una corrección importante, que se introdujo desde el 2007, donde no se especificaba a que usuario del negocio iba dirigida la HU en concreto, solo gestionaba el nombre del programador que la desarrollaría.
- El negocio en SXP 4.0 se recomienda con IDEF 0 y 3 para lo cual hay una tesis que da una breve panorámica de esta decisión. En esencia es muy fácil que el cliente entienda estos diagramas y le aporte información en apenas 1 hora de reunión. Esto hace la agilidad del intercambio con él y no obliga al cliente a aprender N cosas sobre informática que no le interesan.
- Por primera vez ponemos un ejemplo de Manual de Desarrollo hecho con Doxygen. Hace años que hablamos de esto, pero nunca tuvimos un ejemplo real que regalar a la comunidad y supervisado por el equipo de SXP.
- El Acta de aceptación es el artefacto legal que da conclusión al proyecto, generalmente tras la entrega se hace la firma, pero bien puede ocurrir en tiempo de soporte. Esto no es una plantilla de aval, sino el documento que cierra la intención de la "Carta de intención" y además el compromiso de nuestro equipo en el "Proyecto Técnico".
- Muchos artefactos se manejan a través de la herramienta de gestión, y esto es una gran ventaja.

Se mantienen relativamente igual: el Informe de investigación, Levantamiento de información, Tareas de Ingeniería, Casos de prueba de aceptación, Plan de Pruebas, Manual de Usuario, Gestión de Cambio.

SXP 4.0 no tiene: Cronograma de producción, ni ningún otro artefacto que falte en esta imagen. No hay lista de riesgos pues se maneja a través del sistema de gestión, se ha incluído un ejemplo antiguo muy real para los que deseen escribirlo.

El equipo de SXP trabajará en propuestas concretas y buenas prácticas para reducir la complejidad existente de la metodología, y con la intención de que proyectos que utilicen SXP puedan certificarse con CMMI 2 y 3.

Se incluye una carpeta "Legal" en el expediente con nuestros artefactos que han resultado las mejores experiencias para el registro de software e identidad en Cuba, atendiendo a las particularidades del CENDA y la OCPI respectivamente.

v4.1 Release notes
===================

fecha: 30 de julio de 2013

- Se cambiaron todos los .ott a .odt para que cuando un equipo use SXP en una imagen pueda abrir las plantillas desde el HTML pueda guardarlos en la posición donde van sin necesidad de saber su ubicación. La misma podrá saberse - en el sistema de fichero - al mirar la dirección de la URL que se coloca en la barra inferior.
- Se acortaron los nombres de los documentos, eliminando por ejemplo la palabra "plantilla" de manera que la URL ya mencionada se complete en el navegador y no deba ser inferida. Para los nombres grandes esta URL no se visualizaba en el navegador de forma completa sino que aparecía una secuencia como esta nodeA/nodeB/.../Plantilla_X.ott. De esta forma no se podía saber en que carpeta estaba ubicada la plantilla en cuestión. 
- Se eliminaron los espacios de los nombres para que pueda ser ubicada toda la experiencia "SXP en una imagen" en un servidor apache, sin necesidad de que las URLs se deformen por la existencia de caracteres extraños.


COROLARIO
Quiero agradecer a mucha gente que hizo posible este trabajo.

Primero a Malay, Gladys, Susel, Raycel, Lisandra, Irina, Ailema, Lidibet, David, Yusdelmis y Eduardo por su trabajo durante todos estos años que construyeron cada pieza de SXP.

Especialmente agradecer a Yadira Bagarotti y Ernesto Avila quienes han trabajado los últimos 4 años junto a mí en la refactorización de SXP, y que dio a luz esta versión.

A Leonel Salazar por animarme a redactar esta versión mejorada de "SXP en una imagen" y que conllevó a rectificar muchos artefactos que hacía tiempo requerían de mi atención.

A Yudisel Santana que vio, tras largos años de revisión por otros analistas el faltante en la plantilla de Historia de Usuario.

A Yanet Conde, mi compañera, pues su formación alejada de la rama de informática me permitió consultarle cada detalle de este esquema para saber si era entendible por alguien que no supiera mucho de informática. Este es el mejor resultado que pude obtener asesorado por ella.

Al equipo de VUE que ha creado la mejor herramienta de Mapmind para GNU/Linux, probé Cmap, FreeMind durante años, y este resultado obtenido con VUE es excelente en mi criterio.

Finalmente agradecer a todos los equipos que me han retroalimentado de sus experiencias y que en el futuro permitirán obtener una metodología SXP más madura y flexible. Aquí dejo mi correo para futuros intercambios.

						9 de abril de 2013, Abel Meneses Abad
						abelma1980@gmail.com

SXP persigue la norma de calidad CMMI, y a ello se debe el orden de sus carpetas.