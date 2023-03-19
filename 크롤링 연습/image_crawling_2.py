#################################################################
##### 보다 선명한 이미지 다운 & 이미지 여러장 크롤링 후 저장 ########
#################################################################
# 사용 라이브러리
## selenium : 동적크롤링(로그인, 이동처리를 손쉽게 해준다.) / bs4: 정적크롤링(fast)
## urllib / ChromeDriverManager
## time
# 사용 문법
## for 
## try ~ except: 예외처리를 통해서 에러가 나도 작동할 수 있게 하기 위해

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

chrome_options = webdriver.ChromeOptions() # 해상도 조절(창 사이즈 조절), 해드리스(크롬환경에서 브라우져가 열리지 않고 py 가 작동될 수 있게)/ B 지금은 브라우저에서 어떻게 작동되는지 확인하기 위해 아무것도 넣지 않음

driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()), options = chrome_options) # service : 크롬을 열기위해
###################### step1 ####################################
URL = 'https://www.google.co.kr/imghp' #구글 이미지 검색창
driver.get(url= URL)
# input() # 눈으로 확인 할떄 사용, 나중에 전체적으로 코드를 짤떄 없애기
driver.implicitly_wait(time_to_wait=10) # 이미지가 렌더링 될 때 까지 10초 기다려 준다 => max 10초 기다린다.
# time.sleep (무조건 고정된 시간->무조건 10초를 기다려야 한다)/ implicity(유연성->오픈이 되면 10까지 안 기다림)
#################### step2 ##################################
# 자동으로 검색하기 후 스크롤작업(검색어 입력후 enter 키 누르는 작업)
keyElement = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input') # 검색 위치
keyElement.send_keys('손모아 장갑') # 검색어
keyElement.send_keys(Keys.RETURN) # ENTER키 누르기

bodyElement = driver.find_element(By.TAG_NAME,'body') # body tag : html의 body / body의 아무곳이나 클릭한다음 스크롤을 내리기 위해, 클릭하는 작업
time.sleep(5)
for i in range(2) : 
    bodyElement.send_keys(Keys.PAGE_DOWN) # 페이지를 내리는(스크롤을 내리는 작업)
    time.sleep(0.2)
    # 페이지 다운 한번 하고 0.2초 기다리는 작업을 10회 반복 => 2초동안 핸들링 하는 것
    
#################### step3 ##################################
# 이미지를 한번 클릭한 후 해상도 좋은 이미지 가지고 오기

## 규칙 찾기
### 이미지의 경로를 갖고 오는데 속성값이 src가 아니라 a 로 가지고 오기
### 첫번째 이미지 XPATH ://*[@id="islrg"]/div[1]/div[1]/a[1]
### 두번째 이미지 XPATH ://*[@id="islrg"]/div[1]/div[2]/a[1]
### 세번재 이미지 XPATH ://*[@id="islrg"]/div[1]/div[3]/a[1]
### => div[] 의 숫자가 바뀜

# 위의 스크롤10번 내리면 이미지 몇개 찾는지 확인용
images = driver.find_elements(By.XPATH, '//*[@id="islrg"]/div[1]/div/a[1]') # 규칙적인 [숫자](child tag)만 빼줌
# print(len(images)) # 99개의 이미지 검색


# 클릭하면서 움직이기
imageSeq = 1
for image in images:
    image.click()
    time.sleep(0.5)
    
    # 고화질이미지(큰 이미지) 규칙찾기
    # 이미지 1 ://*[@id="Sva75c"]/div[2]/div/div[2]/div[2]/div[2]/c-wiz/div[2]/div[1]/div[1]/div[2]/div/a/img
    # 이미지 2 ://*[@id="Sva75c"]/div[2]/div/div[2]/div[2]/div[2]/c-wiz/div[2]/div[1]/div[1]/div[2]/div/a/img
    # 이미지 3 : //*[@id="Sva75c"]/div[2]/div/div[2]/div[2]/div[2]/c-wiz/div[2]/div[1]/div[1]/div[2]/div/a/img
    # 영상에서는 //*[@id="Sva75c"]/div[2]의 div[2]가 반복되던데 현재는 다른게 없음 => 그냥 아무것도 안지우고 해보기
    
    highImages = driver.find_elements(By.XPATH, '//*[@id="Sva75c"]/div[2]/div/div[2]/div[2]/div[2]/c-wiz/div[2]/div[1]/div[1]/div[2]/div/a/img')
    # 고화질 이미지가 1장 이상인지 확인
    #print(len(highImages)) # 2가 뜨면 1개 이상인것. 현재 검색은 다 1임/ 근데 두개 이상이면 find_elements를 써야해서 딱히 코드가 바뀌는건 없다
    # 고화질 이미지 'src' url 가지고 오기
    #print(highImages[0].get_attribute('src')) # 이미지에서 첫번째 src 을 잘 갖고 오는지 확인
    realImage = highImages[0].get_attribute('src') # url 변수 만들어주기
    
    # 에러발생하면 종료가 되기때문에 그걸 방지하기 위해 try~ except 사용
    try:
        urllib.request.urlretrieve(realImage, 'C:\\Users\\admin\\Desktop\\손모아장갑\\highImage\\test\\'+str(imageSeq)+'.jpg')
        imageSeq += 1
    except:
        pass
        
    
    
    
    
    

    

 

    
    