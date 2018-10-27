from app.forms.book import SearchForm
from . import web
from flask import request, jsonify
from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook


@web.route('/book/search')
def search():
    pass


@web.route('/hello')
def hello():
    headers = {
        'content-type': 'application/json'
    }
    return '{"A": 12}', 400, headers
