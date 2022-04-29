
import unittest
from flask import url_for
import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
projdir = os.path.dirname(parentdir)
sys.path.append(projdir)

from core import app

class BasicTests(unittest.TestCase):

    ''' Setup and teardown '''

    ''' executed prior to each test '''
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        self.app = app.test_client()
        self.assertEqual(app.debug, False)

    ''' executed after each test '''
    def tearDown(self):
        pass


    ''' Helper Methods '''
    def decode(self, url):
        return self.app.post(
            '/decode',
            json={'shortest': url},
            headers={'Content-Type': 'application/json'},
            follow_redirects=True
        )

    def encode(self, url):
        return self.app.post(
            '/encode',
            json={'original': url},
            headers={'Content-Type': 'application/json'},
            follow_redirects=True
        )


    def redirect_url(self, id):
        return self.app.get(
                id
        )


    ''' Tests '''
    def test_main_page(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
    
    def test_valid_encode(self):
        response = self.encode('https://translate.google.com/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'shortest', response.data)

    ''' This might fail initially since you don't have the URL in your cache memory. 
        To fix this, run the app and encode a URL. Then use the reponse 'shortest' 
        url instead of 'http://127.0.0.1:5000/7xA6h8td' for running the test 
    '''
    def test_valid_decode(self):
        response = self.decode('http://127.0.0.1:5000/7xA6h8td')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'original', response.data)

    ''' This might fail initially since you don't have the URL in your cache memory. 
        To fix this, run the app and encode a URL. Then use the reponse 'id' instead 
        of '7xA6h8td' url for running the test 
    '''
    def test_valid_redirect_url(self):
        response = self.redirect_url('7xA6h8td')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.location, 'https://translate.google.com/')



if __name__ == "__main__":
    unittest.main()


 