import numpy as np
import pandas as pd
from data import key_index

# print(key_index)
df_all = pd.read_csv('dataSet_Differences.csv')

colnames = df_all.iloc[1:2, range(3, 17)].columns.values
# print(colnames)

number_of_words = df_all.shape[1]-3-len(colnames)
# print(number_of_words)

effects_per_word_mad = pd.DataFrame(columns=colnames)
effects_per_word_avg = pd.DataFrame(columns=colnames)
# print(effects_per_word)
i = 0

while i < number_of_words:
    temp = df_all.loc[df_all[str(i)] > 0]
    mads = temp[colnames].mad(axis=0)
    avgs = temp[colnames].mean(axis=0)
    #effects_per_word.iloc[i, :] = means.values
    effects_per_word_mad.loc[len(effects_per_word_mad)] = np.around(
        mads.values, 5)  # adding a row
    effects_per_word_avg.loc[len(effects_per_word_avg)] = np.around(
        avgs.values, 5)
    i += 1

effects_per_word_mad = effects_per_word_mad.fillna(0)
effects_per_word_avg = effects_per_word_avg.fillna(0)
# print(effects_per_word)
effects_per_word_mad["Words"] = key_index
effects_per_word_avg["Words"] = key_index
effects_per_word_mad.to_csv('effects_per_word_mad.csv',
                            header=True, index=True, sep=';', decimal=',', na_rep='blank')
effects_per_word_avg.to_csv('effects_per_word_avg.csv',
                            header=True, index=True, sep=';', decimal=',', na_rep='blank')
