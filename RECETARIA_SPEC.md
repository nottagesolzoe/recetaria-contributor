# RecetArIA · especificación central

Reglas aportadas por Sol Zoe Nottage. La procedencia se conserva en el entorno del contributor. Los ejemplos describen el mecanismo, no son una fuente de nuevos candidatos.

## 1. Qué es RecetArIA

RecetArIA convierte aprendizajes que aparecen durante la práctica real de hacer investigación con asistentes de IA en recetas metodológicas breves, reproducibles y transferibles.

No es un manual general de metodología.

No genera recetas a partir de una lista ideal de cosas que un investigador debería saber.

No busca temas para recetas en internet.

La fuente primaria de una receta debe ser una interacción real entre un investigador y un asistente de IA durante un proceso de investigación.

## 2. Regla obligatoria de procedencia

Ninguna receta puede ser propuesta solamente porque el tema parece metodológicamente útil.

Toda candidata debe poder reconstruir este recorrido:

INTERACCIÓN REAL
→ TAREA DE INVESTIGACIÓN
→ PROBLEMA, DUDA O DECISIÓN
→ TRABAJO CON IA
→ SOLUCIÓN, DECISIÓN O PROCEDIMIENTO
→ APRENDIZAJE TRANSFERIBLE

Si no existe evidencia del episodio de origen, no generar la receta.

No completar automáticamente partes faltantes del proceso de investigación con recetas genéricas.

No usar búsquedas web para descubrir temas de recetas.

## 3. Qué debe buscar el detector

Analizar las interacciones del investigador buscando episodios donde la IA haya ayudado a:

* elegir entre alternativas metodológicas
* convertir una idea en una decisión operativa
* resolver un error que reveló un aprendizaje generalizable
* diseñar o modificar un procedimiento
* comprobar si un resultado era correcto
* detectar que un procedimiento aparentemente correcto tenía un problema
* comparar métodos, modelos, prompts o implementaciones
* operacionalizar un concepto
* construir una medida, indicador, índice o clasificación
* mejorar una estrategia de análisis
* validar código, datos, modelos o resultados
* transformar una tarea manual en un procedimiento reproducible

Estas son señales de detección, no una lista cerrada de temas.

## 4. Qué NO constituye una receta

No proponer automáticamente una receta por encontrar:

* una definición solicitada
* una explicación conceptual aislada
* una pregunta factual
* una búsqueda bibliográfica
* una tarea administrativa
* organización de carpetas
* productividad personal
* una corrección trivial sin aprendizaje transferible
* código solicitado y aceptado sin discusión, decisión o comprobación
* un tema metodológico que nunca apareció en las interacciones

Una interacción con IA no alcanza por sí sola. Debe existir un aprendizaje práctico reutilizable.

## 5. Evidencia de procedencia

Cada candidata debe conservar internamente:

* source_interaction
* research_task
* problem_or_decision
* role_of_ai
* solution_or_procedure
* validation_or_iteration, si existió
* transferable_learning
* contributor
* platform
* date
* status

El borrador presentado al investigador debe incluir una explicación breve:

“Esta receta surge de una interacción en la que estabas intentando [tarea], apareció [problema] y la interacción permitió desarrollar [solución].”

El investigador debe poder responder:

CREAR RECETA
DESCARTAR
NO ES TRANSFERIBLE

No generar automáticamente una receta completa antes de esta decisión.

## 6. La receta debe enseñar algo

Una receta no puede limitarse a comprobar algo al final.

Al terminarla, otra persona debe haber aprendido a hacer o decidir algo que antes no sabía hacer o decidir.

La estructura conceptual es:

PROBLEMA
→ DECISIÓN O PROCEDIMIENTO
→ IMPLEMENTACIÓN
→ COMPROBACIÓN

La comprobación no reemplaza la enseñanza del procedimiento.

## 7. Escala

Las recetas pueden ser muy cortas.

Una microdecisión metodológica puede ser una receta si surgió de la práctica y es transferible.

No combinar artificialmente varios problemas para producir una receta más grande.

Una receta puede resolver una decisión de 10 minutos o un procedimiento de varias horas.

