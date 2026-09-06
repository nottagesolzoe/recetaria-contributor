"""Check version-bound reproduction records. Does not grant editorial approval."""
import hashlib
import json
import sys
from datetime import date
from pathlib import Path
from recetaria import load_draft, no_duplicate_keys

def fingerprint(draft):
    payload={key:draft[key] for key in ['original_recipe_id','recipe_version','recipe']}
    return hashlib.sha256(json.dumps(payload,sort_keys=True,ensure_ascii=False,separators=(',',':')).encode()).hexdigest()

def verify(draft, report):
    if set(report) != {'recipe_sha256','tester_id','tested_at','environment','source_grounding_checked_locally','status','checks'}:
        raise ValueError('Unexpected or missing report fields')
    if report['recipe_sha256'] != fingerprint(draft):
        raise ValueError('Recipe changed or report belongs to another version; retest')
    if report['status'] != 'PASSED' or report['source_grounding_checked_locally'] is not True:
        raise ValueError('Reproduction and local source verification are required')
    for field in ['tester_id','environment','tested_at']:
        if not isinstance(report[field],str) or not report[field].strip():
            raise ValueError('Missing test context')
    if report['tester_id'].strip()==draft['contributor_id'].strip():
        raise ValueError('Independent tester required')
    if date.fromisoformat(report['tested_at'])>date.today():
        raise ValueError('Test cannot be dated in the future')
    if not isinstance(report['checks'],list) or not report['checks']:
        raise ValueError('At least one observed check is required')
    for check in report['checks']:
        if not isinstance(check,dict) or set(check)!={'procedure','expected','observed','passed'}:
            raise ValueError('Unexpected or missing check fields')
        if check['passed'] is not True:
            raise ValueError('A check failed or is incomplete')
        if any(not isinstance(check[k],str) or not check[k].strip() for k in ['procedure','expected','observed']):
            raise ValueError('Concrete expected and observed results are required')
    return True

if __name__=='__main__':
    try:
        if len(sys.argv) not in [2,3]: raise ValueError('Usage: python3 verify_test.py draft.json [report.json]')
        draft=load_draft(sys.argv[1])
        if len(sys.argv)==2: print(fingerprint(draft))
        else:
            verify(draft,json.loads(Path(sys.argv[2]).read_text(),object_pairs_hook=no_duplicate_keys))
            print('Version and report structure verified. Sol must assess evidence and decide; no editorial approval granted.')
    except (ValueError,OSError,TypeError,KeyError) as error:
        print(f'NO AVANZAR: {error}',file=sys.stderr);sys.exit(1)
