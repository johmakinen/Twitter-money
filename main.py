import numpy as np
import pandas as pd
import json
from pprint import pprint

with open('10012018_10012019.json') as f:
    data = json.load(f)

# pprint(data["all_data"][0]["text"])
# pprint(data["all_data"][0]["created_at"])
# print(data['all_data'][0]['text'])
number_of_tweets = len(data['all_data'])

common_words = dict()
# Loop through each tweet
i = 0
while i < number_of_tweets:
    tweet = data['all_data'][i]['text']

    # Remove bad characters, go lowercase and split into words
    tweet = tweet.replace('!', '')
    tweet = tweet.replace('?', '')
    tweet = tweet.replace('@', '')
    tweet = tweet.lower()
    words = tweet.split(" ")
   # Iterate over each word in tweet
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
for i in list(common_words_sorted):
    print(i, ":", common_words[i])
