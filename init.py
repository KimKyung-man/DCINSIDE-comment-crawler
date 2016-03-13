# coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

"""
Author: Gracefulife
Date : 2016-03-07

현재 시간으로부터 특정 ms 전까지의 글의 댓글 정보를 긁어온다. 는 귀찮고
그냥 페이지 넘버로 가져오니, 수정해서 쓰도록
디비에 넣는것 또한.

현재 comment_data_list 에 코멘트 정보를 갖도록 되어있음
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
        lines = self._browser.find_elements_by_class_name("tb")
        for line in lines:
            text_no = line.find_element_by_class_name("t_notice").text.encode('utf8')
            post = line.find_element_by_class_name('t_subject')
            if text_no in '공지':
                continue
            else:
                link = post.find_elements_by_tag_name('a')[0]
                self._posts.append(link.get_attribute('href'))
                print text_no

    def load_post(self):
        # 실제로 코멘트 데이터가 들어간 리스트
        comment_data_list = []
        for post in self._posts:
            print 'load post = ' + post
            self._browser.get(post)
            try:
                wait = WebDriverWait(self._browser, 10)
                replies = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'reply_line')))
                for reply in replies:
                    comment_data = {'writer': reply.find_element_by_class_name('user_layer').text,
                                    'content': reply.find_element_by_class_name('reply').text,
                                    'date': reply.find_element_by_class_name('retime').text}
                    comment_data_list.append(comment_data)
                    print comment_data['writer'] + " / " + comment_data['content']
            except TimeoutException:
                continue


parser = DcInsideParser('팬텀JS 경로', '갤러리 ID')
# Example : parser = DcInsideParser(r'D:\Dropbox\workspaces\python\phantomjs-2.1.1-windows\bin\phantomjs.exe', 'programming')
parser.set_page_no(1)
parser.load_document()
parser.load_posts()
parser.load_post()
