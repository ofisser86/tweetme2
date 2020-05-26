from django.test import TestCase
from django.contrib.auth import get_user_model
# Create your tests here.
from .models import Tweet

from rest_framework.test import APIClient

User = get_user_model()


class TweetTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="greta", password='some')
        self.user_b = User.objects.create_user(username="greta2", password='some2')
        Tweet.objects.create(content='hello First test tweet',
                             user=self.user)
        Tweet.objects.create(content='hello Second test tweet',
                             user=self.user)
        Tweet.objects.create(content='hello Third test tweet',
                             user=self.user_b)
        self.currentCount = Tweet.objects.all().count()

    def test_user_created(self):
        self.assertEqual(self.user.username, 'greta')

    def test_tweet_created(self):
        tweet_obj = Tweet.objects.create(content='hello Forth tests tweet', user=self.user)
        self.assertEqual(tweet_obj.id, 4)
        self.assertEqual(tweet_obj.user, self.user)

    def get_client(self):
        client = APIClient()
        client.login(username=self.user.username, password='some')
        return client

    def test_tweet_list(self):
        client = self.get_client()
        response = client.get('/api/tweets/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 3)

    def test_tweet_action_like(self):
        client = self.get_client()
        response = client.post('/api/tweets/action/', {'id': 1,  'action': 'like', })
        like_count = response.json().get('likes')
        self.assertEqual(like_count, 1)
        
        self.assertEqual(response.status_code, 200)
        print(response.json())
        # self.assertEqual(len(response.json()), 3)

    def test_tweet_action_unlike(self):
        client = self.get_client()
        response = client.post('/api/tweets/action/',
                               {'id': 2, 'action': 'like'})
        self.assertEqual(response.status_code, 200)
        response = client.post('/api/tweets/action/',
                               {'id': 2, 'action': 'unlike'})
        self.assertEqual(response.status_code, 200)
        like_count = response.json().get('likes')
        self.assertEqual(like_count, 0)

    def test_tweet_action_retweet(self):
        client = self.get_client()
        current_count = self.currentCount
        response = client.post('/api/tweets/action/',
                               {'id': 2, 'action': 'retweet'})
        self.assertEqual(response.status_code, 201)
        data = response.json()
        new_tweet_id = data.get('id')
        self.assertNotEqual(2, new_tweet_id)
        self.assertEqual(current_count + 1, new_tweet_id)

    def test_tweet_create_api_view(self):
        request_data = {'content': 'data tweet'}
        current_count = self.currentCount
        client = self.get_client()
        response = client.post('/api/tweets/create/', request_data)
        self.assertEqual(response.status_code, 201)
        response_data = response.json()
        new_tweet_id = response_data.get('id')
        self.assertEqual(current_count + 1, new_tweet_id)

    def test_tweet_detail_api_view(self):
        client = self.get_client()
        response = client.get('/api/tweets/1/')
        self.assertEqual(response.status_code, 200)
        data = response.json()
        _id = data.get('id')
        self.assertEqual(_id, 1)

    def test_tweet_delete_api_view(self):
        client = self.get_client()
        response = client.delete('/api/tweets/1/delete/')
        self.assertEqual(response.status_code, 200)
        data = response.json()
        message = data.get('message')
        self.assertEqual(message, 'Tweet removed')
        response = client.delete('/api/tweets/1/delete/')
        self.assertEqual(response.status_code, 404)
        response_incorrect_owner = client.delete('/api/tweets/3/delete/')
        self.assertEqual(response_incorrect_owner.status_code, 403)


