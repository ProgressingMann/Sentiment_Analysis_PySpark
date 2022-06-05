#!/usr/bin/env python
# coding: utf-8

# In[3]:


import json


# In[4]:


MAX_NEG = MAX_POS = 150000


# In[7]:


path = '/Users/mannpurohit/GitHub/Projects/data/reviews_Apps_for_Android_5.json'
with open(path, 'r') as f:
    line = f.readline()
    reviews_text = []
    reviews_score = []
    pos_cnt, neg_cnt = 0, 0

    while line:
        data_h = json.loads(line)
        sentiment = 'positive' if float(data_h['overall']) > 3 else 'negative'
        
        if sentiment == 'positive' and pos_cnt >= MAX_POS:
            pass
        elif sentiment == 'negative' and neg_cnt >= MAX_NEG:
            pass
        else:
            review_h = data_h['reviewText'].split(' ')
            if len(review_h) > 50:
                review_h = review_h[:30] + review_h[-20:]

            review_h = ' '.join(review_h)
            reviews_text.append(review_h+' '+data_h['summary'])

            reviews_score.append(sentiment)
            if sentiment == 'positive':
                pos_cnt += 1
            else:
                neg_cnt += 1

        line = f.readline()


# In[10]:


reviews_json = []
for i in range(len(reviews_score)):
    reviews_json.append({
            "reviewText": reviews_text[i], "reviewScore": reviews_score[i]
    })


# In[11]:


json_object = json.dumps(reviews_json, indent = 4)
  
# Writing to sample.json
with open("/Users/mannpurohit/GitHub/Projects/Sentiment_Analysis_Amazon_NLP/reviews_data.json", "w") as outfile:
    outfile.write(json_object)

