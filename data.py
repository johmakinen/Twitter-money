import numpy as np
import pandas as pd
import json
from pprint import pprint
from datetime import datetime

# Read the data
with open('data_2018_2020.json') as f:
    data = json.load(f)

# with open('10012019_11012020.json') as f2:
#     data2 = json.load(f2)

word_occurence_upper_limit = 999999
word_occurence_lower_limit = 20

char_blacklist = ['!', '?', '@', '"', '%', '.', ',', ':', '-', ';', '&']

# pprint(data["all_data"][0]["text"])
# pprint(data["all_data"][0]["created_at"])

number_of_tweets = len(data['all_data'])


def preprocess_tweet(text, to_replace):
    for char in to_replace:
        text = text.replace(char, '')
    text = text.lower()
    return text


common_words = dict()
# Loop through each tweet
i = 0
# Train dataset
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


for i in list(common_words_sorted):
    print(i, ":", common_words_sorted[i])
# remove too vague words
cleaned_data = dict()


for i in list(common_words_sorted):
    if common_words_sorted[i] < word_occurence_upper_limit and common_words_sorted[i] > word_occurence_lower_limit:
        cleaned_data[i] = common_words_sorted[i]


key_index = list(cleaned_data)

# print(key_index)
# Goal is to give every tweet a 1160 dimensional boolean vector of which words it contains. Also, get the timestamp of the tweet.

dims = (number_of_tweets, len(key_index))

x = np.zeros(dims)

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


# print("date_object =", date_object)

# Process train_tweet datetimes into arrays
dates = list()
i = 0
while i < number_of_tweets:
    # Get the datetime as string
    date_string = data["all_data"][i]["created_at"][4:10] + " " +\
        data["all_data"][i]["created_at"][-4:]
    # Get the datetime object
    date_object = datetime.strptime(date_string, "%b %d %Y")
    dates.append(date_object)
    i += 1


print(dims)
