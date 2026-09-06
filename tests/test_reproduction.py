import unittest
from datetime import date
from recetaria import load_draft, ROOT
from verify_test import fingerprint, verify
class ReproductionTests(unittest.TestCase):
    def setUp(self):
        self.draft=load_draft(ROOT/'examples/synthetic_draft.json')
        self.report=dict(recipe_sha256=fingerprint(self.draft),tester_id='independent',tested_at=date.today().isoformat(),environment='synthetic unit fixture',source_grounding_checked_locally=True,status='PASSED',checks=[dict(procedure='fixture',expected='fixture',observed='fixture',passed=True)])
    def test_version_record(self): self.assertTrue(verify(self.draft,self.report))
    def test_edit_invalidates(self):
        self.draft['recipe']['steps'].append('New step')
        with self.assertRaises(ValueError): verify(self.draft,self.report)
    def test_unexecuted(self):
        self.report['status']='NOT_TESTED'
        with self.assertRaises(ValueError): verify(self.draft,self.report)
    def test_author_cannot_self_certify(self):
        self.report['tester_id']=self.draft['contributor_id']
        with self.assertRaises(ValueError): verify(self.draft,self.report)
    def test_missing_source_check(self):
        self.report['source_grounding_checked_locally']=False
        with self.assertRaises(ValueError): verify(self.draft,self.report)
    def test_failed_check(self):
        self.report['checks'][0]['passed']=False
        with self.assertRaises(ValueError): verify(self.draft,self.report)
