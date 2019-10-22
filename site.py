# -*- coding: utf-8 -*-
from flask import Flask

from flask import render_template
from flask import url_for
from flask import Response
from flaskext.markdown import Markdown

import os
import sys
from flask_flatpages import FlatPages
from flask_frozen import Freezer

try:
    import urlparse
except ImportError:
    import urllib.parse as urlparse

from flask import request
from werkzeug.contrib.atom import AtomFeed

DEBUG = True
# FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = ['.md']
FLATPAGES_MARKDOWN_EXTENSIONS = ['codehilite']
FREEZER_DESTINATION = 'rsmarinho.github.io'

class ReverseProxied(object):
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        scheme = environ.get('HTTP_X_FORWARDED_PROTO')
        if scheme:
            environ['wsgi.url_scheme'] = scheme
        return self.app(environ, start_response)

app = Flask(__name__)
app.wsgi_app = ReverseProxied(app.wsgi_app)
app.config.from_object(__name__)

md = Markdown(app, extensions=['mdx_math',
							   'mdx_truly_sane_lists',
							   'extra'],
							   output_format='html5')

pages = FlatPages(app)
freezer = Freezer(app)

# app.jinja_env.lstrip_blocks = True
# app.jinja_env.trim_blocks = True


#Page definitions
title = "Rafael Marinho"
subtitle = md("Currently PhD at <a href=http://xlim.fr>XLIM</a> and Professor at <a href=http://ufpb.br>UFPB</a>.")
icons = [
    {
        'href': 'http://twitter.com/rsmarinhoo',
        'icon': 'fa-twitter',
        'label': 'Twitter'
    },
    {
        'href': 'http://www.linkedin.com/in/rsmarinho',
        'icon': 'fa-linkedin',
        'label': 'Linkedin'
    },
    {
        'href': 'http://instagram.com/rsmarinhoo',
        'icon': 'fa-instagram',
        'label': 'Instagram'
    },
    {
        'href': 'http://github.com/rsmarinho',
        'icon': 'fa-github',
        'label': 'Github'
    },
    {
        'href': 'mailto:rsmarinho@cear.ufpb.br',
        'icon': 'fa-envelope-o',
        'label': 'Email'
    }
]

#Courses Definitions
years = [
    {
        'year': '2019',
        'period': '2'
    },
    {
        'year': '2019',
        'period': '1'
    },
    {
        'year': '2018',
        'period': '2'
    }
]
classes = [
    {
        'year': '2019',
        'period': '2',
        'class': 'Dispositivos Eletrônicos',
        'href': 'dispositivos'
    },
    {
        'year': '2019',
        'period': '2',
        'class': 'Projeto de Circuitos Integrados',
        'href': 'projeto'
    },
    {
        'year': '2019',
        'period': '1',
        'class': 'Dispositivos Eletrônicos',
        'href': 'dispositivos'
    },
    {
        'year': '2019',
        'period': '1',
        'class': 'Estrutura e concepção de Circuitos Integrados',
        'href': 'estrutura'
    },
    {
        'year': '2018',
        'period': '2',
        'class': 'Dispositivos Eletrônicos',
        'href': 'dispositivos'
    },
    {
        'year': '2018',
        'period': '2',
        'class': 'Projeto de Circuitos Integrados',
        'href': 'projeto'
    }
]
# course = 'home';

@app.route('/')
# @app.route('/index/')
def index():
    return render_template('index.html',
    title=title,
		subtitle=subtitle,
		icons=icons,
		years=years,
		classes=classes,
		home=pages.get_or_404(os.path.join('home')),
		production=pages.get_or_404(os.path.join('production')))

# @app.route('/<path:path>/')
# def page(path):
# 	page = pages.get_or_404(path)
# 	return render_template('index.html',
# 		title=title,
# 		subtitle=subtitle,
# 		icons=icons,
# 		years=years,
# 		classes=classes,
# 		page=page)

# Rota para as aulas
@app.route('/<string:tpath>/<string:aula>/')
def course_class(tpath,aula):
	filename = tpath + '/' + aula
	content = os.path.join('courses/', filename)
	page = pages.get_or_404(content)
	return render_template('course_page.html',
			title=title,
			subtitle=subtitle,
			icons=icons,
			page=page)

# Rota para Cursos aulas
@app.route('/<string:tpath>/<string:ano>/<string:sem>/')
def course_year(tpath, ano, sem):
	filename = ano + '_' + sem + '_' + tpath
	if tpath in [classes[x]['href'] for x in range(0,len(classes))]:
		content = os.path.join('courses/' + filename )
		page = pages.get_or_404(content)
		# page = 'courses/' + filename
		return render_template('course_page.html',
			title=title,
			subtitle=subtitle,
			icons=icons,
			page=page)
	else:
		return render_template('error_pages/404.html')

@freezer.register_generator
def course_class_gen():
	path = os.path.join(app.root_path, 'pages/courses')
	courses = next(os.walk(path))[1]
	for course in courses:
		c = next(os.walk(path + '/' + course))[2]
		for classy in c:
			classy = classy.replace('.md','')
			yield '/' + course + '/' + classy + '/'

@app.route('/dispositivos/')
def dispositivos():
	ano = classes[0]['year']
	sem = classes[0]['period']
	content = os.path.join('courses/' + ano + '_' + sem + '_dispositivos')
	page = pages.get_or_404(content)
	# page = 'courses/' + filename
	return render_template('course_page.html',
		title=title,
		subtitle=subtitle,
		icons=icons,
		page=page)

@app.route('/projeto/')
def projeto():
	ano = classes[0]['year']
	sem = classes[0]['period']
	content = os.path.join('courses/' + ano + '_' + sem + '_projeto')
	page = pages.get_or_404(content)
	# page = 'courses/' + filename
	return render_template('course_page.html',
		title=title,
		subtitle=subtitle,
		icons=icons,
		page=page)

# @app.route('/estrutura/')
# def estrutura():
# 	ano = classes[0]['year']
# 	sem = classes[0]['period']
# 	content = os.path.join('courses/' + ano + '_' + sem + '_estrutura')
# 	page = pages.get_or_404(content)
# 	# page = 'courses/' + filename
# 	return render_template('course_page.html',
# 		title=title,
# 		subtitle=subtitle,
# 		icons=icons,
# 		page=page)

# run the application
if __name__ == '__main__':
	# from warnings import simplefilter as filter_warnings
	# filter_warnings('ignore', 'flask_frozen.MissingURLGeneratorWarning')
	if len(sys.argv) > 1 and sys.argv[1] == "build":
		print("Building website...")
		app.debug = False
		app.testing = True
		freezer.freeze()
		print("Done.")
	else:
		# app.run(port=5555)
		app.jinja_env.auto_reload = True
		app.config['TEMPLATES_AUTO_RELOAD'] = True
		app.run(debug=True, use_reloader=False, host='0.0.0.0')
