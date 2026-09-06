import copy
import json
import tempfile
import unittest
from pathlib import Path
import recetaria
from submission import submit_to_drive

class DraftTests(unittest.TestCase):
    def setUp(self):
        self.value = recetaria.load_draft(recetaria.ROOT/'examples/synthetic_draft.json')
        self.schema = json.loads((recetaria.ROOT/'schemas/recipe_draft.schema.json').read_text())
    def test_extra_raw_history_rejected(self):
        self.value['raw_chat'] = 'private'
        with self.assertRaises(ValueError): recetaria.validate(self.value,self.schema)
    def test_nested_extra_rejected(self):
        self.value['recipe']['source_url'] = 'private'
        with self.assertRaises(ValueError): recetaria.validate(self.value,self.schema)
    def test_no_editorial_approval(self):
        self.value['status']='APROBADA'
        with self.assertRaises(ValueError): recetaria.validate(self.value,self.schema)
    def test_score_is_integer_not_boolean(self):
        self.value['scores']['transferability_score']=True
        with self.assertRaises(ValueError): recetaria.validate(self.value,self.schema)
    def test_duplicate_keys(self):
        with self.assertRaises(ValueError): json.loads('{"a":1,"a":2}',object_pairs_hook=recetaria.no_duplicate_keys)
    def test_cancel_even_if_input_claims_consent(self):
        self.value['consent_to_submit']=True
        with tempfile.TemporaryDirectory() as folder:
            target=Path(folder)/'draft.json'
            self.assertFalse(recetaria.prepare(self.value,target,lambda _: 'KEEP',lambda _: None))
            self.assertFalse(target.exists())
    def test_exact_preview_and_no_source_mutation(self):
        original=copy.deepcopy(self.value)
        with tempfile.TemporaryDirectory() as folder:
            target=Path(folder)/'draft.json'; displayed=[]
            self.assertTrue(recetaria.prepare(self.value,target,lambda _: 'SUBMIT',displayed.append))
            self.assertEqual(target.read_text(),displayed[1])
            self.assertTrue(recetaria.load_draft(target)['consent_to_submit'])
            self.assertEqual(original,self.value)
            with self.assertRaises(FileExistsError): recetaria.prepare(self.value,target,lambda _: 'SUBMIT',lambda _: None)
    def test_plain_language_confirmation(self):
        for answer in ['sí','SI','yes','SUBMIT']:
            with tempfile.TemporaryDirectory() as folder:
                target=Path(folder)/'draft.json'
                self.assertTrue(recetaria.prepare(self.value,target,lambda _, a=answer:a,lambda _:None))
                self.assertTrue(target.exists())
    def test_transport_fails_closed(self):
        with self.assertRaises(NotImplementedError): submit_to_drive(self.value)
    def test_synthetic_date_result(self):
        from datetime import datetime
        result=datetime.strptime('03/04/2024','%d/%m/%Y')
        self.assertEqual((result.day,result.month,result.year),(3,4,2024))
        with self.assertRaises(ValueError): datetime.strptime('31/02/2024','%d/%m/%Y')

if __name__=='__main__': unittest.main()
