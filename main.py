import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as pls
from lyrics_parser import count_word

url = 'ваша ссылка'
word = 'ваше слово'

count_word(url, word)

song = pd.read_csv('lyrics_parser.csv')
res = sns.barplot(data=song, x='Song', y='Love Count')
pls.show()

