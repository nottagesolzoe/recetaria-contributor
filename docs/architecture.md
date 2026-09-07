# Arquitectura

Participante: pega un único prompt en su chat de trabajo → recibe candidatas basadas en episodios reales → elige CREAR RECETA → recibe el borrador → revisa y prueba → autoriza una versión si decide contribuir.

Mantenimiento: RECETARIA_SPEC.md gobierna DETECTOR (recipe_detector.md), EDITOR (recipe_writer.md), VALIDATOR (recipe_validator.md) y SUBMISSION (submission_review.md). system_prompt.md establece activación, alcance y rol. scripts/build_bundle.py compone el prompt español y prepara ambos idiomas sin schema ni archivos externos requeridos por el participante.

candidate.schema.json describe el registro local de procedencia; recipe_draft.schema.json sigue siendo el contrato técnico de exportación. No se adjunta provenance al contrato de envío. La utilidad Python valida estructura y prepara artefactos localmente; no detecta episodios ni envía a Drive. verify_test.py vincula informes a la versión exacta sin conceder aprobación.

La traducción inglesa vive en contributor_en.md y debe mantener la misma metodología. El ZIP para participantes contiene dos textos alternativos, uno por idioma; solo deben pegar uno. La infraestructura y los tests permanecen en el repositorio privado. Enviar desde un chat sigue necesitando un adaptador conectado a un receptor; no se simula esa capacidad.
