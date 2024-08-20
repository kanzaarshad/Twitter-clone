# -*- coding: utf-8 -*-
"""Twitter clone.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1PnPbSgNo7TWW0KPsnTqqTZfJO48GLLB1
"""

import datetime
import uuid

class User:
    def __init__(self, username):
        self.username = username
        self.user_id = str(uuid.uuid4())
        self.tweets = []

    def post_tweet(self, content):
        tweet = {
            "tweet_id": str(uuid.uuid4()),
            "content": content,
            "timestamp": datetime.datetime.now()
        }
        self.tweets.append(tweet)
        return tweet

    def view_tweets(self):
        return self.tweets

class TwitterClone:
    def __init__(self):
        self.users = {}

    def create_user(self, username):
        if username in self.users:
            print("Username already taken. Please choose another one.")
        else:
            user = User(username)
            self.users[username] = user
            print(f"User '{username}' created successfully!")

    def post_tweet(self, username, content):
        if username not in self.users:
            print("User not found. Please create an account first.")
        else:
            tweet = self.users[username].post_tweet(content)
            print(f"Tweet posted by {username}: {tweet['content']}")

    def view_user_tweets(self, username):
        if username not in self.users:
            print("User not found.")
        else:
            tweets = self.users[username].view_tweets()
            if not tweets:
                print(f"{username} has not posted any tweets yet.")
            else:
                for tweet in tweets:
                    print(f"{tweet['timestamp']}: {tweet['content']}")

    def view_all_tweets(self):
        for username, user in self.users.items():
            print(f"\nTweets by {username}:")
            self.view_user_tweets(username)

# Initialize the TwitterClone app
twitter_app = TwitterClone()

# Create users
twitter_app.create_user("Alice")
twitter_app.create_user("Bob")

# Post tweets
twitter_app.post_tweet("Alice", "Hello, world! This is my first tweet!")
twitter_app.post_tweet("Bob", "Hi everyone, Bob here!")

# View tweets by individual users
print("\n--- Alice's Tweets ---")
twitter_app.view_user_tweets("Alice")

print("\n--- Bob's Tweets ---")
twitter_app.view_user_tweets("Bob")

# View all tweets
print("\n--- All Tweets ---")
twitter_app.view_all_tweets()