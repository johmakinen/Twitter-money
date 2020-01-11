import numpy as np
import pandas as pd
import json
from pprint import pprint
from datetime import datetime

# Read the data
with open('10012018_10012019.json') as f1:
    data1 = json.load(f1)

with open('10012019_11012020.json') as f2:
    data2 = json.load(f2)

word_occurence_upper_limit1 = 300
word_occurence_lower_limit1 = 10
word_occurence_upper_limit2 = 1100
word_occurence_lower_limit2 = 20
char_blacklist = ['!', '?', '@', '"', '%', '.', ',', ':', '-', ';', '&']

# pprint(data1["all_data1"][0]["text"])
# pprint(data1["all_data1"][0]["created_at"])

number_of_tweets1 = len(data1['all_data'])
number_of_tweets2 = len(data2['all_data'])


def preprocess_tweet(text, to_replace):
    for char in to_replace:
        text = text.replace(char, '')
    text = text.lower()
    return text


common_words1 = dict()
common_words2 = dict()
# Loop through each tweet
i = 0
# Train dataset
while i < number_of_tweets1:
    tweet = data1['all_data'][i]['text']
    # Remove bad characters, go lowercase
    tweet = preprocess_tweet(tweet, char_blacklist)

   # Iterate over each word in tweet
    words = tweet.split(" ")
    for word in words:
        # Check if the word is already in dictionary
        if word in common_words1:
            # Increment count of word by 1
            common_words1[word] = common_words1[word] + 1
        else:
            # Add the word to dictionary with count 1
            common_words1[word] = 1
    i += 1

common_words_sorted1 = dict(sorted(
    common_words1.items(), key=lambda x: x[1], reverse=True))

i = 0
# Test dataset
while i < number_of_tweets2:
    tweet = data2['all_data'][i]['text']
    # Remove bad characters, go lowercase
    tweet = preprocess_tweet(tweet, char_blacklist)

   # Iterate over each word in tweet
    words = tweet.split(" ")
    for word in words:
        # Check if the word is already in dictionary
        if word in common_words2:
            # Increment count of word by 1
            common_words2[word] = common_words2[word] + 1
        else:
            # Add the word to dictionary with count 1
            common_words2[word] = 1
    i += 1

common_words_sorted2 = dict(sorted(
    common_words2.items(), key=lambda x: x[1], reverse=True))


# for i in list(common_words_sorted2):
#     print(i, ":", common_words_sorted2[i])
# remove too vague words
cleaned_data1 = dict()
cleaned_data2 = dict()


for i in list(common_words_sorted1):
    if common_words_sorted1[i] < word_occurence_upper_limit1 and common_words_sorted1[i] > word_occurence_lower_limit1:
        cleaned_data1[i] = common_words_sorted1[i]

for i in list(common_words_sorted2):
    if common_words_sorted2[i] < word_occurence_upper_limit2 and common_words_sorted2[i] > word_occurence_lower_limit2:
        cleaned_data2[i] = common_words_sorted2[i]

# for i in list(cleaned_data2):
#     print(i, ":", cleaned_data2[i])


key_index1 = list(cleaned_data1)
key_index2 = list(cleaned_data2)
# print(key_index1)
# Goal is to give every tweet a 1160 dimensional boolean vector of which words it contains. Also, get the timestamp of the tweet.

dims1 = (number_of_tweets1, len(key_index1))
dims2 = (number_of_tweets2, len(key_index2))
x_train = np.zeros(dims1)
x_test = np.zeros(dims2)

i = 0
while i < number_of_tweets1:
    tweet = data1['all_data'][i]['text']
    # Remove bad characters, go lowercase
    tweet = preprocess_tweet(tweet, char_blacklist)
   # Iterate over each word in tweet
    words = tweet.split(" ")
    for word in words:
        # Check if the word is in the cleaned_data1 dictionary
        if word in cleaned_data1:
            x_train[i, key_index1.index(word)] = 1
    i += 1

i = 0
while i < number_of_tweets2:
    tweet = data2['all_data'][i]['text']
    # Remove bad characters, go lowercase
    tweet = preprocess_tweet(tweet, char_blacklist)
   # Iterate over each word in tweet
    words = tweet.split(" ")
    for word in words:
        # Check if the word is in the cleaned_data1 dictionary
        if word in cleaned_data2:
            x_test[i, key_index2.index(word)] = 1
    i += 1


# print("date_object =", date_object)

# Process train_tweet datetimes into arrays
dates_train = list()
i = 0
while i < number_of_tweets1:
    # Get the datetime as string
    date_string = data1["all_data"][i]["created_at"][4:10] + " " +\
        data1["all_data"][i]["created_at"][-4:]
    # Get the datetime object
    date_object = datetime.strptime(date_string, "%b %d %Y")
    dates_train.append(date_object)
    i += 1

# Process test_tweet datetimes into arrays
dates_test = list()
i = 0
while i < number_of_tweets2:
    # Get the datetime as string
    date_string = data2["all_data"][i]["created_at"][4:10] + " " +\
        data2["all_data"][i]["created_at"][-4:]
    # Get the datetime object
    date_object = datetime.strptime(date_string, "%b %d %Y")
    dates_test.append(date_object)
    i += 1


print(dates_test[0].year)
