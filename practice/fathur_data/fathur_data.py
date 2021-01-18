import openpyxl
import pprint
li = list()
wb = openpyxl.load_workbook("fathur_data\weight_bloodpressure.xlsx")
print(type(wb))
#シートの取得
ws = wb["Sheet1"]
#ws = wb.worksheets[0]
c1 = ws["C42"]
print(c1.value)