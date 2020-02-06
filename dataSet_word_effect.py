import numpy as np
import pandas as pd
from data import key_index

# print(key_index)
df_all = pd.read_csv('dataSet_Differences.csv')

colnames = df_all.iloc[1:2, range(3, 17)].columns.values
# print(colnames)

number_of_words = df_all.shape[1]-3-len(colnames)
# print(number_of_words)

effects_per_word = pd.DataFrame(columns=colnames)
# print(effects_per_word)
i = 0

while i < number_of_words:
    temp = df_all.loc[df_all[str(i)] > 0]
    means = temp[colnames].mad(axis=0)
    #effects_per_word.iloc[i, :] = means.values
    effects_per_word.loc[len(effects_per_word)] = np.around(
        means.values, 5)  # adding a row
    i += 1

effects_per_word = effects_per_word.fillna(0)
# print(effects_per_word)
effects_per_word["Words"] = key_index
effects_per_word.to_csv('effects_per_word.csv',
                        header=True, index=True, sep=';', decimal=',', na_rep='blank')
