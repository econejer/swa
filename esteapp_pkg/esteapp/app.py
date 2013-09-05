import os
import logging
import bottle
import logging.config

from beaker.middleware import SessionMiddleware


HERE = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_DIR = os.path.join(HERE, "templates")
DEFAULT_SESSION_DATADIR = "/tmp/"

def session_start(app, cookie_path='/'):

    dir = DEFAULT_SESSION_DATADIR

    if not os.path.exists(dir):
        os.makedirs(dir)

    session_opts = {
        'session.type': 'file',
        'session.cookie_expires': 3600 * 24, # 1 dia
        'session.data_dir': dir,
        'session.auto': True,
        'session.path': cookie_path
        }

    return SessionMiddleware(app, session_opts)

def _setup_bottle(bottle, environ):
    bottle.TEMPLATE_PATH = [TEMPLATE_DIR]

@bottle.route('/media/:filename#.*#')
def server_static_common(filename):
    MEDIA = os.path.join(os.path.dirname(os.path.abspath(esteapp.__file__)),
                         "static")
    return bottle.static_file(filename, root=MEDIA)

def application(environ=None, start_response=None):
    import bottle
    _setup_bottle(bottle, environ)
    _application = bottle.default_app()

    _application = session_start(bottle.default_app(), '/admin')

    from bottle import Jinja2Template
    from esteapp.controllers import test

    names = []
    for m in [test]:
        names.append(m.__name__)

    if environ and start_response:
        _application = _application(environ, start_response)

    return _application
