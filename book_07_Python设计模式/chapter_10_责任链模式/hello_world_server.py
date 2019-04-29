# pip install uwsgi
# uwsgi --http :9090 --wsgi-file hello_world_server.py

import pprint

pp = pprint.PrettyPrinter(indent=4)

def application(env, start_response):
    pp.pprint(env)

    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b"Hello World"]

