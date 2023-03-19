
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
import time 
import urllib.request 
import os
# # 1. 이미지 저장할 폴더 생성
# if not os.path.isdir("손모아 장갑/"):
#     os.makedirs("손모아 장갑/")
    
# # 2. 크롬 웹드라이버 연결
# driver = webdriver.Chrome()
# driver.get("https://www.google.co.kr/imghp?hl=ko&ogbl")

# # 3. 검색어 입력하기
# search = "손모아 장갑"
# elem = driver.find_element_by_name("q")
# elem.send_keys(search)
# elem.send_keys(Keys.RETURN)

search = "손모아 장갑"   # 이미지 이름
count = 50    # 크롤링할 이미지 개수
saveurl = "C:\\Users\\admin\\Desktop\\손모아장갑"  # 이미지들을 저장할 폴더 주소

## 셀레니움으로 구글 이미지 접속 후 이미지 검색

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size=1920x1080")

driver = webdriver.Chrome(options=options)  #options=options 
url = 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query={}'.format(search)
driver.get(url)
elem = driver.find_element('q')
elem.send_keys(search)

elem.send_keys(Keys.RETURN) 

# 페이지 끝까지 스크롤 내리기 
SCROLL_PAUSE_TIME = 1 
# 스크롤 깊이 측정하기 
last_height = driver.execute_script("return document.body.scrollHeight") 

# 스크롤 끝까지 내리기 

while True:  

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") 
    # 페이지 로딩 기다리기 
    time.sleep(SCROLL_PAUSE_TIME) 
    # 더 보기 요소 있을 경우 클릭하기 

    new_height = driver.execute_script("return document.body.scrollHeight") 

    if new_height == last_height: 

        try: 
            driver.find_element_by_css_selector(".mye4qd").click() 

        except: 
            break 

    last_height = new_height 

#이미지 찾고 다운받기
images = driver.find_elements_by_css_selector(".rg_i.Q4LuWd")

for i in range(count):

    try: 
        images[i].click() # 이미지 클릭
        time.sleep(1)

        imgUrl = driver.find_element_by_css_selector(".n3VNCb").get_attribute("src")
        urllib.request.urlretrieve(imgUrl, saveurl + str(i) + ".jpg")    # 이미지 다운

    except:
        pass
driver.close()

