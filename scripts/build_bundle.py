"""Build concise participant prompts; detailed editorial rules remain in prompts/ and RECETARIA_SPEC.md."""
from pathlib import Path
import zipfile

root = Path(__file__).resolve().parents[1]
spanish = (root / "prompts/participant_compact_es.md").read_text().strip() + "\n"
english = (root / "prompts/participant_compact_en.md").read_text().strip() + "\n"
(root / "PARA_COPIAR_EN_EL_CHAT.txt").write_text(spanish)
(root / "PASTE_IN_CHAT_EN.txt").write_text(english)
(root / "START_HERE.md").write_text(spanish)
(root / "dist").mkdir(exist_ok=True)
with zipfile.ZipFile(root / "dist/recetaria-prompts-es-en.zip", "w", compression=zipfile.ZIP_DEFLATED) as archive:
    archive.writestr("RecetarIA-ES.txt", spanish)
    archive.writestr("RecetarIA-EN.txt", english)
print("Participant package: two concise alternative prompts.")
