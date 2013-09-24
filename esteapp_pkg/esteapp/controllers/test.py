import logging
import traceback
import pdb
from random import choice
from bottle import route, request, abort
from bottle import jinja2_template as template
from esteapp.routes import routes

logger = logging.getLogger("esteapp.app.test")
@route(routes["test"], method=["GET", "POST"])
def testol():
    pdb.set_trace()
    swa = choice([1, 2, 3])

    if swa == 1:
        return {"message": "swa",
                "state": "swo"}
    elif swa == 2:
        return abort(404, "La swa no estaaaaaaaaaa")
    else:
        return template("test.tpl", {'swa': "asdf"})