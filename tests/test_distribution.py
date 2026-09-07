import unittest
import zipfile
from recetaria import ROOT
class ParticipantDistributionTests(unittest.TestCase):
    def test_participant_zip_excludes_development_and_private_files(self):
        with zipfile.ZipFile(ROOT/'dist/recetaria-prompts-es-en.zip') as archive:
            self.assertEqual(set(archive.namelist()),{'RecetArIA-ES.txt','RecetArIA-EN.txt'})
            for name in archive.namelist():
                text=archive.read(name).decode()
                self.assertNotIn('"$schema"',text)
                self.assertNotIn('snottage@',text)
    def test_legacy_entrypoint_uses_current_spanish_prompt(self):
        self.assertEqual((ROOT/'START_HERE.md').read_bytes(),(ROOT/'PARA_COPIAR_EN_EL_CHAT.txt').read_bytes())
