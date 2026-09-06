"""Rebuild the self-contained prompt from canonical sources."""
from pathlib import Path
root=Path(__file__).resolve().parents[1]
files=['prompts/system_prompt.md','prompts/recipe_detector.md','prompts/recipe_writer.md','prompts/submission_review.md','templates/recipe_draft.md']
text='# RecetArIA Contributor 0.1.0 · paquete portable\n\nCopiá este documento completo como instrucciones. Proporcioná el material fuente por separado.\n\n'
text+='\n\n'.join((root/f).read_text() for f in files)
text+='\n\n# Contrato JSON\n\n```json\n'+(root/'schemas/recipe_draft.schema.json').read_text()+'```\n'
(root/'START_HERE.md').write_text(text)

(root/'PARA_COPIAR_EN_EL_CHAT.txt').write_text(text)
