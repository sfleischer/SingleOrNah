from decouple import config
import requests
import csv
import numpy as np

from user import User
from users_dict import UsersDict
from sentiment import get_sentiment
from match_keywords import get_weighted_sum

def api_entry(target_user, username, password):
    user = User(target_user, username, password)
    user_dict = UsersDict()

    comment_text = []
    comment_counter = 0
    caption_text = []
    caption_counter = 0
    for image in user.json:
        comments = image['comments']['data']
        for comment in comments:
            username = comment['owner']['username']
            if username == target_user:
                continue
            user_dict.incr_user_field_by(username, 'num_comments', 1)
            comment_text.append({
                'language': 'en',
                'id': username + ' ' + str(comment_counter),
                'text': comment['text']
                })
            comment_counter += 1

        image_url = image['display_url']
        caption = image['edge_media_to_caption']['edges'][0]['node']['text']
        caption_text.append({
            'language': 'en',
            'id': target_user + ' ' + str(caption_counter),
            'text': caption
            })
        caption_counter += 1


    # obtaim comment sentiments
    comment_sentiment = get_sentiment({ 'documents': comment_text })
    if (comment_sentiment):
        for k, v in comment_sentiment.items():
            user_dict.append_user_field_with(k.split(' ')[0], 'comment_sentiment', v)

    # obtains comment keyword sums
    keywords = load_keywords()
    for d in comment_text:
        comment_keyword_sum = get_weighted_sum(d['text'], keywords)
        user_dict.append_user_field_with(d['id'].split(' ')[0], 'comment_keyword_sum', comment_keyword_sum)

    # run sentiment analysis on captions
    caption_sentiment = get_sentiment({ 'documents': caption_text })
    if (caption_sentiment):
        caption_sentiment_list = list(caption_sentiment.values())
        print(caption_sentiment_list)
        average_caption_sentiment = np.mean(caption_sentiment_list)

    # run keyword search on captions
    cummulative_keyword_sum = 0.0
    for d in caption_text:
        cummulative_keyword_sum += get_weighted_sum(d['text'], keywords)
    '''
    print(user_dict.users)
    print(average_caption_sentiment)
    print(cummulative_keyword_sum)
    '''


def load_keywords(): 
    CSV_URL = config('KEYWORDS_URL')

    with requests.Session() as s:
        download = s.get(CSV_URL)

        decoded_content = download.content.decode('utf-8')

        cr = csv.reader(decoded_content.splitlines(), delimiter=',')
        l = []
        for row in cr:
            l.append((row[0], float(row[1])))

    return l

if __name__ == "__main__":
    user = api_entry("0lonestar", "chrisdfisch", "JAVAwet3652")
