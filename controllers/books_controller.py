from flask import Blueprint, render_template, request, redirect
from repositories import book_repository, author_repository
from models.book import Book

books_blueprint = Blueprint("books", __name__)

# INDEX
# GET /books
@books_blueprint.route("/books")
def books():
    all_books = book_repository.select_all()
    return render_template('books/index.html', all_books=all_books)

# NEW
# GET /books/new
@books_blueprint.route("/books/new")
def new_book():
    authors = author_repository.select_all()
    return render_template('books/new.html', all_authors = authors)

# CREATE
# POST /books
@books_blueprint.route("/books", methods=["POST"])
def create_book():
    title = request.form['title']
    author_id = request.form['author_id']  

    author = author_repository.select(author_id)
    book = Book(title, author)
    book_repository.save(book)

    return redirect('/books')

# SHOW 
# GET /books/<id>
@books_blueprint.route("/books/<id>")
def show_book(id):
    book_from_repository = book_repository.select(id)
    return render_template('books/show.html', book=book_from_repository)

# EDIT
# GET /books/<id>/edit
@books_blueprint.route("/books/<id>/edit")
def edit_book(id):
    book = book_repository.select(id)
    authors = author_repository.select_all()
    return render_template('books/edit.html', book=book, all_authors=authors)

# UPDATE 
# PUT (POST) /books/<id>
@books_blueprint.route("/books/<id>", methods=['POST'])
def update_book(id):
    title = request.form['title']
    author_id = request.form['author_id']

    author = author_repository.select(author_id)
    book = Book(title, author, id)
    book_repository.update(book)
    return redirect('/books/' + id)


# DELETE
# DELETE (POST) /books/<id>/delete
@books_blueprint.route("/books/<id>/delete", methods=["POST"])
def delete_book(id):
    book_repository.delete(id)
    return redirect('/books')