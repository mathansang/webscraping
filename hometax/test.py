from openpyxl import load_workbook

workbook  = load_workbook(filename='./hometax/사업자폐업여부.xlsx')
worksheet = workbook['Sheet1']

print(worksheet['A1'].value)

workbook.close()