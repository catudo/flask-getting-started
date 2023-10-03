import flask
from flask_classful import FlaskView
from models.example_model import Example
from flask import request, render_template
import json


class ExampleView(FlaskView):

    def index(self):
        return render_template("example.html")

    def get_examples(self):
        email = str(request.args.get('client_email'))
        params = {"client_email": email}
        data = Example().get_examples(params)

        options_resp = flask.Response(json.dumps(data[0]), mimetype='application/json')
        options_resp.headers.add(
            'Access-Control-Expose-Headers', 'X-Total-Count')
        options_resp.headers.add(
            'Access-Control-Expose-Headers', 'Content-Range')
        options_resp.headers.add('Content-Range', 'bytes : 0-9/*')
        options_resp.headers.add('X-Total-Count', str(data[1]))
        return options_resp
