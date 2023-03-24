import os
from celery import Celery
import requests
from collections import Counter
from bs4 import BeautifulSoup
import re
import nltk
import time

broker_url  = os.environ.get("CELERY_BROKER_URL"),
res_backend = os.environ.get("CELERY_RESULT_BACKEND")

celery_app = Celery(name           = 'job_tasks',
                    broker         = broker_url,
                    result_backend = res_backend)

@celery_app.task
def count_words_from_text(text):
    try:
        print(text)
        r = requests.json(text)
    except:
        return 0

    if r:
        # text processing
        # raw = BeautifulSoup(r.text, 'html.parser').get_text()
        raw_words = r.json()
        raw_words_count = len(raw_words.split())

        # tokens = nltk.word_tokenize(raw)
        # text = nltk.Text(tokens)
        # remove punctuation, count raw words
        # nonPunct = re.compile('.*[A-Za-z].*')
        # raw_words_count = len([w for w in text if nonPunct.match(w)])
        time.sleep(raw_words_count)
        return raw_words_count
    
    return 0
        
        