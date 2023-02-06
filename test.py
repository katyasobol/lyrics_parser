import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib
from lyrics_parser import count_word

url = 'https://genius.com/albums/Taylor-swift/Folklore'
word = 'go'

#count_word(url, word)

song = sns.load_dataset('lyrics_parser')
song.head()