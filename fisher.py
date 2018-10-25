from flask import Flask, make_response

app = Flask(__name__)
app.config.from_object('config')


@app.route('/hello')
def hello():
    headers = {
        'content-type': 'application/json'
    }
    return '{"A": 12}', 400, headers


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=app.config['DEBUG'])

