from selenium import webdriver
import csv
import time

driver = webdriver.Chrome("./chromedriver")
driver.get("https://v4.map.naver.com")
driver.find_elements_by_css_selector("button.btn_close")[1].click()

search_box = driver.find_element_by_css_selector("input#search-input")
search_box.send_keys("수원+미용실")
search_button = driver.find_element_by_css_selector("button.spm")
search_button.click()

time.sleep(1)

with open('data.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    page_count = 0
    # 20 페이지
    for count in range(31):
        # 컨테이너(가게 정보) 수
        stores = driver.find_elements_by_css_selector("div.lsnx")
        for store in stores:
            # 세부 데이터 수집
            name = store.find_element_by_css_selector("dt > a").text
            addr = store.find_element_by_css_selector("dd.addr").text
            phone = store.find_element_by_css_selector("dd.tel").text
            spamwriter.writerow((name, addr, phone))

        page_class = driver.find_element_by_class_name("paginate_wrap")
        page = page_class.find_element_by_css_selector('strong')
        next_page = page.find_element_by_xpath('following-sibling::*')

        print(page.text)
        next_page.click()
        time.sleep(1)

