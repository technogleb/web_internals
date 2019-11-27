import os.path
import time

__all__ = ['index', 'article']


def render_template(template):
    with open(os.path.join('templates', '.'.join((template, 'html')))) as f:
        return f.read()


def index():
    time.sleep(5)
    return render_template('index')


def article():
    return render_template('article')
