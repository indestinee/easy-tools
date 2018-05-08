# http://docs.jinkan.org/docs/flask/quickstart.html#quickstart
from flask import Flask
import re, argparse

app = Flask(__name__)

result = 'Hello World!<br>'
with open('./main.py', 'r') as f:
    data = f.read()
urls = re.compile('route\(\'(.*?)\'\)').findall(data)
host = '127.0.0.1/'
for suffix in urls:
    result += '<a href=\'%s\'>%s</a><br>' % (suffix, suffix)
result += '<br><br><br>'

@app.route('/')
def hello_world():
    return result
    

@app.route('/ucas_net')
def net():
    from net.main import main
    return result + main()


@app.route('/reboot')
def reboot():
    from reboot.main import main
    return result + main()


def get_args():
    parser = argparse.ArgumentParser(description='easy net')
    parser.add_argument('--host', default='127.0.0.1', type=str)
    parser.add_argument('--port', default=5000, type=int)
    args = parser.parse_args()
    return args

if __name__ == '__main__':
    args = get_args()
    app.run(host=args.host, port=args.port)
