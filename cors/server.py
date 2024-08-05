import json
import sys
import flask
from flask import Flask, jsonify, request, render_template
app = Flask(__name__)
 
 # 目标域服务器 127.0.0.1:3000
@app.route('/cors', methods=['GET'])
def hello_world():
    print(f" - log {5000}", request.headers)
    callback = request.args.get('callback')
    result = json.dumps({"a":1})
    response = f"{callback}({result})"

    return response, 200, {'Content-Type': 'application/javascript'}

# 本地域服务器 127.0.0.1:3000
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

 
if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=5000, debug=True)
    if len(sys.argv) != 2:
        print(f' should set poort for different server')
    app.run(port=int(sys.argv[1]))