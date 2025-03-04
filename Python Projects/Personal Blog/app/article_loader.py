import os

ARTICLES_DIR = 'articles'

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