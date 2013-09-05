import os
import sys
import bottle
import esteapp
import logging

from esteapp.app import application


HERE = os.path.dirname(os.path.abspath(__file__))
FORMAT = '%(asctime)-15s %(filename)-10s %(levelname)s: %(message)s'

logging.basicConfig(level=logging.DEBUG,
                    format=FORMAT,
                    filemode='w')
logging.getLogger("esteapp").setLevel(logging.CRITICAL)

@bottle.route('/media/:filename#.*#')
def server_static_common(filename):
    MEDIA = os.path.join(os.path.dirname(os.path.abspath(esteapp.__file__)),
                         "static")
    return bottle.static_file(filename, root=MEDIA)

app = application()

try:
    port = int(sys.argv[1])
except:
    port = 8080

bottle.run(app=app, reloader=True, port=port, host='0.0.0.0', server="tornado")