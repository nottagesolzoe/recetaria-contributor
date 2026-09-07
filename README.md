# RecetArIA Contributor

Proyecto creado y dirigido por **Sol Zoe Nottage**, con crédito para quienes contribuyen recetas. Detecta aprendizajes de interacciones reales de investigación con IA y los convierte en recetas breves.

## Para participar

**Copiá un solo prompt y pegalo en el chat donde resolviste un problema.** No hace falta descargar este repositorio, instalar software, abrir una carpeta ni usar GitHub.

- Español: [prompt completo](PARA_COPIAR_EN_EL_CHAT.txt).
- English: [complete prompt](PASTE_IN_CHAT_EN.txt).

Sol puede copiar el texto y entregarlo directamente. Empieza en ese momento, propone candidatas y espera «CREAR RECETA», «DESCARTAR» o «NO ES TRANSFERIBLE». Después muestra la receta en el chat, con preparación, uso de IA, implementación y comprobación.

## Qué queda detrás de ese recorrido

[RECETARIA_SPEC.md](RECETARIA_SPEC.md) es la especificación central. Los componentes DETECTOR, EDITOR, VALIDATOR y SUBMISSION están separados en prompts/. El registro de procedencia es local y no se adjunta al draft. El esquema de candidatos es distinto del contrato de envío existente. Las utilidades Python son opcionales para mantenimiento; el participante no necesita conocerlas.

```sh
python3 scripts/build_bundle.py
python3 -m unittest discover -s tests
```

El script genera los prompts de ambos idiomas y un ZIP de entrega con solo esos dos textos, sin código ni archivos de desarrollo. El repositorio conserva la infraestructura existente. Los protocolos de detección con LLM y de ejecución de recetas están separados; pasar pruebas del software no acredita esos protocolos.

## Estado del envío y la revisión

La confirmación explícita autoriza únicamente la versión mostrada. El envío automático a Drive requiere una conexión real, todavía no desplegada. El prompt no puede crearla ni afirmar una entrega sin comprobante. Mientras no esté habilitada, el borrador permanece en el chat; no se exige contactar a Sol ni descargar archivos para generar la receta.

El estado central sigue siendo DRAFT hasta la revisión editorial de Sol. La reproducción por otra persona precede al OK; un LLM no puede inventarla. El repositorio sigue privado y la licencia permanece pendiente. Ver LICENSE.md.
