'''
Script to extract similar words from google news word2vec
'''

import gensim

model = gensim.models.KeyedVectors.load_word2vec_format('model/google_news_model.bin', binary=True)  

postive_words = [ 'love', 'girlfriend', 'boyfriend', 'relationship', 'marriage', 'faithful'];
negative_words = ['ex', 'heartbroken']

sim_words = model.most_similar_cosmul(positive=postive_words, negative=negative_words, topn=100);


with open('model/keywords.csv', "w") as outfile:
    for s in postive_words:
        outfile.write(s + ',' + '0.5' + '\n')
    for s, n in sim_words:
        outfile.write(s + ',' + str(n) + '\n')