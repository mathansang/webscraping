from selenium import webdriver
import csv
import time
import xlwings as xw

def parsing_contents(contents):
    if '폐업' in contents:
        return '폐업'
    else:
        return '정상'


driver = webdriver.Chrome("./chromedriver")
driver.get("https://www.hometax.go.kr/websquare/websquare.wq?w2xPath=/ui/pp/index_pp.xml&tmIdx=1&tm2lIdx=&tm3lIdx=")
time.sleep(5)
print('click')
el = driver.find_elements_by_id('menuAtag_0108010000')[0]
driver.execute_script("arguments[0].click();", el) 

time.sleep(1)

driver.switch_to.frame(driver.find_element_by_id('txppIframe'))

bsno_el = driver.find_element_by_id('bsno')

wb = xw.Book('./사업자폐업여부.xlsx')
sheet1 = wb.sheets[0]
count = int(xw.Range('bsno_count').value)

for cnt in range(count):
    row = cnt + 4
    bs_no = sheet1.range((row, 1)).value

    bsno_el.send_keys(bs_no)
    trigger5_el = driver.find_element_by_id('trigger5')
    trigger5_el.click()

    time.sleep(1)

    bsno = driver.find_element_by_id('grid2_cell_0_0').find_element_by_css_selector('nobr').text
    contents = driver.find_element_by_id('grid2_cell_0_1').find_element_by_css_selector('nobr').text
    refdate = driver.find_element_by_id('grid2_cell_0_2').find_element_by_css_selector('nobr').text

    sheet1.range((row, 3)).value = parsing_contents(contents)
    #print(bsno, contents, refdate)


