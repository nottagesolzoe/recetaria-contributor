# Arquitectura

Conversaciones autorizadas en el entorno del investigador → detección con un LLM elegido por él → candidatos y evidencia local → selección → draft generalizado → previsualización y SUBMIT → archivo local → futura recepción RecetArIA → Drive privado → revisión de Sol.

La especificación canónica está en prompts/system_prompt.md. START_HERE.md se genera concatenando los cuatro prompts, plantilla y schema. Los adaptadores solo explican cómo suministrar el mismo contrato. La utilidad Python no detecta recetas: valida el esquema y prepara el artefacto sin red. No hay dependencia de GitHub en ejecución.

El ZIP contiene una lista explícita de archivos del paquete, no carpetas de trabajo ni chats. Conservar versión de paquete y modelo permite comparar ejecuciones, pero no garantiza determinismo del LLM. La automatización semanal y adaptadores API son trabajo futuro, no funcionalidades de esta versión.