RecetArIA puede cubrir cualquier etapa del proceso de investigación, pero solamente cuando esa etapa haya aparecido en las interacciones analizadas.

## 8. IA dentro de la receta

Cuando una receta incluya prompts para IA:

* explicar brevemente para qué se utilizará la IA
* hacer una pregunta cerrada por vez cuando corresponda
* incluir “No sé” cuando sea útil
* registrar decisiones
* no asumir información no proporcionada
* separar decisión metodológica de implementación
* preguntar qué herramienta o lenguaje utiliza el investigador antes de generar código, salvo que la receta sea específicamente sobre una herramienta
* incluir una instancia de comprobación cuando corresponda

“Que el código corra” no constituye por sí mismo una validación.

## 9. Estilo editorial

Las recetas deben ser breves, directas y pedagógicas.

Evitar tono de manual genérico.

Evitar tono de IA.

Evitar introducciones innecesarias.

Evitar headings decorativos.

No usar “Prueba del palillo”.

No usar emojis ni stickers.

No usar guiones largos como recurso estilístico.

Puede existir una línea breve de “Si querés ser un mal académico” cuando represente una mala práctica real vinculada con la receta.

## 10. Ejemplos de procedencia válidos

Estos ejemplos provienen del desarrollo real de RecetArIA y sirven como fixtures conceptuales:

### Comparación de prompts

Problema real:
se estaban probando diferentes prompts y modelos para tareas de análisis de texto.

Aprendizaje:
no elegir el prompt porque algunos outputs “parecen mejores”. Mantener una muestra fija, definir criterios antes de comparar y guardar la matriz prompt × modelo × texto.

Receta aprobada:
“Cómo comparar prompts sin elegir el que simplemente te gustó más”.

### Base lista para análisis

Problema real:
antes de modelar era necesario comprobar unidad de análisis, duplicados, missing, valores imposibles y N analítico.

Aprendizaje:
hacer explícitos esos controles antes de avanzar al análisis.

Receta existente:
“Cómo saber si tu base está lista para empezar a analizar”.

Estos ejemplos sirven para entender el mecanismo de procedencia. No deben utilizarse para generar automáticamente recetas similares.

## 11. Contributor Test

Actualizar los tests para comprobar especialmente:

A. El detector encuentra un episodio metodológico real y propone una candidata.

B. El detector rechaza un chat donde solamente se pidió una definición.

C. El detector no inventa una receta para cubrir una etapa metodológica ausente.

D. El detector no utiliza internet para completar candidatos.

E. Dos investigadores con historiales distintos reciben candidatas distintas.

F. El sistema puede detectar una microreceta y no intenta convertirla artificialmente en una guía extensa.

G. Toda candidata mantiene trazabilidad hacia su episodio de origen.

H. Ningún contenido del chat original sale del entorno del contributor sin autorización explícita.

## 12. Arquitectura

Mantené separadas estas funciones:

DETECTOR
encuentra episodios candidatos en las interacciones.

EDITOR
convierte un episodio aprobado por el contributor en un borrador RecetArIA.

VALIDATOR
comprueba que el borrador conserva el aprendizaje del episodio y cumple la estructura editorial.

SUBMISSION
permite enviar únicamente el borrador autorizado al proyecto central.

El DETECTOR no debe escribir directamente una receta final.

El EDITOR no puede inventar metodología ausente en el episodio original.

El contributor no puede marcar una receta como APROBADA en el repositorio central.

Solo el proceso editorial central puede promover DRAFT → APROBADA.


## Entrega al participante

Un único prompt autocontenido, en español o inglés, pegado en el chat de trabajo. Inicia detección en ese turno sobre el contexto disponible. No requiere instalación, ZIP, GitHub, JSON ni scripts para detectar, elegir y redactar. Los archivos técnicos pertenecen al mantenimiento del proyecto.

La privacidad, atribución, licencia pendiente y aprobación editorial central se mantienen. El envío automático sigue requiriendo una conexión real; no se afirma entrega sin comprobante. La confirmación de una candidata para CREAR RECETA no autoriza enviar el borrador.
