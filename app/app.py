from flask import Flask, request
from markupsafe import escape

app = Flask(__name__)

@app.route('/health-check')
def health_check():
    return "<h1>Hello, I'm Alive!</h1>"

@app.route('/hello')
def hello():
    name = request.args.get("name")

    if not name:
        return "Nome não informado", 400
    else:
        return f"Hello, {escape(name)}!"

if __name__ == "__main__": # pragma: no cover
    app.run(debug=False)
    #app.run(host='0.0.0.0')