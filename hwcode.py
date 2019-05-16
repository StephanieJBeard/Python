""" hwcode.py
    Write the code for the HW exercises in this file.
"""

import json


def total_number_of_users(jsonl_filename):
    '''
    Returns the total number of tweets in jsonl_filename
    :param str jsonl_filename: The file path of the twitter dataset
    :return: The total number (int) of tweets
    '''
    # Write code for exercise 1 part 1 here
    total = 0
    return total

def total_number_of_tweets(jsonl_filename):
    '''
    Returns the total number of tweets in jsonl_filename
    :param str jsonl_filename: The file path of the twitter dataset
    :return: The total number (int) of tweets
    '''
    # Write code for exercise 1 part 1 here
    total = 0
    return total

def average_tweets_per_user(jsonl_filename):
    '''
    Returns the average number of tweets per user
    :param str jsonl_filename: The file path of the twitter dataset
    :return: The average number (float) of tweets tweeted by a user
    '''
    # Write code for exercise 1 part 2 here
    average = 0.0
    return average

def max_tweets_per_user(jsonl_filename):
    '''
    Returns the max number of tweets made by a user
    :param str jsonl_filename: The file path of the twitter dataset
    :return: The max number (int) of tweets tweeted by a user
    '''
    # Write code for exercise 1 part 2 here
    max_tweets = 0
    return max_tweets

def user_with_most_tweets(jsonl_filename):
    '''
    Returns the user who made the most tweets
    :param str jsonl_filename: The file path of the twitter dataset
    :return: The screen_name (a string) of the user with the most tweets
    '''
    # Wrte code for exercise 1 part 3 here
    user_tweetsalot = ''
    return user_tweetsalot

def classify_tweets(jsonl_filename, positive_lexicon, negative_lexicon):
    '''
    Classifies each tweet in jsonl_filename as either having positive
    or negative sentiment.

    :param str jsonl_filename: The file path of the twitter dataset
    :param list positive_lexicon: A list of words that represent
                                  positive sentiment
    :param list negative_lexicon: A list of words that represent
                                  negative sentiment
    :return: A list of predictions (a list of strings "positive"
             or "negative") with a prediction for each tweet
    '''
    # Write code for exercise 2 part 1 here
    predictions = []
    return predictions

def most_negative_tweet(jsonl_filename, positive_lexicon, negative_lexicon):
    '''
    Return the tweet that is the "most" negative - has the most negative words.

    :param str jsonl_filename: The file path of the twitter dataset
    :param list positive_lexicon: A list of words that represent
                                  positive sentiment
    :param list negative_lexicon: A list of words that represent
                                  negative sentiment
    :return: The most negatives tweet text (string) 
    '''
    most_negative_tweet = ''
    # Write code for exercise 2 part 2 here.
    return most_negative_tweet
 
def most_positive_tweet(jsonl_filename, positive_lexicon, negative_lexicon):
    '''
    Return the tweet that is the "most" positive - has the most positive words.

    :param str jsonl_filename: The file path of the twitter dataset
    :param list positive_lexicon: A list of words that represent
                                  positive sentiment
    :param list negative_lexicon: A list of words that represent
                                  negative sentiment
    :return: The most negatives tweet text (string) 
    '''
    # Write code for the exercise 2 part 2 here.
    most_positive_tweet = ''
    return most_positive_tweet
 
def most_negative_users(jsonl_filename, positive_lexicon, negative_lexicon, min_tweets):
    '''
    Return the 10 most negative users in the jsonl_filename dataset.

    :param str jsonl_filename: The file path of the twitter dataset
    :param list positive_lexicon: A list of words that represent
                                  positive sentiment
    :param list negative_lexicon: A list of words that represent
                                  negative sentiment
    :param int min_tweets: The minimum number of tweets a user must have
                           to be considered the most positive.
    :return: A list of the 10 most negative users (screen names /strings)
             in the dataset.
    '''
    # Write code for the exercise 2 part 3 here.
    most_negative_users = ["a user"] * 10
    return most_negative_users

def most_positive_users(jsonl_filename, positive_lexicon, negative_lexicon, min_tweets):
    '''
    Return the 10 most positive users in the jsonl_filename dataset.

    :param str jsonl_filename: The file path of the twitter dataset
    :param list positive_lexicon: A list of words that represent
                                  positive sentiment
    :param list negative_lexicon: A list of words that represent
                                  negative sentiment
    :param int min_tweets: The minimum number of tweets a user must have
                           to be considered the most positive.
    :return: A list of the 10 most positive users (screen names /strings)
             in the dataset.
    '''
    # Write code for the exercise 2 part 3 here.
    most_positive_users = ['a user'] * 10
    return most_positive_users

def dates_with_most_tweets(jsonl_filename):
    '''
    Returns a list of dates that had the most tweets.

    :param str jsonl_filename: The file path of the twitter dataset
    :return: A list of the 3 days (strings) with the most tweets
    '''
    # Write code for extra credit
    days_with_most_tweets = ['Wed Oct 04 22:16:18 +0000 2017', 'Wed Oct 05 22:16:18 +0000 2017', 'Wed Oct 06 22:16:18 +0000 2017']
    return days_with_most_tweets 

def dates_with_least_tweets(jsonl_filename):
    '''
    Returns a list of dates that had the least tweets.

    :param str jsonl_filename: The file path of the twitter dataset
    :return: A list of the 3 days (strings) with the least tweets
    '''
    # Write code for extra credit
    days_with_least_tweets = ['Wed Oct 04 22:16:18 +0000 2017', 'Wed Oct 05 22:16:18 +0000 2017', 'Wed Oct 06 22:16:18 +0000 2017']
    return days_with_least_tweets 

