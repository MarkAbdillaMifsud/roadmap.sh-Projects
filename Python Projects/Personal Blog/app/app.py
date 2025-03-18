from flask import Flask, render_template, request, redirect, url_for, flash, session, abort
from article_loader import load_all_articles, get_article_by_slug
import config

app = Flask(__name__, static_folder='static')

# Load configuration from config.py
app.config.from_pyfile('config.py')

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

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    if username == config.ADMIN_USERNAME and password == config.ADMIN_PASSWORD:
        session['admin_logged_in'] = True
        return redirect(url_for('admin_dashboard'))
    else:
        flash('Invalid credentials. Please try again.')
        return redirect(url_for('admin'))

@app.route('/admin/dashboard')
def admin_dashboard():
    if not session.get('admin_logged_in'):
        flash("You need to log in first.")
        return redirect(url_for('admin'))
    return render_template('admin_dashboard.html')

if __name__ == '__main__':
    app.run(debug=True)