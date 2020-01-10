import numpy as np
import pandas as pd
import json
from pprint import pprint

with open('10012018_10012019.json') as f:
    data = json.load(f)

# pprint(data["all_data"][0]["text"])
# pprint(data["all_data"][0]["created_at"])

number_of_tweets = len(data['all_data'])


def preprocess_tweet(text, to_replace):
    for char in to_replace:
        text = text.replace(char, '')
    text = text.lower()
    return text


char_blacklist = ['!', '?', '@', '"', '%', '.', ',', ':', '-', ';']
common_words = dict()
# Loop through each tweet
i = 0
while i < number_of_tweets:
    tweet = data['all_data'][i]['text']
    # Remove bad characters, go lowercase
    tweet = preprocess_tweet(tweet, char_blacklist)

   # Iterate over each word in tweet
    words = tweet.split(" ")
    for word in words:
        # Check if the word is already in dictionary
        if word in common_words:
            # Increment count of word by 1
            common_words[word] = common_words[word] + 1
        else:
            # Add the word to dictionary with count 1
            common_words[word] = 1
    i += 1

common_words_sorted = dict(sorted(
    common_words.items(), key=lambda x: x[1], reverse=True))
# Print the contents of dictionary
# for i in list(common_words_sorted):
#     print(i, ":", common_words[i])

# remove too vague words
cleaned_data = dict()
word_occurence_upper_limit = 300
word_occurence_lower_limit = 10

for i in list(common_words_sorted):
    if common_words_sorted[i] < word_occurence_upper_limit and common_words_sorted[i] > word_occurence_lower_limit:
        cleaned_data[i] = common_words_sorted[i]

for i in list(cleaned_data):
    print(i, ":", cleaned_data[i])


key_index = list(cleaned_data)
print(key_index)
# Goal is to give every tweet a 1160 dimensional boolean vector of which words it contains. Also, get the timestamp of the tweet.

dims = (number_of_tweets, len(key_index))
x = np.zeros(dims)

tweet_length = len(data["all_data"][0]["text"])

i = 0
while i < number_of_tweets:
    tweet = data['all_data'][i]['text']
    # Remove bad characters, go lowercase
    tweet = preprocess_tweet(tweet, char_blacklist)
   # Iterate over each word in tweet
    words = tweet.split(" ")
    for word in words:
        # Check if the word is in the cleaned_data dictionary
        if word in cleaned_data:
            x[i, key_index.index(word)] = 1
    i += 1
