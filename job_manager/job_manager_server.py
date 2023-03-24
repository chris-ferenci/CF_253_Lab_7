from flask import Flask, request
from job_tasks import count_words_from_text, celery_app
from celery.result import AsyncResult
import json
import time

app = Flask(__name__)

@app.route('/count', methods = ['POST'])
def count_words_text():
    data = request.get_json()
    # text = data["text"]
    text = data.get("text")
    # print(text)

    result = count_words_from_text.delay(text)
    return json.dumps({"id": result.id})
    # return json.dumps(text)

@app.route('/status/<id>', methods = ['GET'])
def get_count_words_text(id):

    res = AsyncResult(id, app=celery_app)
    count = -1
    if res.status == "SUCCESS":
        count = res.get()

    return json.dumps({"count": count})
    
# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=5050, debug=True)


# python3 -m flask --app server run --host=0.0.0.0 --port=5050


