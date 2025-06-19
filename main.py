from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from datetime import datetime
from time import sleep

letter1 = {
    'a': 'M38.801224 36.531611',
    'b': 'M41.659899 35.342095',
    'c': 'M44.173231 48.96397',
    'd': 'M38.935524 35.226981',
    'e': 'M38.839595 36.224639',
    'f': 'M40.854098 25.979455',
    'g': 'M39.395982 37.337412',
    'h': 'M44.000559 38.526928',
    'i': 'M38.340766 32.656092',
    'j': 'M33.467588 54.834806',
    'k': 'M36.498935 40.944331',
    'l': 'M37.496593 21.605106',
    'm': 'M48.432465 37.951356',
    'n': 'M43.90463 38.526928',
    'o': 'M40.873283 36.416497',
    'p': 'M41.640713 37.52927',
    'q': 'M38.993081 37.490898',
    'r': 'M43.943002 37.107183',
    's': 'M39.798882 48.848856',
    't': 'M41.256998 47.889569',
    'u': 'M40.508754 49.07908',
    'v': 'M39.683768 48.69537',
    'w': 'M45.477861 48.656998',
    'x': 'M49.103966 49.270942',
    'y': 'M33.851303 57.405695',
    'z': 'M32.911202 48.810484'
}
letter2 = {
    'a': 'M81.401224 36.531611',
    'b': 'M84.259899 35.342095',
    'c': 'M86.773231 48.96397',
    'd': 'M81.535524 35.226981',
    'e': 'M81.439595 36.224639',
    'f': 'M83.454098 25.979455',
    'g': 'M81.995982 37.337412',
    'h': 'M86.600559 38.526928',
    'i': 'M80.940766 32.656092',
    'j': 'M76.067588 54.834806',
    'k': 'M79.09893 40.944331',
    'l': 'M80.096593 21.605106',
    'm': 'M91.032465 37.951356',
    'n': 'M86.50463 38.526928',
    'o': 'M83.473283 36.416497',
    'p': 'M84.240713 37.52927',
    'q': 'M81.593081 37.490898',
    'r': 'M86.543002 37.107183',
    's': 'M82.398882 48.848856',
    't': 'M83.856998 47.889569',
    'u': 'M83.108754 49.07908',
    'v': 'M82.283768 48.69537',
    'w': 'M88.077861 48.656998',
    'x': 'M91.703966 49.270942',
    'y': 'M76.451303 57.405695',
    'z': 'M75.511202 48.810484'
}
letter3 = {
    'a': 'M124.00122 36.531611',
    'b': 'M126.8599 35.342095',
    'c': 'M129.37323 48.96397',
    'd': 'M124.13552 35.226981',
    'e': 'M124.03959 36.224639',
    'f': 'M126.0541 25.979455',
    'g': 'M124.59598 37.337412',
    'h': 'M129.20056 38.526928',
    'i': 'M123.54077 32.656092',
    'j': 'M118.66759 54.834806',
    'k': 'M121.69893 40.944331',
    'l': 'M122.69659 21.605106',
    'm': 'M133.63246 37.951356',
    'n': 'M129.10463 38.526928',
    'o': 'M126.07328 36.416497',
    'p': 'M126.84071 37.52927',
    'q': 'M124.19308 37.490898',
    'r': 'M129.143 37.107183',
    's': 'M124.99888 48.848856',
    't': 'M126.457 47.889569',
    'u': 'M125.70875 49.07908',
    'v': 'M124.88377 48.69537',
    'w': 'M130.67786 48.656998',
    'x': 'M134.30397 49.270942',
    'y': 'M119.0513 57.405695',
    'z': 'M118.1112 48.810484'
}
letter4 = {
    'a': 'M166.60122 36.531611',
    'b': 'M169.4599 35.342095',
    'c': 'M171.97323 48.96397',
    'd': 'M166.73552 35.226981',
    'e': 'M166.63959 36.224639',
    'f': 'M168.6541 25.979455',
    'g': 'M167.19598 37.337412',
    'h': 'M171.80056 38.526928',
    'i': 'M166.14077 32.656092',
    'j': 'M161.26759 54.834806',
    'k': 'M164.29893 40.944331',
    'l': 'M165.29659 21.605106',
    'm': 'M176.23246 37.951356',
    'n': 'M171.70463 38.526928',
    'o': 'M168.67328 36.416497',
    'p': 'M169.44071 37.52927',
    'q': 'M166.79308 37.490898',
    'r': 'M171.743 37.107183',
    's': 'M167.59888 48.848856',
    't': 'M169.057 47.889569',
    'u': 'M168.30875 49.07908',
    'v': 'M167.48377 48.69537',
    'w': 'M173.27786 48.656998',
    'x': 'M176.90397 49.270942',
    'y': 'M161.6513 57.405695',
    'z': 'M160.7112 48.810484'
}
letter5 = {
    'a': 'M166.6012 36.531611',
    'b': 'M169.4599 35.342095',
    'c': 'M171.9732 48.96397',
    'd': 'M166.7355 35.226981',
    'e': 'M166.6396 36.224639',
    'f': 'M168.6541 25.979455',
    'g': 'M167.196 37.337412',
    'h': 'M171.8006 38.526928',
    'i': 'M166.1408 32.656092',
    'j': 'M161.2676 54.834806',
    'k': 'M164.2989 40.944331',
    'l': 'M165.2966 21.605106',
    'm': 'M176.2325 37.951356',
    'n': 'M171.7046 38.526928',
    'o': 'M168.6733 36.416497',
    'p': 'M169.4407 37.52927',
    'q': 'M166.7931 37.490898',
    'r': 'M171.743 37.107183',
    's': 'M167.5989 48.848856',
    't': 'M169.057 47.889569',
    'u': 'M168.3088 49.07908',
    'v': 'M167.4838 48.69537',
    'w': 'M173.2779 48.656998',
    'x': 'M176.904 49.270942',
    'y': 'M161.6513 57.405695',
    'z': 'M160.7112 48.810484'
}
letter6 = {
    'a': 'M124.0012 36.531611',
    'b': 'M126.8599 35.342095',
    'c': 'M129.3732 48.96397',
    'd': 'M124.1355 35.226981',
    'e': 'M124.0396 36.224639',
    'f': 'M126.0541 25.979455',
    'g': 'M124.596 37.337412',
    'h': 'M129.2006 38.526928',
    'i': 'M123.5408 32.656092',
    'j': 'M118.6676 54.834806',
    'k': 'M121.69889 40.944331',
    'l': 'M122.6966 21.605106',
    'm': 'M133.6325 37.951356',
    'n': 'M129.1046 38.526928',
    'o': 'M126.0733 36.416497',
    'p': 'M126.8407 37.52927',
    'q': 'M124.1931 37.490898',
    'r': 'M129.143 37.107183',
    's': 'M124.9989 48.848856',
    't': 'M126.457 47.889569',
    'u': 'M125.7088 49.07908',
    'v': 'M124.8838 48.69537',
    'w': 'M130.6779 48.656998',
    'x': 'M134.304 49.270942',
    'y': 'M119.0513 57.405695',
    'z': 'M118.1112 48.810484'
}
decoded_string = ''
i = 0

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
chrome_options.page_load_strategy = 'none'

