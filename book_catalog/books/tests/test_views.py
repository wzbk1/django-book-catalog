from django.test import TestCase
from django.urls import reverse
from books.models import Book

class BookViewsTest(TestCase):
    def test_create_book_view(self):
        response = self.client.post(reverse('book_create'), {
            'title': 'New Book',
            'author': 'Author Name',
            'publication_year': 2025,
        })
        self.assertEqual(response.status_code, 302) 
        self.assertEqual(Book.objects.count(), 1)
        self.assertEqual(Book.objects.first().title, 'New Book')

    def test_book_list_view(self):
        Book.objects.create(title='Test Book', author='Test Author', publication_year=2025)
        response = self.client.get(reverse('book_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Book')
