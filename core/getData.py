from _ast import arguments

import requests
import gzip
import json
from .models import Book

list_of_books = []


class Books:
    def __init__(self, author, title, publish_date, ISBN, counts_page, image, language):
        self.author = author
        self.title = title
        self.publish_date = publish_date
        self.ISBN = ISBN
        self.counts_page = counts_page
        self.image = image
        self.language = language

    def __str__(self):
        return f'{self.author, self.title, self.publish_date, self.ISBN, self.image, self.language}'


def getdata(arguments):
    print(arguments)
    url = f'https://www.googleapis.com/books/v1/volumes?q={arguments[0]}+intitle:{arguments[1]}'\
          f'+inauthor:{arguments[2]}'
    if arguments[5]:
        url = f'https://www.googleapis.com/books/v1/volumes?q=flow{arguments[0]}ers+intitle:{arguments[1]}+inauthor:{arguments[2]}' \
          f'+inpublisher:{arguments[3]}+subject:{arguments[4]}+isbn:{arguments[5]}'
    elif arguments[6]:
        url = f'https://www.googleapis.com/books/v1/volumes?q=flow{arguments[0]}ers+intitle:{arguments[1]}' \
              f'+inauthor:{arguments[2]}+inpublisher:{arguments[3]}+subject:{arguments[4]}+lccn:{arguments[6]}'
    elif arguments[7]:
        url = f'https://www.googleapis.com/books/v1/volumes?q=flow{arguments[0]}ers+intitle:{arguments[1]}+inauthor:{arguments[2]}' \
          f'+inpublisher:{arguments[3]}+subject:{arguments[4]}+oclc:{arguments[7]}'
    print(f'URLLLL {url}')
    response = requests.get(url)
    json_format = json.loads(response.text)
    print(json_format)

    for book in json_format['items']:
        title = book['volumeInfo']['title'].replace('"', "")

        if 'authors' in book['volumeInfo']:
            author = book['volumeInfo']['authors'][0]
        else:
            author = 'Does not exist'

        if 'publishedDate' in book['volumeInfo']:
            published_date = book['volumeInfo']['publishedDate'][:4] + '-01-01'
        else:
            published_date = '1000-10-10'

        if 'industryIdentifiers' in book['volumeInfo']:
            ISBN = book['volumeInfo']['industryIdentifiers'][0]['identifier']
        else:
            ISBN = 0

        if 'pageCount' in book['volumeInfo']:
            pageCount = book['volumeInfo']['pageCount']
        else:
            pageCount = '0000'

        if 'imageLinks' in book['volumeInfo']:
            imageLinks = book['volumeInfo']['imageLinks']['smallThumbnail']
        else:
            imageLinks = 'Does not exist'

        if 'language' in book['volumeInfo']:
            language = book['volumeInfo']['language']

        else:
            language = 'Not said'

        book = Book(title=title, autor=author, date_publish=published_date, ISBN_number=ISBN, counts_page=pageCount,
                    link_poster=imageLinks, language=language)
        book.save()
        books = Books(title=title, author=author, publish_date=published_date, ISBN=ISBN,
                      counts_page=pageCount, image=imageLinks, language=language)
        list_of_books.append(books)
