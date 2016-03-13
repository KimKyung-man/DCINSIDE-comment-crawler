# DCINSIDE-comment-crawler  

![Promo](http://s8.postimg.org/ivjxz8vk5/commentcrawl.jpg)

python 2.7 + selenium + phantom js  
프갤의 누군가 찾는 것 같아서 작성해둠  

### Usage  
```
parser = DcInsideParser('팬텀JS 경로', '갤러리 ID')  
parser.set_page_no(긁어올 페이지 번호)
parser.load_document()
parser.load_posts()
parser.load_post()
```
코멘트 작성자, 내용, 날짜를 저장하게 됨  
더 필요한 부분은 붙여서 사용하시길.  
