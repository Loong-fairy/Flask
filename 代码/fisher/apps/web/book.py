from flask import jsonify, request
from apps.forms.book import SearchForm

from . import web
from helper import is_isbn_or_key
from yushu_book import YuShuBook


@web.route('/book/search')
def search():
    """
        q :普通关键字 isbn
        page
    :return:
    """
    form = SearchForm(request.args)  # 调用验证器
    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        if isbn_or_key == 'isbn':
            result = YuShuBook.search_by_isbn(q)
        else:
            result = YuShuBook.search_by_keyword(q)
        return jsonify(result)
    else:
        return jsonify(form.errors)

