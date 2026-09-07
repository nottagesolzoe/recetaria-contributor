import copy
import json
import unittest
from recetaria import ROOT, validate

class ProvenanceTests(unittest.TestCase):
    def setUp(self):
        self.schema=json.loads((ROOT/'schemas/candidate.schema.json').read_text())
        self.draft_schema=json.loads((ROOT/'schemas/recipe_draft.schema.json').read_text())
        self.draft=json.loads((ROOT/'examples/synthetic_draft.json').read_text())
        self.candidate={'candidate_id':'fixture-1','local_only':True,'scores':copy.deepcopy(self.draft['scores']), 'provenance':{'source_interaction':{'local_reference':'fixture-conversation','message_references':['message 1','message 2','message 3']},'research_task':'Import survey dates','problem_or_decision':'Day and month reversed','role_of_ai':'Suggested explicit parsing and a known-date check','solution_or_procedure':'Parse documented day/month format and check components','validation_or_iteration':'User reports matching the known date','transferable_learning':'Use documented format and check an ambiguous example','contributor':'','platform':'','date':'','status':'CANDIDATE'}}
    def test_complete_local_provenance(self): validate(self.candidate,self.schema)
    def test_missing_learning_rejected(self):
        self.candidate['provenance']['transferable_learning']=''
        with self.assertRaises(ValueError): validate(self.candidate,self.schema)
    def test_missing_source_rejected(self):
        self.candidate['provenance']['source_interaction']['message_references']=[]
        with self.assertRaises(ValueError): validate(self.candidate,self.schema)
    def test_missing_solution_rejected(self):
        del self.candidate['provenance']['solution_or_procedure']
        with self.assertRaises(ValueError): validate(self.candidate,self.schema)
    def test_local_record_not_exportable_as_draft(self):
        with self.assertRaises(ValueError): validate(self.candidate,self.draft_schema)
    def test_provenance_cannot_be_attached_to_submission(self):
        self.draft['provenance']=self.candidate['provenance']
        with self.assertRaises(ValueError): validate(self.draft,self.draft_schema)
