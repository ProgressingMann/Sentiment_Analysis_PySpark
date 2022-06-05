#!/usr/bin/env python
# coding: utf-8

# # Text Preprocessing

# In[1]:


import json
import pandas as pd
import numpy as np
import sys


# In[34]:


def read_file(path):
    lines = []
    with open(path, 'r') as f:
        line = f.readline()
        while line:
            lines.append(line)
            line = f.readline()
    return lines

def check_blanks(text):
#     is_blank = str(data_str.isspace())
    text = text.strip()
    if len(text) == 0:
        return 'False'
    else:
        return 'True'


# In[39]:


check_blanks(lines[2])


# ### 2) Determine whether the language of the text content is english or not: Use langid module to classify the language to make sure we are applying the correct cleanup actions for English langid

# In[11]:


# !pip install langid
# import langid
# def check_lang(data_str):
#     predict_lang = langid.classify(data_str)
#     if predict_lang[1] >= .9:
#         language = predict_lang[0]
#     else:
#         language = 'NA'
#     return language


# In[12]:


# for line in lines:
#     print(check_lang(line))


# ### 3) Removing punctuations, blank spaces, and other unnecessary strings

# In[13]:


def clean_text(text):
    # Removing URLs
    url_re = re.compile('(www.)?\w+\.\w+(/\w+)*/?')
    text = url_re.sub(' ', text)
    
    # Removing all the words containing numbers and lower casing the text
    pattern = re.compile(r'\b[a-zA-Z]+\b')
    output = ' '.join(pattern.findall(text)).lower()
    
    # Removing single letters like a, i, u
    output = re.sub(r'\b[a-z]\b', '', output)
    
    # Removing blank spaces
    output = re.sub(r'\s+', ' ', output).strip()
    
    return output


# ## 4) Removing StopWords

# In[16]:


from nltk.corpus import stopwords
def remove_stops(data_str):
    # expects a string
    stops = set(stopwords.words("english"))
    list_pos = 0
    cleaned_str = ''
    text = data_str.split()
    for word in text:
        if word not in stops:
            # rebuild cleaned_str
            if list_pos == 0:
                cleaned_str = word
            else:
                cleaned_str = cleaned_str + ' ' + word
            list_pos += 1
    return cleaned_str


# ## 5) Lemmatizing Words

# In[23]:


from nltk.stem import LancasterStemmer
from nltk import word_tokenize
def lemmatize(text):
    stemmer = LancasterStemmer()
#     lemmatizer = WordNetLemmatizer()
    words = word_tokenize(text)
    pp_list = []
    for word in words:
        pp_list.append(stemmer.stem(word))
    
    pp_text = ' '.join(pp_list)
    return pp_text


# In[ ]:




