from django.test import TestCase
from .models import Post

class PostTests(TestCase):
    def setUp(self):

        Post.objects.create(
            firstname='Eli',
            lastname='Eiche',
            content='Eli said something',
            upvotes=8,
            downvotes=9
        )


    def test_summary(self):
        post = Post.objects.get(lastname='Eiche')
        self.assertEqual(post.summary(),
                     'Eiche: Eli said something')

    def test__str__(self):

        post = Post.objects.get(lastname='Eiche')
        self.assertEqual(post.__str__(), 'Eiche +8 -9')
