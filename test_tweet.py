'''
Author: Sri Charan Reddy
Contents: This file has create and delete twitter APIs
'''

import unittest
from unittest.mock import  patch
import tweet

class TestTweetApp(unittest.TestCase):

    def setUp(self):
        self.app = tweet.app.test_client()
        self.app.testing = True
        tweet.tweets.clear()

    def tearDown(self):
        tweet.tweets.clear()

    @patch('tweet.client.create_tweet')
    def test_create_tweet_route(self, mock_create_tweet):
        mock_create_tweet.return_value.data = {
            "id": 12345,
            "text": "Test tweet"
        }
        response = self.app.post("/create_tweet", data={'tweetText': 'test tweet'})
        self.assertEqual(response.status_code, 302)
        self.assertIn(12345, tweet.tweets)

    @patch('tweet.client.delete_tweet')
    def test_delete_tweet_route(self, mock_delete_tweet):

        tweet.tweets[1234] = {"id": 1234, "text": "Test tweet"}
        mock_delete_tweet.return_value = None
        response = self.app.post("/delete_tweet/1234")
        self.assertEqual(response.status_code, 302)  # Check for a redirect
        self.assertNotIn(1234, tweet.tweets)  # Check if tweet was removed from 'tweets' dictionary
