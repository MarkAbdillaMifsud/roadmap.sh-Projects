from flask import Flask, render_template, abort
from article_loader import load_all_articles, get_article_by_slug

app = Flask(__name__, static_folder='static')

@app.route('/')
def home():
    articles = load_all_articles()
    print("Articles loaded:", articles)
    return render_template('home.html', articles=articles)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/articles/<slug>')
def article(slug):
    article_data = get_article_by_slug(slug)
    if article_data is None:
        abort(404)
    return render_template('article.html', article=article_data)
    

if __name__ == '__main__':
    app.run(debug=True)