# Recipe Test (separado)

Pregunta: ¿otro investigador puede ejecutar el prompt de una receta aprobada?

Usá solo el texto canónico proporcionado por la editora, sin reconstruir recetas ausentes. Un investigador distinto intenta obtener el resultado con los ingredientes declarados. Registrá decisiones, correcciones, bloqueos, evidencia de salida y dictamen LISTO/REVISAR/NO AVANZAR. Verificá una pregunta cerrada por turno, gates antes de código y comprobaciones del resultado. Reportá tiempo observado separado del estimado. Una receta ejecutable no demuestra que Contributor detecte bien; una detección correcta no demuestra reproducibilidad de la receta.

## Evidencia y gate

Completar templates/test_report.json después de ejecutar, con huella calculada por verify_test.py. Sustituir placeholders por observaciones reales; nunca inventarlas. La prueba es obligatoria antes de la aprobación de una nueva receta. La revisión de procedencia ocurre localmente; el reporte autorizado contiene solo el resultado de esa comprobación, no el chat. Entregar informe sanitizado junto al draft por el canal que Sol habilite. Una persona distinta del autor prueba; Sol revisa y decide. Corregir exige comprobar la versión nueva.

## Criterio obligatorio: prompt simple y ejecutable

La receta falla la revisión si no contiene el prompt completo y copiable para un chat nuevo, si ese prompt solo diagnostica o si no llega a producir y comprobar el resultado. Probar con una persona que no conozca el proyecto original: debe empezar con una explicación breve del siguiente paso y una única pregunta sencilla, ofrecer opciones comprensibles y «No sé», definir términos técnicos antes de usarlos, y construir el producto progresivamente. Debe preguntar el lenguaje o la herramienta solo cuando corresponda, explicar alternativas, confirmar decisiones antes de código y solicitar una salida observada para su comprobación. Esta inspección es distinta de la reproducción independiente y no justifica marcar APROBADA.
