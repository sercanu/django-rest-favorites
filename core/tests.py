"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class UserTests(APITestCase):
    def test_create_user(self):
        """
        Ensure we can create a new user object.
        """
        user = User()
        user.username = "test"
        user.password = "test"
        user.email = "test@test.com"
        user.save()

        #self.client.login(username='test', password='test')
        expected_data = {'id': 1, 'username': u'test', 'email': u'test@test.com', 'favorites': []}
        self.client.force_authenticate(user=user)
        url = reverse('user-detail', kwargs={"username": "test"})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expected_data)


class FavoritesTests(APITestCase):
    def test_create_favorites(self):
        """
        Ensure we can create a new user object.
        """
        user = User()
        user.username = "test"
        user.password = "test"
        user.email = "test@test.com"
        user.save()

        self.client.force_authenticate(user=user)

        data = {"content": "http://www.test.com", "description": "test url", "owner": "test"}
        url = reverse('favorite-list')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)