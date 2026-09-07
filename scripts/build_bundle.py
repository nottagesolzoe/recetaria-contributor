"""Build participant prompts with no external file requirements or private data."""
from pathlib import Path
import zipfile
root=Path(__file__).resolve().parents[1]
files=['system_prompt.md','recipe_detector.md','recipe_writer.md','recipe_validator.md','submission_review.md']
spanish='\n\n'.join((root/'prompts'/name).read_text().strip() for name in files)+'\n'
english=(root/'prompts/contributor_en.md').read_text()
(root/'PARA_COPIAR_EN_EL_CHAT.txt').write_text(spanish)
(root/'PASTE_IN_CHAT_EN.txt').write_text(english)
# Preserve the old entry point for existing links; it is the same plain prompt.
(root/'START_HERE.md').write_text(spanish)
(root/'dist').mkdir(exist_ok=True)
with zipfile.ZipFile(root/'dist/recetaria-prompts-es-en.zip','w',compression=zipfile.ZIP_DEFLATED) as archive:
    archive.writestr('RecetArIA-ES.txt',spanish)
    archive.writestr('RecetArIA-EN.txt',english)
print('Participant package: two alternative prompts, one per language.')
