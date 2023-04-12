import pdb
from models.book import Book
from models.author import Author

import repositories.book_repository as book_repository
import repositories.author_repository as author_repository

book_repository.delete_all()
author_repository.delete_all()

author1 = Author("Corrine Sing",)
author_repository.save(author1)
author2 = Author("Euan Crawford")
author_repository.save(author2)

author_repository.select_all()

book_1 = Book("A book by Corrine", author1)
book_repository.save(book_1)

book_2 = Book("A book by Euan", author2)
book_repository.save(book_2)


pdb.set_trace()