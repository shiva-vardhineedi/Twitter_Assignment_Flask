'''
Author: Sri Charan Reddy, Mahek Virani
Contents: This file has create and delete tweet APIs
'''

import tweepy
import config

from flask import Flask, render_template, request, jsonify, redirect, url_for

app = Flask(__name__, static_folder="static")

# Store tweets in a dictionary
tweets = {}

client = tweepy.Client(
    consumer_key=config.API_KEY,
    consumer_secret=config.API_SECRET,
    access_token=config.ACCESS_TOKEN,
    access_token_secret=config.ACCESS_TOKEN_SECRET,
)

'''
Author: Sri Charan Reddy
Contents: Routes to the home html content
'''
@app.route("/")
def index():
    print(tweets)
    return render_template("home.html", tweets=tweets)

'''
Author: Sri Charan Reddy
Contents:  This API creates the tweet based on request { 'tweetText' : 'user input'}
'''
@app.route("/create_tweet", methods=["POST"])
def create_tweet():
    text = request.form.get("tweetText")
    response = client.create_tweet(text=text)
    tweets[response.data["id"]] = {
        "text": response.data["text"],
        "id": response.data["id"],
    }
    print("Tweet created with message: ", text)
    return redirect(url_for("index"))

'''
Author: Mahek Virani
Contents: This API deletes the tweet with {tweet_id}
'''
@app.route("/delete_tweet/<tweet_id>", methods=["POST"])
def delete_tweet(tweet_id):
    response = client.delete_tweet(id=tweet_id)
    print("deleted tweet with id", tweet_id)

    tweets.clear()
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
