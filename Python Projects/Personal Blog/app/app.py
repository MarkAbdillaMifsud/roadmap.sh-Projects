from flask import Flask, render_template
from article_loader import load_article_files

app = Flask(__name__, static_folder='static')

@app.route('/')
def home():
    articles = load_article_files()
    return render_template('home.html', articles=articles)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)