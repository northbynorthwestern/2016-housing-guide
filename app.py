#!/usr/bin/env python

import argparse
from flask import Flask, render_template

import app_config
from render_utils import make_context, urlencode_filter
import static

app = Flask(app_config.PROJECT_NAME)

app.jinja_env.filters['urlencode'] = urlencode_filter

# Example application views
@app.route('/')
def index():
    """
    Example view demonstrating rendering a simple HTML page.
    """
    context = make_context()

    context['dorms'] = data.load()

    with open('www/static-data/data.json') as f:
        context['speeches_json'] = Markup(f.read())

    return render_template('index.html', **context)

@app.route('/hall/<string:slug>/')
def _detail(slug):
    """
    Example view demonstrating rendering a simple HTML page.
    """
    context = make_context()

    context['dorms'] = data.load()
    dorm  = next(s for s in context['dorm'] if s['slug'] == slug)
    context['dorm'] = dorm

    with open('www/static-data/data-thin.json') as f:
        context['dorms_json'] = Markup(f.read())

    return render_template('detail.html', **context)

app.register_blueprint(static.static)

# Boilerplate
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--port')
    args = parser.parse_args()
    server_port = 8000

    if args.port:
        server_port = int(args.port)

    app.run(host='0.0.0.0', port=server_port, debug=app_config.DEBUG)
