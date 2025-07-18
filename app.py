import os
from flask import Flask, request, render_template, abort

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ping')
def ping():
    host = request.args.get('host', '')

    # 일부 필터링 – 우회 가능
    if any(x in host for x in [';', '&&', '|']):
        return 'Disallowed characters detected!', 400

    try:
        output = os.popen(f'ping -c 1 {host}').read()
    except Exception as e:
        output = f"Error: {e}"

    return f"<pre>{output}</pre>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
