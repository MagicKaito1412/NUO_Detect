from flask import Flask
app = Flask(__name__,)
app.url_map.strict_slashes = False

if __name__ == '__main__':
    app.run('127.0.0.1', '5010')
