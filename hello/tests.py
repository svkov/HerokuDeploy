from django.test import TestCase

from hello.models import Something
# Create your tests here.


class SomeTestCase(TestCase):
    def setUp(self):
        Something.objects.create(name='abc')
        Something.objects.create(name='sjdfsdk')
"""
    def testName(self):
        self.assertEqual(Something.objects.get(id=1).name, 'abc')
        self.assertEqual(Something.objects.get(id=2).name, 'sjdfsdk')

    def testCreation(self):
        name = 'abcdefghklnopqrstuvwxyz'
        Something.objects.create(name=name)
        self.assertEqual(Something.objects.get(id=3).name, name)

"""