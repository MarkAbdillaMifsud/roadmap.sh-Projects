import os
import json
import frontmatter  # Make sure to install this package with pip if you haven't already

# Get the directory where this file (article_loader.py) is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# Since the articles folder is one level up from the app folder, join BASE_DIR with '..' and 'articles'
ARTICLES_DIR = os.path.join(BASE_DIR, '..', 'articles')

def load_article_files(directory='articles'):
    article_files = [
        file for file in os.listdir(ARTICLES_DIR)
        if file.endswith('.md')
    ]
    return article_files

if __name__ == '__main__':
    # For testing purposes
    articles = load_article_files()
    print("Filtered article files:", articles)