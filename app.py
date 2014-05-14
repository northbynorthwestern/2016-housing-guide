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

    return render_template('index.html', **make_context())

@app.route('/hall/<string:slug>/')
def _detail(slug):

    context = make_context()

    context['dorm'] = []
    context['images'] = []
    context['quotes'] = []
    context['slug'] = ''

    dorms = list(context['COPY']['dorms'])
    images = list(context['COPY']['images'])
    quotes = list(context['COPY']['quotes'])
    dorm_name = ''

    for dorm in dorms:
        dorm = dict(zip(dorm.__dict__['_columns'], dorm.__dict__['_row']))
        dorm_slug = dorm.get('slug')

        if dorm_slug == slug:
            context['dorm'] = dorm
            context['slug'] = str(slug)
            dorm_name = dorm.get('name')


    for image in images:
        image = dict(zip(image.__dict__['_columns'], image.__dict__['_row']))
        image_dorm = image.get('dorm')

        if image_dorm == dorm_name:
            context['images'].append(image)

    for quote in quotes:
        quote = dict(zip(quote.__dict__['_columns'], quote.__dict__['_row']))
        quote_dorm = quote.get('dorm')

        if quote_dorm == dorm_name:
            context['quotes'].append(quote)

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
