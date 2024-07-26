from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from books.models import Book, BookReview
from users.models import CustomUser


class BookReviewAPITestCase(APITestCase):
    def setUp(self):
        self.user = CustomUser.objects.create(username="Marufjon", first_name="Marufjon")
        self.user.set_password("somepass")
        self.user.save()

    def test_book_review_detail(self):
        book = Book.objects.create(title="Book1", description="Description1", isbn="123121")
        br = BookReview.objects.create(book=book, user=self.user, stars_given=5, comment="Very good book")

        response = self.client.get(reverse('api:review-detail', kwargs={'id': br.id}))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['id'], br.id)
        self.assertEqual(response.data['stars_given'], 5)
        self.assertEqual(response.data['comment'], "Very good book")

        # TestCase for books model
        self.assertEqual(response.data['book']['id'], br.book.id)
        self.assertEqual(response.data['book']['title'], 'Book1')
        self.assertEqual(response.data['book']['description'], 'Description1')
        self.assertEqual(response.data['book']['isbn'], '123121')

        # TestCase for user model
        self.assertEqual(response.data['user']['id'], self.user.id)
        self.assertEqual(response.data['user']['first_name'], "Marufjon")
        self.assertEqual(response.data['user']['username'], "Marufjon")

    def test_book_review_list(self):
        user_two = CustomUser.objects.create(username="Somebody", first_name="Somebody")
        book = Book.objects.create(title="Book1", description="Description1", isbn="123121")
        br = BookReview.objects.create(book=book, user=self.user, stars_given=5, comment="Very good book")
        br_two = BookReview.objects.create(book=book, user=user_two, stars_given=3, comment="So bad book. Not recommend")

        response = self.client.get(reverse('api:review-list'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)

        self.assertEqual(response.data[0]['id'], br_two.id)
        self.assertEqual(response.data[0]['stars_given'], br_two.stars_given)
        self.assertEqual(response.data[0]['comment'], br_two.comment)

        self.assertEqual(response.data[1]['id'], br.id)
        self.assertEqual(response.data[1]['stars_given'], br.stars_given)
        self.assertEqual(response.data[1]['comment'], br.comment)