import os.path as osp
import flask
from flask import Flask
import requests


_cur_dir = osp.dirname(__file__)
_data_dir = osp.join(_cur_dir, '../data/')
app=Flask(__name__)
# def after_request(resp):
#     resp.headers['Access-Control-Allow-Origin'] = '*'
#     return resp
# app.after_request(after_request)

@app.route('/video', methods=['GET', 'POST'])
def video():
    name = flask.request.values.get('name')
    return flask.send_from_directory(_data_dir, name, as_attachment=True)

@app.route('/', methods=['GET', 'POST'])
def websockets():
    # print(f" >>> websockets values {flask.request.values.to_dict()}")
    # print(f" >>> form values {flask.request.form.to_dict()}")
    resp = flask.make_response(flask.render_template('index.html'))
    resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers['who'] = 'dd'
    return resp


if __name__ == '__main__':
    # from waitress import serve
    # serve(app, host="0.0.0.0", port=8080)
    
    app.run(port=3000)