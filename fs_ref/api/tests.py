# -*- coding: utf8 -*-
from django.core.urlresolvers import reverse
from django.test import RequestFactory
from django.utils import unittest
from fs_ref.api import views


class ApiSmokeTest(unittest.TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_list_references(self):
        request = self.factory.get(reverse('api.list_references'))
        response = views.references.list_references(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/json')
