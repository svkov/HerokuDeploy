from django.test import TestCase, Client

from hello.models import Something


# Create your tests here.


class SomeTestCase(TestCase):
    def setUp(self):
        Something.objects.create(text='abc')
        Something.objects.create(text='sjdfsdk')

    def testName(self):
        self.assertEqual(Something.objects.get(id=1).text, 'abc')
        self.assertEqual(Something.objects.get(id=2).text, 'sjdfsdk')

    def testCreation(self):
        name = 'abcdefghklnopqrstuvwxyz'
        Something.objects.create(text=name)
        self.assertEqual(Something.objects.get(id=3).text, name)


class TestViews(TestCase):
    client = None

    def setUp(self):
        self.client = Client()

    def testHelloWorld(self):
        ans = self.client.get('/')
        self.assertEqual(ans.status_code, 200)
