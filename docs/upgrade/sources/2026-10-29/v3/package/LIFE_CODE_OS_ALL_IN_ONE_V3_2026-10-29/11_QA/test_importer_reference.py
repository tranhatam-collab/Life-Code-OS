from pathlib import Path
import tempfile,subprocess,hashlib,json,shutil,importlib.util,sys
sys.dont_write_bytecode = True
R=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('imp',R/'12_IMPORT/import_into_repo.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
checks=[]
def run(*args,cwd=None):
 r=subprocess.run(list(args),cwd=cwd,capture_output=True,text=True);assert r.returncode==0,r.stderr;return r.stdout.strip()
def manifest(p):
 fs=[{'path':x.relative_to(p).as_posix(),'bytes':x.stat().st_size,'sha256':hashlib.sha256(x.read_bytes()).hexdigest()} for x in sorted(p.rglob('*')) if x.is_file() and x.name!='MANIFEST.json']
 (p/'MANIFEST.json').write_text(json.dumps({'files':fs}))
def setup(base,branch='review/v3',remote='https://github.com/tranhatam-collab/Life-Code-OS.git'):
 repo=base/'repo';repo.mkdir();run('git','init','-b',branch,cwd=repo);run('git','config','user.email','qa@example.invalid',cwd=repo);run('git','config','user.name','Local QA',cwd=repo);run('git','remote','add','origin',remote,cwd=repo)
 (repo/'README.md').write_text('baseline');run('git','add','README.md',cwd=repo);run('git','commit','-m','baseline',cwd=repo)
 p=base/'package';p.mkdir();shutil.copy2(R/'VERIFY_PACKAGE.py',p/'VERIFY_PACKAGE.py');(p/'sample.txt').write_text('unchanged baseline');manifest(p);return p,repo

def case(name,fn):
 try:fn();checks.append({'case':name,'passed':True})
 except Exception as e:checks.append({'case':name,'passed':False,'error':str(e)})
def expect_refused(fn):
 try:fn()
 except (ValueError,FileNotFoundError):return
 raise AssertionError('Expected refusal')

def dryapply():
 with tempfile.TemporaryDirectory() as td:
  p,r=setup(Path(td));plan=m.preflight(p,r);assert not(r/m.TARGET).exists();receipt=m.apply(p,r,plan);assert receipt['added']==3;assert(r/'README.md').read_text()=='baseline';assert not receipt['deploy'];assert (r/m.TARGET/'sample.txt').read_text()=='unchanged baseline'
case('dry_run_and_add_only',dryapply)
for branch in ['main','master','production']:
 def f(branch=branch):
  with tempfile.TemporaryDirectory() as td:
   p,r=setup(Path(td),branch=branch);expect_refused(lambda:m.preflight(p,r))
 case('reject_'+branch,f)
def wrongremote():
 with tempfile.TemporaryDirectory() as td:
  p,r=setup(Path(td),remote='https://github.com/example/other.git');expect_refused(lambda:m.preflight(p,r))
case('reject_wrong_project',wrongremote)
def dirty():
 with tempfile.TemporaryDirectory() as td:
  p,r=setup(Path(td));(r/'untracked.txt').write_text('dirty');expect_refused(lambda:m.preflight(p,r))
case('reject_dirty_tree',dirty)
def badhash():
 with tempfile.TemporaryDirectory() as td:
  p,r=setup(Path(td));(p/'sample.txt').write_text('changed');expect_refused(lambda:m.preflight(p,r))
case('reject_checksum_change',badhash)
def conflict():
 with tempfile.TemporaryDirectory() as td:
  p,r=setup(Path(td));d=r/m.TARGET;d.mkdir(parents=True);(d/'sample.txt').write_text('other');run('git','add','.',cwd=r);run('git','commit','-m','conflict fixture',cwd=r);expect_refused(lambda:m.preflight(p,r))
case('reject_existing_different',conflict)
def identical():
 with tempfile.TemporaryDirectory() as td:
  p,r=setup(Path(td));d=r/m.TARGET;d.mkdir(parents=True);shutil.copy2(p/'sample.txt',d/'sample.txt');run('git','add','.',cwd=r);run('git','commit','-m','identical fixture',cwd=r);plan=m.preflight(p,r);assert sum(x['action']=='IDENTICAL_SKIP' for x in plan['plan'])==1
case('skip_existing_identical',identical)
def traversal():
 with tempfile.TemporaryDirectory() as td:
  p,r=setup(Path(td));j=json.loads((p/'MANIFEST.json').read_text());j['files'][0]['path']='../escape';(p/'MANIFEST.json').write_text(json.dumps(j));expect_refused(lambda:m.preflight(p,r))
case('reject_path_traversal',traversal)
def symlink():
 with tempfile.TemporaryDirectory() as td:
  p,r=setup(Path(td));(r/'docs').symlink_to(Path(td)/'outside');run('git','add','.',cwd=r);run('git','commit','-m','symlink fixture',cwd=r);expect_refused(lambda:m.preflight(p,r))
case('reject_destination_symlink',symlink)
def unsafeurl():
 expect_refused(lambda:m.remote_name('https://token@github.com/tranhatam-collab/Life-Code-OS.git'))
case('reject_credentials_in_remote',unsafeurl)
receipt={'checked_on':'2026-10-29','mode':'temporary_local_git_repositories_only','tests':len(checks),'passed':sum(x['passed'] for x in checks),'failed':sum(not x['passed'] for x in checks),'results':checks,'remote_mutations':False,'production_mutations':False}
(R/'11_QA/IMPORTER_TEST_RECEIPT.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2));print(json.dumps(receipt,ensure_ascii=False,indent=2))
