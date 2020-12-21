import json
from django.conf import settings

# Book Genre list
def book_genre():
    with open(settings.BASE_DIR / 'data/book_genre.json') as f:
        data = json.loads(f.read())
    return data or None
BOOK_GENRE = book_genre()

# book edition list
def book_edition():
    with open(settings.BASE_DIR / 'data/book_edition.json') as f:
        data = json.loads(f.read())
    return data or None
BOOK_EDITION = book_edition()

