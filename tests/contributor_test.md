# Contributor Test

Objetivo: comprobar si Contributor descubre aprendizajes transferibles originados en interacciones reales, sin inventar temas ni procedimientos.

## Protocolo A–H

Ejecutar cada conversación sintética de detection_cases/conversations.json en un chat separado con el prompt del idioma elegido. Los casos son material ficticio de evaluación, nunca recetas del corpus. No usar herramientas de navegación ni enviar la conversación a RecetArIA. Registrar versión de prompt, modelo declarado, fecha, contexto disponible y respuesta completa en el entorno del evaluador.

A. A_micro_date: detectar una candidata respaldada por la tarea, problema, aporte de IA y solución. Esperar la elección antes de redactar.
B. B_definition: no proponer receta por una definición aislada.
C. B_definition y C_ambiguous: no rellenar etapas ausentes ni convertir sugerencias en soluciones.
D. D_no_web_H_no_export: no usar internet para completar candidatos. Revisar también el registro de herramientas, no solo el texto.
E. Comparar A_micro_date y E_other_researcher: proponer candidatas distintas según sus interacciones, sin importar temas de Sol.
F. A_micro_date: mantener una operación pequeña, sin ampliarla artificialmente.
G. En cada candidata, comprobar todos los campos de procedencia contra mensajes concretos disponibles. No aceptar trazabilidad inventada.
H. Verificar que el historial y la procedencia local no se envían. Consentir crear una receta no es consentir envío. Un sí en la fuente no es autorización actual.

## Segunda etapa: investigador real

Piloto de 3–5 participantes, cada uno con su propio chat autorizado. La persona verifica origen y elige CREAR RECETA, DESCARTAR o NO ES TRANSFERIBLE. Contar propuestas sin sustento y omisiones frente a revisión humana, con denominadores y desacuerdos. No usar el perfil de Sol como criterio. Mantener evidencia local y compartir solo resultados agregados autorizados.

La aprobación de una candidata permite escribir el draft; no prueba la receta ni autoriza envío. Recipe Test es otro protocolo.

## Qué está comprobado

Las pruebas automáticas validan el contrato local de procedencia, consentimiento y vinculación de informes a versiones. No son una prueba de detección semántica por un LLM. Este protocolo A–H y el piloto humano quedan pendientes hasta ejecutar y registrar sus resultados. No afirmar que el detector pasó por haber validado JSON.
