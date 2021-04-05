from flask import Flask, render_template
from vsearch import search4letters


app = Flask(__name__)
@app.route('/')
def hello() -> str:
    return 'hello world from flask!'
@app.route('/search4')
def do_search() -> str:
    return ''.join(search4letters('life, the universe, and everything!', 'eiru,!'))
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', the_title='Welcome to search for letters on the web!')


app.run()
