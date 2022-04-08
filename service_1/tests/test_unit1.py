import pytest, pytest_cov
from flask import url_for
from flask_testing import TestCase
from requests_mock import mock
import unittest
from service_1.app import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):

    def test_index(self):
        
        with mock() as m:
            m.get('http://service_2:5000/get/alc_drink', text='Lager')
            m.get('http://service_3:5000/get/soft_drink', text='Water')
            m.post('http://service_4:5000/post/round', json=0.00)

            response = self.client.get(url_for('home'))

        self.assert200(response)

        self.assertIn('Your round has one alcholic drink and a soft drink for £0.0', response.data.decode())

        

        















