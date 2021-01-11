import xlrd
import pprint
li = list()
wb = xlrd.open_workbook("fathur_data\weight_bloodpressure.xlsx")
print(type(wb))