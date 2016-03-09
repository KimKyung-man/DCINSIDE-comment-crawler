# coding=utf-8
from selenium import webdriver

"""
Author: Gracefulife
Date : 2016-03-07

현재 시간으로부터 특정 ms 전까지의 글의 댓글 정보를 긁어온다.
디비에 넣는건 니 알아서 해.
"""


class DcInsideParser:
    def __init__(self, phantom_js, gall_id):
        self._browser = webdriver.PhantomJS(executable_path=phantom_js)
        self._gall_id = gall_id
        self._url = 'http://gall.dcinside.com'
        self._page_no = None
        self._posts = []

    def set_page_no(self, page_no):
        self._page_no = page_no

    def load_document(self):
        url = self._url + '/board/lists/?id=' + self._gall_id
        if self._page_no is not None:
            url += '&page=' + str(self._page_no)
        self._browser.get(url)

    def load_posts(self):
        posts = self._browser.find_elements_by_class_name("t_subject")
        for post in posts:
            link = post.find_elements_by_tag_name('a')[0]
            self._posts.append(link.get_attribute('href'))

            # def load_post(self):


parser = DcInsideParser(r'D:\Dropbox\workspaces\python\phantomjs-2.1.1-windows\bin\phantomjs.exe', 'programming')
parser.set_page_no(2)
parser.load_document()
parser.load_posts()
