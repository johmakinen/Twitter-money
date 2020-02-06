import numpy as np
import pandas as pd

df_all = pd.read_csv('dataSet_Differences.csv')

colnames = df_all.iloc[1:2, range(3, 17)].columns.values
print(colnames)

number_of_words = df_all.shape[1]-3-len(colnames)
print(number_of_words)


# Ota kaikki joissa df_all["0"] > 0
# laske näistä riveistä ka median max ja min jokaiselle kurssille erikseen.
# lisää tulokset uuteen df
#
# to_csv
# newcolnames = []
# results = pd.DataFrame(columns=)

# df_all.loc[df_all["0"] >0]
