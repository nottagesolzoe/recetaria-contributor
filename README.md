# RecetArIA Contributor · 0.1.0

Proyecto colaborativo creado y mantenido por **Sol Zoe Nottage**. Convierte problemas reales del trabajo de investigación en recetas breves que el investigador revisa antes de ofrecerlas al proyecto central.

## Empezar sin GitHub ni programación

Español: **[INSTRUCCIONES.txt](INSTRUCCIONES.txt)** + [PARA_COPIAR_EN_EL_CHAT.txt](PARA_COPIAR_EN_EL_CHAT.txt).

English: **[INSTRUCTIONS_EN.txt](INSTRUCTIONS_EN.txt)** + [PASTE_IN_CHAT_EN.txt](PASTE_IN_CHAT_EN.txt).

**Abrí la guía de tu idioma.** Es la guía paso a paso para participantes, sin programación ni instalación de software.

**Funciona en el momento:** al pegar las instrucciones, analiza el contenido disponible de ese chat y propone candidatos. No espera una semana ni revisa otras conversaciones automáticamente.

Solo necesitás esa guía y [PARA_COPIAR_EN_EL_CHAT.txt](PARA_COPIAR_EN_EL_CHAT.txt). El segundo archivo contiene las instrucciones completas listas para pegar en el chat donde resolviste un problema. Se genera desde las mismas fuentes que START_HERE.md.

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
