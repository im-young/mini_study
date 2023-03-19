# https://youtu.be/Al-S0DQsVsk 참고
# selenium 은 크롤링, 엔터 등을 핸들링 할 수 있음(dynamic-> 쉽다)
# bs4 은 static(fast)

# https://www.google.co.kr/imghp : 구글 이미지 검색창
# xpath,css select: 태그정보를 정확히 알지 못할 때 사용(xpath 가 좀더 직관적임) - 검색의 카피 종류
# 둘다 사용해보기
## image selector : #islrg > div.islrc > div:nth-child(2) > a.wXeWr.islib.nfEiy > div.bRMDJf.islir > img
## search xpath(구글 이미지의 검색창 부분) : /html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input

############### 모듈 import ############################################
 
# pip install webdriver-manager selenium (터미널에 설치)
from selenium.webdriver.common.keys import Keys #enter 키 누를 때 사용(Keys.RETURN)
import time # 웹페이지가 렌더링될 지연시간을 주기위해서
from selenium import webdriver # 셀레니움의 기본.
from webdriver_manager.chrome import ChromeDriverManager # 크롬드라이버를 매번 설치하지 않기 위해서 
from selenium.webdriver.common.by import By 
# 기존 : driver.find_element_by_ID
# 변경 : driver.find_element(By.ID,) -> by 하나로 핸들링 하기 위해
#        driver.find_elements(By.ID,)
from selenium.webdriver.chrome.service import Service  # 셀레니움 실행 할 때 서비스를 활용해서 실행이 되게끔 최신의 환경에 맞춰 변경됨
import urllib.request # 정적 크롤링 방식으로 url이 제공됐을 때 바로 이미지를 다운받기 위해

chrome_options = webdriver.ChromeOptions() # 해상도 조절, 해드리스 : 크롬환경에서 브라우져가 열리지 않고 py 가 작동될 수 있게/ B 지금은 브라우저에서 어떻게 작동되는지 확인하기 위해 아무것도 넣지 않음

driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()), options = chrome_options) # service : 크롬을 열기위해서 / ChromeDriverManager.install : 드라이브 설치 
#################################################################
################## 이미지 한장 크롤링 후 저장 #####################
###################### step1 ####################################
# URL 창이 뜨는지 확인
URL = 'https://www.google.co.kr/imghp' #구글 이미지 검색창
driver.get(url= URL)
# input() # 눈으로 확인 할떄 사용, 나중에 전체적으로 코드를 짤떄 없애기
driver.implicitly_wait(time_to_wait=10) # 이미지가 렌더링 될 때 까지 10초 기다려 준다 => max 10초 기다린다.

#################### step2 ##################################
# 자동으로 검색하기(검색어 입력후 enter 키 누르는 작업)
keyElement = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input') # 검색 위치
keyElement.send_keys('손모아 장갑') # 검색어
keyElement.send_keys(Keys.RETURN) # ENTER키 누르기
# 승우오빠 코드
## d.find_element("xpath",shoppingmall_review).click() # 클릭
# input() # 확인용(이거 켜져있으면 웹이 안꺼지는 듯)

#################### step3 ##################################
# 이미지 선택 후 저장
# find_element : 하나만 다운 / find_elements
url = driver.find_element(By.CSS_SELECTOR,'#islrg > div.islrc > div:nth-child(2) > a.wXeWr.islib.nfEiy > div.bRMDJf.islir > img').get_attribute('src')
# get_attribute : 속성값(ex.image => src 같은것 )
# print(url) # 터미널 창에 뜨는게 이미지 데이터
# 이미지 다운로드에 대표적으로 많이 씀(이미지 다운)
urllib.request.urlretrieve(url,'C:\\Users\\admin\\Desktop\\손모아장갑\\손모아장갑_크롤링1.jpg') # 경로로 저장


#################################################################
################## 이미지 여러장 크롤링 후 저장 #####################
###################### step1 ####################################





