# Recipe Test (separado)

Pregunta: ¿otro investigador puede ejecutar el prompt de una receta aprobada?

Usá solo el texto canónico proporcionado por la editora, sin reconstruir recetas ausentes. Un investigador distinto intenta obtener el resultado con los ingredientes declarados. Registrá decisiones, correcciones, bloqueos, evidencia de salida y dictamen LISTO/REVISAR/NO AVANZAR. Verificá una pregunta cerrada por turno, gates antes de código y comprobaciones del resultado. Reportá tiempo observado separado del estimado. Una receta ejecutable no demuestra que Contributor detecte bien; una detección correcta no demuestra reproducibilidad de la receta.

## Evidencia y gate

Completar templates/test_report.json después de ejecutar, con huella calculada por verify_test.py. Sustituir placeholders por observaciones reales; nunca inventarlas. La prueba es obligatoria antes de la aprobación de una nueva receta. La revisión de procedencia ocurre localmente; el reporte autorizado contiene solo el resultado de esa comprobación, no el chat. Entregar informe sanitizado junto al draft por el canal que Sol habilite. Una persona distinta del autor prueba; Sol revisa y decide. Corregir exige comprobar la versión nueva.
