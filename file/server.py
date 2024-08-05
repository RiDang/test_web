import flask
from flask import Flask
import requests



app=Flask(__name__)


@app.route('/', methods=['GET', 'POST'], endpoint='index')
def index():
    print(f">>> request form {flask.request.form}")
    print(f">>> request files {flask.request.files}")
    
    if flask.request.method == "POST":
        obj = flask.request.files.get("uploadfile")
        print(f' - obj {type(obj)}, name {obj.filename}')
        if obj.filename:
            obj.save(obj.filename)
    
    return flask.render_template('index.html')


if __name__ == '__main__':
    # from waitress import serve
    # serve(app, host="0.0.0.0", port=8080)
    app.run(port=3000)