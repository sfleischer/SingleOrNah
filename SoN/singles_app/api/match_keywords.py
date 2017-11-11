import csv
import requests
from decouple import config
from collections import defaultdict

# takes in a list of (keywords,weight) and a target string
# returns dictionary weight -> count
def get_key_word_matches(target_string, keywords):
    counts = defaultdict(int)
    for pair in keywords:
        counts[pair[1]] += target_string.count(pair[0]) 

    return counts

def get_weighted_sum(target_string, keywords):
    sum = 0.0
    for weight, count in get_key_word_matches(target_string, keywords).items():
        sum += weight * min(count,5)/5
    return sum

if __name__ == "__main__":
    CSV_URL = config('KEYWORDS_URL')

    with requests.Session() as s:
        download = s.get(CSV_URL)

        decoded_content = download.content.decode('utf-8')

        cr = csv.reader(decoded_content.splitlines(), delimiter=',')
        l = []
        for row in cr:
            l.append((row[0], float(row[1])))

        print(get_weighted_sum("love love love", l))