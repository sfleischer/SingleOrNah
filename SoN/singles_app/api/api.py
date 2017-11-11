from decouple import config
import requests
import csv
import numpy as np

from user import User
from users_dict import UsersDict
from sentiment import get_sentiment
from match_keywords import get_weighted_sum
from detect_gender import gather_info_profile_pic, gather_info_post

def api_entry(target_user, username, password):
    user = User(target_user, username, password)
    u_dict = UsersDict()

    profile_pic_url = user.getProfilePicture()
    print(profile_pic_url)

    [user_gender, user_age] = gather_info_profile_pic(profile_pic_url)

    comment_text = []
    comment_counter = 0
    caption_text = []
    caption_counter = 0

    gender_smile = []

    for image in user.json:
        comments = image['comments']['data']
        for comment in comments:
            username = comment['owner']['username']
            if username == target_user:
                continue
            u_dict.incr_user_field_by(username, 'num_comments', 1)
            comment_text.append({
                'language': 'en',
                'id': username + ' ' + str(comment_counter),
                'text': comment['text']
                })
            comment_counter += 1

        # handle image
        image_url = image['display_url']
        post_data = gather_info_post(image_url, user_gender, user_age)
        if post_data:
            [num_same_gender, num_opp_gender, agg_happiness, agg_disgust, agg_smile] = post_data
            sum = num_same_gender + num_opp_gender + agg_happiness + agg_disgust + agg_smile
            happy_ratio = (agg_happiness + agg_smile) / sum
            opp_gender_ratio = num_opp_gender / sum
            gender_smile.append(opp_gender_ratio + happy_ratio)

        caption = image['edge_media_to_caption']['edges'][0]['node']['text']
        caption_text.append({
            'language': 'en',
            'id': target_user + ' ' + str(caption_counter),
            'text': caption
            })
        caption_counter += 1

    # obtain comment sentiments
    comment_sentiment = get_sentiment({ 'documents': comment_text })
    if (comment_sentiment):
        for k, v in comment_sentiment.items():
            u_dict.append_user_field_with(k.split(' ')[0], 'comment_sentiment', v)

    # obtains comment keyword sums
    keywords = load_keywords()
    for d in comment_text:
        comment_keyword_sum = get_weighted_sum(d['text'], keywords)
        u_dict.append_user_field_with(d['id'].split(' ')[0], 'comment_keyword_sum', comment_keyword_sum)

    # run sentiment analysis on captions
    caption_sentiment = get_sentiment({ 'documents': caption_text })
    if (caption_sentiment):
        caption_sentiment_list = list(caption_sentiment.values())
        average_caption_sentiment = np.mean(caption_sentiment_list)

    # run keyword search on captions
    cummulative_keyword_sum = 0.0
    for d in caption_text:
        cummulative_keyword_sum += get_weighted_sum(d['text'], keywords)
    
    average_gender_smile = np.mean(gender_smile)

    top_three = get_top_three(u_dict)
     
    p = ((average_gender_smile*0.6) + \
    (average_caption_sentiment*0.2) + \
    (cummulative_keyword_sum*2) + \
    np.mean(list(comment_sentiment.values())) * 0.2) + \
    np.mean([np.mean(v['comment_keyword_sum']) for k,v in u_dict.users.items()]) * 5

    return {
        'p': p,
        'top_three': top_three
    }


def get_top_three(u_dict):
    tup_list = list(u_dict.users.items())
    tup_list.sort(key=lambda tup: tup[1]['num_comments']*np.mean(tup[1]['comment_sentiment']), reverse=True)
    return tup_list[0:3]

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
    #user = api_entry("kpunkka", "singleornaw1154", "phacks")
    #user = api_entry("kpunkka", "chrisdfisch", "")
    user = api_entry("nadinevm", "wae3wae3", "phacks")
