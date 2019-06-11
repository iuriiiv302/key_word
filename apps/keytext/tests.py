from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APIClient, APIRequestFactory

from django.test import TestCase

from apps.comment.models import Comment
from apps.notification.views import AddNotificationComment

from django.test import TestCase

class TextTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

        response = self.client.post(reverse('token_register'), {
            "first_name": "test_first_name_1",
            "last_name": "test_last_name_1",
            "username": "test_username_1",
            "password": "test_password_1"
        })
        self.assertEqual(response.status_code, 201)

        response = self.client.post(reverse('token_register'), {
            "first_name": "test_first_name_2",
            "last_name": "test_last_name_2",
            "username": "test_username_2",
            "password": "test_password_2"
        })
        self.assertEqual(response.status_code, 201)

        self.user = User.objects.filter(username='test_username_1').first()
        self.assertIsNotNone(self.user)
        self.client.force_authenticate(self.user)

    #Add New TEXT
    def test_text_create(self):
        print("--create task--start")
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.assertIsNotNone(self.user)
        response = self.client.post(reverse('text_add_new'), {
            "key": "string",
            "full_text": "string",
        })
        print(response.status_code)
        self.assertEqual(response.status_code, 201)
        print("--create text--end")
        print("")

    # delete TEXT
    def test_text_delete(self):
        print("--delete text--start")
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.assertIsNotNone(self.user)
        response1 = self.client.post(reverse('text_add_new'), {
            "key": "string",
            "full_text": "string",
        })
        response2 = self.client.delete(reverse('text_deleted', args=(1,)))
        print(response1.status_code)
        print(response2.status_code)

        self.assertEqual(response2.status_code, 204)
        print("--delete text--end")
        print("")

    # GET TEXT_FILTER_KEY
    def test_task_get_mine(self):
        print("--get list text--start")
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.assertIsNotNone(self.user)
        response1 = self.client.post(reverse('text_add_new'), {
            "key": "string",
            "full_text": "string",
        })
        response2 = self.client.get(reverse('text_list_key'))
        print(response1.status_code)
        print(response2.status_code)
        self.assertEqual(response2.status_code, 200)
        print("--get list text--end")
        print("")

    # GET TEXT_All_LIST
    def test_task_get_mine(self):
        print("--get list all--start")
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.assertIsNotNone(self.user)
        response1 = self.client.post(reverse('text_add_new'), {
            "key": "string",
            "full_text": "string",
        })
        response2 = self.client.get(reverse('text_all_list'))
        print(response1.status_code)
        print(response2.status_code)
        self.assertEqual(response2.status_code, 200)
        print("--get list all--end")
        print("")

    # UpdateTEXT by ID
    def test_task_update(self):
        print("--update task--start")
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.assertIsNotNone(self.user)
        response1 = self.client.post(reverse('text_add_new'), {
            "key": "string",
            "full_text": "string",,
        })
        response2 = self.client.put(reverse('text_update'), {
            "id": 1,
            "key": "update_key",
            "full_text": "updated_text",
            })
