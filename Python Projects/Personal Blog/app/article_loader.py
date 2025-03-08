import os
import json
import frontmatter  # Make sure to install this package with pip if you haven't already

# Get the directory where this file (article_loader.py) is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# Since the articles folder is one level up from the app folder, join BASE_DIR with '..' and 'articles'
ARTICLES_DIR = os.path.join(BASE_DIR, '..', 'articles')

def extract_article_data(filepath):
    """
    Extracts article metadata and content from a Markdown file
    Requires 'title' and 'publication_date' fields
    """
    _, ext = os.path.splitext(filepath)
    ext = ext.lower()

    if ext == '.md':
        post = frontmatter.load(filepath)
        metadata = post.metadata
        if 'title' not in metadata or 'publication_date' not in metadata:
            raise ValueError(f"Missing required fields in {filepath}")
        return {
            "title": metadata["title"],
            "publication_date": metadata["publication_date"],
            "content": post.content,
            "filepath": filepath
        }
    else:
        raise ValueError(f"Unsupported file type: {ext}")

def load_all_articles(directory=ARTICLES_DIR):
    """
    Loads all articles from the specified directory
    Returns a list of dictionaries with their metadata
    """
    articles = []
    for filename in os.listdir(directory):
        print("Found file:", filename)
        if filename.endswith('.md'):
            filepath = os.path.join(directory, filename)
            try:
                article_data = extract_article_data(filepath)
                articles.append(article_data)
                print("Loaded article:", article_data)
            except Exception as e:
                print(f"Error processing {filepath}: {e}")
    return articles

if __name__ == '__main__':
    # For testing purposes
    articles = load_all_articles()
    print("Filtered article files:", articles)