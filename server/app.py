import uuid

from flask import Flask, jsonify, request
from flask_cors import CORS

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


# Article List

articles = [
    {
        'id': uuid.uuid4().hex,
        'name': 'key1',
        'content': 'content1'
    },
    {
        'id': uuid.uuid4().hex,
        'name': 'key2',
        'content': 'content2'
    },
    {
        'id': uuid.uuid4().hex,
        'name': 'key3',
        'content': 'content3'
    }
]

# GET/articles route
# POST/new_article route

@app.route('/', methods=['GET', 'POST'])
def all_articles():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        articles.append({
            'id': uuid.uuid4().hex,
            'name': post_data.get('name'),
            'content': post_data.get('content')
        })
        response_object['message'] = 'Article added!'
    else:
        response_object['articles'] = articles
    return jsonify(response_object)


# Get/article route

@app.route('/<article_id>', methods=['GET'])
def read_article(article_id):
    response_object = {'status': 'success'}
    temp = {}
    for article in articles:
        if article['id'] == article_id:
            temp = article
            break
    response_object['article'] = temp
    return jsonify(response_object)


# PUT/update_article route

@app.route('/edit/<article_id>', methods=['PUT'])
def single_article(article_id):
    response_object = {'status': 'success'}
    if request.method == 'PUT':
        post_data = request.get_json()
        index = find_index(article_id)
        if index != -1:
            articles[index]['content'] = post_data.get('content')
            response_object['message'] = 'Article updated!'
        else:
            response_object['message'] = 'Article not found!'
    return jsonify(response_object)

def find_index(article_id):
    i = 0
    while i < len(articles):
        if articles[i]['id'] == article_id:
            return i
        i += 1
    return -1


if __name__ == '__main__':
    app.run()