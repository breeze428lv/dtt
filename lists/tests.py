from django.urls import resolve
from django.http import HttpRequest
from django.test import TestCase
from lists.views import home_page

# Create your tests here.
'''
class SmokeTest(TestCase):
    def test_bad_maths(self):
        self.assertEqual(1 + 1, 3)
'''


class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['item_text'] = 'A new list item'
        response = home_page(request)
        print(response.content.decode())
        # self.assertTrue(response.content.startswith(b'<html>'))
        # self.assertIn(b'<title>To-Do lists</title>', response.content)
        # self.assertTrue(response.content.endswith(b'</html>'))


'''
======================================================================
Traceback (most recent call last):
  File "/home/breeze/PycharmProjects/TddPrj(TestDrivenDevelopment)/Prj01/superlists/lists/tests.py", line 15, in test_root_url_resolves_to_home_page_view
    found = resolve('/')
  File "/home/breeze/.local/lib/python3.8/site-packages/django/urls/base.py", line 24, in resolve
    return get_resolver(urlconf).resolve(path)
  File "/home/breeze/.local/lib/python3.8/site-packages/django/urls/resolvers.py", line 702, in resolve
    raise Resolver404({"tried": tried, "path": new_path})
django.urls.exceptions.Resolver404: {'tried': [[<URLPattern 'admin/' [name='home']>]], 'path': ''}


'''