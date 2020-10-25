from selenium import webdriver
import time
import json

driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.get('https://ngs.ru/text/')

articles = driver.find_elements_by_css_selector('div:nth-child(3)>article')
news = []
f = open('data.txt', 'w')

for article in articles:
    link = article.find_element_by_tag_name('a').get_attribute('href')
    title = article.find_element_by_css_selector('div>div>h2>a>span').text
    news.append({'title': title, 'link': link, 'text': None})


for n in news:
    print (n['link'], n['title'])
    time.sleep(2)

json.dump(news, f)
driver.close()
