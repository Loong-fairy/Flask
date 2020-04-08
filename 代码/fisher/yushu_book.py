from Http import HTTP


class YuShuBook:
    per_page = 15
    isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
    keyword_url = 'http://t.yushu.im/v2/book/search?q={}&count={}&start={}'

    @classmethod
    def search_by_isbn(cls, isbn):
        url = cls.isbn_url.format(isbn)
        result = HTTP.get(url)  # 返回json类型, 在python中会转换成dict
        return result

    @classmethod
    def search_by_keyword(cls, keyword, page=1):
        url = cls.keyword_url.format(keyword, cls.per_page, (page-1) * cls.per_page)
        result = HTTP.get(url)
        return result


if __name__ == '__main__':
    print(YuShuBook.search_by_isbn('9787501524044'))

