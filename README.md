# RecetArIA Contributor · 0.1.0

Proyecto colaborativo creado y mantenido por **Sol Zoe Nottage**. Convierte problemas reales del trabajo de investigación en recetas breves que el investigador revisa antes de ofrecerlas al proyecto central.

## Empezar sin GitHub ni programación

1. Recibí el ZIP privado de Sol y descomprimilo. No necesitás cuenta de GitHub.
2. Abrí `START_HERE.md`. Copiá su contenido completo en el LLM que uses.
3. Proporcioná solo las conversaciones o fragmentos propios que quieras analizar. No asumas que un prompt puede acceder a otros chats. Revisá qué datos estás compartiendo con tu proveedor antes de pegarlos; podés usar un modelo local.
4. Pedí: «Detectá candidatos en este material y mostrámelos para revisión». Revisá las cinco dimensiones y la evidencia local. Elegí REJECT, EDIT o KEEP para cada candidato.
5. Pedí redactar los candidatos elegidos con el formato incluido. Revisá especialmente datos privados y resultados que no fueron comprobados.
6. Guardá el JSON como archivo local. Para una contribución, revisá el contenido completo y elegí explícitamente SUBMIT para ese draft.

**V0.1 prepara un archivo local; todavía no envía a Drive.** Conservá el archivo hasta que Sol habilite el canal de recepción. No subas chats, drafts ni exportaciones privadas como issues o commits.

## Utilidad local opcional

Requiere Python 3.10 o posterior y solo su biblioteca estándar. No hace llamadas a LLMs ni a Internet.

```sh
python3 recetaria.py validate mi-draft.json
python3 recetaria.py prepare mi-draft.json --out mi-contribucion.json
python3 -m unittest discover -s tests
```

`prepare` muestra el archivo exacto que se va a preparar y solicita `SUBMIT`. Cancelar no crea salida. El resultado es un artefacto local autorizado para envío, no un comprobante de recepción. Usá una carpeta local privada fuera del repositorio para tus archivos.

## Qué incluye

- Una especificación común, prompts de detección, escritura y revisión, y adaptadores manuales para ChatGPT, Claude, Gemini y otros modelos.
- Schema JSON, plantilla de receta y ejemplo sintético que no pertenece al corpus aprobado.
- Protocolos separados para Contributor Test y Recipe Test.
- Documentación de privacidad, atribución y futura recepción controlada en Drive.

Las instrucciones son portables; la calidad y el cumplimiento deben probarse en cada modelo. No incluye acceso automático al historial, ejecución semanal, APIs de modelos ni servicio de recepción desplegado. Cambiar de LLM no garantiza respuestas idénticas: registrá modelo, fecha y versión del paquete.

## Acceso y licencia

Repositorio privado para un piloto de 3–5 investigadores. Sol puede distribuir el mismo ZIP directamente a los participantes. El repositorio privado no es un catálogo de acceso público. Licencia pendiente: ver `LICENSE.md`. Usar Contributor no crea una instancia independiente del proyecto editorial RecetArIA.

## Cuándo puede recibir el OK

Una receta debe estar respaldada por un episodio real, contener instrucciones ejecutables y ser probada por otra persona. El informe registra resultado esperado, observado y comprobaciones; queda vinculado a la versión exacta. Sol conserva la decisión APROBADA. Ver `templates/test_report.json` y `tests/recipe_test.md`. No se afirma haber completado ese piloto.
