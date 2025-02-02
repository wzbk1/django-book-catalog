from django.test import TestCase
from books.models import Book

class BookModelTest(TestCase):
    def test_book_creation(self):
        book = Book.objects.create(title="Test Book", author="Test Author", publication_year=2025)
        self.assertEqual(book.title, "Test Book")
        self.assertEqual(book.author, "Test Author")
        self.assertEqual(book.publication_year, 2025)

    def test_book_year(self):
        book = Book(title="Another Book", author="Author Name", publication_year=2020)
        self.assertEqual(book.publication_year, 2020)