driver = webdriver.Chrome(options=chrome_options)

url = input("url:")
waitTO = int(input("wait to:"))

driver.get(url)


sleep(3)


#倒數

if waitTO != 0:
    waitSec = int(input("wait second:"))
    current_time = datetime.now()
    target_time = current_time.replace(hour=waitTO ,minute=0, second=0, microsecond=150000)
    time_to_wait = (target_time - current_time).total_seconds()
    if time_to_wait > 0:
        print(f"等待 {time_to_wait} 秒，直到 {target_time}")
        sleep(time_to_wait)
        print(f"已等待到 {target_time}")
else:
    sleep(5)


time0 = datetime.now()

driver.refresh()

time1 = datetime.now()



                                                                                
Btn = WebDriverWait(driver, 200000).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div/div/main/div/div/div[2]/div[3]/div/div[2]/div[2]/div[2]/div/div[1]/button')))
time2 = datetime.now()
driver.execute_script("arguments[0].click();", Btn)

# 點擊+


js_script = 'var element = document.querySelector("button.v-btn.v-btn--fab.v-btn--has-bg.v-btn--round.theme--light.v-size--x-small.light-primary-2");' \
            'element.dispatchEvent(new Event("click"));'
driver.execute_script(js_script)

time3 = datetime.now()
svg_path_element = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div/main/div/div/div[2]/div[3]/div/div[2]/div[3]/div/div[2]/span[1]'))) 
svg_path_element = svg_path_element.find_element(By.TAG_NAME, 'path')     
d = svg_path_element.get_attribute("d")


# 驗證碼演算v3
input_numbers = d

time4 = datetime.now()


find = True
while find:
    for letter, code in letter1.items():
        if input_numbers[i:i+len(code)] == code:
            decoded_string += letter
            find = False
    i += 1

find = True
while find:
    for letter, code in letter2.items():
        if input_numbers[i:i+len(code)] == code:
            decoded_string += letter
            find = False
    i += 1
        
check = True
find = True
i1 = i
while find:
    for letter, code in letter3.items():
        if input_numbers[i:i+len(code)] == code:
            decoded_string += letter
            check = False
            find = False         
    i += 1
find = True
if check:
    i = i1
    while find:
        for letter, code in letter6.items():
            if input_numbers[i:i+len(code)] == code:
                decoded_string += letter
                find = False             
        i += 1

check = True
find = True
i1 = i
while find:
    for letter, code in letter4.items():
        if input_numbers[i:i+len(code)] == code:
            decoded_string += letter   
            check = False
            find = False
    i += 1

find = True
if check:
    i = i1
    while find:
        for letter, code in letter5.items():
            if input_numbers[i:i+len(code)] == code:
                decoded_string += letter
                find = False
        i += 1
print(decoded_string)

time5 = datetime.now()



# 輸入驗證碼



capchaText = driver.find_element(By.ID, "input-52")

capchaText.send_keys(decoded_string)

time6 = datetime.now()


if waitTO != 0:
    current_time = datetime.now()
    target_time = current_time.replace(hour=waitTO ,minute=0, second=waitSec, microsecond=150000)
    time_to_wait = (target_time - current_time).total_seconds()
    if time_to_wait > 0:
        print(f"等待 {time_to_wait} 秒，直到 {target_time}")
        sleep(time_to_wait)
        print(f"已等待到 {target_time}")

nextBtn = WebDriverWait(driver, 200000).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div/div/main/div/div/div[2]/div[4]/div/div/div[3]/div/div[2]/button')))
driver.execute_script("arguments[0].click();", nextBtn)
                                                                                    
time7 = datetime.now()
    
print("刷新:",(time1 - time0).total_seconds())
print("載入:",(time2 - time1).total_seconds())
print("點擊:",(time3 - time2).total_seconds())
print("抓驗證碼密碼:",(time4 - time3).total_seconds())
print("驗證碼演算法v4:",(time5 - time4).total_seconds())
print("輸入驗證碼:",(time6 - time5).total_seconds())
print("下一步:",(time7 - time6).total_seconds())
print("總耗時:",(time7 - time0).total_seconds())


input("Press Enter to go...")
driver.quit()
