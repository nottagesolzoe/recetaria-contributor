# Cambio a un único prompt por participante

## Inspección

DETECTOR, EDITOR y SUBMISSION ya existían en prompts/. Se conservaron y actualizaron. Faltaba un componente explícito VALIDATOR de contenido; verify_test.py comprueba informes de reproducción, no sustituye esa revisión. recipe_draft.schema.json es el contrato de envío, no un registro local de candidatos. Se agregó el contrato de candidatos sin exponer su procedencia en el draft.

## Archivos creados

- RECETARIA_SPEC.md: reglas centrales entregadas por Sol.
- schemas/candidate.schema.json: procedencia local estructurada.
- prompts/recipe_validator.md: revisión de aprendizaje, procedencia y estructura.
- tests/detection_cases/conversations.json: cinco conversaciones sintéticas para evaluación A–H.
- tests/test_provenance.py: seis pruebas del contrato local y su separación del envío.
- tests/test_distribution.py: dos pruebas de distribución sin infraestructura ni schemas.
- docs/editorial_reference.md y este informe.

## Archivos modificados

- prompts/system_prompt.md, recipe_detector.md, recipe_writer.md, submission_review.md y contributor_en.md.
- templates/recipe_draft.md y schemas/recipe_draft.schema.json (ironía opcional; prompt de implementación opcional, sin romper drafts existentes).
- scripts/build_bundle.py y los tres archivos generados PARA_COPIAR_EN_EL_CHAT.txt, PASTE_IN_CHAT_EN.txt y START_HERE.md.
- README.md, INSTRUCCIONES.txt, INSTRUCTIONS_EN.txt, adapters/*.md, docs/architecture.md y tests/contributor_test.md.
- CHANGELOG.md.

## Decisiones

Sol confirmó usar la especificación recién aportada. La presentación sigue los encabezados de su receta de Drive, manteniendo implementación y comprobación separadas; la línea de mala práctica es opcional. No se modificaron documentos fuente en Drive, licencia, permisos, propiedad ni transporte. La infraestructura continúa en el repositorio privado y no forma parte de la entrega del participante.

## Pendientes

El envío automático todavía no tiene receptor desplegado. El prompt no lo simula. Los protocolos A–H con un LLM y el piloto con investigadores deben ejecutarse y documentarse; las pruebas de contratos y empaquetado no demuestran calidad de detección. La revisión editorial central y la prueba de reproducción siguen separadas de la aceptación de una candidata.

## ZIP para participantes

```text
recetaria-prompts-es-en.zip
├── RecetArIA-ES.txt
└── RecetArIA-EN.txt
```

Cada persona recibe únicamente el texto de su idioma. No necesita el ZIP ni el repositorio: Sol puede copiar y entregar ese prompt directamente.
