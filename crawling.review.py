import io
import pandas as pd
from urllib.request import urlopen
from bs4 import BeautifulSoup

# robots.txt 검사
def get_robots_txt (url) :
    path = ''
    if url.endswith('/'):
        path = url
    else :
        path = url + '/'

    request = urlopen(path + 'robots.txt', data = None)
    response = io.TextIOWrapper(request)
    return response.read()

def get_review_data (url) :
    print('###### url : ' + url)
    webpage = urlopen(url).read()
    source = BeautifulSoup(webpage, 'html.parser', from_encoding='utf-8')
    reviews_list = source.find_all('div', {'class':'review_info'})
    review_data = []

    for review in reviews_list : 
        score = review.find_all('em', { 'class' : 'emph_grade' })[0].get_text().strip()
        content = review.find_all('p', { 'class' : 'desc_review' })[0].get_text().strip()
        review_data.append([score, content])

    return review_data


# 웹 페이지 불러오기
url_base = 'http://movie.daum.net/'
restrict = get_robots_txt(url_base)
print(restrict)

sum_list = []

for idx in range(10):
    sum_list.extend(get_review_data(url_base + 'moviedb/grade?movieId=94074&type=netizen&page=' + str(idx + 1)))

print(sum_list)

result = pd.DataFrame(sum_list, columns = ['score', 'content'])
result.to_excel('./data/review.xlsx', encoding='utf-8')

