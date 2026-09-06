# Adaptador manual: local

Usá START_HERE.md completo como instrucciones en una conversación con el modelo elegido. Proporcioná después únicamente los episodios que autorizás a analizar. Si la interfaz admite instrucciones persistentes, podés guardar allí el mismo contenido; no hace falta hacerlo para el piloto.

Pedí primero que indique qué material puede leer. No asumas acceso entre chats, a un historial completo, a archivos no adjuntados ni a tareas programadas. Si el contexto no alcanza, procesá episodios por separado y conservá los IDs locales para evitar duplicados.

Registrá plataforma, modelo exacto si se conoce (si no, «unknown»), fecha y versión 0.1.0. Exportá el JSON y seguí la revisión común. Este adaptador es un procedimiento manual portable, no una integración API probada. Para modelos locales, revisá que tu ejecutor esté configurado para procesamiento local. Para servicios remotos, proporcionar texto lo comparte con ese proveedor aunque no lo envíe a RecetArIA.

No modifica criterios, estados ni permisos de la especificación común.
