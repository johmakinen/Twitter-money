import numpy as np
import pandas as pd
import json
from pprint import pprint
from datetime import datetime
import sys
import csv
##############################################################
# READ THE TWEET DATA AND TIMESTAMPS INTO FORMATS:
# tweets = list('tweet1','tweet2',...)
# timestamps = list('Jan 01 2018','Jan 02 2018'...)
##############################################################
# Read the data
with open('data_2018_2020.json') as f:
    data = json.load(f)

# Initialise tweet and timestamp lists, then fill them
number_of_tweets = len(data['all_data'])
tweets = list()
dates = list()

i = 0
while i < number_of_tweets:
    tweets.append(data["all_data"][i]["text"])
    dates.append(data["all_data"][i]["created_at"])
    i += 1
##############################################################

# Set word occurence limits to filter out "a", "the" etc.
word_occurence_upper_limit = sys.maxsize
word_occurence_lower_limit = 1
char_blacklist = ['!', '?', '@', '"', '%', '.', ',', ':', '-', ';', '&']

##############################################################
##############################################################
# SCRIPT BEGINS HERE


def preprocess_tweet(text, to_replace):
    for char in to_replace:
        text = text.replace(char, '')
    text = text.lower()
    return text


common_words = dict()
# Loop through each tweet
i = 0
while i < number_of_tweets:
    tweet = tweets[i]
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


# for i in list(common_words_sorted):
#     print(i, ":", common_words_sorted[i])

# remove too vague words
cleaned_data = dict()
for i in list(common_words_sorted):
    if common_words_sorted[i] < word_occurence_upper_limit and common_words_sorted[i] > word_occurence_lower_limit:
        cleaned_data[i] = common_words_sorted[i]

key_index = list(cleaned_data)


print("Number of words taken into consideration: ", len(cleaned_data))

# Goal is to give every tweet a "number_of_tweets" dimensional boolean vector of which words it contains.
dims = (number_of_tweets, len(key_index))
x = np.zeros(dims)
i = 0
while i < number_of_tweets:
    tweet = tweets[i]
    # Remove bad characters, go lowercase
    tweet = preprocess_tweet(tweet, char_blacklist)
   # Iterate over each word in tweet
    words = tweet.split(" ")
    for word in words:
        # Check if the word is in the cleaned_data dictionary
        if word in cleaned_data:
            x[i, key_index.index(word)] = 1
    i += 1


# Process tweet datetimes into arrays
dates_dtm = list()
i = 0
while i < number_of_tweets:
    # Get the datetime as string
    date_string = dates[i][4:10] + " " + dates[i][-4:]
    # Get the datetime object
    date_object = datetime.strptime(date_string, "%b %d %Y")
    dates_dtm.append(date_object)
    i += 1

# Merge tweets from same day
x_merged = np.zeros((dims[0], dims[1]+3))
curr_index = 0
new_index = 0
while curr_index < number_of_tweets:
    curr = x[curr_index]
    j = curr_index+1
    if j >= number_of_tweets or curr_index >= number_of_tweets:
        break
    while dates_dtm[curr_index] == dates_dtm[j]:
        curr = curr + x[j]
        j += 1
        if j >= number_of_tweets:
            break

    x_merged[new_index, 3:] = curr

    x_merged[new_index, 0:3] = np.array(
        [dates_dtm[curr_index].month, dates_dtm[curr_index].day, dates_dtm[curr_index].year])
    curr_index = j
    new_index += 1


# Export into a csv file for later use
x_merged = x_merged[~(x_merged == 0).all(1)]
df = pd.DataFrame(x_merged)
df = df[::-1]
df.to_csv("x_all.csv", header=False, index=False)
