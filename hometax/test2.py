import xlwings as xw

wb = xw.Book('./hometax/사업자폐업여부.xlsx')
sheet1 = wb.sheets[0]

count = int(xw.Range('bsno_count').value)

for cnt in range(count):
    row = cnt + 4
    
    bs_no = sheet1.range((row, 1)).value
    print(bs_no)




