from flask import Flask, render_template
from markupsafe import escape
from articles import articles


app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template('index.html',
                           title='Главная страница',
                           articles=articles)


@app.route('/articles/<int:article_id>')
def get_article(article_id):
    return render_template('article.html',
                           article=articles[article_id - 1])


if __name__ == '__main__':
    app.run()
