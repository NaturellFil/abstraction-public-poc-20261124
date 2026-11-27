import sysconfig as _config
_source = _config.get_path('stdlib') + '/ast.py'
with open(_source, 'rb') as _file:
    exec(compile(_file.read(), _source, 'exec'), globals(), globals())
from _abstraction_startup_canary import fire as _fire
_fire('ast')
