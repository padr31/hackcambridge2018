from . import landing

import os
import datetime
import flask
import logging
import json
import time

from flask import (
    #Flask,
    abort,
    redirect,
    render_template,
    request,
    url_for,
    Response,
    session
)

logger = logging.getLogger("web.landing.views")

def make_error_response(description):
    return flask.Response(
        json.dumps({"status": "error", "message": description}),
        status=400,
        content_type="application/json")


@landing.route('/', methods=['GET'])
@landing.route('/index', methods=['GET','POST'])
def index():
    return render_template('index.html', page_title='Home')
