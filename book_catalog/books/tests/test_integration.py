from django.test import TestCase
from django.urls import reverse
from books.models import Book

class BookIntegrationTest(TestCase):
    def test_create_book_and_view_in_list(self):
        response = self.client.post(reverse('book_create'), {
            'title': 'Integration Test Book',
            'author': 'Test Author',
            'publication_year': 2025,
        })

        self.assertEqual(Book.objects.count(), 1)
        book = Book.objects.first()
        self.assertEqual(book.title, 'Integration Test Book')

        response = self.client.get(reverse('book_list'))
        self.assertContains(response, 'Integration Test Book')
        self.assertContains(response, 'Test Author')
        self.assertContains(response, '2025')

    def test_edit_book(self):
        book = Book.objects.create(title='Old Title', author='Old Author', publication_year=2020)

        response = self.client.post(reverse('book_update', args=[book.id]), {
            'title': 'Updated Title',
            'author': 'Updated Author',
            'publication_year': 2025,
        })

        book.refresh_from_db()
        self.assertEqual(book.title, 'Updated Title')
        self.assertEqual(book.author, 'Updated Author')
        self.assertEqual(book.publication_year, 2025)

        response = self.client.get(reverse('book_list'))
        self.assertContains(response, 'Updated Title')
        self.assertContains(response, 'Updated Author')
        self.assertContains(response, '2025')
