import requests
from bs4 import BeautifulSoup
import pandas as pd

def count_word(url, word):
    '''вставьте ссылку на альбом c сайта genuis.com и слово, частоту употребления которого хотите найти'''

    response = requests.get(url).text
    soup = BeautifulSoup(response, "html5lib")
    lyrics = []

    song_links = soup.find_all('a', 'u-display_block')

    for link in song_links:
        song_response = requests.get(link['href']).text
        song_soup = BeautifulSoup(song_response, "html5lib")
        song_lyrics = song_soup.find('div', class_='Lyrics__Container-sc-1ynbvzw-6 YYrds')
        lyrics.append(song_lyrics)

    love_counts = [lyric.text.count(word) for lyric in lyrics]

    #df = pd.DataFrame({'Song': [song_link.text for song_link in song_links], 'Lyrics': [lyric.text for lyric in lyrics], 'Love Count': [love_count for love_count in love_counts]})

    #df.to_csv('taylor_swift_lyrics.csv', index=False)
    print(love_counts)


